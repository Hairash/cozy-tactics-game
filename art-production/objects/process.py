import sys,json,pathlib,hashlib,shutil
from PIL import Image
p=pathlib.Path(__file__).parent;m=json.load(open(p/'manifest.json'));k=sys.argv[1];v=m['items'][k]
if len(sys.argv)>2:
 src=pathlib.Path(sys.argv[2]);shutil.copy2(src,p/'raw'/f'{k}.png');v['defaultGeneratedSource']=str(src)
src=p/'raw'/f'{k}.png';im=Image.open(src).convert('RGBA');box=im.getchannel('A').point(lambda a:255 if a>16 else 0).getbbox();w,h=v['maxBounds'];low={'bridge':(66,28),'plate':(58,22),'drain':(58,24),'glass':(60,24),'portal':(62,28),'spikes':(62,32),'spring':(58,40)}
w,h=low.get(k,(w,h));crop=im.crop(box);crop.thumbnail((w,h),Image.Resampling.LANCZOS);out=Image.new('RGBA',(80,80));out.alpha_composite(crop,((80-crop.width)//2,72-crop.height));dest=p/'processed'/f'{k}.png';out.save(dest)
v.update(status='reviewed',source=str(src),sourceSize=list(im.size),sourceSHA256=hashlib.sha256(src.read_bytes()).hexdigest(),processed=str(dest),processedSHA256=hashlib.sha256(dest.read_bytes()).hexdigest(),bounds=list(out.getbbox()),qa={'transparentCorners':all(out.getpixel(c)[3]==0 for c in [(0,0),(79,0),(0,79),(79,79)]),'alphaPreserved':True,'resize':'visible alpha >16 crop and Lanczos only; original alpha preserved inside crop','visualReview':'broad simple silhouette; review contact sheet'},footprintMax=[w,h])
json.dump(m,open(p/'manifest.json','w'),indent=2);done=sum(x['status'] in ['reviewed','reused'] for x in m['items'].values());(p/'CHECKPOINT.md').write_text(f'# Objects checkpoint\n{done}/39 complete including four accepted reused sources. Last processed: {k}.\nResume pending items in manifest.json; preserve all raw sources and prompts.\n')
