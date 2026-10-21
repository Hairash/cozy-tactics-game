# Raster80 — angular illustrated pilot

User requested a middle point between the consistent schematic vectors and the older detailed painted raster art. This pass returns final sprite creation to local ComfyUI. The schematic SVG identities are only composition references, not final art exports. DreamShaper XL Turbo img2img + IPAdapter transfers the concept-board illustration style while preserving crew colors, equipment and silhouettes.

Calibration: denoise.48 reproduced icons too closely; archived and increased to.70 with style.70, composition.65, CFG2.5,8steps,dpmpp_sde/karras. Full perasset graphs, hashes, seeds, promptIDs and history are saved. Source images are512px working candidates; final runtime PNGs are80×80. Larger sources are retained only for reproducibility, not loaded by the game/preview. No new model downloads or paid endpoints.

Processing: raster80_process.py performs localu2net matting, main-component cleanup, gray shadow-remnant removal below contact line and common62px silhouette bounds in80px RGBA canvases. No SVG/vector paint is applied to these outputs. Shared canvas anchor(.5,.9), scale1.1. Preview uses no CSS drop-shadow or floor rings. Terrain retains the12quiet80px texture variants from the previous pass.

Prior versions: archive/schematic80 has the complete vector pilot and archive/painterly-pilot the first raster pilot. Never overwrite these. No live game/dist changes or deployment authorized at pilot stage. Next human review, then full catalog/animation/runtime integration only after acceptance.

Rebuild: run worker.py for pending sprite IDs, then raster80_process.py, raster80_sheet.py, validate.py sequentially. Do not run simultaneous manifest writers. Do not run schematic_pass.py unless intentionally reverting to vectors. Original vector geometry is retained under vector/ as reference only.
