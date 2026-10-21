#!/usr/bin/env python3
"""Regenerate analysis and graphics in temporary directories and compare every output."""
import tempfile
from pathlib import Path
from analyze_codebase import analyze
from render_game_graphics import generate
from restore_c16 import ROOT, digest

def check():
    with tempfile.TemporaryDirectory(prefix='xargon-generated-') as temp:
        tmp=Path(temp);a=tmp/'analysis';analyze(ROOT/'build',a);generate(a/'asset-data.json',a/'graphics')
        expected={p.relative_to(a) for p in a.rglob('*') if p.is_file()}
        actual={p.relative_to(ROOT/'docs/analysis') for p in (ROOT/'docs/analysis').rglob('*') if p.is_file() and p.name!='README.md' and p.name!='.DS_Store'}
        if expected!=actual:raise ValueError(f'Generated output set differs: {expected^actual}')
        for p in sorted(expected):
            if (a/p).read_bytes()!=(ROOT/'docs/analysis'/p).read_bytes():raise ValueError(f'Stale generated analysis/graphics: {p}; run make docs')
    print('Analysis and graphics are current:',len(expected),'files')
if __name__=='__main__':check()
