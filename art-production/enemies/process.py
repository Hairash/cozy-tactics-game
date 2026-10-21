import json,pathlib,shutil,hashlib,sys
from PIL import Image
cat,id,src,promptfile=sys.argv[1:]
root=pathlib.Path(__file__).resolve().parents[2];p=root/'art-production'/cat
m=json.loads((p/'manifest.json').read_text());d=m['items'][id]
raw=p/'raw'/f'{id}.png';shutil.copy2(src,raw)
im=Image.open(raw).convert('RGBA');bb=im.getchannel('A').point(lambda v:255 if v>16 else 0).getbbox() if cat=='enemies' else im.getbbox()
if cat=='enemies':
 crop=im.crop(bb);crop.thumbnail((66,58 if id in ['heart','sovereign','foundry'] else 62),Image.Resampling.LANCZOS);out=Image.new('RGBA',(80,80));out.alpha_composite(crop,((80-crop.width)//2,72-crop.height))
else:out=im.resize((80,80),Image.Resampling.LANCZOS)
path=p/'processed'/f'{id}.png';out.save(path)
d.update(status='processed',inputpaths=([str(root/'art-pilot/builtin-simple80/raw/enemy-1.png'),str(root/'art-pilot/builtin-simple80/raw/enemy-2.png'),str(root/'art-pilot/builtin-simple80/reference-character-strip.png')] if cat=='enemies' else [str(root/'art-pilot/builtin-terrain-simple/raw/ground.png'),str(root/'art-pilot/builtin-terrain-simple/raw/grass.png'),str(root/'art-pilot/builtin-terrain-simple/raw/water.png'),str(root/'art-pilot/reference/concept-board.png')]),actual_source_path=str(raw),tool_output_path=src,source_dimensions=list(im.size),source_alpha_extrema=im.getchannel('A').getextrema(),processed=str(path.relative_to(root)),processed_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),prompt_path=promptfile,qa={'canvas':[80,80],'bounds':out.getbbox(),'generated_alpha_preserved':True,'processing':'alpha>16 bounding box crop only (original alpha retained inside crop) + Lanczos resize + transparent canvas positioning only'})
(p/'manifest.json').write_text(json.dumps(m,indent=2));(p/'CHECKPOINT.md').write_text(f'Latest processed: {id}.\nCompleted: '+', '.join(k for k,v in m['items'].items() if v['status'] in ['processed','reviewed','reused'])+'\nPending: '+', '.join(k for k,v in m['items'].items() if v['status']=='pending')+'\n')
print(path)
