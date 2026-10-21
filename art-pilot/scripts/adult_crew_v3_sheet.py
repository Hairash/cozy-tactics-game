from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
r=Path(__file__).resolve().parents[1];out=Image.new('RGB',(820,580),'#ede4ce');d=ImageDraw.Draw(out);f=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',24);small=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',15)
d.text((22,16),'THE LAST CURRENT · ADULT CREW REDRAW',font=f,fill='#263e40');d.text((22,50),'New ComfyUI raster sprites ·80px exports · experimental only',font=small,fill='#55675f')
for n,aid in enumerate(['ally-1','ally-2']):
 x=20+n*400;d.rounded_rectangle((x,82,x+380,552),8,fill='#f7f0dd',outline='#c1b89f');d.text((x+16,94),'Mara · Vanguard' if n==0 else 'Neri · Tidecaller',font=f,fill='#263e40');im=Image.open(r/'processed'/f'{aid}.png').convert('RGBA');big=im.resize((240,240),Image.Resampling.LANCZOS);out.paste(big,(x+70,129),big)
 for sz,dx,color in [(80,22,'#214342'),(64,142,'#c3c793'),(40,252,'#214342')]:
  b=Image.new('RGBA',(sz,sz),color);b.alpha_composite(im.resize((sz,sz),Image.Resampling.LANCZOS));out.paste(b.convert('RGB'),(x+dx,394));d.text((x+dx,484),str(sz)+'px',font=small,fill='#55675f')
 d.text((x+16,525),'Light + dark alpha check',font=small,fill='#55675f')
out.save(r/'reviews/adult-crew-v3.png')
