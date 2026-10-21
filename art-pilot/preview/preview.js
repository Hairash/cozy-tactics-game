'use strict';
const board=document.querySelector('#board'),sheet=document.querySelector('#sheet');
const expected=['ground','grass','water','wall','column','tree','fan','ally-1','ally-2','enemy-1','enemy-2'];
let assets=[],tile=64,terrainMode='original',terrainAlternates={};
const root=new URL('../',location.href);
function assetFor(id){const a=assets.find(a=>a.id===id)||assets.find(a=>a.kind===id)||assets.find(a=>String(a.id).replaceAll('_','-')===id);return terrainMode==='simple'&&terrainAlternates[id]?{...a,...terrainAlternates[id]}:a;}
function imageFor(a,variant=0){if(!a?.file || ['missing','rejected','failed','pending'].includes(a.status))return null;const img=document.createElement('img');img.src=new URL(a.variants?.[variant%a.variants.length]||a.file,root).href;img.alt=a.id;img.onerror=()=>img.replaceWith(missing(a.id+' · load failed'));return img;}
function missing(label){const d=document.createElement('div');d.className='missing';d.textContent=label+' · missing';return d;}
const water=new Set(['0,2','1,2','2,2','2,3','2,4','3,4','4,4','5,4','5,5','5,6']);
// Connected grassy banks frame a cream path from the lower-left to the ruins.
const grass=new Set(['0,0','1,0','2,0','0,1','1,1','2,1','0,5','0,6','1,6','6,0','7,0','6,1','7,1','7,2','7,3','6,4','7,4','6,5','7,5','6,6','7,6']);
let boardRevision=0;
function usable(a){return a?.file&&!['missing','rejected','failed','pending'].includes(a.status);}
function loadTexture(id){const a=assetFor(id);if(!usable(a))return Promise.resolve(null);return new Promise(resolve=>{const img=new Image();img.onload=()=>resolve(img);img.onerror=()=>resolve(null);img.src=new URL(a.file,root).href;});}
function riverPath(ctx,size){
 const points=[[-.5,2.5],[.5,2.5],[1.5,2.5],[2.5,2.5],[2.5,3.5],[2.5,4.5],[3.5,4.5],[4.5,4.5],[5.5,4.5],[5.5,5.5],[5.5,6.5],[5.5,7.5]].map(([x,y])=>[x*size,y*size]);
 ctx.beginPath();ctx.moveTo(...points[0]);
 // Quadratic joins curve inside bends; straight segments cross exact edge centers.
 for(let i=1;i<points.length-1;i++){const p=points[i],next=points[i+1];ctx.quadraticCurveTo(...p,(p[0]+next[0])/2,(p[1]+next[1])/2);}
 ctx.lineTo(...points.at(-1));
}
async function renderRiver(revision,size){
 const texture=await loadTexture('water');if(revision!==boardRevision)return;
 const canvas=document.createElement('canvas');canvas.className='river-canvas';const dpr=window.devicePixelRatio||1;canvas.width=size*8*dpr;canvas.height=size*7*dpr;canvas.style.width=size*8+'px';canvas.style.height=size*7+'px';const ctx=canvas.getContext('2d');ctx.scale(dpr,dpr);ctx.lineJoin='round';ctx.lineCap='round';
 const stroke=(width,color)=>{riverPath(ctx,size);ctx.lineWidth=width*size;ctx.strokeStyle=color;ctx.stroke();};
 stroke(.78,'#344e43');stroke(.73,'#c8b88b');stroke(.59,'#7faaa0');
 if(texture){const stamp=document.createElement('canvas');stamp.width=size;stamp.height=size;stamp.getContext('2d').drawImage(texture,0,0,size,size);stroke(.57,ctx.createPattern(stamp,'repeat'));}
 else{canvas.setAttribute('aria-label','Water texture missing; connectivity mask only');for(const pos of [[1,2],[3,4],[5,6]]){const label=missing('water texture');label.classList.add('river-missing');label.style.left=pos[0]*size+'px';label.style.top=(pos[1]+.3)*size+'px';board.append(label);}}
 board.append(canvas);
}
function renderBoard(){const revision=++boardRevision;board.replaceChildren();board.classList.toggle('grid-lines',document.querySelector('#gridToggle').getAttribute('aria-pressed')==='true');for(let y=0;y<7;y++)for(let x=0;x<8;x++){const terrain=water.has(x+','+y)?'ground':(grass.has(x+','+y)?'grass':'ground');const cell=document.createElement('div');cell.className='cell '+terrain;cell.style.left=x*tile+'px';cell.style.top=y*tile+'px';const img=imageFor(assetFor(terrain),(x*7+y*11+x*y)%4);if(img){img.className='tile-art';cell.append(img);}else{const m=missing(terrain);m.style.height='100%';cell.append(m);}board.append(cell);}
renderRiver(revision,tile);
const pieces=[['wall',3,0],['wall',4,0],['column',6,1],['tree',0,0],['tree',7,5],['fan',6,4],['ally-1',1,4,'ally'],['ally-2',3,5,'ally'],['enemy-1',5,2,'enemy'],['enemy-2',6,6,'enemy']];
for(const[id,x,y,team]of pieces){const p=document.createElement('div');p.className='piece';p.style.left=x*tile+'px';p.style.top=y*tile+'px';p.style.zIndex=y+10;const a=assetFor(id);const img=imageFor(a);if(img){const anchor=a.anchor||[.5,.8789],scale=Number(a.scale)||1.35;img.style.width=scale*100+'%';img.style.height=scale*100+'%';img.style.left=(.5-anchor[0]*scale)*100+'%';img.style.top=(.9-anchor[1]*scale)*100+'%';p.append(img);}else p.append(missing(id));board.append(p);}}
function renderSheet(){sheet.replaceChildren();const entries=expected.map(id=>assetFor(id)||{id,status:'missing'});for(const a of entries){const card=document.createElement('article');card.className='card';const head=document.createElement('div');head.className='card-head';const name=document.createElement('h3');name.textContent=a.id;const status=document.createElement('span');status.className='status';status.textContent=a.status||'review';head.append(name,status);const samples=document.createElement('div');samples.className='samples';for(const size of ['native','large']){const sample=document.createElement('div');sample.className='sample checker '+size;const img=imageFor(a);if(img){if(size==='native'&&!['ground','grass','water'].includes(a.id)){const scale=Number(a.scale)||1.35;sample.style.width=tile*scale+'px';sample.style.height=tile*scale+'px';}sample.append(img);}else sample.append(missing(a.id));samples.append(sample);}const detail=document.createElement('small');detail.textContent=a.file||'Awaiting generated / processed asset';const anchor=document.createElement('small');anchor.textContent='Anchor '+(a.anchor||[.5,.88]).join(', ');card.append(head,samples,detail,anchor);sheet.append(card);}}
for(const b of document.querySelectorAll('[data-size]'))b.onclick=()=>{tile=b.dataset.size==='phone'?40:64;document.documentElement.style.setProperty('--tile',tile+'px');for(const button of document.querySelectorAll('[data-size]'))button.setAttribute('aria-pressed',String(button===b));document.querySelector('#scaleLabel').textContent=`8 × 7 · ${tile} px tiles · ${tile*8} × ${tile*7} px`;renderBoard();renderSheet();};
for(const b of document.querySelectorAll('[data-terrain]'))b.onclick=()=>{terrainMode=b.dataset.terrain;for(const button of document.querySelectorAll('[data-terrain]'))button.setAttribute('aria-pressed',String(button===b));renderBoard();renderSheet();};
fetch(new URL('builtin-terrain-simple/mapping.json',root)).then(r=>{if(!r.ok)throw Error('Terrain comparison unavailable');return r.json();}).then(data=>{terrainAlternates=data;document.querySelector('[data-terrain="simple"]').disabled=false;}).catch(()=>{});
document.querySelector('#gridToggle').onclick=e=>{const on=board.classList.toggle('grid-lines');e.target.setAttribute('aria-pressed',String(on));e.target.textContent='Grid '+(on?'on':'off');};
fetch(new URL('assets.json',root)).then(r=>{if(!r.ok)throw Error('Manifest unavailable');return r.json();}).then(data=>{assets=Array.isArray(data)?data:data.assets||[];document.querySelector('#loadStatus').textContent=`${assets.filter(a=>a.file).length} assets in manifest · All artwork remains experimental.`;renderBoard();renderSheet();}).catch(err=>{document.querySelector('#loadStatus').textContent=err.message+' · Showing explicit missing-asset placeholders.';renderBoard();renderSheet();});
