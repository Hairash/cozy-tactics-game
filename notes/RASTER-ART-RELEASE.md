# Approved raster production

The user approved the simple raster sprite style and quiet simplified terrain. This pass replaces all crew, enemy, object and terrain illustrations while preserving the story, 100 missions, rules, AI, dialogue, controls and existing animation system.

## Asset contract

All 130 game art IDs have individual 80×80 PNG runtime masters, listed in `dist/asset-catalog.js`: 50 crew, 20 enemies, 39 objects, 21 terrain types. Unit/object images retain genuine generated alpha and a common ground anchor; no CSS ground shadow is added. Low objects intentionally use flatter footprints. Terrain variations are selected deterministically. Animated directional arrows, river connectivity, status marks, selection outlines and mission map diagrams remain code because they communicate rules.

The built-in image generation tool produces larger source images; prompts specify artwork designed for 80 px. Sources are cropped and resized with Lanczos to 80 px, without palette quantization, manual repainting or synthetic background removal. This is raster art, not SVG tracing. Crew portraits, guide entries, inspections, briefings and speech bubbles reuse the same sprites. The briefing vista is a separate wide background illustration, exported at 1200×400 WebP.

## Reproducible production

- `art-production/inventory.json`: exact game metadata and required IDs.
- `art-production/BRIEF.md`: shared style, scale and camera contract.
- Category `manifest.json`, `prompts/`, `raw/`, `processed/`, `CHECKPOINT.md`: per-image provenance and durable progress.
- `art-production/shared/`: panorama source and prompt.
- `scripts/assemble-art.cjs`: idempotent assembly; records exact remaining IDs.
- `scripts/check-art.py`: dimensions, alpha, bounds, hashes and 80/40 px review sheets.
- `scripts/finalize-art.cjs`: refuses incomplete release, then writes the offline cache inventory.
- `tests/art-gallery.html`: browser decode and 80 px size check for every runtime ID.
- `tests/visual-qa.html`: all 100 maps, desktop/mobile sizing, image loading, no legacy SVG illustrations.

Accepted originals and previous experiments remain in `art-pilot/`. The full previous playable build is preserved in `checkpoints/before-approved-raster-art/`. Source images and prompts are kept separately from the small runtime images. No paid image API or ComfyUI model downloads were used for this production pass. Generation workers use GPT-6.1 Sol with low effort; the built-in image backend does not expose a selectable model ID.

## Validation and publication

81 rules checks, 9 AI/balance checks and 100 legal winning mission replays passed after the renderer integration. Final image and responsive browser checks are recorded in `art-production/qa-report.json` and `reviews/full-raster/`. Publication keeps the existing owner-only site audience. Final deployment and evidence will be appended after all required art is complete.

Final verification completed: 130/130 runtime images load in a browser and pass 80×80/alpha/opacity checks. All 100 missions rendered with zero failures at 1280×720, 1024×600 and 390×844. The opening mission was manually completed in two rounds using an ice slide, ram collision, enemy phase, persistent dialogue and column topple; raster ghost scale and action closure behaved correctly. Reports and screenshots are in `evidence/full-raster/`; contact sheets are in `reviews/full-raster/`. The offline cache includes 156 local resources and the refreshed portable ZIP is 1,118,018 bytes. Mobile verification is responsive browser testing rather than physical handset testing.

The initial source push exceeded the hosting Git request size limit because it included all large original art and prior experiments. Those files remain unchanged on this device and in the local Git branch `local-art-archive-df99c55`. The hosted source keeps the small processed exports, prompts, manifests, checks, runtime game and rollback build; large `raw/`, archived pilot experiments and reference originals are ignored for upload. This does not remove any local art or affect the playable package.

Published successfully on 2026-10-23 at https://the-last-current.groovyray257.chatgpt.site with the existing owner-private audience. Verified source commit: `5071b7dee25bc2f98f11bee33fd2a67513a61779`. Version: `appgprj_6ad941cb6a948191b9a41ebec2143981~appgver_977763e0f5108191b585d1ab7a60cb35`. Deployment: `appgdep_6adbb62685508191ac70cf4496faacb2`, terminal status succeeded. The unchanged verified deployment archive is `../raster-art-release.tar.gz`. Live browser verification opened the saved mission17 and confirmed the new raster artwork; proof `evidence/full-raster/live-game.png`. No battle actions were taken on the live mission.
