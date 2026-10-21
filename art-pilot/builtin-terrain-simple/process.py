from pathlib import Path
from PIL import Image,ImageDraw
import numpy as np,json,hashlib
R=Path(__file__).resolve().parent;rows={};mapping={}
for n,k in enumerate(['ground','grass','water']):
 raw=Image.open(R/'raw'/f'{k}.png').convert('RGB');im=raw.resize((80,80),Image.Resampling.LANCZOS);paths=[]
 for v,angle in enumerate([0,90,180,270]):
  name=f'{k}'+(f'-{v}' if v else '')+'.png';img=im.rotate(angle);img.save(R/'processed'/name);paths.append(f'builtin-terrain-simple/processed/{name}')
 ar=np.asarray(im).astype(float);edge_x=float(np.abs(ar[:,0]-ar[:,-1]).mean());edge_y=float(np.abs(ar[0]-ar[-1]).mean());inside=float((np.abs(np.diff(ar,axis=0)).mean()+np.abs(np.diff(ar,axis=1)).mean())/2)
 rows[k]={'status':'processed','source_size':raw.size,'export_size':[80,80],'edge_mean_difference_rgb':[round(edge_x,2),round(edge_y,2)],'interior_neighbor_mean_rgb':round(inside,2),'edge_note':'numerical seam differences reported, visual repeat review required','variants':'90degree rotations only','sha256':hashlib.sha256((R/'processed'/f'{k}.png').read_bytes()).hexdigest()}
 mapping[k]={'file':paths[0],'variants':paths}
(R/'mapping.json').write_text(json.dumps(mapping,indent=2));(R/'manifest.json').write_text(json.dumps({'phase':'ab-review','canonical_terrain_unchanged':True,'default':'original','actual_sources_larger_than_requested80':True,'assets':rows},indent=2))
out=Image.new('RGB',(780,390),'#eae2cf');d=ImageDraw.Draw(out)
for n,k in enumerate(rows):
 x=n*260;d.text((x+10,10),k+' old / new actual80',fill='#273c3c');old=Image.open(R/'original-terrain'/f'{k}.png').convert('RGB');im=Image.open(R/'processed'/f'{k}.png');out.paste(old,(x+10,32));out.paste(im,(x+100,32));d.text((x+10,127),'New 2x2 repeat (actual80 tiles)',fill='#273c3c')
 for yy in range(2):
  for xx in range(2):out.paste(im,(x+10+xx*80,150+yy*80))
 d.text((x+10,327),'Edge RGB mean: '+str(rows[k]['edge_mean_difference_rgb']),fill='#273c3c')
out.save(R.parent/'reviews/terrain-repeat-comparison.png');print(json.dumps(rows,indent=2))
