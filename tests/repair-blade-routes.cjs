// Legal, explicit cart routes after contiguous-blade rule correction.
const g=require('../dist/game.js'),fs=require('node:fs'),assert=require('node:assert/strict');
const results=require('./blade-route-repair/blade-routes-before.json');const repaired=require('./blade-route-repair/blade-routes-new.json');results[23]=repaired.find(r=>r.mission===24);
for(const mission of [44,84]){
 g.load(mission-1,false);const s=g.getState(),actions=[];
 function move(id,x,y){g.setModal(null);g.select(id);assert(g.moveOptions(s.units.find(u=>u.id===id)).has(x+','+y),'move '+id+' '+x+','+y);g.clickCell(x,y);actions.push({type:'move',id,x,y})}
 function act(id,x,y){g.setModal(null);g.select(id);assert(g.act(s.units.find(u=>u.id===id),x,y),'act '+id+' '+x+','+y);actions.push({type:'act',id,x,y})}
 function end(){g.setModal(null);g.endTurn();actions.push({type:'end'});console.log(mission,'round',s.round,'crew',s.units.filter(u=>u.team==='ally').map(u=>[u.id,u.x,u.y,u.hp]),'cart',Object.entries(s.objects).find(([k,o])=>o==='cart'))}
 if(mission===44){
 act('a2',1,9);move('a2',5,8);move('a1',3,8);move('a0',4,9);end();
 act('a2',4,9);move('a0',4,6);act('a0',4,5);move('a2',4,7);move('a1',3,6);act('a1',3,6);end();
 move('a0',4,5);act('a0',4,4);move('a1',3,5);end();
 act('a2',4,5);g.select('a0');assert(g.interact(4,4));actions.push({type:'interact',id:'a0',x:4,y:4});move('a0',4,4);end();
 act('a0',4,3);move('a0',4,3);end();act('a0',4,2);
 }else{
 // Ranger clears the approach while Rook stays immediately behind the cart.
 move('a2',4,6);move('a1',3,7);move('a0',3,8);end();
 move('a2',4,4);move('a0',4,6);end();
 move('a2',5,4);move('a0',4,4);act('a0',4,3);end();
 move('a0',4,3);act('a0',4,2);
 }
 assert.equal(s.result,'victory',mission+' must win');results[mission-1]={mission,title:g.MISSIONS[mission-1].title,goal:'push',won:true,rounds:s.round,actions,manual:true,seconds:0};
}
fs.writeFileSync(__dirname+'/campaign-results.json',JSON.stringify(results,null,2));
