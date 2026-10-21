"""Deterministic color matte for the painterly tree; u2net erased its fine canopy."""
from pathlib import Path
from PIL import Image,ImageFilter
import numpy as np
from scipy import ndimage
import json
r=Path(__file__).resolve().parents[1];im=Image.open(r/'raw/tree.png').convert('RGB');p=np.array(im).astype(float);rr,gg,bb=p[:,:,0],p[:,:,1],p[:,:,2]
# Tan paper has red > blue and red >= green; foliage/ink has teal or dark pigment.
m=((gg-rr>2)&(bb-rr>-20)) | ((rr+gg+bb)/3<95) | ((rr>160)&(gg<153)&(bb<100))
m[:220,:95]=False;m[:140,650:]=False
lab,n=ndimage.label(m);sizes=np.bincount(lab.ravel());sizes[0]=0;mask=lab==sizes.argmax();mask=ndimage.binary_closing(mask,iterations=1);mask=ndimage.binary_fill_holes(mask)
a=Image.fromarray((mask*255).astype('uint8')).filter(ImageFilter.GaussianBlur(.45));cut=im.convert('RGBA');cut.putalpha(a);cut=cut.crop(cut.getbbox());cut.thumbnail((400,420),Image.Resampling.LANCZOS);out=Image.new('RGBA',(512,512));out.alpha_composite(cut,((512-cut.width)//2,450-cut.height));out.save(r/'processed/tree.png')
data=json.loads((r/'assets.json').read_text());x=next(x for x in data['assets'] if x['id']=='tree');x['processing']='Color-separated teal/ink foreground matte, largest connected tree component, normalized anchor';x['alpha_coverage']=round(float((np.array(out.getchannel('A'))>64).mean()),4);(r/'assets.json').write_text(json.dumps(data,indent=2))
