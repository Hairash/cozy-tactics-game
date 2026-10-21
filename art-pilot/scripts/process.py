"""Deterministic local pilot processing: matting, shared anchors, texture exports."""
from pathlib import Path
import os,json,argparse
ROOT=Path(__file__).resolve().parents[1];RUNTIME=ROOT.parents[1]/'art-runtime'
os.environ['U2NET_HOME']=str(RUNTIME/'matting-models')
from PIL import Image,ImageFilter
import numpy as np
from scipy import ndimage

def save(data):
 p=ROOT/'assets.json';t=p.with_suffix('.tmp');t.write_text(json.dumps(data,indent=2));t.replace(p)
def process(ids):
 data=json.loads((ROOT/'assets.json').read_text());session=None
 for a in data['assets']:
  if ids and a['id'] not in ids:continue
  if a['status']!='generated':continue
  im=Image.open(ROOT/a['raw_file']).convert('RGBA')
  if a['kind']=='terrain':
   # Mirror small edge strips so export has matching opposite edges without tiling seams.
   im=im.resize((256,256),Image.Resampling.LANCZOS).convert('RGB');pix=np.array(im,dtype=float)
   for i in range(12):
    w=(12-i)/24
    mix=(pix[:,i,:]+pix[:,-i-1,:])/2;pix[:,i,:]=pix[:,i,:]*(1-w*2)+mix*w*2;pix[:,-i-1,:]=pix[:,-i-1,:]*(1-w*2)+mix*w*2
    mix=(pix[i,:,:]+pix[-i-1,:,:])/2;pix[i,:,:]=pix[i,:,:]*(1-w*2)+mix*w*2;pix[-i-1,:,:]=pix[-i-1,:,:]*(1-w*2)+mix*w*2
   out=Image.fromarray(pix.clip(0,255).astype('uint8'));a['processing']='256px matched-edge opaque texture'
  else:
   from rembg import remove,new_session
   if session is None:session=new_session('u2net',providers=['CPUExecutionProvider'])
   cut=remove(im,session=session,post_process_mask=True)
   rgba=np.array(cut);mask=rgba[:,:,3]>64;labels,n=ndimage.label(mask)
   sizes=np.bincount(labels.ravel());keep=np.where(sizes>max(32,mask.size*.0003))[0];keep=keep[keep!=0]
   rgba[:,:,3]=np.where(np.isin(labels,keep),rgba[:,:,3],0);cut=Image.fromarray(rgba)
   bbox=cut.getbbox()
   if not bbox:raise ValueError('Empty matting result: '+a['id'])
   cut=cut.crop(bbox);maxw,maxh=(430,438) if a['id']=='enemy-2' else (400,420)
   cut.thumbnail((maxw,maxh),Image.Resampling.LANCZOS);out=Image.new('RGBA',(512,512),(0,0,0,0));out.alpha_composite(cut,((512-cut.width)//2,450-cut.height));a['anchor']=[.5,450/512];a['processing']='u2net CPU alpha + connected component cleanup + normalized512px anchor'
   alpha=np.array(out.getchannel('A'));a['alpha_coverage']=round(float((alpha>64).mean()),4)
   a['alpha_edge_clear']=bool(not alpha[0,:].any() and not alpha[-1,:].any() and not alpha[:,0].any() and not alpha[:,-1].any())
  target=ROOT/'processed'/f"{a['id']}.png";out.save(target);a['file']=str(target.relative_to(ROOT));a['status']='processed';a['review_status']='awaiting-independent-review';save(data);print('PROCESSED',a['id'],flush=True)
 data['phase']='pilot-review';save(data)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--only',nargs='*');args=p.parse_args();process(set(args.only or []))
