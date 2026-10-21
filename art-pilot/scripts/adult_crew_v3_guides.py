"""Original adult editorial studies: 512px conditioning only, never final art.
Final output must be generated in ComfyUI then exported <=80px.
"""
from pathlib import Path
import resvg_py
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[1];O=R/'reference/adult-crew-v3';O.mkdir(exist_ok=True)
ink='#263e40';ivory='#e8d7ae';teal='#397c77';rust='#ad583e';ochre='#bf934e'
def p(d,c):return f'<path d="{d}" fill="{c}"/>'
def l(d,w=.65):return f'<path d="{d}" fill="none" stroke-width="{w}"/>'
# Six-and-a-half-head silhouettes; thin contour, planar anatomy, no toy mittens/boots.
m=''.join([
 # weight-bearing leg is nearly straight, rear leg counterbalances through bent knee
 p('M44 52 L51 54 L47 69 L46 82 L41 82 L40 68 Z',teal),
 p('M41 80 L46 80 L46 84 L40 86 L36 86 L36 84 L41 82 Z',ink),
 p('M51 53 L57 53 L54 69 L61 80 L56 82 L47 70 Z',teal),
 p('M56 79 L60 79 L63 82 L62 85 L54 84 L55 82 Z',ink),
 # rear short mantle establishes broad, hard-edged shoulders
 p('M39 27 L48 23 L58 28 L62 45 L57 54 L48 50 L34 54 L36 38 Z',rust),
 p('M45 28 L51 27 L55 49 L48 53 L40 50 Z',ivory),
 # elbow down and out, lean forearm returning toward waist; small wedge hand
 p('M55 28 L59 29 L62 42 L57 49 L52 47 L53 44 L57 43 L56 36 Z',rust),
 p('M50 44 L54 43 L56 46 L54 49 L50 47 Z',ivory),
 # adult visible neck, oblique jaw, short planar nose on three-quarter face
 p('M45 20 L50 20 L50 28 L46 30 L43 27 Z',ivory),
 p('M42 13 L51 12 L52 18 L54 20 L51 21 L49 25 L43 23 L41 18 Z',ivory),
 p('M49 15 L51 15 L52 18 L54 20 L51 21 L49 25 L47 23 L49 20 Z',ochre),
 # brimless guard casque is a faceted trapezoid with sloped back, not a round cap
 p('M40 15 L41 9 L49 8 L54 12 L54 17 L49 14 L42 17 Z',ochre),
 l('M43 18 L46 17.5 M49 17 L51 17.6',.85),
 l('M47.5 18 L48.5 20.6 L47 21 M46 22 L48.5 22',.55),
 # broad simple shield at oblique angle, not a rounded crest badge
 p('M31 34 L41 30 L44 35 L37 42 L33 43 Z',rust),
 p('M21 33 L35 29 L40 52 L31 64 L20 54 Z',ochre),
 p('M24 36 L32 33 L36 51 L30 58 L24 52 Z',teal),
])
n=''.join([
 p('M43 53 L49 55 L44 70 L45 82 L40 82 L38 69 Z',teal),
 p('M40 80 L45 80 L45 84 L40 86 L34 86 L35 83 L40 82 Z',ink),
 p('M49 54 L55 54 L53 71 L59 80 L54 82 L47 72 Z',teal),
 p('M54 79 L58 79 L60 82 L59 85 L52 84 L53 82 Z',ink),
 # long tailored outer coat; lapels are large planes, not decoration
 p('M39 28 L46 25 L54 28 L58 56 L51 66 L46 57 L34 65 L36 44 Z',teal),
 p('M44 29 L49 28 L52 53 L46 58 L41 54 Z',ivory),
 # folded free arm: elbow is sharp, forearm bends upward to waist
 p('M39 30 L35 31 L27 46 L30 52 L39 49 L39 45 L32 47 L37 38 Z',teal),
 p('M37 44 L40 44 L42 47 L39 50 L36 48 Z',ivory),
 # long bent staff arm with narrow wrist, one unobtrusive grip
 p('M53 29 L57 31 L58 43 L66 37 L69 40 L59 49 L54 47 L51 36 Z',teal),
 p('M66 36 L70 35 L72 38 L70 41 L67 40 Z',ivory),
 p('M69 86 L71 86 L73 18 Q81 16 79 10 L75 7 L73 9 L76 12 L76 14 L70 16 Z',ochre),
 # visible neck + narrow three-quarter angular face set inside modest hood
 p('M44 20 L49 20 L50 28 L46 30 L42 27 Z',ivory),
 p('M37 18 L40 9 L47 6 L54 13 L54 25 L48 29 L38 25 Z',ivory),
 p('M40 16 L47 11 L51 15 L51 19 L54 21 L51 22 L48 26 L42 23 L40 19 Z',ivory),
 p('M48 15 L51 15 L51 19 L54 21 L51 22 L48 26 L46 24 L48 21 Z',ochre),
 # dark inner hood edge is framing cloth, no hairstyle
 p('M38 18 L40 13 L47 10 L52 14 L53 22 L50 18 L48 14 L41 18 L40 23 Z',ink),
 l('M42 19 L45 18.5 M48 18 L50 18.5',.85),
 l('M46 19 L47 21.4 L45.8 21.8 M44.5 23 L47 23',.55),
])
for name,body in [('ally-1',m),('ally-2',n)]:
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 100 100"><rect width="100" height="100" fill="white"/><g stroke="{ink}" stroke-width=".95" stroke-linejoin="miter" stroke-linecap="butt">{body}</g></svg>'
 (O/f'{name}.svg').write_text(svg);(O/f'{name}-init.png').write_bytes(resvg_py.svg_to_bytes(svg_string=svg,width=512,height=512,skip_system_fonts=True))
sheet=Image.new('RGB',(800,570),'#eee7d3');d=ImageDraw.Draw(sheet)
style=Image.new('RGB',(512,512),'white')
for i,(name,label) in enumerate([('ally-1','MARA / guard'),('ally-2','NERI / tidecaller')]):
 im=Image.open(O/f'{name}-init.png').convert('RGB');x=i*400
 d.text((x+20,15),label,fill=ink);sheet.paste(im.resize((380,380),Image.Resampling.LANCZOS),(x+10,35))
 for size,dx in [(80,90),(40,220)]:sheet.paste(im.resize((size,size),Image.Resampling.LANCZOS),(x+dx,430))
 # Same body height in a clean square, no text. Crop only white side margins.
 crop=im.crop((80,0,420,512));crop.thumbnail((256,440),Image.Resampling.LANCZOS);style.paste(crop,(i*256+(256-crop.width)//2,(512-crop.height)//2))
d.text((20,540),'ADULT V3 / conditioning only / final ComfyUI raster <=80px',fill=ink)
sheet.save(O/'paired-guides.png');style.save(O/'style-reference.png')
print(O)
