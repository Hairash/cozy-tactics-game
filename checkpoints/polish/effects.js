'use strict';
// Gameplay stays synchronous and testable. The UI replays the recorded state changes.
async function playAction(fn){
 if(busy||modal)return;
 const before=clone(S);let queue;
 try{queue=captureAction(fn)}catch(error){S=before;render();console.error(error);return}
 if(!queue.length){render();return}
 const result=S,resultModal=modal;busy=true;modal=null;S=before;phaseLabel=queue[0].label||'Resolving action';render();if(window.innerWidth<=700)document.querySelector('.board-wrap')?.scrollIntoView({block:'center',behavior:'instant'});
 try{for(const frame of queue){const previous=visualSnapshot();S=frame.state;phaseLabel=frame.label||phaseLabel;render();await animateFrame(frame,previous)}}
 finally{S=result;modal=resultModal;busy=false;phaseLabel='';render()}
}
function visualSnapshot(){const units=new Map,objects=new Map;document.querySelectorAll('[data-piece]').forEach(el=>units.set(el.dataset.piece,{rect:el.getBoundingClientRect(),node:el.cloneNode(true)}));document.querySelectorAll('.cell .scenery').forEach(el=>{const cell=el.closest('.cell');objects.set(cell.dataset.x+','+cell.dataset.y,{rect:cell.getBoundingClientRect(),node:el.parentElement.cloneNode(true)})});return{units,objects}}
function tileElement(x,y){return document.querySelector(`.cell[data-x="${x}"][data-y="${y}"]`)}
function animateNode(el,keyframes,duration,extra={}){if(!el?.animate)return Promise.resolve();return el.animate(keyframes,{duration,easing:'ease-in-out',...extra}).finished.catch(()=>{})}
function ghost(item){const node=item.node.cloneNode(true);node.classList.add('fx-ghost');node.setAttribute('aria-hidden','true');Object.assign(node.style,{left:item.rect.left+'px',top:item.rect.top+'px',width:item.rect.width+'px',height:item.rect.height+'px'});document.body.appendChild(node);return node}
async function animateFrame(f,previous){
 if(f.type==='dialogue'){await showSpeech(f.speaker,f.text);return}
 const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
 const durations={move:210,slide:170,current:210,push:270,shot:430,melee:260,grapple:420,cast:280,damage:310,blast:480,column:480,phase:370};
 const ms=reduced?85:(durations[f.type]||300),jobs=[],cleanup=[];
 const animate=(el,k,opts={})=>{jobs.push(animateNode(el,k,ms,opts));return el};
 const ring=(x,y,color='#e6ad59')=>{const c=tileElement(x,y);if(!c)return;const el=document.createElement('span');el.className='fx-ring';el.style.borderColor=color;c.appendChild(el);cleanup.push(el);animate(el,[{transform:reduced?'none':'scale(.3)',opacity:1},{transform:reduced?'none':'scale(1.45)',opacity:0}])};
 const number=(x,y,text,color)=>{const c=tileElement(x,y);if(!c)return;const el=document.createElement('span');el.className='fx-number';el.textContent=text;el.style.color=color;c.appendChild(el);cleanup.push(el);animate(el,[{transform:'translateY(0)',opacity:1},{transform:reduced?'none':'translateY(-25px)',opacity:0}])};
 for(const el of document.querySelectorAll('[data-piece]')){const old=previous.units.get(el.dataset.piece);if(!old)continue;const box=el.getBoundingClientRect(),scale=box.width/(el.offsetWidth||box.width)||1,dx=(old.rect.left-box.left)/scale,dy=(old.rect.top-box.top)/scale;if((dx||dy)&&!reduced){el.style.zIndex='9';animate(el,[{transform:`translate(${dx}px,${dy}px)`},{transform:'translate(0,0)'}])}}
 for(const[id,item]of previous.units)if(!document.querySelector(`[data-piece="${id}"]`)){const el=ghost(item);cleanup.push(el);animate(el,[{opacity:1,transform:'scale(1)'},{opacity:0,transform:reduced?'none':'scale(.55) rotate(12deg)'}])}
 if(['shot','grapple','cast','melee'].includes(f.type)&&f.from&&f.to){
  const source=tileElement(f.from.x,f.from.y),target=tileElement(f.to.x,f.to.y),board=document.querySelector('.board');
  if(source&&target&&board){
   const a=source.getBoundingClientRect(),b=target.getBoundingClientRect(),box=board.getBoundingClientRect();
   // Use a fixed overlay so lines also remain aligned inside scaled QA frames.
   const layer=document.createElementNS('http://www.w3.org/2000/svg','svg');layer.classList.add('fx-line');layer.setAttribute('aria-hidden','true');layer.setAttribute('viewBox',`0 0 ${box.width} ${box.height}`);Object.assign(layer.style,{left:box.left+'px',top:box.top+'px',width:box.width+'px',height:box.height+'px'});
   const line=document.createElementNS('http://www.w3.org/2000/svg','line');line.setAttribute('x1',a.left+a.width/2-box.left);line.setAttribute('y1',a.top+a.height/2-box.top);line.setAttribute('x2',b.left+b.width/2-box.left);line.setAttribute('y2',b.top+b.height/2-box.top);line.setAttribute('stroke',f.type==='shot'?'#e6794c':f.type==='grapple'?'#e1c27e':f.role==='tidecaller'?'#78bfce':'#a9c17f');line.setAttribute('stroke-width',f.type==='melee'?'8':'4');line.setAttribute('stroke-linecap','round');layer.appendChild(line);document.body.appendChild(layer);cleanup.push(layer);const length=Math.max(1,Math.hypot(b.left-a.left,b.top-a.top));line.style.strokeDasharray=length;animate(line,reduced?[{opacity:1},{opacity:.2}]:[{strokeDashoffset:length,opacity:1},{strokeDashoffset:0,opacity:1,offset:.6},{strokeDashoffset:f.type==='grapple'?-length:0,opacity:0}]);
   const attacker=document.querySelector(`[data-piece="${f.id}"]`);if(attacker&&!reduced)animate(attacker,[{transform:'translate(0,0)'},{transform:`translate(${Math.sign(b.left-a.left)*8}px,${Math.sign(b.top-a.top)*8}px)`,offset:.4},{transform:'translate(0,0)'}]);
  }
 }
 if(f.type==='damage'){ring(f.x,f.y,'#d77356');number(f.x,f.y,'−'+f.amount,'#b64835');const p=document.querySelector(`[data-piece="${f.id}"]`);if(p)animate(p,[{filter:'brightness(2) sepia(1)'},{filter:'none'}])}
 if(['shield','charm','haste','teleport','evacuate'].includes(f.type)){const u=S.units.find(u=>u.id===f.id);ring(f.x??u?.x,f.y??u?.y,f.type==='charm'?'#b391ac':'#80b3a4')}
 if(f.type==='heal'){ring(f.x,f.y,'#66a38c');number(f.x,f.y,'+'+f.amount,'#267d67')}
 if(f.type==='collect'){ring(f.x,f.y,'#dfb64f');number(f.x,f.y,'✦','#a58024')}
 if(f.type==='blast'){for(const[dx,dy]of [[0,0],...DIR]){const c=tileElement(f.x+dx,f.y+dy);if(c){animate(c,[{backgroundColor:'#fff2c2'},{backgroundColor:'#eb995b',offset:.4},{backgroundColor:''}]);ring(f.x+dx,f.y+dy,'#edaa54')}}}
 if(['grow','plant','spawn'].includes(f.type)){const c=tileElement(f.x,f.y),p=c?.querySelector('.object, .unit-sprite');if(p)animate(p,reduced?[{opacity:.25},{opacity:1}]:[{transform:'scale(.1) translateY(10px)',opacity:.2},{transform:'scale(1.12)',opacity:1,offset:.75},{transform:'scale(1)'}]);ring(f.x,f.y,'#8ea76d')}
 if(['fire','rain','water','lever','wind','collision'].includes(f.type)){const color=f.type==='fire'?'#df8751':['rain','water'].includes(f.type)?'#6eafc2':'#c9ad6b';ring(f.x,f.y,color);if(f.type==='wind')for(let n=1;n<Math.max(width(),height());n++){const dx=f.dx??1,dy=f.dy??0;if(inside(f.x+dx*n,f.y+dy*n))ring(f.x+dx*n,f.y+dy*n,'#a2bfa5')}}
 if(['gate','break'].includes(f.type)){const item=previous.objects.get(f.x+','+f.y);if(item){const el=ghost(item);cleanup.push(el);animate(el,reduced?[{opacity:1},{opacity:0}]:[{opacity:1,transform:'translateY(0)'},{opacity:0,transform:f.type==='gate'?'translateY(-30px)':'scale(.5) rotate(15deg)'}])}}
 if(f.type==='column'){const item=previous.objects.get(f.x+','+f.y);if(item){const el=ghost(item);cleanup.push(el);const c=tileElement(f.x,f.y);const art=c?.querySelector('.object');if(art)art.style.visibility='hidden';animate(el,[{transform:'translate(0,0) rotate(0)',opacity:1},{transform:reduced?'none':`translate(${f.dx*item.rect.width}px,${f.dy*item.rect.height}px) rotate(${f.dx?f.dx*90:f.dy*100}deg)`,opacity:0}]);for(let n=1;n<=2;n++)ring(f.x+f.dx*n,f.y+f.dy*n,'#c8b88b')}}
 if(f.type==='objectMove'){const c=tileElement(f.to.x,f.to.y),el=c?.querySelector('.object'),a=tileElement(f.from.x,f.from.y)?.getBoundingClientRect(),b=c?.getBoundingClientRect();if(el&&a&&b&&!reduced)animate(el,[{transform:`translate(${a.left-b.left}px,${a.top-b.top}px)`},{transform:'translate(0,0)'}])}
 if(!jobs.length)jobs.push(new Promise(resolve=>setTimeout(resolve,ms)));
 await Promise.all(jobs);cleanup.forEach(el=>el.remove());
}
function clearRoutePreview(){document.querySelectorAll('.path-step,.path-landing').forEach(el=>el.classList.remove('path-step','path-landing'));document.querySelectorAll('.path-number').forEach(el=>el.remove());const caption=document.getElementById('routecaption');if(caption?.dataset.default)caption.textContent=caption.dataset.default}
function showRoutePreview(x,y){clearRoutePreview();if(busy||modal||inspectMode||mode!=='move')return;const u=S.units.find(u=>u.id===selected&&u.hp>0);if(!u)return;const route=moveOptions(u).get(key(x,y));if(!route)return;route.trace.forEach((point,index)=>{const el=tileElement(point.x,point.y);if(!el)return;el.classList.add('path-step');if(!el.querySelector('.path-number')){const n=document.createElement('span');n.className='path-number';n.setAttribute('aria-hidden','true');n.textContent=index+1;el.appendChild(n)}});tileElement(route.x,route.y)?.classList.add('path-landing');const caption=document.getElementById('routecaption');if(caption){caption.dataset.default||=caption.textContent;caption.textContent=routeDescription(route)}}
function attachCellControls(){
 const wrap=document.querySelector('.board-wrap');if(wrap)wrap.onclick=e=>{if(!busy&&!modal&&!inspectMode&&!e.target.closest('.cell'))deselect()};
 for(const el of document.querySelectorAll('[data-x]')){
  const x=+el.dataset.x,y=+el.dataset.y;let timer=null,held=false,start=null;
  const cancel=()=>{clearTimeout(timer);timer=null};
  el.onclick=()=>{cancel();if(held){held=false;return}if(busy||modal)return;if(inspectMode)inspectAt(x,y);else playAction(()=>clickCell(x,y))};
  el.oncontextmenu=e=>{e.preventDefault();cancel();if(busy)return;held=true;inspectAt(x,y)};
  el.onpointerdown=e=>{held=false;start={x:e.clientX,y:e.clientY};if(e.pointerType==='mouse'&&e.button!==0)return;timer=setTimeout(()=>{held=true;inspectAt(x,y)},550)};
  el.onpointermove=e=>{if(start&&Math.hypot(e.clientX-start.x,e.clientY-start.y)>10)cancel()};
  el.onpointerup=cancel;el.onpointercancel=cancel;el.onpointerenter=e=>{if(e.pointerType==='mouse')showRoutePreview(x,y)};el.onpointerleave=()=>{cancel();clearRoutePreview()};el.onfocus=()=>showRoutePreview(x,y);el.onblur=clearRoutePreview;
  el.onkeydown=e=>{if(e.key==='F1'||(e.shiftKey&&e.key==='F10')){e.preventDefault();inspectAt(x,y)}};
 }
}

