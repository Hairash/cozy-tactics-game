'use strict';
// Presentation-only preferences. These never enter saved tactical state.
let visualSpeed=1,quietMotion=false;
try{visualSpeed=Number(localStorage.getItem('current-animation-speed'))||1;quietMotion=localStorage.getItem('current-quiet-motion')==='true'}catch{}
if(![1,1.5,2].includes(visualSpeed))visualSpeed=1;
function reducedMotion(){return quietMotion||matchMedia('(prefers-reduced-motion: reduce)').matches}
function saveVisualPreferences(){try{localStorage.setItem('current-animation-speed',visualSpeed);localStorage.setItem('current-quiet-motion',quietMotion)}catch{}document.body.classList.toggle('quiet-motion',quietMotion)}
function cycleSpeed(){visualSpeed=visualSpeed===1?1.5:visualSpeed===1.5?2:1;saveVisualPreferences();redraw()}
function toggleMotion(){quietMotion=!quietMotion;saveVisualPreferences();redraw()}
function missionMap(m){const tiles=new Map(m.tiles.map(([x,y,t])=>[x+','+y,t])),objects=new Set(m.objects.map(([x,y])=>x+','+y)),voids=new Set((m.voids||[]).map(p=>p.join(',')));let out='';for(let y=0;y<m.height;y++)for(let x=0;x<m.width;x++){const k=x+','+y;if(voids.has(k))continue;const t=tiles.get(k)||'ground';out+=`<rect x="${x*8}" y="${y*8}" width="7" height="7" rx="1" fill="${TERRAIN_INFO[t]?.color||'#b3c8ad'}" opacity="${t==='ground'?'.6':'1'}"/>`;if(objects.has(k))out+=`<rect x="${x*8+2}" y="${y*8+2}" width="3" height="3" rx=".5" fill="#35575a"/>`;}for(const[x,y]of m.enemies)out+=`<circle cx="${x*8+3.5}" cy="${y*8+3.5}" r="2.5" fill="#eb956c"/>`;for(const[x,y]of m.allies)out+=`<circle cx="${x*8+3.5}" cy="${y*8+3.5}" r="2.5" fill="#f6e4ab"/>`;return `<svg class="mission-map" viewBox="-3 -3 ${m.width*8+5} ${m.height*8+5}" aria-hidden="true">${out}</svg>`}
function chapterVista(act=0,small=false){return `<div class="chapter-vista ${small?'small':''}" style="--vista-position:${20+act*6}%"><div class="vista-haze"></div><div class="vista-label"><span>FIELD JOURNAL / ${String(act+1).padStart(2,'0')}</span><strong>${esc(CAMPAIGN.acts[act].region)}</strong></div><span class="vista-compass" aria-hidden="true">✧</span></div>`}
function guideArt(id,category){if(category==='crew'||category==='enemies')return portrait(id,category==='enemies');if(category==='objects')return objectArt(id);return `<span class="guide-terrain">${groundArt(0,0,id)}</span>`}
