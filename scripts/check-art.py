"""Asset integrity and scale proof; never modifies art pixels."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,hashlib
root=Path(__file__).resolve().parent.parent
inv=json.loads((root/'art-production/inventory.json').read_text())
report={'total':sum(len(c['items']) for c in inv.values()),'complete':0,'missing':[],'errors':[],'warnings':[],'assets':[]}
out=root/'reviews/full-raster';out.mkdir(parents=True,exist_ok=True)
for cat,data in inv.items():
    tiles=[]
    for name in data['items']:
        path=root/'dist/assets/art'/cat/(name+'.png')
        if not path.exists():report['missing'].append(cat+'/'+name);continue
        im=Image.open(path).convert('RGBA');alpha=im.getchannel('A');box=alpha.getbbox();w,h=im.size
        if im.size!=(80,80):report['errors'].append(f'{cat}/{name}: wrong size {im.size}')
        if cat=='terrain' and name not in ['smoke','mist'] and alpha.getextrema()!=(255,255):report['errors'].append(f'{cat}/{name}: ground texture must be opaque')
        if cat!='terrain' and alpha.getextrema()[0]!=0:report['errors'].append(f'{cat}/{name}: missing transparency')
        if not box:report['errors'].append(f'{cat}/{name}: empty')
        if box and cat!='terrain' and (box[0]==0 or box[1]==0 or box[2]==80 or box[3]==80):report['warnings'].append(f'{cat}/{name}: touches canvas edge')
        report['assets'].append({'id':cat+'/'+name,'size':[w,h],'bounds':box,'visibleBounds':alpha.point(lambda a:255 if a>16 else 0).getbbox(),'alpha':alpha.getextrema(),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
        report['complete']+=1
        tile=Image.new('RGB',(196,130),'#e5dcc0');d=ImageDraw.Draw(tile);d.rectangle((100,0,195,95),fill='#26484a')
        tile.paste(im,(10,7),im);small=im.resize((40,40),Image.Resampling.LANCZOS);tile.paste(small,(127,45),small)
        d.text((8,105),name,fill='#20383a');tiles.append(tile)
    rows=(len(tiles)+5)//6;sheet=Image.new('RGB',(6*196,max(1,rows)*130),'#20383a')
    for i,t in enumerate(tiles):sheet.paste(t,((i%6)*196,(i//6)*130))
    sheet.save(out/(cat+'-80-40.png'))
(root/'art-production/qa-report.json').write_text(json.dumps(report,indent=2))
print(json.dumps({k:report[k] for k in ['total','complete','missing','errors','warnings']},indent=2))
