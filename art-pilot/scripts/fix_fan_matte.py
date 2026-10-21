"""Reconstruct fan alpha from its closed ink silhouette, retaining original cream pedestal."""
from pathlib import Path
from PIL import Image,ImageFilter
from scipy import ndimage
import numpy as np,json,shutil
r=Path(__file__).resolve().parents[1];arch=r/'archive/raster80-v1';arch.mkdir(parents=True,exist_ok=True)
if not (arch/'assets.json').exists():
 shutil.copy2(r/'assets.json',arch/'assets.json');shutil.copytree(r/'processed',arch/'processed',dirs_exist_ok=True);shutil.copy2(r/'reviews/raster80-assets.png',arch/'contact-sheet.png')
im=Image.open(r/'raw/fan.png').convert('RGB');rgb=np.array(im);ink=rgb.min(2)<220;labels,n=ndimage.label(ink);sizes=np.bincount(labels.ravel());sizes[0]=0;mask=labels==sizes.argmax();mask=ndimage.binary_fill_holes(mask)
cut=im.convert('RGBA');cut.putalpha(Image.fromarray((mask*255).astype('uint8')).filter(ImageFilter.GaussianBlur(.4)));cut=cut.crop(cut.getbbox());cut.thumbnail((62,62),Image.Resampling.LANCZOS);out=Image.new('RGBA',(80,80));out.alpha_composite(cut,((80-cut.width)//2,72-cut.height));out.save(r/'processed/fan.png')
d=json.loads((r/'assets.json').read_text());a=next(a for a in d['assets'] if a['id']=='fan');a['processing']='Closed ink silhouette matte retaining original cream fan pedestal;80px';a['review_status']='fan-alpha-repaired';(r/'assets.json').write_text(json.dumps(d,indent=2))
# Inspect exact final sprite against two contrasting backgrounds; neither can hide missing alpha.
out=Image.new('RGB',(480,240),'#f1e6ce')
for n,color in enumerate(['#183a3c','#c0c591']):
 b=Image.new('RGBA',(240,240),color);fan=Image.open(r/'processed/fan.png').resize((240,240),Image.Resampling.LANCZOS);b.alpha_composite(fan);out.paste(b.convert('RGB'),(n*240,0))
out.save(r/'reviews/fan-alpha-repaired.png')
