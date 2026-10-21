
'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),g=require('../dist/game.js');
const context=vm.createContext({});vm.runInContext(fs.readFileSync('dist/asset-catalog.js','utf8')+'\n'+fs.readFileSync('dist/art.js','utf8'),context);
const draw=u=>vm.runInContext('unitPortrait('+JSON.stringify(u)+')',context);
assert(draw({role:'beekeeper',team:'ally',drone:true}).includes('companions/worker-drone.png'));
assert(draw({role:'beekeeper',team:'ally'}).includes('roles/beekeeper.png'));
assert(draw({role:'drone',team:'enemy'}).includes('enemies/drone.png'));
g.load(0,false);const s=g.getState(),u=s.units[0];u.role='beekeeper';s.units=s.units.filter(v=>v===u);s.objects={};s.tiles={};s.voids=[];g.setModal(null);assert(g.act(u,u.x+1,u.y));const worker=s.units.find(v=>v.drone);assert(worker&&worker.life===3&&worker.hp===1);assert(draw(worker).includes('companions/worker-drone.png'));
console.log('PASS distinct summoner, friendly drone, enemy drone, and real summon artwork');
