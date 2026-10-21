from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
r=Path(__file__).resolve().parents[1];out=Image.new('RGB',(1000,770),'#eee6d1');d=ImageDraw.Draw(out);f=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',22);small=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',14)
d.text((22,15),'CREW STYLE · SAVED VERSIONS + MATURE RASTER PASS',font=f,fill='#263e40')
cols=[('Consistent schematic · saved',r/'archive/schematic80/processed'),('Rejected raster · saved',r/'archive/raster80-v1/processed'),('Mature raster · new',r/'processed')]
for c,(name,folder) in enumerate(cols):
 x=15+c*330;d.text((x+9,55),name,font=small,fill='#263e40')
 for n,aid in enumerate(['ally-1','ally-2']):
  y=85+n*310;d.rounded_rectangle((x,y,x+315,y+292),7,fill='#f8f2df',outline='#c4bca5');d.text((x+12,y+8),'Mara · shield' if n==0 else 'Neri · tide staff',font=small,fill='#263e40');im=Image.open(folder/f'{aid}.png').convert('RGBA');big=im.resize((160,160),Image.Resampling.LANCZOS);out.paste(big,(x+76,y+28),big)
  for sz,dx,color in [(80,20,'#214342'),(64,120,'#c5c798'),(40,215,'#214342')]:
   b=Image.new('RGBA',(sz,sz),color);b.alpha_composite(im.resize((sz,sz),Image.Resampling.LANCZOS));out.paste(b.convert('RGB'),(x+dx,y+199));d.text((x+dx,y+278),str(sz)+'px',font=small,fill='#55675f')
d.text((22,730),'Dark + light samples expose background fragments. All runtime exports80×80. Experiment only.',font=small,fill='#55675f');out.save(r/'reviews/mature-crew-comparison.png')
