from PIL import Image,ImageDraw
import pathlib,json,sys
root=pathlib.Path(__file__).resolve().parents[2]
cat=sys.argv[1];p=root/'art-production'/cat;m=json.loads((p/'manifest.json').read_text());items=[(k,v) for k,v in m['items'].items() if v['status'] in ['processed','reviewed','reused']]
w=800;h=((len(items)+4)//5)*160
sheet=Image.new('RGB',(w,max(h,160)), '#e9e5d5');d=ImageDraw.Draw(sheet)
for n,(id,v) in enumerate(items):
 path=pathlib.Path(v['processed']);path=path if path.is_absolute() else root/path
 if not path.exists():continue
 im=Image.open(path).convert('RGBA');x=(n%5)*160;y=(n//5)*160
 for i,bg in enumerate(['#e9e5d5','#243d40']):
  bgim=Image.new('RGBA',(80,120),bg);bgim.alpha_composite(im,(0,0));bgim.alpha_composite(im.resize((40,40),Image.Resampling.LANCZOS),(20,80));sheet.paste(bgim.convert('RGB'),(x+i*80,y+20))
 d.text((x+4,y+3),id,fill='#233a3b')
 if cat=='terrain':
  rep=Image.new('RGBA',(160,160))
  for a,b in [(0,0),(80,0),(0,80),(80,80)]:rep.alpha_composite(im,(a,b))
  rep.save(p/'reviews'/f'{id}-repeat2x2.png')
sheet.save(p/'reviews'/'contact-80-40-light-dark.png')
print(len(items),'available entries')
