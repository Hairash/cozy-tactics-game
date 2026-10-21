from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json
ROOT=Path(__file__).resolve().parents[1]
def sheet():
 data=json.loads((ROOT/'assets.json').read_text());ids=['ally-1','ally-2','enemy-1','enemy-2','tree','column','wall','fan','ground','grass','water'];assets=[next(a for a in data['assets'] if a['id']==i) for i in ids];out=Image.new('RGB',(1120,1000),'#efe9d6');d=ImageDraw.Draw(out)
 try:font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',20);small=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',14)
 except:font=small=ImageFont.load_default()
 d.text((24,16),'THE LAST CURRENT · LOCAL COMFYUI PILOT',font=font,fill='#293d3c');d.text((24,45),'Experimental candidates · human review before production',font=small,fill='#826844')
 for n,a in enumerate(assets):
  x=20+(n%4)*275;y=85+(n//4)*300;d.rounded_rectangle((x,y,x+260,y+282),radius=8,fill='#f9f5e8',outline='#c8c3ad');d.text((x+12,y+10),a['id'],font=font,fill='#293d3c')
  for row in range(12):
   for col in range(12):d.rectangle((x+10+col*20,y+42+row*18,x+30+col*20,y+60+row*18),fill=('#eee9da' if(row+col)%2 else '#f7f4e8'))
  if a.get('file'):
   im=Image.open(ROOT/a['file']).convert('RGBA');im.thumbnail((240,216),Image.Resampling.LANCZOS);out.paste(im,(x+10+(240-im.width)//2,y+42+(216-im.height)//2),im)
  d.text((x+12,y+263),a.get('review_status',a['status']),font=small,fill='#758174')
 out.save(ROOT/'reviews/pilot-assets.png')
if __name__=='__main__':sheet()
