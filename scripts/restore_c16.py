#!/usr/bin/env python3
"""Reassemble Xargon's Revenge from the preserved disks and explicit 1992 fallbacks."""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path
from d64_image import D64Image
from source_converter import convert, flatten

ROOT = Path(__file__).resolve().parents[1]
INPUTS = ROOT / 'Original Source Recovered'
OLDER = INPUTS / '1992/DISK9'
REFERENCE = ROOT / 'Original Artifacts/xargons_revenge.prg'
IMAGES = [INPUTS/'2026/XargonsRevenge-C16.d64', INPUTS/"2026/Xargon'sRevenge-C16.d64"]
EXTRACTED = [INPUTS/f'2026/Xargons-Revenge-C16-Side{i}' for i in (1, 2)]
FALLBACKS = {'COMPLETED-SHEET':'COMPLETE.TXT', 'DATA-LAND/CHARS':'DATALAND.TXT',
             'RASTER-ROUTINES':'RASTERRO.TXT', 'WHOOPPEE-MESSAGE':'WHOOPPEE.TXT',
             'FIRING-MEGA/CODE':'FIRINGME.TXT', 'ALI-PRINT&CLEAR':'ALIPRINT.TXT'}
LOAD = 0x0400
ENTRY = 0x1800


def digest(data):
    return hashlib.sha256(data).hexdigest()


def tool(name):
    found = shutil.which(name)
    if found:
        return found
    for directory in ('/opt/homebrew/bin', '/usr/local/bin'):
        candidate = Path(directory) / name
        if candidate.is_file():
            return str(candidate)
    raise FileNotFoundError(f'{name} not found; see docs/BUILD_AND_RUN.md')


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=True)+'\n')


def prepare_sources(build):
    build.mkdir(parents=True, exist_ok=True)
    sources, provenance, binaries, disks = {}, [], {}, []
    for image, folder in zip(IMAGES, EXTRACTED):
        disk = D64Image(image).files()
        manifest = json.loads((folder/'manifest.json').read_text())
        if digest(image.read_bytes()) != manifest['source_sha256']:
            raise ValueError(f'Disk hash differs from extraction manifest: {image.name}')
        records = {bytes.fromhex(f['petscii_name_hex']).rstrip(b'\xa0').decode('ascii'):f for f in manifest['files']}
        if len(records) != len(manifest['files']) or set(records) != {f.name for f in disk}:
            raise ValueError('Disk/extraction directory mismatch')
        for f in disk:
            record = records[f.name]
            if not f.closed or f.kind.lower() != record['type']:
                raise ValueError(f'Unclosed/type mismatch: {f.name}')
            data = f.data
            if data != (folder/record['output']).read_bytes() or digest(data) != record['sha256']:
                raise ValueError(f'Disk/extraction byte mismatch: {f.name}')
            row = {'name':f.name, 'kind':f.kind, 'bytes':len(data), 'sha256':digest(data),
                   'source':str(image.relative_to(ROOT)), 'extracted_copy':str((folder/record['output']).relative_to(ROOT)),
                   'fallback':False, 'closed':f.closed, 'normalization':'none for binary; CR/CRLF to logical lines for SEQ; latin-1 maps comment byte AF to U+00AF; generated assembly UTF-8'}
            provenance.append(row)
            # Side 1 and side 2 each have a distinct LOADER; namespaces stay separate.
            if folder == EXTRACTED[1]:
                if f.kind == 'SEQ':
                    sources[f.name] = data.decode('latin1').splitlines()
                else:
                    binaries[f.name] = data
        disks.append({'path':str(image.relative_to(ROOT)), 'sha256':digest(image.read_bytes()),
                      'files':len(disk), 'extraction_matches':True})
    index = (OLDER/'INDEX').read_text()
    mapped = {name:stem+'.TXT' for name, stem in re.findall(r'^\d+\s+"([^"]+)"\s+SEQ\s+(\S+)\s+TXT', index, re.M)}
    for name, filename in FALLBACKS.items():
        if name in sources or mapped.get(name) != filename:
            raise ValueError(f'Fallback not supported by original INDEX: {name}')
        data = (OLDER/filename).read_bytes()
        sources[name] = data.decode('ascii').upper().splitlines()
        provenance.append({'name':name, 'kind':'SEQ', 'source':str((OLDER/filename).relative_to(ROOT)),
                           'sha256':digest(data), 'bytes':len(data), 'fallback':True,
                           'normalization':'ASCII uppercase and CRLF to logical lines; MOS case convention'})
    manifest = {'disks':disks, 'index_sha256':digest((OLDER/'INDEX').read_bytes()), 'files':provenance,
                'source_priority':'2026 disk bytes; only six explicit INDEX-mapped 1992 fallbacks',
                'excluded_host_metadata':['.DS_Store']}
    write_json(build/'recovery-manifest.json', manifest)
    return sources, manifest, binaries


def mos_hex(lines):
    memory, records, terminal = {}, 0, False
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if terminal:
            raise ValueError('Data after MOS hex terminator')
        if not line.startswith(';'):
            raise ValueError('Invalid MOS hex record')
        raw = bytes.fromhex(line[1:])
        if len(raw) < 5:
            raise ValueError('MOS hex record is too short')
        count = raw[0]
        if len(raw) != count+5 or sum(raw[:-2]) != int.from_bytes(raw[-2:], 'big'):
            raise ValueError('MOS hex length/checksum mismatch')
        address = int.from_bytes(raw[1:3], 'big')
        if not count:
            if address != records:
                raise ValueError('MOS hex record count mismatch')
            terminal = True
            continue
        if address+count > 0x10000:
            raise ValueError('MOS hex address overflow')
        records += 1
        for offset, byte in enumerate(raw[3:-2]):
            if address+offset in memory:
                raise ValueError('Overlapping MOS hex records')
            memory[address+offset] = byte
    if not terminal:
        raise ValueError('Missing MOS hex terminator')
    return memory


