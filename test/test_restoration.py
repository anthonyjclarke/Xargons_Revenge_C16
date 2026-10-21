"""Regression tests for the historical source, file formats and assembled output."""
import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from restore_c16 import ROOT, LOAD, FALLBACKS, build_game, digest, mos_hex, prepare_sources, IMAGES
from d64_image import D64Image
from source_converter import convert, flatten
from catalogue_inputs import catalogue

class RestorationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp=tempfile.TemporaryDirectory(prefix='xargon-test-');cls.build=Path(cls.tmp.name)
        with contextlib.redirect_stdout(io.StringIO()):cls.output=build_game(cls.build).read_bytes()
        cls.sources,cls.manifest,cls.binaries=prepare_sources(cls.build/'inputs')
    @classmethod
    def tearDownClass(cls):cls.tmp.cleanup()
    def test_prg_header_extent_and_hash(self):
        self.assertEqual(self.output[:2],b'\x00\x04');self.assertEqual(len(self.output),15362)
        self.assertEqual(digest(self.output),'32c13c8867ea97bb4fd60ac9a73e5d7a600c04ece5699ac37680143c12adce33')
    def test_every_object_byte(self):
        obj=mos_hex(self.sources['OBJ']);self.assertEqual(len(obj),8094);self.assertEqual((min(obj),max(obj)),(0x1800,0x379d))
        for a,b in obj.items():self.assertEqual(self.output[2+a-LOAD],b,hex(a))
    def test_source_priority_and_fallbacks(self):
        rows=[f for f in self.manifest['files'] if f['fallback']]
        self.assertEqual({r['name'] for r in rows},set(FALLBACKS));self.assertEqual(len(rows),6)
        self.assertTrue(any('LDA #5'==l for l in self.sources['PLAY-GAME']))
        self.assertIn('SELF', ''.join(self.sources['TITLE-WORK']))
    def test_loader_selected_assets_and_relocation(self):
        for name,addr,size in [('BJH',0x400,1024),('LANDSCAPE-2',0x1000,2048),('FRAK!',0x3800,2048)]:
            self.assertEqual(self.output[2+addr-LOAD:2+addr-LOAD+size],self.binaries[name][2:])
        report=json.loads((self.build/'comparison.json').read_text())
        self.assertEqual(len(report['terrain_source_vs_loader_differences']),29)
    def test_original_session_input_hashes(self):
        baseline=json.loads((ROOT/'docs/verification/original-inputs.json').read_text())['files']
        for path,info in baseline.items():self.assertEqual(digest((ROOT/path).read_bytes()),info['sha256'],path)
    def test_complete_catalogue_archive_and_input_hashes(self):
        expected=json.loads((ROOT/'docs/verification/input-catalogue.json').read_text())
        self.assertEqual(catalogue(),expected)
    def test_missing_ambiguous_recursive_includes(self):
        for sources in [{'MAIN':['.LIB LOST*']},{'MAIN':['.LIB AL*'],'ALPHA':[],'ALTO':[]},{'MAIN':['.LIB MAIN*']}]:
            with self.assertRaises(ValueError):flatten(sources,'MAIN')
    def test_converter_retains_operands_equates_strings_and_reservations(self):
        text=convert([('X',1,'SELFMD LDA $FFFF,X'),('X',2,'TED = $FF00'),('X',3,"TEXT .BYTE 'A;B',0"),('X',4,"LDA #'Z"),('X',5,'BUF *=*+16')])
        for expected in ['SELFMD: LDA $FFFF,X','TED = $FF00','TEXT: .BYTE "A;B",0',"LDA #'Z'",'BUF: .res 16']:self.assertIn(expected,text)
    def test_malformed_mos_records(self):
        valid=';011800AA00C3'
        self.assertEqual(mos_hex([valid,';0000010001']),{0x1800:0xaa})
        for records in [[valid],[valid,';0000010002'],[valid,valid,';0000020002'],[';011800AA0000'],[valid,';0000010001',valid]]:
            with self.assertRaises(ValueError):mos_hex(records)
    def test_corrupt_and_cyclic_disks(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'bad.d64';p.write_bytes(b'broken')
            with self.assertRaises(ValueError):D64Image(p)
        disk=D64Image(IMAGES[0]);raw=bytearray(disk.data);raw[:2]=b'\x01\x00';disk.data=raw
        with self.assertRaisesRegex(ValueError,'Cyclic'):list(disk.chain(1,0))
        with self.assertRaises(ValueError):disk.sector(36,0)

if __name__=='__main__':unittest.main()
