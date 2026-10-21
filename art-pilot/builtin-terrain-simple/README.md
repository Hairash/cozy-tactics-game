# Optional simplified terrain A/B trial

Accepted builtin-simple80 sprites are unchanged. This trial generates only3raster terrain masters (ground/grass/water), then80px exports and4rotationvariants pertype. Prompts/rawsources/process.py/manifest retained here. Codexbuiltinimagegen generated the images, GPT-6.1Sol Low agent handled prompts and implementation. Exact built-in imagebackendmodel is not exposed. Source1254px despite requesting80; exports80px, no claimnativegeneration.

Original20PNGs+canonicalmanifest+preview snapshot retained in ../archive/accepted-simple80-original-terrain, and original12texturePNGs in original-terrain/. Current canonicalassets.json and all20processedPNGs match archive byte-for-byte (final-qa.json). Newtexturemapping is separate mapping.json. No livegame/dist/publishing.

Preview http://127.0.0.1:4174/art-pilot/preview/ has Original terrain and Simplified terrain buttons. DEFAULT ORIGINAL on everyreload; choosingOriginalrestoresoldtexturepaths immediately without changing sprites/map. Experimental selection is not persisted. To undo the experiment completely, the archived preview is available; usercanrevertvisuallywithbuttonnow.

Newsoil: warmbeige broadlowcontrastpatches. Newgrass: quietsagepatches withfewbluntstrokes. Newwater: flatteal sparsepaintedripples; darker thanoriginal and moredefined thanprompt, intentionaltrialonly. Noedges/banks/bakedgrid/perspective/shadows; riverpathmaskremainscontinuousinpreview. 2x2repeats in ../reviews/terrain-repeat-comparison.png; reportedRGBedgeerrorsarelowbutnotzeroforgrass. No severe seams seen64/40; gridlinesremainintentionalUIoverlay.

Browserevidence ../reviews/terrain-original-laptop.png, terrain-simple-laptop.png and terrain-simple-phone-scale.png. Phone means40pxcellsindesktopbrowser, notphysicalphone. Oneclickrollback and reloaddefault tested. My recommendation: the newterrain bettermatchesacceptedquietsprites andriverreadswell, butkeepbothoptionsforhumanreview.

Usageinterruptedsubagentafterassets+togglecompleted. ParentresumedfromsavedfilesandfinishedbrowserQA; noimagesregenerated. Thistrialdoesnotchangefullcampaignart/gameplay orapproveallproductionassets.
