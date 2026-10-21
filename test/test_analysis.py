"""Check exported assets and composition against preserved bytes and VICE fixtures."""
import json
import sys
import unittest
import zipfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from restore_c16 import ROOT, digest
from render_game_graphics import Graphics

class AnalysisTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.assets=json.loads((ROOT/'docs/analysis/asset-data.json').read_text())
        cls.index=json.loads((ROOT/'docs/analysis/codebase-index.json').read_text())
        cls.g=Graphics(cls.assets,json.loads((ROOT/'config/ted-palette.json').read_text())['rgb'])
    def test_exported_banks_match_original_binary_payloads(self):
        for bank in self.assets['banks'].values():
            raw=(ROOT/bank['source']).read_bytes()
            self.assertEqual(raw[2:],bytes.fromhex(bank['hex']))
            self.assertEqual(digest(raw),bank['source_sha256'])
            self.assertEqual(digest(raw[2:]),bank['payload_sha256'])
    def test_wave_records_resolve_to_exported_pattern_streams(self):
        tables=self.assets['tables'];patterns={v['address']:v for n,v in tables.items() if n.startswith('PATD')}
        self.assertEqual(len(self.assets['waves']),16)
        for wave in self.assets['waves']:
            raw=bytes.fromhex(patterns[wave['movement_address']]['hex'])
            self.assertEqual(raw[-1],255)
            self.assertTrue(all(v<16 for v in raw[:-1]))
    def test_reconstructed_player_matches_original_runtime_glyphs(self):
        with zipfile.ZipFile(ROOT/'docs/verification/vice-evidence.zip') as z:
            mem=z.read('gameplay-memory.bin')
        codes=list(self.g.table('SHPCHR'));rows=[codes[i:i+4] for i in (0,4,8)]
        state=self.assets['startup_state'];colors=tuple(state[n] for n in ['BAKCOL','SHIPC1','SHIPC2'])
        expected=self.g.render(rows,mem[0x3800:0x4000],state['SHPINK'],colors)
        self.assertEqual(expected.tobytes(),self.g.player(3).tobytes())

if __name__=='__main__':unittest.main()
