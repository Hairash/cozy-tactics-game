"""Raster pilot matting and deterministic80px final export. No vector drawing."""
from pathlib import Path
import os,json,argparse
from PIL import Image,ImageFilter
import numpy as np
from scipy import ndimage
r=Path(__file__).resolve().parents[1];os.environ['U2NET_HOME']=str(r.parents[1]/'art-runtime/matting-models')
from rembg import remove,new_session
p=argparse.ArgumentParser();p.add_argument('--only',nargs='*');args=p.parse_args();ids=set(args.only or []);d=json.loads((r/'assets.json').read_text());session=None
for a in d['assets']:
 if a['status']!='generated' or a['id'].startswith('test-') or (ids and a['id'] not in ids):continue
 if session is None:session=new_session('u2net',providers=['CPUExecutionProvider'])
 im=Image.open(r/a['raw_file']).convert('RGBA');cut=remove(im,session=session,post_process_mask=True);arr=np.array(cut);mask=arr[:,:,3]>64;lab,n=ndimage.label(mask);sizes=np.bincount(lab.ravel());sizes[0]=0;main=lab==sizes.argmax()
 # Keep only the main piece and immediate close details, excluding detached ground debris.
 near=ndimage.binary_dilation(main,iterations=3);keep=np.unique(lab[near]);keep=keep[keep!=0];alpha=np.where(np.isin(lab,keep),arr[:,:,3],0)
 # Neutral paper/floor outside the colored figure is not part of the art.
 rgb=np.array(im)[:,:,:3];low=rgb.min(2);high=rgb.max(2);gray=(high-low<20)&(low>110)
 # Remove gray ground-shadow remnants only below the guide's contact line.
 yy=np.indices(alpha.shape)[0];alpha=np.where(gray&(yy>im.height*.9),0,alpha)
 if a['id']=='tree':
  fg=rgb.min(2)<230;labs,nn=ndimage.label(fg);ss=np.bincount(labs.ravel());keep=np.where(ss>80)[0];keep=keep[keep!=0];alpha=(np.isin(labs,keep)*255).astype('uint8')
 if a['id']=='enemy-2':
  # Matting mistook the broad gray feet for background; preserve nonwhite enclosed paint.
  fg=(rgb.min(2)<230);labs,nn=ndimage.label(fg);ss=np.bincount(labs.ravel());ss[0]=0;fg=labs==ss.argmax();fg=ndimage.binary_fill_holes(fg);alpha=(fg*255).astype('uint8')
 if a['id']=='enemy-2':
  shadow=(yy>im.height*.82)&(rgb[:,:,0]>rgb[:,:,1]*1.02)&(rgb[:,:,1]>rgb[:,:,2]*1.08)
  alpha=np.where(shadow,0,alpha)
 if a['id']=='wall':
  xx=np.indices(alpha.shape)[1];alpha=np.where((xx>im.width*.87)&(yy>im.height*.6),0,alpha)
 white=(rgb.min(2)>230)&((rgb.max(2)-rgb.min(2))<18)
 seed=np.zeros_like(white);seed[0,:]=white[0,:];seed[-1,:]=white[-1,:];seed[:,0]=white[:,0];seed[:,-1]=white[:,-1]
 background=ndimage.binary_propagation(seed,mask=white)
 if a['id'] in ['ally-1','ally-2']:
  # White inside a closed arm/staff gap is background too; cream paint is warmer, not neutral white.
  background=background|((rgb.min(2)>232)&((rgb.max(2)-rgb.min(2))<20))
 alpha=np.where(background,0,alpha)
 arr[:,:,:3]=rgb;arr[:,:,3]=alpha;cut=Image.fromarray(arr);box=cut.getbbox()
 if not box:raise RuntimeError('Empty cutout '+a['id'])
 cut=cut.crop(box)
 if a['id']=='column':cut=cut.resize((round(cut.width*1.6),cut.height),Image.Resampling.LANCZOS)
 cut.thumbnail((62,62),Image.Resampling.LANCZOS);out=Image.new('RGBA',(80,80));out.alpha_composite(cut,((80-cut.width)//2,72-cut.height));out.save(r/'processed'/f"{a['id']}.png")
 a.update(file=f"processed/{a['id']}.png",status='processed',review_status='raster80-review',anchor=[.5,.9],scale=1.1,export_size=[80,80],processing='ComfyUI raster img2img;u2net foreground;normalized80px RGBA;no vector repaint')
d['art_revision']='raster80-v1';d['phase']='raster-pilot-review';d['production_approved']=False;(r/'assets.json').write_text(json.dumps(d,indent=2))
