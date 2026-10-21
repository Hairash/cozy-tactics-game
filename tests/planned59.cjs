const g=require('../dist/game.js');g.load(58,false);g.setModal(null);let s=g.getState(),actions=[];function move(id,x,y){g.select(id);const u=s.units.find(u=>u.id===id);if(!g.moveOptions(u).has(x+','+y))throw Error('move '+id+' '+x+','+y);g.clickCell(x,y);actions.push({type:'move',id,x,y});}function act(id,x,y,weather){g.select(id);if(weather)g.setWeather(weather);if(!g.act(s.units.find(u=>u.id===id),x,y))throw Error('act '+id+' '+x+','+y);actions.push({type:'act',id,x,y,...(weather?{weather}:{})});}function end(){g.setModal(null);g.endTurn();actions.push({type:'end'})}
act('a0',1,6,'frost');act('a2',2,6);move('a2',3,3);move('a1',1,4);act('a1',1,2);end();
act('a2',1,4);move('a1',1,3);act('a1',1,0);end();

for(let n=0;n<12&&!s.ended;n++){act('a2',s.units[1].x,s.units[1].y);act('a1',1,0);if(!s.ended)end();}console.log('RESULT',s.result);if(s.result==='victory'){const fs=require('fs'),p=__dirname+'/campaign-results.json',r=require(p);r[58]={mission:59,title:g.MISSIONS[58].title,goal:'boss',won:true,rounds:s.round,actions,seconds:0,manual:true};fs.writeFileSync(p,JSON.stringify(r,null,2));}

require('node:assert/strict').equal(s.result,'victory');
