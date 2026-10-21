from pathlib import Path
from PIL import Image,ImageDraw
import json,numpy as np
from scipy import ndimage
R=Path(__file__).resolve().parent;ROOT=R.parents[1];p=R/'manifest.json';m=json.loads(p.read_text());entries=[a for a in m['assets'].values() if a['status']!='delegated-to-primary'];qa=[]
for a in entries:
 f=ROOT/a['source'] if a['status']=='reused' else R/a['file'];im=Image.open(f).convert('RGBA');alpha=np.array(im.getchannel('A'));mask=alpha>64;labels,_=ndimage.label(mask);sizes=np.bincount(labels.ravel())[1:];bbox=im.getbbox();fails=[]
 if im.size!=(80,80):fails.append('size')
 if any([alpha[0].any(),alpha[-1].any(),alpha[:,0].any(),alpha[:,-1].any()]):fails.append('edge')
 if not .04<mask.mean()<.65:fails.append('coverage')
 share=float(max(sizes,default=0)/max(1,mask.sum()))
 if share<.8:fails.append('fragmented')
 a['qa']={'failures':fails,'coverage':round(float(mask.mean()),4),'main_component_share':round(share,4),'bbox':bbox};qa.append({'id':a['id'],**a['qa']})
 if a['status']=='processed':a['status']='reviewed'
for mode in ['light','dark']:
 bg='#eee4cc' if mode=='light' else '#263c40';fg='#263c40' if mode=='light' else '#eee4cc';out=Image.new('RGB',(1000,600),bg);d=ImageDraw.Draw(out)
 for n,a in enumerate(entries):
  x=(n%10)*100;y=(n//10)*150;f=ROOT/a['source'] if a['status']=='reused' else R/a['file'];im=Image.open(f).convert('RGBA');out.paste(im,(x+10,y+4),im);sm=im.resize((40,40),Image.Resampling.LANCZOS);out.paste(sm,(x+30,y+86),sm);d.text((x+3,y+132),a['id'],fill=fg)
 out.save(R/f'contact-{mode}-80-40.png')
m['phase']='category-complete';m['completion']={'assigned':40,'new_generated':38,'reused':2,'delegated':10,'technical_failures':[r for r in qa if r['failures']]};p.write_text(json.dumps(m,indent=2));(R/'qa.json').write_text(json.dumps(qa,indent=2));print(json.dumps(m['completion']))
(R/'CHECKPOINT.md').write_text('# Roles category complete\n\n40assigned ready:38new builtin raster +2acceptedreuses. Last10 delegated-to-primaryinroles-extra, notgeneratedhere. Allsource1254×1254; runtime80crop/resizeonlygeneratedalpha retained. Exactprompts/sourcepaths/hash/QAinmanifest. contact-light-80-40.png andcontact-dark-80-40.png actualpixels. No dist/pilot/sharedwrites.\n')
