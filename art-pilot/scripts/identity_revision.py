from pathlib import Path
from PIL import Image,ImageDraw
import json
r=Path(__file__).resolve().parents[1]; inp=r.parents[1]/'art-runtime/ComfyUI/input'
for aid in ['ally-1','ally-2']:
 im=Image.new('RGB',(512,512),'white');d=ImageDraw.Draw(im)
 d.polygon([(249,60),(163,174),(207,199),(306,187),(324,164)],fill='#436d68',outline='#293e3e',width=5)
 d.ellipse((224,126,281,181),fill='#273e3d')
 d.polygon([(205,185),(293,180),(343,352),(162,350)],fill='#497974',outline='#293e3e',width=5)
 d.polygon([(216,210),(266,217),(289,347),(210,343)],fill='#ddd3b4')
 d.rectangle((205,346,237,410),fill='#574d40');d.rectangle((271,347,302,410),fill='#574d40')
 d.polygon([(193,401),(237,398),(242,427),(185,427)],fill='#303f3d');d.polygon([(271,399),(306,399),(325,427),(268,427)],fill='#303f3d')
 if aid=='ally-1':
  d.polygon([(141,221),(204,221),(213,338),(129,327)],fill='#bb975b',outline='#293e3e',width=7);d.polygon([(151,240),(188,241),(191,306),(145,301)],fill='#e1d5b3',outline='#293e3e',width=4)
 else:
  d.line((357,112,345,419),fill='#91774b',width=14);d.arc((320,70,395,155),0,180,fill='#91774b',width=14);d.ellipse((341,91,372,121),fill='#79aca1',outline='#293e3e',width=4)
 im.save(inp/f'pilot-{aid}-init.png');im.save(r/'reference'/f'{aid}-init.png')
# Preserve the original broad robot guide as the img2img initial shape.
Image.open(r/'reference/enemy-2-guide.png').save(inp/'pilot-enemy-2-init.png')
data=json.loads((r/'assets.json').read_text());changes={}
for aid in ['ally-1','ally-2','enemy-2']:
 a=next(x for x in data['assets'] if x['id']==aid)
 changes[aid]={'init_image':f'pilot-{aid}-init.png','reference':f'pilot-{aid}-init.png','denoise':.72,'composition_weight':.8,'style_weight':.65,'steps':8,'cfg':2.5,'seed':a['seed']+1000,'prompt':a['prompt']+' One single complete painted game piece. Keep the broad graphic silhouette and equipment. White empty background.','negative':a['negative']+', dagger, sword, baby, child, cute anime face, scenery, trees in background'}
(r/'workflows/identity-revision.json').write_text(json.dumps(changes,indent=2))
