"""Small vector art study: original SVG shapes, final raster assets never exceed80px.
Idempotent: archives the reviewed painterly pilot once, then rebuilds deterministically.
No ComfyUI model call or live game changes.
"""
from pathlib import Path
import json,shutil,hashlib
import numpy as np
from PIL import Image,ImageEnhance,ImageFilter
import resvg_py
R=Path(__file__).resolve().parents[1];V=R/'vector';V.mkdir(exist_ok=True);A=R/'archive/painterly-pilot';A.mkdir(parents=True,exist_ok=True)
if not (A/'assets.json').exists():
 shutil.copy2(R/'assets.json',A/'assets.json')
 shutil.copytree(R/'processed',A/'processed',dirs_exist_ok=True)
 shutil.copy2(R/'reviews/pilot-assets.png',A/'contact-sheet.png')
D=json.loads((R/'assets.json').read_text());ink='#233d3d';cream='#f3dfb2';teal='#367d78';sage='#9bae7a';rust='#ba583c';gold='#d9a64b';dark='#284c52'
def path(d,c,stroke=True):return f'<path d="{d}" fill="{c}"'+(' stroke="'+ink+'"' if stroke else '')+'/>'
def line(d,c=ink,w=1.7):return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}"/>'
def circle(x,y,r,c):return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" stroke="none"/>'
def p(d,c):return path(d,c)
S={}
# Mara: low broad rust cape, off-centre crest, enormous shield. No second pointed teal hood.
S['ally-1']=''.join([
 p('M25 57 L36 57 L35 67 L25 70 L20 70 L21 66 Z',dark),p('M44 57 L54 57 L57 68 Q52 72 43 70 Z',dark),
 p('M25 32 Q39 27 53 33 L63 58 L48 63 L38 56 L23 61 L14 53 Z',rust),
 p('M31 35 L46 33 L50 59 L34 59 Z',cream),
 p('M22 26 Q23 14 35 13 L52 20 L51 33 L29 34 Z',gold),
 p('M23 24 L48 25 L45 35 Q35 40 28 33 Z',ink),
 p('M29 26 L44 26 L42 32 Q36 36 31 31 Z',cream),circle(33,28,1,ink),circle(40,28,1,ink),
 p('M34 14 L42 7 L47 11 L44 20 Z',rust),
 p('M13 34 L32 31 L36 51 L29 61 L12 56 Z',gold),p('M17 38 L27 36 L30 49 L25 54 L17 51 Z',dark),
 line('M14 34 L32 31 M12 56 L29 61',cream,1.5),circle(43,37,2,gold)])
# Neri: ivory crescent hood, long narrow blue-green coat, large open tide hook.
S['ally-2']=''.join([
 p('M28 57 L37 57 L35 69 L24 70 L24 66 Z',dark),p('M41 57 L49 57 L52 69 L41 70 Z',dark),
 p('M28 32 L45 31 Q51 42 54 59 L41 64 L36 53 L25 62 L21 48 Z',teal),
 p('M35 36 L40 35 L45 57 L33 58 Z',cream),
 p('M21 27 Q24 16 39 9 L35 18 Q53 16 53 30 L46 36 L27 34 Z',cream),
 p('M27 26 Q37 21 48 27 L43 34 Q34 38 29 32 Z',dark),
 p('M32 27 L43 27 L41 32 Q36 34 33 31 Z','#a6c9b1'),circle(35,28.5,.9,ink),circle(40,28.5,.9,ink),
 p('M56 70 L59 70 L61 24 Q72 22 69 14 Q67 9 61 12 L63 16 Q66 14 66 18 Q65 21 58 20 Z',gold),
 p('M48 38 Q53 35 59 36 L59 42 L50 43 Z',teal),circle(59,38,2.2,cream),
 p('M29 36 Q22 38 21 47 L25 49 L30 42 Z',teal),circle(24,48,2,cream),
 p('M47 16 L52 13 L54 22 Z',rust),circle(39,38,2,gold)])
S['enemy-1']=''.join([
 p('M24 48 L30 49 L24 68 L18 70 L20 64 Z',gold),p('M47 49 L53 48 L60 68 L53 70 L51 64 Z',gold),
 p('M37 49 L42 49 L43 69 L38 71 Z',dark),
 p('M39 9 L61 48 Q41 57 19 47 Z',dark),p('M39 9 L42 42 L55 46 L39 49 Z',teal),
 p('M22 45 Q40 50 58 45 L61 49 Q42 57 19 49 Z',cream),
 p('M34 29 Q43 24 48 31 L46 39 L36 40 L31 34 Z',gold),circle(40,33,3.5,ink),circle(40,33,1.5,cream),
 p('M36 41 L44 41 L45 47 L35 47 Z',ink)])
S['enemy-2']=''.join([
 p('M23 52 L34 52 L33 66 L35 70 L17 70 L18 65 Z',dark),p('M46 52 L57 52 L60 67 L63 70 L45 70 Z',dark),
 p('M18 21 L57 17 L63 53 L48 61 L20 55 Z',teal),
 p('M16 15 L58 12 L64 24 L19 28 Z',cream),
 p('M8 30 L21 27 L24 54 L9 56 Z',gold),p('M59 27 L71 30 L70 55 L58 52 Z',cream),
 p('M26 30 L54 28 L53 39 L29 42 Z',ink),circle(34,35,2.7,gold),circle(47,33,2.7,gold),
 line('M12 34 L15 48 M64 34 L64 47',ink,2.3),p('M30 49 L50 47 L51 54 L33 56 Z',dark)])
