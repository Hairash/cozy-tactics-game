from pathlib import Path
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parent;P=R.parent;ids=['ally-1','ally-2','enemy-1','enemy-2','tree','column','wall','fan']
out=Image.new('RGB',(800,440),'#e9e1ce');d=ImageDraw.Draw(out)
for row,(folder,bg,label) in enumerate([(P/'archive/builtin-painted-detailed/processed','#e9e1ce','OLD · detailed'),(R/'processed','#e9e1ce','NEW · simple'),(P/'archive/builtin-painted-detailed/processed','#253c40','OLD · detailed'),(R/'processed','#253c40','NEW · simple')]):
 y=row*110;d.rectangle((0,y,800,y+109),fill=bg);fg='#233b3c' if row<2 else '#ebe4ce';d.text((8,y+5),label+' · actual64px',fill=fg)
 for n,k in enumerate(ids):
  x=100+n*87;im=Image.open(folder/f'{k}.png').convert('RGBA').resize((64,64),Image.Resampling.LANCZOS);out.paste(im,(x,y+24),im);d.text((x,y+91),k,fill=fg)
out.save(P/'reviews/simple80-old-new-64.png')
