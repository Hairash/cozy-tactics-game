from pathlib import Path
from PIL import Image,ImageDraw
import json
root=Path(__file__).resolve().parents[1];input=root.parents[1]/'art-runtime/ComfyUI/input';board=Image.open(root/'reference/concept-board.png').convert('RGB')
for aid,box in {'tree':(1304,855,1351,915),'column':(1482,845,1526,909),'wall':(1310,919,1370,963),'ground':(1205,815,1246,849),'grass':(1155,815,1197,849),'water':(1205,862,1246,900)}.items():
 im=board.crop(box);scale=400/max(im.size);im=im.resize((round(im.width*scale),round(im.height*scale)),Image.Resampling.LANCZOS);out=Image.new('RGB',(512,512),'#f1e8d0');out.paste(im,((512-im.width)//2,(512-im.height)//2));out.save(root/'reference'/f'{aid}.png');out.save(input/f'pilot-{aid}.png')
# Neutral geometric composition guides, not final art; generated output receives painted reference style.
for aid in ['fan','enemy-2']:
 im=Image.new('RGB',(512,512),'#f4ecd9');d=ImageDraw.Draw(im)
 if aid=='fan':
  d.rounded_rectangle((165,386,348,450),radius=8,fill='#caba91',outline='#263e3d',width=6);d.rectangle((223,310,288,410),fill='#879b85',outline='#263e3d',width=5);d.ellipse((105,90,407,360),fill='#be9c62',outline='#263e3d',width=7);d.ellipse((122,106,390,344),fill='#e4d8b5',outline='#263e3d',width=5)
  for poly in [[(250,226),(189,135),(153,193),(222,247)],[(251,225),(351,190),(345,259),(277,256)],[(252,226),(267,323),(199,298),(228,245)]]:d.polygon(poly,fill='#477a73',outline='#263e3d')
  d.ellipse((232,212,274,252),fill='#c5ac73',outline='#263e3d',width=4)
 else:
  d.polygon([(140,130),(330,105),(367,318),(127,318)],fill='#4e6260',outline='#263e3d');d.polygon([(122,126),(336,100),(363,169),(129,181)],fill='#dbd4b5',outline='#263e3d');d.rectangle((205,186,292,209),fill='#bf8c4f',outline='#263e3d',width=4)
  d.polygon([(119,183),(61,208),(72,345),(140,332)],fill='#72827a',outline='#263e3d');d.polygon([(351,178),(418,201),(440,329),(362,343)],fill='#8d9a85',outline='#263e3d');d.rectangle((150,314,207,414),fill='#687e76',outline='#263e3d',width=5);d.rectangle((285,316,343,414),fill='#687e76',outline='#263e3d',width=5);d.polygon([(135,397),(209,397),(218,440),(127,440)],fill='#374e4e');d.polygon([(282,397),(355,397),(374,440),(273,440)],fill='#374e4e')
 im.save(root/'reference'/f'{aid}-guide.png');im.save(input/f'pilot-{aid}.png')
style=' Peculiar angular hand-painted fantasy storybook gouache, thin broken dark ink contours, flat matte paint, muted cream sage teal ochre, restrained detail. Full object visible from elevated FRONT camera, centered alone, plain white background.'
subjects={
'ally-1':'One cozy harbor keeper woman, short sturdy proportions, very large asymmetric triangular teal work cloak, cream cuffs, chunky square boots, tiny face shaded under crooked hood, a large blunt rectangular brass ram guard on left forearm, free right hand. Broad lopsided silhouette, no sword.',
'ally-2':'One cozy river tender, oversized sharp pointed cream hood, tiny face shaded deep in the hood with two small eyes, short asymmetric deep teal coat with huge cuffs, short square boots, holding one curved brass tuning fork with small round turquoise tide dial. Narrow angular silhouette, no flames.',
'enemy-1':'One compact weather-city Sentinel automaton, front facing, narrow upright dark slate triangular ceramic body, one small centered amber eye, two short spindly mechanical legs, one short brass emitter pointed toward viewer, asymmetrical ivory shoulder. Simple strange attentive silhouette, no face or hands.',
'enemy-2':'One heavy Bellwether maintenance robot, broad lopsided slate trapezoid body, huge blunt square ram forearms, two short thick mechanical legs, chipped ivory shoulder shell, tiny amber horizontal eye slit, brass joints. Squat angular silhouette. Clearly a machine, no skull or monster.',
 'tree':'One small crooked briar tree, bent short trunk, three broad angular sage and dark teal foliage masses, exaggerated lopsided crown, sparse bold twig notches, small roots. Cozy expressive unusual shape without face. No scenery.',
 'column':'One freestanding squat ruined ivory column, broad tapering square shaft, huge skewed square cap, compact cracked stepped foot, tiny sage moss patches. Three bold cracks and small brass tide gauge. Thick simple topplable silhouette, only one column.',
 'wall':'One low solid cream masonry wall block, three huge irregular angular stones, two dark joints, shallow flat top, tiny sage moss patch. Closed sturdy rectangular barrier, horizontal front edge, compact square footprint, no doorway, only one wall block.',
 'fan':'One antique weather-control table FAN, one circular old brass rim enclosing three broad dark teal fan blades and a cream central hub, two chunky supports on low square ceramic base, asymmetric practical bracket. A short wide mechanical fan, not a creature or totem.'}
negative='multiple figures, collection, variants, character sheet, panels, frames, border, swatches, diagram, text, letters, watermark, profile, side view, diamond ground tile, glossy plastic, 3d render, photograph, anime, big eyes, eyelashes, realistic anatomy, long legs, icon, sticker, vector logo, thick smooth outlines, neon glow, skull, skeleton, horns, demon'
changes={}
for i,(aid,prompt) in enumerate(subjects.items()):
 changes[aid]={'prompt':prompt+style,'negative':negative,'model':'DreamShaperXL_Turbo_v2_1.safetensors','sampler':'dpmpp_sde','scheduler':'karras','steps':6,'cfg':2.0,'style_reference':'pilot-style-map.png','style_weight':.8,'composition_weight':.2 if aid=='ally-2' else .5,'seed':484410+i*79}
for i,aid in enumerate(['ground','grass','water']):
 prompt={'ground':'Seamless flat TOP DOWN quiet sandstone soil texture, muted warm ochre beige, a few very small angular stone flecks and fine matte gouache paper grain. No objects no perspective no grid no diamond pattern no borders no grass clumps.', 'grass':'Seamless flat TOP DOWN quiet sage moss meadow texture, muted sage green gouache, a few tiny irregular grass specks and soft painted patches. No objects no perspective no grid no diamond pattern no crosshatching no borders.', 'water':'Seamless flat TOP DOWN turquoise water texture, muted teal gouache, a few tiny thin cream broken ripples, matte painted surface, quiet broad flat color. No objects no perspective no grid no lines across entire image no waves no banks no borders.'}[aid]
 changes[aid]={'prompt':prompt,'negative':negative+', scenery, building, plants, floor tiles, crosshatch, diamond pattern','model':'DreamShaperXL_Turbo_v2_1.safetensors','sampler':'dpmpp_sde','scheduler':'karras','steps':6,'cfg':2.0,'style_reference':'pilot-style-map.png','style_weight':.35,'composition_weight':.2,'seed':485510+i*71}
(root/'workflows/painterly-revision.json').write_text(json.dumps(changes,indent=2))