S['tree']=''.join([
 p('M34 42 L45 40 L43 58 L54 70 L43 68 L37 62 L31 70 L22 70 L33 57 Z',gold),
 p('M39 50 L24 38 L27 34 L40 43 L52 30 L55 34 Z',gold),
 p('M10 35 Q7 27 17 20 L24 21 L31 10 L43 17 Q55 10 60 24 L69 29 L64 44 L50 48 L38 42 L25 49 L10 45 Z',teal),
 p('M13 35 L27 28 L31 15 L39 23 L51 20 L62 29 L56 36 L43 33 L33 40 L20 40 Z',sage),
 p('M19 21 L24 15 L27 24 Z',cream),circle(25,35,2.8,rust),circle(53,32,2.5,gold),
 line('M36 53 L38 61',ink)])
S['column']=''.join([
 p('M15 60 L59 56 L66 65 L59 71 L14 69 L11 65 Z',cream),
 p('M24 27 L55 26 L52 59 L25 63 Z',cream),p('M44 28 L55 26 L52 59 L43 61 Z',sage),
 p('M12 14 L59 10 L68 19 L61 29 L15 30 L10 25 Z',cream),
 p('M10 25 L61 24 L68 19 L61 29 L15 30 Z',gold),
 line('M34 30 L31 40 L38 46 L35 53'),p('M25 57 L32 59 L32 63 L23 64 Z',teal),
 line('M15 65 L58 67',gold)])
S['wall']=''.join([
 p('M10 30 L60 24 L69 32 L68 65 L58 71 L10 66 Z',cream),
 p('M10 30 L60 24 L69 32 L20 39 Z',gold),p('M58 37 L69 32 L68 65 L58 71 Z',sage),
 line('M10 48 L58 52 L68 46 M33 37 L31 50 M39 51 L40 68'),
 p('M12 57 L18 55 L25 62 L23 67 L11 66 Z',teal),line('M50 40 L46 44 L49 48',ink,1.3)])
S['fan']=''.join([
 p('M31 52 L48 52 L48 62 L61 65 L63 71 L16 71 L18 65 L32 63 Z',cream),
 p('M39 10 Q65 10 67 34 Q66 57 42 60 Q16 59 13 37 Q11 14 39 10 Z',gold),
 p('M39 16 Q61 16 61 35 Q60 53 42 54 Q21 53 19 36 Q17 19 39 16 Z',dark),
 p('M38 34 Q22 32 25 22 Q36 20 40 31 Z',cream),
 p('M42 33 Q47 18 56 26 Q59 35 45 37 Z',sage),
 p('M42 40 Q55 49 44 51 Q33 49 38 39 Z',cream),
 circle(40,36,5,gold),circle(40,36,1.8,ink)])
for aid,body in S.items():
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 80 80"><g stroke="{ink}" stroke-width="1.65" stroke-linejoin="round" stroke-linecap="round">{body}</g></svg>'
 (V/f'{aid}.svg').write_text(svg);(R/'processed'/f'{aid}.png').write_bytes(resvg_py.svg_to_bytes(svg_string=svg,width=80,height=80,skip_system_fonts=True))
 a=next(a for a in D['assets'] if a['id']==aid)
 a.update(file=f'processed/{aid}.png',vector_file=f'vector/{aid}.svg',status='processed',review_status='schematic-review',anchor=[.5,.9],scale=1.1,processing='Original80-unit vector shapes; resvg0.5 raster export80x80; no shadow or gradients',source_type='original-vector',export_size=[80,80])
 a['export_sha256']=hashlib.sha256((R/a['file']).read_bytes()).hexdigest()
# Quiet texture variety: deterministic rotation, very mild tonal shifts and broad painted patches.
for aid in ['ground','grass','water']:
 a=next(a for a in D['assets'] if a['id']==aid);base=Image.open(A/'processed'/f'{aid}.png').convert('RGB').resize((80,80),Image.Resampling.LANCZOS);variants=[]
 for n in range(4):
  im=base.transpose([Image.Transpose.FLIP_LEFT_RIGHT,Image.Transpose.ROTATE_90,Image.Transpose.FLIP_TOP_BOTTOM,Image.Transpose.ROTATE_270][n]);im=ImageEnhance.Brightness(im).enhance([1.0,1.018,.982,1.008][n])
  # Smooth low-contrast mottling avoids repeated recognisable speckle without noisy terrain.
  yy,xx=np.mgrid[:80,:80];field=np.sin(xx*.055+n*1.9)*np.cos(yy*.048+n)*1.1;arr=np.array(im).astype(float)+field[:,:,None];im=Image.fromarray(np.clip(arr,0,255).astype('uint8'));f=f'processed/{aid}'+(f'-{n}' if n else '')+'.png';im.save(R/f);variants.append(f)
 a.update(file=variants[0],variants=variants,status='processed',review_status='schematic-review',export_size=[80,80],processing='80px quiet painted texture, four deterministic subtle variants')
D['phase']='schematic-pilot-review';D['production_approved']=False;D['art_revision']='schematic80-v1';(R/'assets.json').write_text(json.dumps(D,indent=2))
print('Exported8vector sprites and12terrain textures; all80x80. Painterly pilot archived.')
