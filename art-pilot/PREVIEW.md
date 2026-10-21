# Isolated art preview

Serve the project root with an HTTP server and open `/last-current/art-pilot/preview/` (or `/art-pilot/preview/` when serving `last-current`). No build step or dependencies are required.

The preview reads `art-pilot/assets.json`:

```json
{"assets":[{"id":"tree","kind":"prop","status":"processed","file":"processed/tree.png","anchor":[0.5,0.88]}]}
```

Canonical scene IDs: `ground`, `grass`, `water`, `wall`, `column`, `tree`, `fan`, `ally-1`, `ally-2`, `enemy-1`, `enemy-2`. Files are relative to `art-pilot/`. A matching `kind` is also accepted. The contact sheet includes only these eleven canonical IDs; diagnostic manifest entries remain hidden. `missing`, `pending`, `failed` and `rejected` entries remain explicit placeholders even if they have a file.

The static 8 × 7 square grid uses 64 px laptop tiles or 40 px phone tiles, with connected water bends and ten placed props/units. The contact sheet shows terrain at native tile size and sprite canvases at the same scale as the board (default 1.35 tiles), alongside a 128 × 144 px inspection area. Use the page at 100% browser zoom to judge CSS pixel sizes. This is a composition and art review, with human review required before production integration.

Validation: JavaScript syntax checked with `node --check`. Asset availability is reported by placeholders; no production/gameplay files are modified.

River rendering tiles the manifest water texture inside a continuous quadratic centerline mask with tan banks and a dark ink edge. Fixed-width sockets cross exact shared edge centers. Ground texture remains beneath the water. Sprite canvases use the declared normalized foot anchor (default `[0.5, 0.8789]`) at 79% of cell height; optional manifest `scale` controls canvas size in tile units (default `1.35`). Grid state persists across size changes.

Terrain uses fixed connected grass patches framing a cream ground route, rather than alternating tile noise.
