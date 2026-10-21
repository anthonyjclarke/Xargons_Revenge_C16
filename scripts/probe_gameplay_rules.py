#!/usr/bin/env python3
"""Controlled original-routine probes; workspace caller, SEI/CLD, no game-code patches."""
import json
from pathlib import Path
from restore_c16 import ROOT, digest, write_json
from verify_vice import labels, run_monitor


def probe(build):
    build=build.resolve();s=labels(build);out=build/'rule-probes';out.mkdir(parents=True,exist_ok=True)
    checks=[]
    for version,prg in [('source',build/'xargons-revenge.prg'),('running-reference',build/'reference-unpacked.prg')]:
        commands=f'load "{prg}" 0\nbreak 30b\n'
        specs=[]
        def call(name,routine,fields,acc=0,x=0,y=0,blocks=()):
            nonlocal commands
            for key,data in fields.items():
                if isinstance(data,int):data=[data]
                commands+=f'> {s[key]:x} '+' '.join(f'{v:02x}' for v in data)+'\n'
            for a,data in blocks:commands+=f'> {a:x} '+' '.join(f'{v:02x}' for v in data)+'\n'
            a=s[routine];caller=[0x78,0xd8,0xa9,acc,0xa2,x,0xa0,y,0x20,a&255,a>>8,0xea]
            commands+='> 300 '+' '.join(f'{v:02x}' for v in caller)+'\ng 300\n'
            capture=out/f'{version}-{name}.bin';commands+=f'bsave "{capture}" 0 0000 3fff\n'
            specs.append((name,routine,fields,capture,{'a':acc,'x':x,'y':y},[{'address':a,'hex':bytes(data).hex()} for a,data in blocks]))
        for sheet in range(16):call(f'alien-{sheet}','ALIDEF',{'SHEET':sheet})
        call('score-49999-plus-1','SCORE',{'SCRBUF':[0,0,0,4,9,9,9,9],'XTRA':0,'LIVES':5,'RND':[1,2,3,4]},acc=1)
        call('score-99999-plus-1','SCORE',{'SCRBUF':[0,0,0,9,9,9,9,9],'XTRA':5,'LIVES':5,'RND':[1,2,3,4]},acc=1)
        call('score-full-overflow','SCORE',{'SCRBUF':[9]*8,'XTRA':0,'LIVES':5,'SCRADD':0,'RND':[1,2,3,4]},acc=1,blocks=[(s['SCRBUF']+255,[0xaa])])
        call('fuel-cap','ADFUEL',{'FUEL':110,'FULINC':4,'CTLFUL':0})
        call('fuel-zero-shot','SHOTFL',{'FUEL':0,'DEAD':0,'FXNUMB':128,'RND':[1,2,3,4]})
        call('fuel-one-shot','SHOTFL',{'FUEL':1,'DEAD':0,'FXNUMB':128})
        for flag in [0x80,0xc0]:
            call(f'ship-fire-{flag:02x}','SHIP',{'JFIRE':flag,'OLDFIR':0x80,'JMOVE':1,'JUP':0,'JDOWN':0,'DNTFIR':0,'DEAD':0,'LASERS':0,'FIRCNT':1,'FULDWN':0,'FUEL':111,'SNDFLG':0,'SHIPY':7,'YPIX':3,'SHPSCR':[0xb9,0x0d],'SHPCOL':[0xb9,0x09]})
        commands+='quit\n';log=run_monitor(out,version,commands)
        if log.lower().count('.c:030b')<len(specs):raise ValueError('Probe caller did not return for every case')
        for name,routine,fields,p,registers,blocks in specs:
            mem=p.read_bytes()
            row={'version':version,'probe':name,'routine':routine,'address':s[routine], 'inputs':fields,'registers':registers,'memory_blocks':blocks,'memory_sha256':digest(mem)}
            if name.startswith('alien-'):row['output_hex']=mem[0x3ea8:0x3ee8].hex()
            elif name.startswith('ship-fire-'):row['lasers']=mem[s['LASERS']];row['oldfire']=mem[s['OLDFIR']]
            elif name.startswith('score-'):row['score_digits']=list(mem[s['SCRBUF']:s['SCRBUF']+8]);row['lives']=mem[s['LIVES']];row['scradd']=mem[s['SCRADD']];row['overflow_store_address']=s['SCRBUF']+255;row['overflow_store_value']=mem[s['SCRBUF']+255]
            else:row.update(fuel=mem[s['FUEL']],request=mem[s['FULINC']],dead=mem[s['DEAD']])
            checks.append(row)
    bjh=(ROOT/'Original Source Recovered/2026/Xargons-Revenge-C16-Side2/089_BJH.prg').read_bytes()[2:]
    for row in checks:
        n=row['probe']
        if n.startswith('alien-') and row['version']=='source':
            i=int(n.split('-')[1]);assert row['output_hex']==bjh[i*64:i*64+64].hex()
        if n=='score-49999-plus-1':assert row['score_digits']==[0,0,0,5,0,0,0,0] and row['lives']==6
        if n=='score-99999-plus-1':assert row['score_digits']==[0,0,1,0,0,0,0,0] and row['lives']==6
        if n=='ship-fire-80':assert (row['lasers'],row['oldfire'])==(0,128)
        if n=='ship-fire-c0':assert (row['lasers'],row['oldfire'])==(1,192)
        if n=='score-full-overflow':assert row['overflow_store_value']==1
        if n=='fuel-cap':assert (row['fuel'],row['request'])==(111,0)
        if n=='fuel-zero-shot':assert (row['fuel'],row['dead'])==(255,0)
        if n=='fuel-one-shot':assert (row['fuel'],row['dead'])==(0,1)
    report={'method':'Workspace caller at $0300; SEI/CLD; A/X/Y and named RAM set as recorded; original instructions unchanged; no concurrent IRQ execution; sequential calls within each loaded revision, with only listed fields/registers/blocks reset',
            'scope':'48 isolated observations; not manual controls, timing, transitions, overflow safety or full gameplay verification',
            'source_prg_sha256':digest((build/'xargons-revenge.prg').read_bytes()),'reference_memory_sha256':digest((build/'reference-memory.bin').read_bytes()),'checks':checks}
    write_json(out/'rule-probes.json',report)
    print('Completed',len(checks),'controlled routine observations')
    return report

if __name__=='__main__':probe(ROOT/'build')
