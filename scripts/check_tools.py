#!/usr/bin/env python3
"""Record actual tools without confusing package versions with executable reports."""
import json
import platform
import re
import subprocess
import sys
from pathlib import Path
from restore_c16 import ROOT, tool, write_json

def check():
    result={'python':{'version':platform.python_version(),'executable':sys.executable},'minimums':{'python':'3.9','cc65':'2.18','vice':'3.10','pillow':'10.1','node':'22','platformio':'6.1.19'}}
    for name,args in [('ca65',['--version']),('ld65',['--version']),('node',['--version']),('pio',['--version'])]:
        try:
            executable=tool(name);p=subprocess.run([executable,*args],capture_output=True,text=True,timeout=10)
            result[name]={'executable':executable,'output':(p.stdout+p.stderr).strip(),'exit_code':p.returncode}
        except (FileNotFoundError,subprocess.SubprocessError) as e:result[name]={'available':False,'reason':str(e)}
    # macOS VICE exits early for --version; use the successful bounded run's banner.
    p=ROOT/'build/gameplay-console.log'
    try:
        found=tool('xplus4');banner=re.search(r'VICE Version ([\d.]+)',p.read_text()) if p.exists() else None
        result['vice']={'executable':found,'version':banner.group(1) if banner else None,'method':'successful gameplay run banner' if banner else 'no recorded run banner'}
    except FileNotFoundError as e:result['vice']={'available':False,'reason':str(e)}
    try:
        import PIL
        result['pillow']={'version':PIL.__version__}
    except ImportError:result['pillow']={'available':False}
    write_json(ROOT/'docs/verification/tool-checks.json',result);print(json.dumps(result,indent=2))
if __name__=='__main__':check()
