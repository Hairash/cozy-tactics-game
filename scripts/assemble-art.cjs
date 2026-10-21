// Repeatable assembly: production sources remain separate from runtime exports.
const fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'..'),inv=require('../art-production/inventory.json');
const total=Object.values(inv).reduce((n,c)=>n+Object.keys(c.items).length,0);
const catalog={version:'simple-raster-2',size:80};let complete=0,missing=[];
const accepted={roles:{vanguard:'ally-1',tidecaller:'ally-2'},enemies:{sentinel:'enemy-1',brute:'enemy-2'},objects:{tree:'tree',column:'column',wall:'wall',fan:'fan'}};
for(const [category,data]of Object.entries(inv)){
 const dest=path.join(root,'dist/assets/art',category);fs.mkdirSync(dest,{recursive:true});catalog[category]={};
 for(const id of Object.keys(data.items)){
  const reuse=accepted[category]?.[id];
  const candidates=[...(category==='roles'?[path.join(root,'art-production/roles-extra/processed',id+'.png')]:[]),path.join(root,'art-production',category,'processed',id+'.png')];
  if(reuse)candidates.push(path.join(root,'art-pilot/builtin-simple80/processed',reuse+'.png'));
  if(category==='terrain'&&['ground','grass','water'].includes(id))candidates.push(path.join(root,'art-pilot/builtin-terrain-simple/processed',id+'.png'));
  const src=candidates.find(fs.existsSync);if(src){fs.copyFileSync(src,path.join(dest,id+'.png'));complete++}else missing.push(category+'/'+id);
  const variants=[];
  if(category==='terrain'&&['ground','grass','water'].includes(id))for(let n=1;n<=3;n++){
   const file=path.join(root,'art-pilot/builtin-terrain-simple/processed',id+'-'+n+'.png');
   if(fs.existsSync(file)){fs.copyFileSync(file,path.join(dest,id+'-'+n+'.png'));variants.push('assets/art/'+category+'/'+id+'-'+n+'.png')}
  }
  catalog[category][id]={src:'assets/art/'+category+'/'+id+'.png',...(variants.length?{variants}:{})};
 }
}
fs.writeFileSync(path.join(root,'dist/asset-catalog.js'),"'use strict';\nconst ART_CATALOG="+JSON.stringify(catalog,null,2)+';\n');
fs.writeFileSync(path.join(root,'art-production/assembly-status.json'),JSON.stringify({complete,total,missing},null,2));
console.log(`${complete}/${total} runtime assets assembled; ${missing.length} pending.`);
