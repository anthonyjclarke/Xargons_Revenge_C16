#!/usr/bin/env python3
"""Catalogue unchanged historical files and compare the legacy ZIP's extraction."""
import argparse
import json
import subprocess
import tempfile
import zipfile
import zlib
from pathlib import Path
from restore_c16 import ROOT, digest, write_json


def catalogue():
    rows=[]
    for root in [ROOT/'Original Source Recovered',ROOT/'Original Artifacts']:
        for p in sorted(root.rglob('*')):
            if not p.is_file() or p.name=='.DS_Store':continue
            data=p.read_bytes()
            kind=('disk image' if p.suffix.lower()=='.d64' else 'archive' if p.suffix.lower()=='.zip' else
                  'historical source export' if p.suffix.lower() in ('.txt','.seq') else
                  'capture manifest/log' if p.suffix.lower() in ('.json','.log') else
                  'artwork, packaging or screenshot' if p.suffix.lower() in ('.png','.jpg','.pdf') else 'historical binary or utility')
            rows.append({'path':str(p.relative_to(ROOT)),'bytes':len(data),'sha256':digest(data),'category':kind})
    ref=ROOT/'xargons_revenge.prg';rows.append({'path':ref.name,'bytes':ref.stat().st_size,'sha256':digest(ref.read_bytes()),'category':'compressed running reference'})
    archive=ROOT/"Original Source Recovered/1992/DISK9 - Xargon's Revenge.ZIP"
    with zipfile.ZipFile(archive) as z:
        ziprows=[]
        for f in z.infolist():
            if f.is_dir() or f.filename.endswith('.DS_Store'):continue
            p=ROOT/'Original Source Recovered/1992'/f.filename
            raw=p.read_bytes()
            if len(raw)!=f.file_size or zlib.crc32(raw)!=f.CRC:raise ValueError(f'Archive CRC/length mismatch: {f.filename}')
            ziprows.append({'name':f.filename,'sha256':digest(raw),'crc32':f'{f.CRC:08x}','bytes':len(raw)})
    # unzip supports these historical Implode and Shrunk members; never extract in place.
    with tempfile.TemporaryDirectory(prefix='xargon-zip-') as tmp:
        subprocess.run(['unzip','-qq',str(archive),'-d',tmp],check=True)
        for f in ziprows:
            if (Path(tmp)/f['name']).read_bytes()!=(ROOT/'Original Source Recovered/1992'/f['name']).read_bytes():
                raise ValueError('ZIP member differs from preserved extracted copy')
        extra={p.name for p in (ROOT/'Original Source Recovered/1992/DISK9').iterdir() if p.is_file() and p.name!='.DS_Store'}-{Path(f['name']).name for f in ziprows}
        if extra:raise ValueError(f'Extra legacy files: {extra}')
    return {'excluded_host_metadata':['.DS_Store'],'inputs':rows,'legacy_archive_comparison':{'method':'unzip to temporary directory; byte comparison; CRC/length also checked','files':ziprows,'byte_identical':True}}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=ROOT/'docs/verification/input-catalogue.json');a=p.parse_args();write_json(a.output,catalogue())
