from pathlib import Path
import json,shutil,sys
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'assets.json').read_text());changes=json.loads(Path(sys.argv[1]).read_text())
for aid,update in changes.items():
 a=next(a for a in data['assets'] if a['id']==aid);version=len(a.get('versions',[]))+1;folder=ROOT/'raw'/f'v{version}';folder.mkdir(exist_ok=True)
 old={k:v for k,v in a.items() if k!='versions'}
 for key in ['raw_file','file']:
  if a.get(key) and (ROOT/a[key]).exists():
   target=folder/(('processed-' if key=='file' else '')+Path(a[key]).name);shutil.copy2(ROOT/a[key],target);old[key]=str(target.relative_to(ROOT))
 wf=ROOT/'workflows'/f'{aid}.json'
 if wf.exists():shutil.copy2(wf,folder/f'{aid}-workflow.json')
 a.setdefault('versions',[]).append(old)
 for key in ['prompt_id','raw_file','file','started_at','elapsed_seconds','workflow_sha256','alpha_coverage','alpha_edge_clear','processing']:a.pop(key,None)
 a.update(update);a['status']='pending';a['review_status']='revision-requested'
(ROOT/'assets.json').write_text(json.dumps(data,indent=2));print('Revised',','.join(changes))
