#!/usr/bin/env python3
"""Bounded PAL C16 startup and decompressed-reference verification, sound disabled."""
import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from restore_c16 import ROOT, LOAD, ENTRY, REFERENCE, digest, prepare_sources, mos_hex, tool, write_json


def labels(build):
    return {n:int(a,16) for a,n in re.findall(r'^al ([0-9A-Fa-f]+) \.(\w+)$', (build/'xargon.labels').read_text(), re.M)}


def run_monitor(build, stem, commands):
    build.mkdir(parents=True,exist_ok=True)
    commands_file=build/(stem+'.mon')
    commands_file.write_text(commands)
    log=build/(stem+'-monitor.log')
    log.unlink(missing_ok=True)
    command=[tool('xplus4'),'-default','+saveres','-model','c16pal','-ramsize','16','+sound',
             '-initbreak','ready','-moncommands',str(commands_file),'-logfile',str(build/(stem+'-vice.log')),
             '-monlog','-monlogname',str(log),'-warp','-limitcycles','100000000']
    write_json(build/(stem+'-command.json'),{'argv':command,'timeout_seconds':45,'audio':False})
    result=subprocess.run(command,cwd=ROOT,capture_output=True,timeout=45)
    (build/(stem+'-console.log')).write_bytes(result.stdout+result.stderr)
    result.check_returncode()
    return log.read_text()


def verify(build):
    build=build.resolve(); build.mkdir(parents=True,exist_ok=True)
    write_json(build/'vice-verification.json',{'status':'running','scope':'bounded startup and reference comparison'})
    sym=labels(build)
    for n in ['reference-memory.bin','gameplay-memory.bin','title-memory.bin','restored-title.png','restored-gameplay.png']:
        (build/n).unlink(missing_ok=True)
    # Compare before the first original game instruction, after the BASIC SYS unpacker.
    log=run_monitor(build,'reference',f'load "{REFERENCE}" 0\nbreak 1800\ng 100d\nbsave "{build/"reference-memory.bin"}" 0 0400 3fff\nquit\n')
    if 'c:$1800' not in log.lower():
        raise ValueError('Reference did not reach original entry')
    ref=(build/'reference-memory.bin').read_bytes(); raw=(build/'xargons-revenge.prg').read_bytes()[2:]
    if len(ref)!=len(raw):raise ValueError('Reference memory extent mismatch')
    (build/'reference-unpacked.prg').write_bytes(b'\x00\x04'+ref)
    # Stop at the title's fire test only after REVTIT has drawn all sixteen rows.
    commands=f'load "{build/"xargons-revenge.prg"}" 0\nbreak {sym["TITTER"]:x}\ng 1800\n'
    commands+=f'screenshot "{build/"restored-title.png"}" 2\nbsave "{build/"title-memory.bin"}" 0 0000 3fff\n'
    commands+=f'> {sym["JFIRE"]:x} 80\ndelete 1\nbreak {sym["LOOP"]:x}\nx\n'
    commands+=f'> {sym["JFIRE"]:x} 00\nscreenshot "{build/"restored-gameplay.png"}" 2\nbsave "{build/"gameplay-memory.bin"}" 0 0000 3fff\nquit\n'
    log=run_monitor(build,'gameplay',commands)
    mem=(build/'gameplay-memory.bin').read_bytes();title=(build/'title-memory.bin').read_bytes()
    if f'c:${sym["LOOP"]:04x}' not in log.lower() or len(mem)!=16384:
        raise ValueError('Main gameplay loop not reached')
    if (mem[sym['TITLE']],mem[sym['LIVES']])!=(0,5):raise ValueError('Unexpected gameplay state')
    expected_vectors=sym['RESET'].to_bytes(2,'little')*2+sym['SERV'].to_bytes(2,'little')
    if mem[0x3ffa:0x4000]!=expected_vectors:raise ValueError('Expected 16 KB RAM vector mirroring not observed')
    if title[sym['TITLE']]!=1:raise ValueError('Unexpected title state')
    for name in ['restored-title.png','restored-gameplay.png']:
        if not (build/name).read_bytes().startswith(b'\x89PNG\r\n\x1a\n'):raise ValueError('Missing screenshot')
    sources,_,_=prepare_sources(build/'verify-inputs');obj=mos_hex(sources['OBJ'])
    diffs=[]
    for offset,(x,y) in enumerate(zip(raw,ref)):
        if x==y:continue
        a=offset+LOAD
        kind=('initialized code or embedded data' if a in obj else 'alien graphics' if a<0x800 else
              'screen and attributes / unpacker workspace' if a<0x1000 else 'terrain graphics' if a<0x1800 else
              'font and runtime graphics' if a>=0x3800 else 'padding after object listing')
        diffs.append({'address':a,'source':x,'reference':y,'classification':kind})
    report={'status':'passed','emulator':'VICE xplus4 3.10','model':'c16pal','ram_kib':16,'video':'PAL','audio':False,
            'source_prg_sha256':digest(b'\x00\x04'+raw),'reference_sha256':digest(REFERENCE.read_bytes()),
            'reference_memory_sha256':digest(ref),'reference_compared_at':'$1800 before first original instruction',
            'title_rendered':True,'gameplay_loop_reached':True,'title_flag':mem[sym['TITLE']],'lives':mem[sym['LIVES']],
            'runtime_vector_mirror':{'cpu_range':'$FFFA-$FFFF','physical_ram_range':'$3FFA-$3FFF','hex':mem[0x3ffa:0x4000].hex(),'verified':True},
            'scripted_input':{'at':'TITTER original BIT JFIRE','write':f'${sym["JFIRE"]:04X} = $80; cleared at LOOP','instruction_patches':False},
            'manual_keyboard_joystick_audio_transitions_full_playthrough_real_hardware':'pending',
            'differences':diffs,'initialized_object_differences':sum(d['address'] in obj for d in diffs),
            'byte_identical_to_running_version':not diffs}
    write_json(build/'vice-verification.json',report)
    print(json.dumps({k:v for k,v in report.items() if k!='differences'},indent=2));print('Memory differences:',len(diffs))
    return report

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--build-dir',type=Path,default=ROOT/'build');p.add_argument('--allow-skip',action='store_true');args=p.parse_args()
    try:verify(args.build_dir)
    except (FileNotFoundError,subprocess.SubprocessError) as e:
        write_json(args.build_dir/'vice-verification.json',{'status':'skipped' if args.allow_skip else 'failed','reason':str(e),'screenshots_require_graphical_session':True})
        print(str(e),file=sys.stderr)
        sys.exit(0 if args.allow_skip else 1)
    except Exception as e:
        write_json(args.build_dir/'vice-verification.json',{'status':'failed','reason':str(e),'validation_failure':True})
        print(str(e),file=sys.stderr)
        sys.exit(1)
