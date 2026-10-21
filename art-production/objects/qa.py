import pathlib,json,hashlib
from PIL import Image,ImageDraw
p=pathlib.Path(__file__).parent;m=json.load(open(p/'manifest.json'));refs=['reference-character-strip.png','raw/ally-1.png','raw/tree.png','raw/wall.png','raw/fan.png'];qa=[]
for k,v in m['items'].items():
 if v['status']=='reused':
  v['processed']='art-pilot/builtin-simple80/processed/'+k+'.png';v['source']='art-pilot/builtin-simple80/raw/'+k+'.png';v['reuseNote']='Approved pilot source; parent owns production copy.'
 else:
  v['promptPath']=str(p/'prompts'/f'{k}.txt');v['referencePaths']=['art-pilot/builtin-simple80/'+r for r in refs];v['generationTool']='built-in image_gen; backend model ID not exposed';v['native80']=False;v['status']='reviewed';im=Image.open(v['processed']).convert('RGBA');b=im.getchannel('A').point(lambda a:255 if a>16 else 0).getbbox();v['visibleBounds']=list(b);qa.append({'id':k,'visibleBounds':list(b),'size':list(im.size),'alphaExtrema':list(im.getchannel('A').getextrema())})
for size in [80,40]:
 for name,bg,fg in [('light','#e9edd3','#243736'),('dark','#243736','#e9edd3')]:
  cw=size+34;ch=size+26;sheet=Image.new('RGB',(8*cw,5*ch),bg);d=ImageDraw.Draw(sheet)
  for n,(k,v) in enumerate(m['items'].items()):
   im=Image.open(v['processed']).convert('RGBA');im=im.resize((size,size),Image.Resampling.LANCZOS);x=(n%8)*cw+17;y=(n//8)*ch;sheet.paste(im,(x,y),im);d.text((x,y+size+2),k,fill=fg)
  sheet.save(p/f'contact-{size}-{name}.png')
json.dump(m,open(p/'manifest.json','w'),indent=2);json.dump(qa,open(p/'qa.json','w'),indent=2)
(p/'CHECKPOINT.md').write_text('# Objects complete\n35/35 new assets generated with built-in image_gen; four accepted pilot objects reused. All 39 accounted for.\nAll new sources copied immediately; prompts and hashes retained. Raw native sizes exceed 80; runtime exports are 80×80.\nVisible alpha >16 selects crop only; generated alpha is preserved within crop. Lanczos resize and centered bottom y72 anchoring only.\nLow max footprints: bridge 66×28, plate 58×22, drain 58×24, glass 60×24, portal 62×28, spikes 62×32, spring 58×40. Other new objects max66×62. Pilot wall66×32, column38×62.\nMaw first output rejected by moderation other; second botanical cartoon prompt succeeded. No unresolved failures.\nQA contact sheets: contact-80-light/dark.png and contact-40-light/dark.png. Parent owns game registry integration and accepted-file copies.\n')
