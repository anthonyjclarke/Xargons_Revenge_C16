#!/usr/bin/env python3
"""Generate a static source index, code reference and original asset exports.

Table, source parser, listing ownership and neutral atlas helpers adapted from
Anthony Clarke's Tycoon Tex restoration. This is not a complete call graph.
"""
import argparse
import ast
import collections
import hashlib
import html
import json
import re
import zipfile
from pathlib import Path
from urllib.parse import quote
from restore_c16 import ROOT, LOAD, ENTRY, prepare_sources, digest, write_json, mos_hex
from source_converter import OPCODES, flatten, split_comment

def table(headers, rows):
    rows = [[str(c).replace('|', '/') for c in row] for row in [headers] + rows]
    widths = [max(3, max(len(row[i]) for row in rows)) for i in range(len(headers))]
    if max(widths) > 45:
        raise ValueError('Markdown table cell exceeds 45 characters')
    fmt = lambda row: '| ' + ' | '.join(v.ljust(widths[i]) for i, v in enumerate(row)) + ' |'
    return '\n'.join([fmt(rows[0]), fmt(['-' * w for w in widths])] + [fmt(r) for r in rows[1:]])


def parse_line(line):
    code, comment = split_comment(line)
    code = code.strip()
    definition = None
    if code and not code.startswith('.') and not code.startswith('*'):
        first, *rest = code.split(None, 1)
        if first not in OPCODES | {'DPINC', 'DPDEC'} and re.fullmatch(r'[A-Z][A-Z0-9_]*', first):
            definition = first
            code = rest[0] if rest else ''
        else:
            match = re.match(r'^([A-Z][A-Z0-9_]*)\s*=', code)
            if match:
                definition = match[1]
                code = code[len(definition):].lstrip()
    return definition, code, comment.lstrip(';* ')


def listing_owners(path):
    """Use printed PC changes so abbreviated long data lines retain full size."""
    owners = {}
    owner = None
    address = None
    pending = None
    for line in path.read_text().splitlines():
        match = re.match(r'^([0-9A-F]{6})[ r]', line)
        if not match:
            continue
        current = int(match[1], 16)
        if address is not None and current != address:
            if pending and 0 < current-address <= 0x2000:
                for a in range(max(address, 0x1800), min(current, 0x379E)):
                    owners[a] = pending
            pending = None
        address = current
        source = re.search(r'; SOURCE: (.+):\d+$', line)
        if source:
            owner = source[1]
        if re.fullmatch(r'(?:(?:[0-9A-F]{2}|xx)\s*)+', line[11:23].strip()):
            pending = owner
    return owners