async function showSpeech(speaker,text){const actor=[...S.units].reverse().find(u=>u.role===speaker&&u.hp>0&&!u.escaped),cell=actor?tileElement(actor.x,actor.y):null;const bubble=document.createElement('div');bubble.className='speech-bubble '+(cell?'anchored':'radio');bubble.setAttribute('role','status');const meta=ROLES[speaker];bubble.innerHTML=`<span class="speech-portrait">${meta?portrait(speaker):'<span class="radio-face">☼</span>'}</span><div><strong>${esc(meta?.name||speaker)} <small>${actor?meta?.title||'':'RADIO'}</small></strong><p>${esc(text)}</p><button class="speech-next">Continue ↵</button></div>`;document.body.appendChild(bubble);const box=cell?.getBoundingClientRect();if(box){const w=Math.min(310,window.innerWidth-24);bubble.style.width=w+'px';bubble.style.left=Math.max(12,Math.min(window.innerWidth-w-12,box.left+box.width/2-w/2))+'px';bubble.style.top=Math.max(12,Math.min(window.innerHeight-bubble.offsetHeight-16,box.top-bubble.offsetHeight-12))+'px';bubble.style.setProperty('--tail',Math.max(20,Math.min(w-20,box.left+box.width/2-parseFloat(bubble.style.left)))+'px')}await new Promise(resolve=>{const keyAdvance=e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();e.stopImmediatePropagation();done()}};const done=()=>{document.removeEventListener('keydown',keyAdvance,true);resolve()};document.addEventListener('keydown',keyAdvance,true);bubble.querySelector('button').onclick=done});bubble.remove()}
