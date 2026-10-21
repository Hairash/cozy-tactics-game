const g=require('../dist/game.js');g.load(43,false);g.setModal(null);let s=g.getState(),actions=[];function move(id,x,y){g.select(id);const u=s.units.find(u=>u.id===id);if(!g.moveOptions(u).has(x+','+y))throw Error('move '+id+' '+x+','+y);g.clickCell(x,y);actions.push({type:'move',id,x,y});}function act(id,x,y){g.select(id);if(!g.act(s.units.find(u=>u.id===id),x,y))throw Error('act '+id+' '+x+','+y);actions.push({type:'act',id,x,y});}function end(){g.setModal(null);g.endTurn();actions.push({type:'end'});}
act('a2',1,9);move('a2',4,8);move('a1',3,8);move('a0',4,9);act('a0',4,5);end();
act('a2',4,9);move('a2',5,7);move('a0',4,7);act('a0',4,4);move('a1',3,6);act('a1',3,6);end();
move('a0',4,4);act('a0',4,3);move('a2',5,6);act('a2',4,4);if(s.objects['3,5']==='bomb'){g.select('a1');if(!g.interact(3,5))throw Error('disarm');actions.push({type:'interact',id:'a1',x:3,y:5});}end();act('a0',4,2);console.log(s.result);
if(s.result==='victory'){const fs=require('fs'),p=__dirname+'/campaign-results.json',r=require(p);r[43]={mission:44,title:g.MISSIONS[43].title,goal:'push',won:true,rounds:s.round,actions,seconds:0,manual:true};fs.writeFileSync(p,JSON.stringify(r,null,2));}

require('node:assert/strict').equal(s.result,'victory');
