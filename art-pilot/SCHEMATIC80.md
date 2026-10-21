# Schematic80 pilot revision

User feedback: less detail, more contrast, consistent units/objects, at most80×80 game images, similar cell occupation, no shadows, distinct crew silhouettes and calm terrain variety.

This experimental revision intentionally uses original SVG shape artwork rather than another diffusion batch. ComfyUI remains installed and the painterly pilot remains archived; it was not used to generate these vectors. It can still generate future concept references, while final vector shapes keep the small asset budget deterministic. No higher model was used for this pass. No paid services or new image checkpoints.

## Export contract
- Vector viewBox80×80; transparent PNG exports80×80, antialiased, never pixel-art nearest-neighbor rendering.
- Eight sprite originals in vector/. Each has restrained flat color and a shared1.65-unit dark contour. No gradients, ground ellipses, filters or shadows. Internal color blocks express planes; no textured micro-detail.
- Shared canvas anchor(.5,.9), scene scale1.1. Foreground spans roughly60px height; wall deliberately shorter. Similar silhouette extent across units/props rather than identical filled area, preserving recognisable shapes.
- Normal display64px cells, small display40px cells. Contract requires both silhouette and palette to distinguish units at small size.
- Mara: broad rust cape, low crest, large brass shield. Neri: narrow teal coat, ivory crescent hood, open hooked tide staff.
- All three terrain types have four quiet80px raster variants. Rotation, tiny tone shifts and broad low-contrast mottling preserve the existing calm painted textures.
- Preview removes CSS drop-shadows and ground rings. Live game is untouched.

## Rebuild / review
Run ../art-runtime/venv/bin/python art-pilot/scripts/schematic_pass.py then scripts/schematic_sheet.py and scripts/validate.py with that Python. The first run archives the prior painterly pilot in archive/painterly-pilot; reruns never overwrite that archive. Do not run old diffusion/matting scripts on the vector revision. Final assets are80px; larger images in reviews/ are documentation/contact sheets only, and old archived rasters are historical candidates.

Review: reviews/schematic80-assets.png shows enlarged and actual80/64/40px sprites. reviews/schematic80-review.md contains independent review. The browser board is static; gameplay overlays, animation frames, facing variants and full campaign integration remain future work after approval. Terrain art style remains more textured than sprites by user request. The four terrain variants are subtle reuse of the existing textures, not four entirely new biome designs.
