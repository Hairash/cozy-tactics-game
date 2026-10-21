from pathlib import Path
from PIL import Image
import shutil,json
r=Path(__file__).resolve().parents[1];src=r/'reference/mature-crew';inp=r.parents[1]/'art-runtime/ComfyUI/input'
style=Image.new('RGB',(512,512),'white')
for i,aid in enumerate(['ally-1','ally-2']):
 im=Image.open(src/f'{aid}-init.png').convert('RGB');shutil.copy2(src/f'{aid}-init.png',inp/f'mature-{aid}.png');im.thumbnail((256,480),Image.Resampling.LANCZOS);style.paste(im,(i*256+(256-im.width)//2,(512-im.height)//2))
style.save(inp/'mature-crew-style.png');style.save(src/'style-reference.png')
common='One mature adult harbor worker in an angular illustrated fantasy world. Lean adult proportions, small angular head, bent elbow and bent knees, quietly balanced working stance. Two short dark line eyes, plain calm face, no visible hair. Broad flat matte color planes, confident irregular ink outline, subtle handmade edge variation, only one restrained darker plane, restrained woodcut storybook illustration. No small decorations, no fabric folds, no highlights. Entire single figure elevated frontal view on pure white empty background, no floor, no cast shadow.'
negative='child, baby, chibi, kawaii, anime, mobile game character, glossy, plastic, 3d, realistic, detailed face, hair strands, hair lines, eyebrows, eyelashes, dot eyes, big eyes, smile, open mouth, moustache, beard, decorative buttons, buckles, embroidery, straps, fabric folds, dramatic shading, gradient, highlights, boot shine, glare, tiny detail, scenery, floor, ground shadow, multiple figures, sheet, text, border, cropped, weapon sword'
changes={}
for i,aid in enumerate(['ally-1','ally-2']):
 subject={'ally-1':'Mara wears a short asymmetrical rust-red work cape, small low ochre cap, cream tunic, plain dark boots, and carries a large blunt brass shield with teal center. Rust and ochre silhouette.','ally-2':'Neri wears a long asymmetrical teal work coat with plain ivory hood and cream front, plain dark boots, holds a tall blunt hooked brass tide staff in a bent arm. Teal and ivory silhouette.'}[aid]
 changes[aid]={'prompt':subject+' '+common,'negative':negative,'init_image':f'mature-{aid}.png','reference':f'mature-{aid}.png','style_reference':'mature-crew-style.png','denoise':.56,'style_weight':.35,'composition_weight':.8,'cfg':2.0,'steps':8,'sampler':'dpmpp_sde','scheduler':'karras','seed':843231+i,'source_type':'comfyui-raster','art_direction_model':'gpt-6-astra-low','vector_file':None,'export_size':[80,80]}
(r/'workflows/mature-crew-revision.json').write_text(json.dumps(changes,indent=2))
