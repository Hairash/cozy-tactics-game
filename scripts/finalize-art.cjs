const fs=require('fs'),path=require('path'),cp=require('child_process');
const root=path.resolve(__dirname,'..');
cp.execFileSync(process.execPath,[path.join(__dirname,'assemble-art.cjs')],{stdio:'inherit'});
const status=JSON.parse(fs.readFileSync(path.join(root,'art-production/assembly-status.json')));
if(status.missing.length)throw new Error('Refusing incomplete release: '+status.missing.length+' assets pending');
const qa=JSON.parse(fs.readFileSync(path.join(root,'art-production/qa-report.json')));
if(qa.complete!==qa.total||qa.errors.length)throw new Error('Image integrity review must pass before release');
const dist=path.join(root,'dist');
function walk(dir){return fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(dir,e.name)):[path.relative(dist,path.join(dir,e.name)).replaceAll('\\','/')])}
const files=walk(dist).filter(f=>f!=='sw.js'&&f!=='assets/shores-vista.png').map(f=>'./'+f);
for(const match of fs.readFileSync(path.join(dist,'index.html'),'utf8').matchAll(/(?:src|href)="([^"]+\?[^"]+)"/g))files.push('./'+match[1]);
files.unshift('./');
const sw=`const CACHE='cozy-tactics-v13';\nconst FILES=${JSON.stringify(files)};\nself.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(FILES)));self.skipWaiting()});\nself.addEventListener('activate',e=>e.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));\nself.addEventListener('fetch',e=>{if(e.request.method!=='GET'||new URL(e.request.url).origin!==self.location.origin)return;e.respondWith(fetch(e.request).then(r=>{if(r.ok){const copy=r.clone();caches.open(CACHE).then(c=>c.put(e.request,copy))}return r}).catch(()=>caches.match(e.request).then(r=>r||(e.request.mode==='navigate'?caches.match('./index.html'):Response.error()))))});\n`;
fs.writeFileSync(path.join(dist,'sw.js'),sw);
console.log('Release cache includes '+files.length+' local resources.');
