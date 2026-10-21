from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json
R=Path(__file__).resolve().parents[1];data=json.loads((R/'assets.json').read_text());out=Image.new('RGB',(1080,870),'#eee6d1');d=ImageDraw.Draw(out)
f=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',21);small=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',14)
d.text((24,18),'THE LAST CURRENT · SIMPLE RASTER PILOT',font=f,fill='#233d3d');d.text((24,48),'Codex built-in image generation →80×80 PNGs · large quiet shapes · no ground shadows',font=small,fill='#445b55')
for n,aid in enumerate(['ally-1','ally-2','enemy-1','enemy-2','tree','column','wall','fan']):
 a=next(a for a in data['assets'] if a['id']==aid);x=20+n%4*265;y=85+n//4*300;d.rounded_rectangle((x,y,x+250,y+282),8,fill='#f8f3e4',outline='#c3bca5');d.text((x+12,y+10),{'ally-1':'Mara · Vanguard','ally-2':'Neri · Tidecaller','enemy-1':'Sentinel','enemy-2':'Breaker'}.get(aid,aid.capitalize()),font=f,fill='#233d3d')
 im=Image.open(R/a['file']).convert('RGBA');big=im.resize((160,160),Image.Resampling.LANCZOS);out.paste(big,(x+45,y+30),big)
 for size,dx in [(80,12),(64,98),(40,176)]:
  d.rectangle((x+dx,y+192,x+dx+size,y+192+size),fill='#d7d6bf');sm=im.resize((size,size),Image.Resampling.LANCZOS);out.paste(sm,(x+dx,y+192),sm);d.text((x+dx,y+271),str(size)+'px',font=small,fill='#556a60')
for n,aid in enumerate(['ground','grass','water']):
 a=next(a for a in data['assets'] if a['id']==aid);x=20+n*350;d.text((x,706),aid+' · four quiet variants',font=f,fill='#233d3d')
 for k,fp in enumerate(a['variants']):out.paste(Image.open(R/fp).convert('RGB'),(x+k*80,740))
d.text((24,843),'Experimental pilot only · live game unchanged · all exported game images ≤80px',font=small,fill='#556a60');out.save(R/'reviews/simple80-assets.png')
