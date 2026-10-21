from pathlib import Path
from PIL import Image
import json
r=Path(__file__).resolve().parent;p=r/'manifest.json';d=json.loads(p.read_text())
for k,a in d['assets'].items():
 f=r/'raw'/f'{k}.png'
 if f.exists(): a.update(status='generated',raw=f'raw/{k}.png',prompt=f'prompts/{k}.txt',actual_source_dimensions=Image.open(f).size)
d['phase']='generating';p.write_text(json.dumps(d,indent=2))
