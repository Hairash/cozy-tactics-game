from pathlib import Path
from PIL import Image
from scipy import ndimage
import numpy as np,json,hashlib
ROOT=Path(__file__).resolve().parents[1];data=json.loads((ROOT/'assets.json').read_text());rows=[]
for a in data['assets']:
 if a['id'].startswith('test-'):continue
 r={'id':a['id'],'status':a['status'],'failures':[]}
 if not a.get('file'):r['failures'].append('missing processed file')
 else:
  p=ROOT/a['file'];im=Image.open(p);r['size']=list(im.size);
  if ('80' in data.get('art_revision','')) and max(im.size)>80:r['failures'].append('asset exceeds80px')
  for variant in a.get('variants',[]):
   if max(Image.open(ROOT/variant).size)>80:r['failures'].append('variant exceeds80px')
  r['sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
  if a['kind']!='terrain':
   if im.mode!='RGBA':r['failures'].append('not RGBA')
   else:
    alpha=np.array(im.getchannel('A'));mask=alpha>64;labels,n=ndimage.label(mask);sizes=np.bincount(labels.ravel())[1:];r['main_component_share']=round(float(max(sizes,default=0)/max(1,mask.sum())),4);r['coverage']=round(float(mask.mean()),4);r['foreground_bbox']=list(im.getbbox());r['normalized_height']=round((im.getbbox()[3]-im.getbbox()[1])/im.height,3)
    if ('80' in data.get('art_revision','')) and not((.35 if a['id']=='wall' else .55)<=r['normalized_height']<=.85):r['failures'].append('inconsistent cell height')
    if alpha[0].any() or alpha[-1].any() or alpha[:,0].any() or alpha[:,-1].any():r['failures'].append('clipped edge')
    if not(.025<r['coverage']<.75):r['failures'].append('suspicious alpha coverage')
    if r['main_component_share']<.8:r['failures'].append('fragmented foreground; visual review needed')
 rows.append(r)
result={'checked':len(rows),'failures':[r for r in rows if r['failures']],'assets':rows};(ROOT/'reviews/technical-validation.json').write_text(json.dumps(result,indent=2));print(json.dumps({'checked':result['checked'],'failures':result['failures']}))
