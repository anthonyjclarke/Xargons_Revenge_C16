#!/usr/bin/env python3
"""Save bounded verification evidence in a reproducible ZIP, excluding build products."""
from pathlib import Path
import json
import re
import zipfile
from restore_c16 import ROOT, write_json, digest

def retain():
    build=ROOT/'build';out=ROOT/'docs/verification'
    for src,dest in [('comparison.json','build-comparison.json'),('recovery-manifest.json','source-manifest.json'),('vice-verification.json','vice-verification.json'),('rule-probes/rule-probes.json','rule-probes.json')]:
        (out/dest).write_bytes((build/src).read_bytes())
    paths=[]
    for folder in [build,build/'rule-probes']:
        for p in folder.iterdir():
            if p.is_file() and (p.suffix=='.mon' or p.name.endswith(('-monitor.log','-console.log','-command.json','-vice.log','memory.bin')) or (folder.name=='rule-probes' and p.suffix=='.bin')):
                paths.append(p)
    archive=out/'vice-evidence.zip'
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(paths):
            info=zipfile.ZipInfo(str(p.relative_to(build)),(1980,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16
            z.writestr(info,p.read_bytes())
    write_json(out/'evidence-manifest.json',{'archive':'vice-evidence.zip','sha256':digest(archive.read_bytes()),'members':{str(p.relative_to(build)):digest(p.read_bytes()) for p in sorted(paths)},'note':'Captured local evidence; paths and cycle counters are actual run data, not deterministic emulator state. ZIP container dates are fixed.'})
if __name__=='__main__':retain()
