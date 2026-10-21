from pathlib import Path
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parent;ids=['ally-1','ally-2','enemy-1','enemy-2','tree','column','wall','fan']
out=Image.new('RGB',(960,400),'#e9e1ce');d=ImageDraw.Draw(out)
for row,bg in enumerate(['#eee5cf','#253c40']):
 for n,k in enumerate(ids):
  x=n*120;y=row*200;d.rectangle((x,y,x+119,y+199),fill=bg);d.text((x+8,y+8),k,fill='#243a3c' if row==0 else '#e8e1cc')
  im=Image.open(R/'processed'/f'{k}.png').convert('RGBA');out.paste(im,(x+20,y+28),im)
  sm=im.resize((40,40),Image.Resampling.LANCZOS);out.paste(sm,(x+40,y+122),sm)
d.text((8,382),'80px and 40px actual images on light/dark · crop/resize only · generated alpha preserved',fill='#d9dfd5')
out.save(R.parent/'reviews'/'simple80-light-dark.png')
