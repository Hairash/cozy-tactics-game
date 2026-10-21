from pathlib import Path
from PIL import Image,ImageDraw
import json
r=Path(__file__).resolve().parents[1];inp=r.parents[1]/'art-runtime/ComfyUI/input'
im=Image.open(inp/'pilot-ally-1-init.png');d=ImageDraw.Draw(im)
d.polygon([(204,143),(249,103),(295,151),(277,181),(223,181)],fill='#263e3d')
d.polygon([(228,142),(271,143),(267,167),(249,177),(230,166)],fill='#d7b995')
d.ellipse((237,148,242,153),fill='#273637');d.ellipse((258,148,263,153),fill='#273637');d.line((246,164,253,164),fill='#755c48',width=2)
d.ellipse((239,183,258,202),fill='#ba9657',outline='#293e3e',width=3)
im.save(inp/'pilot-mara-front-init.png');im.save(r/'reference/mara-front-init.png')
a=next(x for x in json.loads((r/'assets.json').read_text())['assets'] if x['id']=='ally-1')
c={'ally-1':{'init_image':'pilot-mara-front-init.png','reference':'pilot-mara-front-init.png','denoise':.62,'seed':a['seed']+191,'prompt':a['prompt']+' FRONT FACING, visible small human face inside the hood, two dark eyes, small mouth, chest clasp. Looking at viewer.','negative':a['negative']+', back view, rear view, faceless, closed helmet'}}
(r/'workflows/mara-front-revision.json').write_text(json.dumps(c,indent=2))
