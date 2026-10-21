from pathlib import Path
import json
R=Path(__file__).resolve().parent;inv=json.loads((R.parent/'inventory.json').read_text())['roles']['items']
specs={
'ranger':'sage short surveyor coat, brown close cap, large coiled grapple rope with one blunt hook, no bow',
'gardener':'sage broad gardening apron, wide straw hat, small ivory seed tin with one sprout',
'engineer':'ochre work vest, rust flat cap, carrying one round charge and broad wrench',
'archer':'muted plum short cape, uncovered dark hair, one large simple longbow',
'medic':'ivory tabard with one rust medical cross, ochre soft cap, broad medical satchel',
'carrier':'teal rolled sleeves, broad ivory padded shoulder yoke, sturdy open carrying frame on back',
'mawkeeper':'sage overalls, ochre floppy hat, one pot holding a single broad toothed plant mouth',
'vinekeeper':'deepteal wrap, sage leaf shaped shoulder cape, one large simple loop of vine',
'shaman':'rust draped shawl, ivory hair bun, one short ochre hearth totem with simple flame shape',
'blight':'mutedplum long apron, sage headscarf, one squat dark vessel with one pale green droplet',
'bulldozer':'broad ochre work coat, rust helmet, enormous plain rectangular pushing board held across torso',
'witch':'mutedplum crooked brim hat, ivory shawl, one crescent shaped charm held forward',
'astronomer':'deepteal long coat, ivory round cap, one large brass astrolabe ring',
'digger':'sage rolled sleeves, ochre workcap, large broad spade across shoulder',
'geomancer':'ivory short mantle, sage hoodless tunic, holding one solid square stone block',
'sapper':'rust short jacket, ivory headband, large simple demolition shears held low',
'mirror':'mutedplum asymmetric dancer robe, ivory hair sweep, one broad oval handheld mirror',
'blink':'teal short fitted tunic, rust scarf trailing one broad ribbon, lightly bent running stance, no weapon',
'ferryman':'ochre raincape, broad flat teal boat hat, one long blunt wooden paddle',
'builder':'ivory workshirt, teal apron, ochre cap, one broad bridge plank and simple mallet',
'alchemist':'sage long apron, ivory headscarf, one broad flask containing pale teal liquid',
'firestarter':'rust sleeveless mantle, dark hair topknot, one simple orange flame cup',
'warden':'ivory heavy coat, ochre guard helmet, large round teal protective shield',
'herder':'sage dress, ivory scarf, one short wooden flute held near mouth',
'gust':'ivory loose tunic, teal swept cape, one large simple folding fan',
'magnet':'teal workjacket, ochre close cap, one enormous horseshoe magnet with rust tips',
'courier':'rust short coat, ivory messenger cap, large teal envelope pouch, forward running pose',
'anchorite':'ochre heavy robe, ivory bare head and short beard, holding simple dark anchor stone',
'tinkerer':'sage workvest, rust beret, one broad crank handle and small square gear',
'conductor':'deepteal uniform coat, ivory conductor cap, one short ochre signal baton raised',
'weaver':'mutedplum shawl, ivory cloth cap, one large open oval loom loop with two crossing threads',
'siren':'deepteal flowing dress, ivory hair bob, one broad shell horn',
'icewright':'ivory workcoat with teal cuffs, sage cap, one large pale teal ice crystal block',
'beekeeper':'ochre smock, broad ivory beekeeper veil silhouette, one simple round honey pot and single small bee drone',
'demolition':'rust padded jacket, ochre helmet, broad square detonator box with one plunger',
'recaller':'mutedplum travel coat, ivory hood folded down, one large simple compass disk',
'scout':'sage short cloak, rust featherless cap, broad map scroll held open, crouched ready stance',
'liberator':'ivory tunic, rust scarf, one enormous brass key held upward',
'harvester':'sage workapron, ivory rolled sleeves, one broad curved pruning sickle held low',
'plumber':'deepteal overalls, ochre cap, one enormous pipe wrench with open jaw',
'rainmaker':'sage raincoat, ivory brim hat, one broad teal umbrella held overhead',
'firefighter':'rust rescue coat, ivory protective helmet, broad dark hose nozzle held forward',
'mason':'ivory workvest, sage cap, one large blunt stone lifting tong gripping square block',
'lantern':'deepteal longcoat, ochre softcap, one broad warm ivory lantern with dark frame',
'spore':'mutedplum apron, sage mushroom shaped hat, one broad spore puff vessel, no floating particle cloud',
'puppeteer':'mutedplum short mantle, ivory closecap, one large wooden control cross with two clear strings',
'rigger':'ochre overalls, teal workcap, holding one short broad conveyor roller section',
'bombardier':'rust aviator workcoat, ivory cap, one round blunt shell tucked under arm, no gun'}
common='ONE full-body original tactical game character RASTER sprite designed FOR80x80, clearat64px. Reference1 accepted originalsmallcharacterstrip, reference2 accepted simple Mara; match EXACT quiet broad opaque gouache shapes, irregular dark ink outline, compact3–4head proportions, tiny warm natural face with one simple dark eye mark, large readable equipment. 12–18major paintshapesTOTAL, one solid base plus ONE broad shade per material, no tiny details. Elevated frontal square-grid camera. Genuine transparentalpha background. NO grain/granulation, texture, scuffs, scratches, hatching, laces, rivets, filigree, tinystraps, gloss, realisticrender, vector substitution, text, multiplefigures, floor, ground/cast/contactshadow or tilebase. Single complete character centered. '
m={'category':'roles','phase':'generating','assets':{}}
for k,a in inv.items():
 entry={'id':k,'name':a['name'],'title':a['title'],'status':'pending','file':f'processed/{k}.png'}
 if k in ['vanguard','tidecaller']:
  entry.update(status='reused',source='art-pilot/builtin-simple80/processed/'+('ally-1' if k=='vanguard' else 'ally-2')+'.png')
 else:
  prompt=common+'Identity: '+a['name']+', '+a['title']+'. Visual signature: '+specs[k]+'. Character context: '+a['lore']+' Ability context: '+a['desc']+' Do not depict a second person or abilityscene; equipment represents the role.'
  (R/'prompts'/f'{k}.txt').write_text(prompt);entry['prompt']=f'prompts/{k}.txt';entry['signature']=specs[k]
 m['assets'][k]=entry
(R/'manifest.json').write_text(json.dumps(m,indent=2))
