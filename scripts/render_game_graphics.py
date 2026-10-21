#!/usr/bin/env python3
"""Deterministic original-byte graphics reconstruction; no redrawn game artwork."""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from restore_c16 import ROOT, digest, write_json

PAPER='#f4f7fb';INK='#152c43';MUTED='#50657a'

def label(im,xy,text,size=17,fill=INK):
    ImageDraw.Draw(im).text(xy,text,font=ImageFont.load_default(size=size),fill=fill)

def canvas(title,note,height,width=1200):
    im=Image.new('RGB',(width,height),PAPER);label(im,(25,18),title,26);label(im,(25,60),note,16,MUTED);return im

def zoom(im,scale):return im.resize((im.width*scale,im.height*scale),Image.Resampling.NEAREST)

def save(im,path):im.save(path,compress_level=9,optimize=False)

class Graphics:
    def __init__(self,data,palette):
        self.data=data;self.palette=palette
    def table(self,n):return bytes.fromhex(self.data['tables'][n]['hex'])
    def bank(self,n):return bytes.fromhex(self.data['banks'][n]['hex'])
    def render(self,rows,bank,attr=0x78,colors=(0,0x34,0x65)):
        # TED multicolor window: bit 3 in the attribute selects 2-bit rendering.
        im=Image.new('RGB',(8*len(rows[0]),8*len(rows)));pens=[self.palette[i&0x7f] for i in (*colors,attr&0x77)]
        for r,row in enumerate(rows):
            for c,code in enumerate(row):
                glyph=bank[code*8:code*8+8]
                if len(glyph)!=8:raise ValueError('Missing glyph')
                for y,b in enumerate(glyph):
                    for x in range(8):
                        index=(b>>(6-2*(x//2)))&3 if attr&8 else 3 if b&(0x80>>x) else 0
                        im.putpixel((c*8+x,r*8+y),tuple(pens[index]))
        return im
    def player(self,offset):
        bank=bytearray(self.bank('font'));bank[0x3e0:0x440]=bytes(96);raw=self.table('SHPDT1')
        for c in range(4):bank[0x3e0+c*24+offset:0x3e0+c*24+offset+16]=raw[c*16:(c+1)*16]
        codes=list(self.table('SHPCHR'));rows=[codes[i:i+4] for i in (0,4,8)]
        wave=self.data['waves'][0]
        return self.render(rows,bank,0x2a,tuple(self.data['startup_state'][n] for n in ['BAKCOL','SHIPC1','SHIPC2']))

def generate(assets,output):
    output.mkdir(parents=True,exist_ok=True)
    data=json.loads(assets.read_text());palettefile=ROOT/'config/ted-palette.json';palette=json.loads(palettefile.read_text());g=Graphics(data,palette['rgb'])
    im=canvas('Player ship: source columns become twelve writable glyphs','SHPDT1: 64 bytes | SHIPCH $3BE0 | 4 columns x 16 rows | twelve screen cells',690)
    for offset in range(8):
        x=35+(offset%4)*290;y=112+(offset//4)*220
        im.paste(zoom(g.player(offset),6),(x,y));label(im,(x,y+152),f'YPIX {offset}: vertical glyph phase',16)
    label(im,(25,571),'SHPCHR screen rows: 124 127 130 133 / 125 128 131 134 / 126 129 132 135',19)
    label(im,(25,615),'The game starts at phase 3 and moves by 2. This sheet includes all eight representable phases.',17,MUTED)
    save(im,output/'player-assembly.png')
    frames=[zoom(g.player(i),5) for i in (3,1,7,5)]
    frames[0].save(output/'player-phases.gif',save_all=True,append_images=frames[1:],duration=250,loop=0,optimize=False,disposal=2)
    im=canvas('Sixteen alien designs: both original frames','BJH $0400-$07FF | 64 bytes per design | two 2 x 2 hires frames | neutral black/white key',1280)
    pool=g.bank('aliens')
    for i in range(16):
        x=25+(i%4)*295;y=110+(i//4)*285
        label(im,(x,y),f'Wave {i+1:02d} | ${0x400+i*64:04X}',19)
        for f in range(2):
            rows=[[f*4,f*4+1],[f*4+2,f*4+3]];tile=g.render(rows,pool[i*64:i*64+64],0x71)
            im.paste(zoom(tile,5),(x+f*100,y+40));label(im,(x+f*100,y+127),f'Frame {f}',15)
    save(im,output/'alien-variants.png')
    raw=g.table('BANNER');rows=[]
    for r in range(16):
        values=[v for b in raw[r*20:(r+1)*20] for v in [b>>4,b&15]]
        rows.append([136+v if v else 32 for v in values])
    im=canvas('Title artwork: packed nibbles become screen glyphs','BANNER: 320 bytes | 16 rows x 40 cells | neutral hires preview; title colours animate in the game',560,1050)
    im.paste(zoom(g.render(rows,g.bank('font'),0x71),3),(30,115));label(im,(30,510),'Nibble zero -> space 32. Other nibbles -> code 136 + value. Row order is preserved.',17,MUTED)
    save(im,output/'title-reconstruction.png')
    frames=[zoom(g.render([[f*4,f*4+1],[f*4+2,f*4+3]],pool[:64],0x71),10) for f in range(2)]
    frames[0].save(output/'alien-frames.gif',save_all=True,append_images=frames[1:],duration=250,loop=0,optimize=False,disposal=2)
    # Directly indexed source-bank atlas, with colour indices labelled as an interpretation key.
    for name in ['terrain','font']:
        bank=g.bank(name);im=canvas(name.capitalize()+' character atlas','Codes and RAM addresses | neutral index-key preview; not a final raster palette',1290,1000)
        for code in range(256):
            x=16+(code%16)*61;y=110+(code//16)*73;im.paste(zoom(g.render([[code]],bank,0x78),4),(x,y));label(im,(x,y+35),f'{code:03d}',12);label(im,(x,y+49),f'{data["banks"][name]["address"]+code*8:04X}',11,MUTED)
        # Preserve an actual indexed PNG alongside the vector index atlases.
        save(im.convert('P',palette=Image.Palette.ADAPTIVE,colors=256),output/f'{name}-indexed.png')
    im=canvas('Landscape motifs: source bytes in display order','Bottom: eight columns x four rows. Top: four columns x two rows. Columns are stored bottom first.',1120)
    terrain=g.bank('terrain');wave=data['waves'][0];colors=(wave['background'],wave['multi1'],wave['multi2'])
    for i in range(6):
        x=25+(i%3)*390;y=112+(i//3)*230;rows=[[i*32+c*4+3-r for c in range(8)] for r in range(4)]
        im.paste(zoom(g.render(rows,terrain,wave['land_attribute'],colors),5),(x,y));label(im,(x,y+171),f'Bottom {i}: codes {i*32}-{i*32+31}',17)
    for i in range(8):
        x=25+(i%4)*290;y=610+(i//4)*180;rows=[[192+i*8+c*2+1-r for c in range(4)] for r in range(2)]
        im.paste(zoom(g.render(rows,terrain,wave['land_attribute'],colors),5),(x,y));label(im,(x,y+93),f'Top {i}: codes {192+i*8}-{199+i*8}',16)
    label(im,(25,1020),'Rendered with the first wave attributes and the explicit VICE colodore TED palette.',17,MUTED)
    save(im,output/'terrain-composition.png')
    im=canvas('Runtime replacements: fuel, laser, terrain animation and explosions','Original tables and captured original-routine output. Explosion masks vary with TED state.',1030)
    for phase in range(2):
        b=bytearray(g.bank('font'));raw=g.table('FUELDA')[phase*24:phase*24+24]
        for c in range(3):b[0x5a0+c*16:0x5a0+c*16+8]=raw[c*8:c*8+8];b[0x5a8+c*16:0x5b0+c*16]=bytes(8)
        codes=list(g.table('FUELCH'));offsets=list(g.table('FUELYP'));rows=[[codes[offsets.index(r*40+c)] for c in range(3)] for r in range(2)];im.paste(zoom(g.render(rows,b,0x6f),7),(30+phase*260,120));label(im,(30+phase*260,244),f'Fuel horizontal phase {phase}',17)
    label(im,(600,124),'Laser: glyph 63 at $39F8',19)
    for i,row in enumerate(g.table('FLOYD')):
        b=bytearray(g.bank('font'));b[0x1f8:0x200]=bytes(8);b[0x1f8+row]=255
        im.paste(zoom(g.render([[63]],b,0x61),5),(610+i*120,173));label(im,(610+i*120,223),f'row {row}',15)
    for t,n in enumerate(['CHR87','CHR91']):
        raw=g.table(n);label(im,(30,330+t*150),f'{n}: 4 x 8-byte frames',19)
        for f in range(4):im.paste(zoom(g.render([[0]],raw[f*8:f*8+8],0x78),7),(340+f*170,315+t*150))
    raw=bytes.fromhex(data['runtime_explosions']['waves'][0]['hex']);label(im,(30,655),'Wave 1 explosion: captured CALEXP sample',22)
    for f in range(4):
        tile=g.render([[f*4,f*4+1],[f*4+2,f*4+3]],raw,0x78);im.paste(zoom(tile,7),(30+f*280,708));label(im,(30+f*280,831),f'Frame {f}: codes {221+f*4}-{224+f*4}',17)
    label(im,(30,916),'The original routine alternates alien masks and ANDs TED-derived bytes repeatedly.',18,MUTED)
    label(im,(30,954),'These are measured glyph samples; the GIF delay and preview colours are illustrative.',17,MUTED)
    save(im,output/'runtime-effects.png')
    capture=Image.open(ROOT/'docs/images/restored-gameplay.png').convert('RGB')
    im=canvas('From source bytes to the displayed game','Left: actual VICE startup capture. Right: the memory and raster bands that compose it.',850)
    im.paste(zoom(capture,2),(25,105));x=815
    for i,(title,detail) in enumerate([('HUD: rows 0-1','$0C00/$0800; font at $3800'),('Top terrain: rows 2-3','$0C50; bank $1000; TOPLX'),('Play area: rows 4-19','font/glyph RAM; fixed X'),('Bottom: rows 20-23','$0F20; bank $1000; BOTLX'),('Message: row 24','$0FC0; font; MESSX')]):
        label(im,(x,130+i*95),title,18);label(im,(x,165+i*95),detail,16,MUTED)
    label(im,(25,730),'Screen cells select glyphs; the corresponding attributes are $0400 bytes earlier in RAM.',20)
    label(im,(25,774),'IRQ service changes banks, colours and fine scroll within the same frame. This is not a TED emulator.',17,MUTED)
    save(im,output/'screen-composition.png')
    # Fixture-derived pixel geometry and source bytes are exported beside the illustrations.
    manifest={'method':'Original byte decoding, source table composition and retained original-routine samples; nearest-neighbour enlargement; no redrawn artwork.',
              'asset_data_sha256':digest(assets.read_bytes()),'palette':palette,
              'palette_file_sha256':digest(palettefile.read_bytes()),'script_sha256':digest(Path(__file__).read_bytes()),
              'screenshot_sha256':digest((ROOT/'docs/images/restored-gameplay.png').read_bytes()),
              'animation_order':[3,1,7,5],'animation_delay_ms':250,'timing':'Illustrative phase playback; not measured game animation cadence.',
              'images':{p.name:{'sha256':digest(p.read_bytes()),'size':list(Image.open(p).size),'mode':Image.open(p).mode} for p in sorted(output.iterdir()) if p.suffix in ('.png','.gif')}}
    write_json(output/'graphics-manifest.json',manifest);print('Generated',len(manifest['images']),'graphics references')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--assets',type=Path,default=ROOT/'docs/analysis/asset-data.json');p.add_argument('--output-dir',type=Path,default=ROOT/'docs/analysis/graphics');a=p.parse_args();generate(a.assets,a.output_dir)