def assemble(build, sources, name, stem, config):
    lines = flatten(sources, name)
    (build/(stem+'.s')).write_text(convert(lines))
    write_json(build/(stem+'-source-lines.json'), [dict(module=n, line=i, text=l) for n,i,l in lines])
    subprocess.run([tool('ca65'), '-g', '-l', str(build/(stem+'.lst')), '-o', str(build/(stem+'.o')), str(build/(stem+'.s'))], check=True)
    subprocess.run([tool('ld65'), '-C', str(config), '-o', str(build/(stem+'.bin')),
                    '-m', str(build/(stem+'.map')), '-Ln', str(build/(stem+'.labels')),
                    '--dbgfile', str(build/(stem+'.dbg')), str(build/(stem+'.o'))], check=True)
    return list(dict.fromkeys(n for n,_,_ in lines))


def build_game(build):
    build = build.resolve()
    sources, manifest, binaries = prepare_sources(build)
    used = assemble(build, sources, 'REVENGE', 'xargon', ROOT/'config/c16.cfg')
    code = (build/'xargon.bin').read_bytes()
    obj = mos_hex(sources['OBJ'])
    differences = [{'address':a, 'assembled':code[a-ENTRY] if ENTRY<=a<ENTRY+len(code) else None,
                    'object':b} for a,b in obj.items() if not ENTRY<=a<ENTRY+len(code) or code[a-ENTRY]!=b]
    memory = bytearray(0x4000-LOAD)
    def install(address, data):
        if not LOAD<=address or address+len(data)>0x4000:
            raise ValueError('Asset outside 16 KB output memory')
        memory[address-LOAD:address-LOAD+len(data)] = data
    assets=[]
    for name,address,size in [('BJH',0x0400,1024), ('LANDSCAPE-2',0x1000,2048), ('FRAK!',0x3800,2048)]:
        raw=binaries[name]
        if len(raw)!=size+2:
            raise ValueError(f'Unexpected {name} asset size')
        saved=int.from_bytes(raw[:2],'little')
        if saved != (0x2000 if name=='BJH' else address):
            raise ValueError(f'Unexpected {name} saved address')
        install(address,raw[2:])
        assets.append({'name':name,'saved_address':saved,'runtime_address':address,'bytes':size,
                       'sha256':digest(raw), 'payload_sha256':digest(raw[2:]),
                       'selection':'C16 autobooter and original BJH relocation loader; no reference PRG bytes'})
    install(ENTRY,code)
    output=build/'xargons-revenge.prg'
    output.write_bytes(LOAD.to_bytes(2,'little')+memory)
    # Editable landscape source is compared to the loader-selected binary; it is not silently substituted.
    terrain_used=assemble(build,sources,'ASSEM-GRAPHS','terrain',ROOT/'config/terrain.cfg')
    terrain=(build/'terrain.bin').read_bytes()
    landscape=binaries['LANDSCAPE-2'][2:]
    asset_diffs=[{'address':0x1000+i,'source':x,'loader_asset':y} for i,(x,y) in enumerate(zip(terrain,landscape)) if x!=y]
    for row in manifest['files']:
        if row['kind']=='SEQ' and row['name'] in used:row['role']='active source'
        elif row['name'] in ('OBJ','O.ALI'):row['role']='object listing' if row['name']=='OBJ' else 'alternative alien object listing'
        elif row['kind']=='SEQ' and row['name'] in terrain_used:row['role']='graphics source comparison'
        elif row['name'] in ('BJH','LANDSCAPE-2','FRAK!') and row.get('source')==str(IMAGES[1].relative_to(ROOT)):row['role']='active loader-selected graphics'
        elif row['name'].startswith('ALIBUM') or row['name'] in ('HILLS','LANDSCAPE-1','TITLE-DATA','XARG-SCREEN'):row['role']='alternative graphics or design data'
        elif row['kind']=='PRG':row['role']='historical development utility, loader or saved fragment'
        else:row['role']='unused source'
    manifest.update(used_modules=used, graphics_source_modules=terrain_used, assets=assets)
    write_json(build/'recovery-manifest.json',manifest)
    report={'load_address':f'${LOAD:04X}','entry_address':f'${ENTRY:04X}','output_bytes':output.stat().st_size,
            'sha256':digest(output.read_bytes()),'code_and_embedded_data_bytes':len(code),
            'object_listing_bytes':len(obj),'object_listing_differences':differences,
            'object_listing_range':[min(obj),max(obj)+1],
            'unrecorded_code_bytes':[a for a in range(ENTRY,ENTRY+len(code)) if a not in obj],
            'terrain_source_bytes':len(terrain),'terrain_source_vs_loader_differences':asset_diffs,
            'reference_sha256':digest(REFERENCE.read_bytes()),'reference_runtime_comparison':'separate check: scripts/verify_vice.py; retained docs/verification/vice-verification.json'}
    write_json(build/'comparison.json',report)
    print(json.dumps(report,indent=2))
    if differences or min(obj)!=ENTRY or max(obj)+1!=ENTRY+len(code):
        raise ValueError('Assembled output differs from surviving OBJ records')
    return output

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--build-dir',type=Path,default=ROOT/'build')
    build_game(p.parse_args().build_dir)
