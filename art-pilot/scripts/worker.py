"""Resumable local ComfyUI queue. Never publishes or starts mass production."""
from pathlib import Path
import argparse,json,time,urllib.request,urllib.error,shutil,hashlib,sys,subprocess
ROOT=Path(__file__).resolve().parents[1];RUNTIME=ROOT.parents[1]/'art-runtime';COMFY=RUNTIME/'ComfyUI';URL='http://127.0.0.1:8188'
def api(path,data=None):
 req=urllib.request.Request(URL+path,data=None if data is None else json.dumps(data).encode(),headers={'Content-Type':'application/json'})
 try:
  with urllib.request.urlopen(req,timeout=45) as r:return json.load(r)
 except urllib.error.HTTPError as e:raise RuntimeError(e.read().decode()) from e
def save(data):
 p=ROOT/'assets.json';tmp=p.with_suffix('.tmp');tmp.write_text(json.dumps(data,indent=2));tmp.replace(p)
def workflow(a):
 wf={'1':{'class_type':'CheckpointLoaderSimple','inputs':{'ckpt_name':a.get('model','sdxl_lightning_8step.safetensors')}},'2':{'class_type':'CLIPTextEncode','inputs':{'clip':['1',1],'text':a['prompt']}},'3':{'class_type':'CLIPTextEncode','inputs':{'clip':['1',1],'text':a['negative']}},'4':{'class_type':'EmptyLatentImage','inputs':{'width':a['width'],'height':a['height'],'batch_size':1}},'5':{'class_type':'KSampler','inputs':{'model':['12',0],'positive':['2',0],'negative':['3',0],'latent_image':['4',0],'seed':a['seed'],'steps':a['steps'],'cfg':a.get('cfg',1.0),'sampler_name':a.get('sampler','euler'),'scheduler':a.get('scheduler','sgm_uniform'),'denoise':a.get('denoise',1.0)}},'6':{'class_type':'VAEDecode','inputs':{'samples':['5',0],'vae':['1',2]}},'7':{'class_type':'SaveImage','inputs':{'images':['6',0],'filename_prefix':'pilot/'+a['id']}},'9':{'class_type':'LoadImage','inputs':{'image':a['reference']}},'10':{'class_type':'CLIPVisionLoader','inputs':{'clip_name':'CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors'}},'11':{'class_type':'IPAdapterModelLoader','inputs':{'ipadapter_file':'ip-adapter-plus_sdxl_vit-h.safetensors'}},'12':{'class_type':'IPAdapterAdvanced','inputs':{'model':['1',0],'ipadapter':['11',0],'image':['9',0],'weight':a.get('weight',.75),'weight_type':a.get('weight_type','style transfer'),'combine_embeds':'concat','start_at':0.0,'end_at':1.0,'embeds_scaling':'V only','clip_vision':['10',0]}}}

 if a.get('style_reference'):
  wf['14']={'class_type':'LoadImage','inputs':{'image':a['style_reference']}}
  wf['12']={'class_type':'IPAdapterStyleComposition','inputs':{'model':['1',0],'ipadapter':['11',0],'image_style':['14',0],'image_composition':['9',0],'weight_style':a.get('style_weight',.85),'weight_composition':a.get('composition_weight',.35),'expand_style':False,'combine_embeds':'average','start_at':0.0,'end_at':1.0,'embeds_scaling':'V only','clip_vision':['10',0]}}
 if a.get('init_image'):
  wf['15']={'class_type':'LoadImage','inputs':{'image':a['init_image']}}
  wf['4']={'class_type':'VAEEncode','inputs':{'pixels':['15',0],'vae':['1',2]}}
 return wf

def run(ids):
 data=json.loads((ROOT/'assets.json').read_text());data['phase']='pilot-generation'
 for a in data['assets']:
  if ids and a['id'] not in ids:continue
  if a['status'] not in ['pending','submitted','generating']:continue
  used=int(subprocess.check_output(['du','-sk',str(RUNTIME)]).split()[0])*1024
  if used>25_000_000_000:raise RuntimeError('25GB disk cap reached')
  if not a.get('prompt_id'):
   a['reference_sha256']=hashlib.sha256((COMFY/'input'/a['reference']).read_bytes()).hexdigest();wf=workflow(a);(ROOT/'workflows'/f"{a['id']}.json").write_text(json.dumps(wf,indent=2));a['workflow_sha256']=hashlib.sha256(json.dumps(wf,sort_keys=True).encode()).hexdigest();a['status']='submitting';save(data)
   result=api('/prompt',{'prompt':wf,'client_id':'last-current-pilot'});a['prompt_id']=result['prompt_id'];a['status']='submitted';a['started_at']=time.time();save(data);print('SUBMITTED',a['id'],a['prompt_id'],flush=True)
  while True:
   history=api('/history/'+a['prompt_id']);entry=history.get(a['prompt_id'])
   if entry:
    a['elapsed_seconds']=round(time.time()-a.get('started_at',time.time()),2)
    (ROOT/'logs'/f"history-{a['id']}.json").write_text(json.dumps(entry,indent=2))
    if entry.get('status',{}).get('status_str')=='error':a['status']='failed';save(data);raise RuntimeError('ComfyUI failed; inspect history-'+a['id']+'.json')
    images=entry.get('outputs',{}).get('7',{}).get('images',[])
    if not images:raise RuntimeError('Job ended without saved image')
    image=images[0];source=COMFY/'output'/image.get('subfolder','')/image['filename'];target=ROOT/'raw'/f"{a['id']}.png";shutil.copy2(source,target);a['raw_file']=str(target.relative_to(ROOT));a['status']='generated';save(data);print('GENERATED',a['id'],a['elapsed_seconds'],'seconds',flush=True);break
   time.sleep(3)
 data['phase']='pilot-processing';save(data)
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--only',nargs='*');args=parser.parse_args()
 try:run(set(args.only or []))
 except Exception as e:print(type(e).__name__+': '+str(e),file=sys.stderr);sys.exit(1)
