from PIL import Image
from pathlib import Path
import sys,json,hashlib,shutil
root=Path(__file__).resolve().parent.parent
id,source=sys.argv[1:3];folder=root/'art-production/roles-extra';raw=folder/'raw'/(id+'.png')
if Path(source).resolve()!=raw.resolve():shutil.copyfile(source,raw)
im=Image.open(raw).convert('RGBA');box=im.getchannel('A').point(lambda a:255 if a>16 else 0).getbbox()
if not box or im.getchannel('A').getextrema()[0]!=0:raise ValueError('Missing genuine alpha')
cut=im.crop(box);scale=min(66/cut.width,62/cut.height);cut=cut.resize((round(cut.width*scale),round(cut.height*scale)),Image.Resampling.LANCZOS)
canvas=Image.new('RGBA',(80,80));canvas.alpha_composite(cut,((80-cut.width)//2,72-cut.height));out=folder/'processed'/(id+'.png');canvas.save(out)
manifestpath=folder/'manifest.json';m=json.loads(manifestpath.read_text()) if manifestpath.exists() else {'category':'roles-extra','assets':{}}
original=m['assets'].get(id,{}).get('originalToolPath',source)
m['assets'][id]={'status':'processed','source':str(raw.relative_to(root)),'originalToolPath':original,'sourceSize':list(im.size),'file':'processed/'+id+'.png','prompt':'prompts/'+id+'.txt','sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'runtimeSize':[80,80],'anchor':[.5,.9]}
manifestpath.write_text(json.dumps(m,indent=2));(folder/'CHECKPOINT.md').write_text('# Primary crew shard\n\nCompleted: '+', '.join(m['assets'])+'\n\nOwn IDs: harvester, plumber, rainmaker, firefighter, mason, lantern, spore, puppeteer, rigger, bombardier. Continue missing IDs only. Sources/prompts preserved. Parent assembly reads this folder before roles.\n')
print(id+': 80px genuine-alpha export saved')