def atlas(path, title, data, start, mode, columns=16):
    """Decode original glyph bits to SVG; colors are index keys, not a TED palette."""
    count = len(data) // 8
    cell_w, cell_h, scale = 60, 70, 5
    height = 75 + ((count+columns-1)//columns)*cell_h
    colors = ['#111827', '#ef4444', '#38bdf8', '#fef08a']
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{columns*cell_w}" height="{height}" viewBox="0 0 {columns*cell_w} {height}">',
           '<rect width="100%" height="100%" fill="#f8fafc"/>',
           f'<text x="12" y="24" font-family="monospace" font-size="16">{html.escape(title)}</text>',
           '<text x="12" y="45" font-family="monospace" font-size="12">Raw glyph bytes; neutral index colors; not final in-game palette.</text>']
    for i in range(count):
        x, y = (i % columns)*cell_w+10, (i//columns)*cell_h+65
        glyph = data[i*8:(i+1)*8]
        for row, byte in enumerate(glyph):
            width = 4 if mode == 'multicolor' else 8
            for col in range(width):
                value = (byte >> (6-col*2)) & 3 if mode == 'multicolor' else (byte >> (7-col)) & 1
                color = colors[value] if mode == 'multicolor' else ['#111827', '#e2e8f0'][value]
                w = scale*2 if mode == 'multicolor' else scale
                out.append(f'<rect x="{x+col*w}" y="{y+row*scale}" width="{w}" height="{scale}" fill="{color}"/>')
        out.append(f'<text x="{x}" y="{y+53}" font-family="monospace" font-size="10">{i:03d} {start+i*8:04X}</text>')
    out.append('</svg>')
    path.write_text('\n'.join(out)+'\n')


def analyze(build, output):
    output.mkdir(parents=True,exist_ok=True)
    sources,manifest,binaries=prepare_sources(build/'analysis-inputs')
    provenance={r['name']:r for r in manifest['files'] if r['kind']=='SEQ'}
    labels={n:int(a,16) for a,n in re.findall(r'^al ([0-9A-Fa-f]+) \.(\w+)$',(build/'xargon.labels').read_text(),re.M)}
    used=list(dict.fromkeys(n for n,_,_ in flatten(sources,'REVENGE')));main=set(used)
    owners=listing_owners(build/'xargon.lst');code=(build/'xargon.bin').read_bytes()
    if set(owners)!=set(range(ENTRY,ENTRY+len(code))):raise ValueError('Listing ownership must cover all object bytes')
    sizes=collections.Counter(owners.values());definitions={};modules=[];transfers=[];variables=[]
    for name,lines in sources.items():
        instructions=0
        for number,line in enumerate(lines,1):
            definition,body,comment=parse_line(line)
            if body=='.END':break
            if definition and name in main:
                kind='equate' if body.startswith('=') else 'label'
                if '*=*+' in body:kind='reserved'
                elif body.startswith(('.BYTE','.WORD')):kind='data'
                if definition in definitions:raise ValueError('Duplicate active definition '+definition)
                definitions[definition]={'symbol':definition,'module':name,'line':number,'address':labels.get(definition),
                                         'kind':kind,'comment':comment,'expression':body[1:].strip() if kind=='equate' else None}
                if kind=='reserved':
                    expr=body.split('*=*+',1)[1];size=int(expr[1:],16) if expr.startswith('$') else int(expr)
                    variables.append({'symbol':definition,'module':name,'address':labels[definition],'bytes':size,'source_line':number,'comment':comment})
            op=body.split(None,1)
            if op and op[0] in OPCODES:instructions+=1
            if name in main and op and op[0] in {'JSR','JMP','BCC','BCS','BEQ','BMI','BNE','BPL','BVC','BVS'} and len(op)==2:
                transfers.append({'module':name,'line':number,'operation':op[0],'operand':op[1]})
        owned=[a for a,n in owners.items() if n==name]
        modules.append({'name':name,'path':provenance[name].get('extracted_copy',provenance[name]['source']),
                        'source_sha256':provenance[name]['sha256'],'fallback':provenance[name]['fallback'],
                        'raw_bytes':provenance[name]['bytes'],'logical_lines':len(lines),'instruction_statements':instructions,
                        'active':name in main,'main_region_bytes':sizes[name],
                        'main_region_extent':[min(owned),max(owned)+1] if owned else None})
    def constant(expression):
        expr=re.sub(r'\$([0-9A-F]+)',r'0x\1',expression)
        def walk(node):
            if isinstance(node,ast.Constant) and type(node.value)==int:return node.value
            if isinstance(node,ast.Name):
                a=definitions[node.id]['address']
                if a is None:raise ValueError('unresolved')
                return a
            if isinstance(node,ast.BinOp):
                a,b=walk(node.left),walk(node.right)
                if isinstance(node.op,ast.Add):return a+b
                if isinstance(node.op,ast.Sub):return a-b
                if isinstance(node.op,ast.Mult):return a*b
            raise ValueError('unsupported expression')
        return walk(ast.parse(expr,mode='eval').body)
    for _ in range(6):
        for d in definitions.values():
            if d['kind']=='equate' and d['address'] is None:
                try:d['address']=constant(d['expression'])
                except (KeyError,ValueError,SyntaxError):pass
    for d in definitions.values():
        if d['kind']!='label':continue
        for later in sources[d['module']][d['line']-1:]:
            _,body,_=parse_line(later)
            if body:
                d['kind']='instruction-label' if body.split()[0] in OPCODES else 'data' if body.startswith(('.BYTE','.WORD')) else 'reserved' if body.startswith('*=*+') else 'control-label'
                if d['kind']=='reserved' and body.startswith('*=*+'):
                    size=constant(body.split('*=*+',1)[1]);variables.append({'symbol':d['symbol'],'module':d['module'],'address':d['address'],'bytes':size,'source_line':d['line'],'comment':d['comment']})
                break
    for t in transfers:
        target=re.match(r'^([A-Z][A-Z0-9_]*)',t['operand']);dest=definitions.get(target[1]) if target else None
        t['target_module']=dest['module'] if dest else None
        try:t['target_address']=constant(t['operand'])
        except (KeyError,ValueError,SyntaxError):t['target_address']=None
    symbols=sorted(definitions.values(),key=lambda d:d['symbol']);payload=(build/'xargons-revenge.prg').read_bytes()[2:]
    asset_data={'method':'Raw little-endian word and byte payloads. Data spans end at the next greater active symbol address; consult source for record semantics.',
                'prg_sha256':digest((build/'xargons-revenge.prg').read_bytes()),'tables':{},'banks':{}}
    addresses=sorted(set(d['address'] for d in symbols if d['address'] is not None and ENTRY<=d['address']<=ENTRY+len(code)))+[ENTRY+len(code)]
    for d in symbols:
        a=d['address']
        if d['kind']=='data' and a is not None and ENTRY<=a<ENTRY+len(code):
            end=next(v for v in addresses if v>a);raw=payload[a-LOAD:end-LOAD]
            asset_data['tables'][d['symbol']]={'address':a,'bytes':len(raw),'hex':raw.hex(),'module':d['module'],'source_line':d['line'],'input_sha256':provenance[d['module']]['sha256'],'payload_sha256':digest(raw)}
    for name,address,length in [('aliens',0x400,1024),('terrain',0x1000,2048),('font',0x3800,2048)]:
        binary={'aliens':'BJH','terrain':'LANDSCAPE-2','font':'FRAK!'}[name];raw=payload[address-LOAD:address-LOAD+length]
        source=next(r for r in manifest['files'] if r['name']==binary)
        asset_data['banks'][name]={'address':address,'bytes':length,'hex':raw.hex(),'glyph_bytes':8,'source':source['extracted_copy'],'source_sha256':source['sha256'],'payload_sha256':digest(raw)}
    # Actual movement records decoded from the table, not inferred from filenames.
    records=bytes.fromhex(asset_data['tables']['SHTABL']['hex'])
    asset_data['waves']=[{'index':i,'movement_address':int.from_bytes(records[i*8:i*8+2],'little'),'land_attribute':records[i*8+2],'multi1':records[i*8+3],'multi2':records[i*8+4],'background':records[i*8+5],'reserved':list(records[i*8+6:i*8+8]),'alien_pool_offset':i*64} for i in range(16)]
    evidence=ROOT/'docs/verification/vice-evidence.zip'
    asset_data['runtime_explosions']={'source':'docs/verification/vice-evidence.zip','source_sha256':digest(evidence.read_bytes()),'method':'Original CALEXP output captured after isolated ALIDEF calls; TED-derived masks are samples, not a unique stored animation.','waves':[]}
    with zipfile.ZipFile(evidence) as z:
        alternate=mos_hex(sources['O.ALI']);alt=bytes(alternate[i] for i in range(1024));pool=bytes.fromhex(asset_data['banks']['aliens']['hex']);ref=z.read('reference-memory.bin')[:1024]
        asset_data['alternative_alien_listing_comparison']={'source':'O.ALI','source_sha256':provenance['O.ALI']['sha256'],'bytes':1024,'differences_from_selected_bjh':sum(a!=b for a,b in zip(alt,pool)),'differences_from_unpacked_reference':sum(a!=b for a,b in zip(alt,ref)),'selection':'comparison only; default follows original loader BJH dependency'}
        startup=z.read('gameplay-memory.bin')
        asset_data['startup_state']={n:startup[labels[n]] for n in ['BAKCOL','SHIPC1','SHIPC2','SHPINK']}
        for i in range(16):
            name=f'rule-probes/source-alien-{i}.bin';mem=z.read(name);raw=mem[0x3ee8:0x3f68]
            asset_data['runtime_explosions']['waves'].append({'index':i,'address':0x3ee8,'bytes':128,'hex':raw.hex(),'member':name,'member_sha256':digest(mem),'payload_sha256':digest(raw)})
    data={'method':'Static definitions and resolvable direct transfers; emitted byte ownership from ca65 listing PCs; no dynamic call graph or cycle profile',
          'source_disks':manifest['disks'],'prg_sha256':asset_data['prg_sha256'],'assembly_order':used,'modules':modules,'symbols':symbols,'variables':variables,'direct_transfers':transfers,
          'counts':{'available_source_modules':len(sources),'main_modules':len(main),'main_logical_lines':sum(len(sources[n]) for n in main),
                    'main_instruction_statements':sum(m['instruction_statements'] for m in modules if m['active']),
                    'active_symbol_definitions':len(symbols),'direct_transfer_statements':len(transfers),
                    'resolved_direct_transfers':sum(t['target_address'] is not None for t in transfers),
                    'zero_page_reserved_bytes':sum(v['bytes'] for v in variables if v['address']<256),
                    'extra_work_reserved_bytes':sum(v['bytes'] for v in variables if 0x200<=v['address']<0x400),
                    'object_region_bytes':len(code),'exported_data_spans':len(asset_data['tables'])}}
    write_json(output/'codebase-index.json',data);write_json(output/'asset-data.json',asset_data)
    text='# Generated Code Reference\n\n## Method and Limits\n\nGenerated from original normalized modules, linker symbols and listing PCs. Logical line numbers refer to the preserved module after CR/CRLF splitting, not the flattened assembly. Labels include branch points, data, equates and alternate entries; they are not all functions. Module allocations include embedded data. Direct transfers omit fall-through, indirect vectors, runtime patches and nonlocal stack control. Data spans stop at the next greater symbol address and retain raw byte order; their field semantics require reading the source.\n\n---\n\n## Assembly Order and Allocation\n\n'
    text+=table(['Module','Bytes','Lines','Origin'],[(f'`{n}`',sizes[n],len(sources[n]),'1992' if provenance[n]['fallback'] else '2026') for n in used])+'\n\n---\n\n## Variables and Reserved Memory\n\n'
    text+=table(['Symbol','Address','Bytes','Line'],[(f"`{v['symbol']}`",f"`${v['address']:04X}`",v['bytes'],v['source_line']) for v in variables])+'\n\n---\n\n## Symbols and Preserved Source Locations\n\n'
    for name in used:
        row=provenance[name];path=row.get('extracted_copy',row['source']);text+=f'### {name}\n\n[Preserved input](../../{quote(path,safe="/")}). Logical lines use this module; origin: {"1992 fallback" if row["fallback"] else "2026 disk"}.\n\n'
        defs=[d for d in symbols if d['module']==name]
        if defs:text+=table(['Symbol','Address','Line','Kind'],[(f"`{d['symbol']}`",f"`${d['address']:04X}`" if d['address'] is not None else 'unresolved equate',d['line'],d['kind']) for d in defs])+'\n\n'
    text+='---\n\n## Direct Transfers\n\nThe complete machine-readable transfer list is in [codebase-index.json](codebase-index.json). Resolved targets include constant offsets such as `SCORE+2`; they do not imply normal subroutine calling conventions. [Analysis](../../CODEBASE_ANALYSIS.md), [reference guide](README.md).\n'
    (output/'CODE_REFERENCE.md').write_text(text)
    for bank in ['terrain','font']:
        b=asset_data['banks'][bank]
        for mode in ['hires','multicolor']:atlas(output/f'{bank}-{mode}.svg',f'{bank.capitalize()} bank: codes 000-255',bytes.fromhex(b['hex']),b['address'],mode)
    print(json.dumps(data['counts'],indent=2))
    return data

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--build-dir',type=Path,default=ROOT/'build');p.add_argument('--output-dir',type=Path,default=ROOT/'docs/analysis');a=p.parse_args();analyze(a.build_dir,a.output_dir)
