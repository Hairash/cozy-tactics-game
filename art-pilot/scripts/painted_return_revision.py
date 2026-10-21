"""Return to actual first painted raster sources, never geometric/vector guides."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFilter
import numpy as np,json,shutil
r=Path(__file__).resolve().parents[1];inp=r.parents[1]/'art-runtime/ComfyUI/input';ref=r/'reference/painted-return';ref.mkdir(exist_ok=True);old=r/'archive/painterly-pilot/processed';arc=r/'archive/adult-crew-v3';arc.mkdir(parents=True,exist_ok=True)
if not(arc/'assets.json').exists():
 shutil.copy2(r/'assets.json',arc/'assets.json');shutil.copytree(r/'processed',arc/'processed',dirs_exist_ok=True);shutil.copy2(r/'reviews/adult-crew-v3.png',arc/'contact-sheet.png')
ids=['ally-1','ally-2','enemy-1','enemy-2','tree','column','wall','fan']
for aid in ids:
 im=Image.open(old/f'{aid}.png').convert('RGBA');arr=np.array(im);rgb=arr[:,:,:3].astype(float);yy,xx=np.indices(arr.shape[:2])
 if aid=='ally-1':
  # Warm rust pigment replaces cloak teal while preserving the original painted values/ink.
  mask=(rgb[:,:,1]>rgb[:,:,0]*1.10)&(rgb[:,:,2]>rgb[:,:,0]*1.03)&(rgb.mean(2)>65)&(arr[:,:,3]>80)
  lum=rgb.mean(2)/120;target=np.stack([lum*154,lum*86,lum*61],2);rgb=np.where(mask[:,:,None],target,rgb);arr[:,:,:3]=rgb.clip(0,255).astype('uint8')
 if aid=='ally-2':
  # Ivory hood from original raster brushwork; no new geometry figure.
  mask=(yy<228)&(xx<308)&(rgb[:,:,1]>rgb[:,:,0]*1.06)&(rgb.mean(2)>78)&(arr[:,:,3]>80)
  lum=rgb.mean(2)/135;target=np.stack([lum*218,lum*205,lum*167],2);rgb=np.where(mask[:,:,None],target,rgb);arr[:,:,:3]=rgb.clip(0,255).astype('uint8')
 if aid=='enemy-2':
  # Remove neutral ground-shadow pixels outside the painted machine footprint.
  m=(yy>432)&((rgb.max(2)-rgb.min(2))<35)&(rgb.mean(2)>80);arr[:,:,3]=np.where(m,0,arr[:,:,3])
 im=Image.fromarray(arr)
 if aid=='ally-2':
  # Local raster staff top edit, conditioning only: keep the painted staff shaft.
  d=ImageDraw.Draw(im);d.rectangle((305,78,382,202),fill=(0,0,0,0));d.line([(336,199),(337,177),(356,168),(365,149),(363,130),(350,120),(339,123)],fill='#354b42',width=15,joint='curve');d.line([(336,199),(337,177),(356,168),(365,149),(363,130),(350,120),(339,123)],fill='#b29a66',width=10,joint='curve')
 bg=Image.new('RGBA',(512,512),'white');bg.alpha_composite(im);bg.convert('RGB').save(ref/f'{aid}-init.png');bg.convert('RGB').save(inp/f'painted-return-{aid}.png')
# Shared style is the ACTUAL original painted Mara, not later vector references.
style=Image.open(old/'ally-1.png').convert('RGBA');bg=Image.new('RGBA',style.size,'white');bg.alpha_composite(style);bg.convert('RGB').save(inp/'painted-return-style.png');bg.convert('RGB').save(ref/'style.png')
subjects={'ally-1':'Mara harbor guard, warm muted rust hooded cloak and ivory work tunic, broad ochre blunt shield with teal inset, plain boots, small quiet natural face shaded under hood.', 'ally-2':'Neri river tender, folded ivory pointed hood, muted teal long coat, cream front, hooked brass tide staff, plain boots, small quiet natural face shaded in hood.', 'enemy-1':'Sentinel weather automaton, tall narrow conical slate ceramic body, one small amber eye and three mechanical brass legs.', 'enemy-2':'Breaker maintenance automaton, broad squat teal rectangular torso, chipped ivory top plate and square blunt ram arms, short thick mechanical feet, two small amber sensor lights. No mouth.', 'tree':'Small crooked tree, bent trunk, restrained sage and teal painted foliage clusters, two ochre fruit, irregular silhouette. Simplified broad leaves, no tiny vein detail.', 'column':'Substantial ruined ivory column, broad skewed square cap, tapering thick shaft, stepped compact foot, a few large cracks and sage moss patches.', 'wall':'Low solid ivory masonry barrier, three broad irregular stones, dark joints, shallow flat top, small sage moss patch.', 'fan':'Antique weather fan, circular brass rim, broad dark teal blades, simple practical bracket and short ivory pedestal. Preserve cream color of pedestal. Restrained grille lines.'}
common=' Faithful hand-painted fantasy adventure game sprite, fine irregular dark ink drawing, broad restrained matte gouache color planes, subtle brush texture, muted teal ivory warm rust ochre palette, readable silhouette, consistent moderate detail, two or three large value planes per material, no shiny glints. Same elevated frontal square-grid camera. Single complete subject isolated on pure white background, no floor, no ground shadow.'
negative='vector art, geometric abstraction, flat icon, thick uniform outline, sticker, plastic 3D, glossy highlights, mobile game render, photorealistic, dense scratches, filigree, tiny ornaments, detailed hair strands, boot laces, sparkles, ground shadow, cast shadow, floor, scenery, text, panels, sheet, multiple figures, cropped, diamond base, toy, toddler, huge anime eyes, eyelashes'
c={}
for i,aid in enumerate(ids):c[aid]={'prompt':subjects[aid]+common,'negative':negative,'model':'DreamShaperXL_Turbo_v2_1.safetensors','init_image':f'painted-return-{aid}.png','reference':f'painted-return-{aid}.png','style_reference':'painted-return-style.png','denoise':.4,'style_weight':.7 if aid.startswith('ally') else .45,'composition_weight':.8,'cfg':2.5,'steps':8,'sampler':'dpmpp_sde','scheduler':'karras','seed':751913,'source_type':'comfyui-raster-first-pilot-restyle','art_direction_model':'gpt-6-astra-low','vector_file':None,'export_size':[80,80]}
(r/'workflows/painted-return-revision.json').write_text(json.dumps(c,indent=2))
