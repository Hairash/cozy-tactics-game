"""Preserve generated RGBA: crop/resize only; never paint or remove backgrounds."""
from pathlib import Path
from PIL import Image, ImageDraw
import json, hashlib, shutil
ROOT=Path(__file__).resolve().parent
IDS=['ally-1','ally-2','enemy-1','enemy-2','tree','column','wall','fan']
def process(asset):
 src=ROOT/'raw'/f'{asset}.png'; im=Image.open(src).convert('RGBA'); alpha=im.getchannel('A')
 if alpha.getextrema()[0]!=0: raise ValueError(f'{asset}: generated image has no genuine transparent pixels')
 bbox=alpha.point(lambda p:255 if p>16 else 0).getbbox()
 if not bbox: raise ValueError(f'{asset}: empty alpha')
 crop=im.crop(bbox); limit=(66,62) if asset!='wall' else (66,42)
 scale=min(limit[0]/crop.width,limit[1]/crop.height)
 size=tuple(max(1,round(n*scale)) for n in crop.size)
 if asset=='wall': size=(66,32)
 if asset=='column': size=(38,62)
 if asset=='enemy-2': size=(66,46)
 crop=crop.resize(size,Image.Resampling.LANCZOS)
 out=Image.new('RGBA',(80,80)); out.alpha_composite(crop,((80-size[0])//2,72-size[1])); (ROOT/'processed').mkdir(exist_ok=True); out.save(ROOT/'processed'/f'{asset}.png')
 a=out.getchannel('A'); hist=a.histogram(); return {'raw_size':im.size,'raw_bbox':bbox,'size':[80,80],'bbox':a.getbbox(),'coverage':round(sum(hist[65:])/6400,4),'alpha_preserved':True,'sha256':hashlib.sha256((ROOT/'processed'/f'{asset}.png').read_bytes()).hexdigest()}
if __name__=='__main__':
 import sys
 results={i:process(i) for i in (sys.argv[1:] or IDS)}
 (ROOT/'technical-qa.json').write_text(json.dumps(results,indent=2)); print(json.dumps(results,indent=2))
