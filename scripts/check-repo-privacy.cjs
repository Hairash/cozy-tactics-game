'use strict';
// Scan tracked text without printing matched personal data or credential values.
const fs=require('node:fs'),cp=require('node:child_process');
const files=cp.execFileSync('git',['ls-files','-z'],{encoding:'utf8'}).split('\0').filter(Boolean);
const checks=[
 ['personal filesystem path',new RegExp('/'+'(?:Users|home)/[^/\\s]+/|~/'+'(?:GIT|Documents|Downloads)/|file:'+'///|[A-Z]:\\\\'+'Users\\\\','i')],
 ['credential',/(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9]{30,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|https?:\/\/[^/\s:@]+:[^/\s@]+@)/],
 ['authorization bearer',/(?:authorization)["\s:]+Bearer [A-Za-z0-9._-]{20,}/i],
 ['private contact email',/[\w.+-]+@(?:gmail|yandex|hotmail|outlook|icloud|protonmail)\.[a-z]{2,}/i]
];
const findings=[];
for(const file of files){
 if(/(?:^|\/)(?:\.env(?:\..+)?|id_rsa|id_ed25519|\.netrc)$/.test(file)&&!file.endsWith('.env.example'))findings.push({file,kind:'private configuration filename'});
 if(!fs.existsSync(file))continue;
 const bytes=fs.readFileSync(file);if(bytes.includes(0))continue;
 const text=bytes.toString('utf8');
 for(const[kind,pattern]of checks)if(pattern.test(text))findings.push({file,kind});
}
console.log(JSON.stringify({trackedFiles:files.length,findings},null,2));
if(findings.length)process.exitCode=1;
