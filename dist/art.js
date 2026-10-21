'use strict';
// Approved bitmap masters are exported at 80px. Rules and directional marks remain code.
let artSerial=0;
function artSource(category,id,x=0,y=0){
 const asset=ART_CATALOG[category]?.[id];if(!asset)return '';
 const variants=[asset.src,...(asset.variants||[])];
 return variants[Math.abs(x*17+y*31)%variants.length];
}
function rasterArt(category,id,cls,x=0,y=0){return `<img class="${cls}" src="${artSource(category,id,x,y)}" width="80" height="80" alt="" aria-hidden="true" draggable="false">`}
function portrait(role,enemy=false){return rasterArt(enemy?'enemies':'roles',role,'piece raster-unit')}
function unitPortrait(u){return u.drone?rasterArt('companions','worker-drone','piece raster-unit'):portrait(u.role,u.team==='enemy')}
function objectArt(id){return rasterArt('objects',id,'scenery raster-object')}
function groundArt(x,y,t){
 const overlay=['smoke','mist'].includes(t);
 const base=overlay?rasterArt('terrain','ground','ground-art raster-ground',x,y):'';
 const direction=t==='conveyor'?`<span class="terrain-direction" aria-hidden="true">${ARROWS[typeof S!=='undefined'?(S.dirs[key(x,y)]??1):1]}</span>`:'';
 return base+rasterArt('terrain',t,'ground-art raster-ground'+(overlay?' terrain-overlay':''),x,y)+direction;
}
