"""Original 512px CONDITIONING studies. Never use these PNGs as final sprites.
Run with art-runtime/venv/bin/python. Final assets must be ComfyUI raster, <=80px.
"""
from pathlib import Path
import resvg_py
from PIL import Image, ImageDraw
R=Path(__file__).resolve().parents[1]; O=R/'reference/mature-crew'; O.mkdir(exist_ok=True)
ink='#263e40'; ivory='#e8d7ae'; teal='#397c77'; rust='#ad583e'; ochre='#bf934e'
def p(d,c): return f'<path d="{d}" fill="{c}"/>'
def l(d,w=1.3): return f'<path d="{d}" fill="none" stroke-width="{w}"/>'
# 5-head adult figures; bent knees, long forearms, small angular faces.
mara=''.join([
 p('M39 53 L50 56 L45 70 L39 75 L40 86 L29 87 L31 82 L32 71 Z',ink),
 p('M50 55 L60 55 L57 70 L66 82 L65 87 L53 86 L53 82 L48 72 Z',ink),
 p('M36 29 Q45 27 57 30 L66 57 L55 64 L47 55 L34 61 L30 46 Z',rust),
 p('M43 30 L53 31 L57 56 L44 58 L40 42 Z',ivory),
 # Far arm: shoulder down to angular elbow then curved forearm inward.
 p('M55 31 Q62 31 63 39 L66 48 Q65 53 58 53 L52 49 L55 45 L59 46 L57 40 Z',rust),
 p('M52 45 L57 46 L58 50 L54 53 L50 49 Z',ivory),
 # Angular mature face, no dots / smile / tiny ornaments.
 p('M40 15 L53 15 L55 24 L49 29 L42 26 L39 21 Z',ivory),
 p('M37 17 Q38 10 46 10 L57 15 L57 20 L49 17 L39 20 Z',ochre),
 l('M42 21 L45 21 M49 20 L52 20',1.4),
 # Shield overlaps near bent arm; broad simple split plane without highlights.
 p('M26 36 Q31 31 37 35 L42 43 L37 49 L31 44 Z',rust),
 p('M20 36 L35 32 L41 54 L32 65 L19 56 Z',ochre),
 p('M24 39 L32 37 L36 53 L31 59 L24 54 Z',teal),
])
neri=''.join([
 p('M39 55 L49 57 L43 73 L45 85 L33 87 L33 82 L34 71 Z',ink),
 p('M49 56 L58 55 L56 70 L63 81 L62 87 L51 86 L52 81 L47 72 Z',ink),
 # Long off-centre coat, restrained ivory collar rather than giant horn hood.
 p('M38 30 Q47 27 56 30 L60 59 L49 63 L46 54 L34 62 L32 45 Z',teal),
 p('M44 30 L50 30 L54 57 L44 59 L43 42 Z',ivory),
 # Left elbow projects, forearm hooks back toward hip.
 p('M38 32 Q31 34 28 43 L26 49 L34 55 L38 51 L32 47 L36 42 Z',teal),
 p('M35 49 L39 50 L40 54 L36 57 L32 53 Z',ivory),
 # Bent staff arm, visible negative space under elbow.
 p('M54 32 Q60 32 60 39 L61 44 L69 39 L72 43 L62 51 Q57 52 55 46 L52 39 Z',teal),
 p('M69 39 L73 37 L76 41 L73 45 L69 44 Z',ivory),
 p('M70 85 L73 85 L75 21 Q86 18 81 10 L77 9 L76 13 Q81 14 78 17 L71 18 Z',ochre),
 # Head exactly same scale as Mara; hood frames rather than enlarges head.
 p('M38 18 L41 11 L48 8 L55 14 L57 24 L52 28 L40 26 Z',ivory),
 p('M40 17 L52 16 L54 23 L48 29 L42 26 Z',ivory),
 p('M39 17 L48 13 L53 16 L53 19 L47 17 L40 21 Z',ink),
 l('M43 22 L46 22 M49 21 L52 21',1.4),
])
for name,body in [('ally-1',mara),('ally-2',neri)]:
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 100 100"><rect width="100" height="100" fill="white"/><g stroke="{ink}" stroke-width="1.65" stroke-linejoin="round" stroke-linecap="round">{body}</g></svg>'
 (O/f'{name}.svg').write_text(svg)
 (O/f'{name}-init.png').write_bytes(resvg_py.svg_to_bytes(svg_string=svg,width=512,height=512,skip_system_fonts=True))
# Review only: large studies plus honest 80px / 40px raster previews.
sheet=Image.new('RGB',(780,560),'#eee7d3'); d=ImageDraw.Draw(sheet)
for i,(name,label) in enumerate([('ally-1','MARA / warm rust'),('ally-2','NERI / ivory teal')]):
 im=Image.open(O/f'{name}-init.png').convert('RGB'); x=i*390
 d.text((x+24,18),label,fill=ink); sheet.paste(im.resize((360,360),Image.Resampling.LANCZOS),(x+15,42))
 for size,dx in [(80,90),(40,220)]: sheet.paste(im.resize((size,size),Image.Resampling.LANCZOS),(x+dx,422))
d.text((24,532),'COMPOSITION CONDITIONING ONLY - final ComfyUI exports <=80px',fill=ink)
sheet.save(O/'paired-guides.png')
print(O)
