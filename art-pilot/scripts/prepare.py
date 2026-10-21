from pathlib import Path
from PIL import Image
import json, shutil
root=Path(__file__).resolve().parents[1]
runtime=root.parents[1]/'art-runtime'/'ComfyUI'
board=Image.open(root/'reference/concept-board.png').convert('RGB')
# Crops are conditioning inputs only. None are exported as game assets.
crops={'ally-1':(67,412,139,492),'ally-2':(195,413,255,492),'enemy-1':(778,417,827,493),'enemy-2':(337,412,414,492),'tree':(14,276,87,376),'column':(1454,824,1526,911),'wall':(1175,910,1240,986),'fan':(829,419,884,493),'ground':(81,173,145,239),'grass':(237,271,296,330),'water':(328,258,362,296)}
for name,box in crops.items():
 im=board.crop(box);factor=400/max(im.size);im=im.resize((round(im.width*factor),round(im.height*factor)),Image.Resampling.LANCZOS)
 square=Image.new('RGB',(512,512),(244,234,209));square.paste(im,((512-im.width)//2,(512-im.height)//2))
 square.save(root/'reference'/f'{name}.png');shutil.copy2(root/'reference'/f'{name}.png',runtime/'input'/f'pilot-{name}.png')
style='A single isolated hand painted tactical game sprite, confident irregular dark ink contours, flat opaque gouache fills on clean plain white background. Cozy peculiar angular silhouette, exaggerated asymmetric shapes, restrained detail, three value groups, muted cream sage deep teal old brass. Elevated frontal view, screen-aligned square grid camera, no diamond base. Entire subject fully visible, centered with clear margin, feet near lower center. Original artwork, stylish illustrated fantasy industrial world.'
subjects={
'ally-1':'One harbor keeper woman with an oversized angular teal hooded cloak, broad trapezoid shoulders, cream work clothes, square boots, small kind face, a large brass rectangular ram shield on one forearm, empty other hand. Compact two-and-half head proportions, weird charming silhouette.',
'ally-2':'One slim waterway tender in a long pointed cream hood, asymmetric deep teal coat, oversized folded cuffs, tiny thoughtful face, holding a crooked brass tide-gauge staff with turquoise stone. Angular flowing silhouette, compact proportions.',
'enemy-1':'One strange weather sentry automaton, narrow dark slate wedge body, long thin jointed legs, one small amber diamond eye, a cream asymmetric ceramic shoulder, short brass emitter, curious lopsided stance. Simple flat triangular shapes, no human face.',
'enemy-2':'One heavy squat maintenance golem machine, broad dark slate trapezoid body, two blunt giant ram forearms, short sturdy legs, chipped ivory shoulder shell, tiny amber eye, old brass joints. Weird asymmetrical chunky silhouette, hand inked.',
 'tree':'One crooked small briar tree, angular forked brown trunk, three broad jagged sage green and deep teal foliage masses, unusual asymmetric canopy, sparse bold leaves, tiny roots. Simple graphic silhouette, no face.',
 'column':'One cracked ivory stone column, tapering squared shaft, exaggerated skewed square capital, compact stepped square foot, moss patches, small old brass tide-measure fitting. Topplable ancient ruin, only one column.',
 'wall':'One low cream masonry wall block, three large angular irregular stones, broken dark ink joints, sage moss, one brass repair clamp, broad front face and shallow top visible. Horizontal front edge, compact square footprint, no diamond ground tile.',
 'fan':'One unusual antique weather machine fan, large brass circular guard, three wide angular deep teal blades, cream ceramic frame and short square pedestal, chunky asymmetrical bracket. Hand drawn simple readable manufactured object, no face.',
 'ground':'Seamless flat top-down warm cream sandstone ground texture, broad quiet matte gouache color, very sparse tiny chipped stones, subtle paper grain, no objects no perspective no shadows no lines no borders.',
 'grass':'Seamless flat top-down muted sage meadow ground texture, quiet flat painted color, very sparse tiny angular grass tufts, subtle paper grain, no objects no perspective no shadows no lines no borders.',
 'water':'Seamless flat top-down turquoise water texture, quiet muted teal blue flat gouache with few small cream ripples, subtle painted grain, no banks no objects no perspective no shadows no borders.'}
neg='photograph, 3d render, glossy, plastic, mobile game, chibi, anime, gradients, bloom, dramatic light, dense detail, scenery, floor, diamond, isometric tile, text, watermark, health bar, multiple subjects, character sheet, cropped'
assets=[]
for i,(aid,subject) in enumerate(subjects.items()):
 terrain=aid in ['ground','grass','water'];assets.append({'id':aid,'kind':'terrain' if terrain else 'character' if aid.startswith(('ally','enemy')) else 'object','status':'pending','prompt':subject if terrain else style+' '+subject,'negative':neg,'seed':482701+i*53,'reference':f'pilot-{aid}.png','steps':8,'width':768,'height':768,'weight':0.5 if terrain else 0.75,'anchor':[.5,.88]})
if not (root/'assets.json').exists():(root/'assets.json').write_text(json.dumps({'phase':'pilot-awaiting-generation','human_approval_required':True,'assets':assets},indent=2))
print('Prepared',len(assets),'jobs and conditioning references')
