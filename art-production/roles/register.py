from pathlib import Path
from PIL import Image
import json,shutil,hashlib,sys,os
R=Path(__file__).resolve().parent;k=sys.argv[1];p=R/'manifest.json';m=json.loads(p.read_text());a=m['assets'][k]
if len(sys.argv)>2 and sys.argv[2]=='start':
 a['status']='generating';p.write_text(json.dumps(m,indent=2));sys.exit()
src=max(Path(os.environ.get('IMAGEGEN_INPUT_DIR',str(R/'raw'/'incoming'))).glob('*.png'),key=lambda f:f.stat().st_mtime);dest=R/'raw'/f'{k}.png';shutil.copy2(src,dest);im=Image.open(dest).convert('RGBA');alpha=im.getchannel('A');b=alpha.point(lambda x:255 if x>16 else 0).getbbox()
if alpha.getextrema()[0]!=0:raise ValueError('No genuine transparency')
crop=im.crop(b);crop.thumbnail((66,62),Image.Resampling.LANCZOS);out=Image.new('RGBA',(80,80));out.alpha_composite(crop,((80-crop.width)//2,72-crop.height));out.save(R/'processed'/f'{k}.png');h=out.getchannel('A').histogram()
a.update(status='processed',raw=f'raw/{k}.png',builtin_source=f'raw/{k}.png',actual_source_size=im.size,export_size=[80,80],bbox=out.getbbox(),coverage=round(sum(h[65:])/6400,4),sha256=hashlib.sha256((R/'processed'/f'{k}.png').read_bytes()).hexdigest(),references=['art-pilot/builtin-simple80/reference-character-strip.png','art-pilot/builtin-simple80/raw/ally-1.png'])
p.write_text(json.dumps(m,indent=2));done=sum(a['status'] in ['processed','reused','reviewed'] for a in m['assets'].values());(R/'CHECKPOINT.md').write_text(f'# Roles checkpoint\n\n{done}/50 processed or reused. Last {k}. One builtin call per newrole; native tool outputs larger than80, exportedcrop/resizeonly with genuinealpha. Manifest authoritative; skip completed, reconcile generatingbeforeduplicate.\n');print(k,done,'/50',a['actual_source_size'])
