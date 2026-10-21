# The Last Current — local art pilot direction

Status: specification only. No generation, installation, publishing, or production approval is implied. The user must review the assembled pilot before mass production.

## Reference and intent

Inspected reference: `art-pilot/reference/Tactical Fantasy Worlds Concept Board.png`. Borrow its confident uneven ink contours, compact expressive silhouettes, restrained painted fills, mossy cream stone, small dark faces, generous negative space, and readable terrain. Combine the warmth of A (Whimsical Fantasy), the angular machinery and ruins of B (Ancient Ruins), and the living foliage of C (Nature Spirits). Do not copy the reference characters or swap the game into a generic fantasy setting. Unusual asymmetry and exaggerated shapes matter more than surface detail.

Bellwether borrowed its weather from a machine. Crew are people tending and reclaiming its waterways; enemies are weather infrastructure following old orders. Keep worn brass, tide gauges, ceramic housings, pale masonry, moss and turquoise channels. Sentinel and Breaker are machines, not goblins or demons. Cozy means humane, tactile and curious; machinery may remain unsettling. No generic mobile-game gloss, candy gradients, jewel loot, shiny armor, photorealistic materials, cinematic bloom or dense ornamental noise.

## Shared visual contract

- Camera: orthographic elevated front view, looking down at approximately 55 degrees to the ground; enough top surface to read footprints, upright fronts visible. No perspective convergence. Screen north is up, east is right. World grid edges remain horizontal/vertical on screen; never rotate the board into diamonds or use an isometric grid. No ground diamonds beneath isolated assets.
- One shared default unit facing: toward screen south, slight face/torso turn toward screen east. Do not mirror asymmetrical equipment between units or variants. Camera, lighting and ground plane stay fixed across assets.
- Master isolated sprite canvas: 512 × 512 px, RGBA after approved background removal, no baked ground or UI. Ground/contact anchor at (256, 432); footprint centered at (256, 416). Render contact shadow separately in integration, not into sprites. Leave 24 px minimum clear margin. Preserve common anchor when cropping/exporting; never automatically center by visible bounds.
- Nominal tile width T: 128 px in the review composite; these are pilot ratios, not a change to game layout. Unit foot contact at tile center, 0.55–0.70T body width, 0.95–1.15T visible height. Breaker 0.82T wide / 1.25T high. Tree 0.85T canopy / 1.45T high; column 0.50T wide / 1.30T high; wall 0.90T wide / 0.65T high; fan 0.78T wide / 0.90T high. Bases must fit one tile. Upper artwork can extend north but must not conceal a neighboring unit's feet or runtime direction marker.
- Shape: broad asymmetrical wedges, bent trunks, tapering stone, oversized cuffs/tools and a few decisive notches. Characters roughly 2.5 heads tall, calm small faces, expressive posture; no uniform round capsule bodies. Distinguish roles by silhouette in grayscale.
- Line: irregular deep petrol ink, approximately 2–3 px at a 128 px sprite height, lighter interior marks, sparse broken edges. Gouache/watercolor-like opaque paint with restrained paper grain inside forms. Three value groups, at most one broad shadow per material. Light from upper left for every asset.
- Palette anchors: ink #243D3D, warm cream #E8D8AF, sage #819A6A, deep teal #356C68, turquoise #55A7AE, old brass #B99453, rust #A85F46. Allies use cream/teal plus brass; enemies use dark slate and a small amber/rust sensor. Color alone must never identify allegiance or role.
- Runtime overlays own health, selection, status, range, direction arrows and movement indicators. No text, badges, outlines, health bars, selection rings, arrows or spell circles baked into art.

## Terrain and connectivity contract

This pilot covers eight isolated assets and a small review composite, not a new terrain catalog. Ground remains a screen-aligned square grid. Preserve the actual board mask, terrain, objects, coordinates, collision rules and movement logic. Decoration never adds apparent walkable islands, bridges, gaps, cover or blockers.

For subsequent river tiles, define N/E/S/W sockets at the exact center of each square edge, same width (0.42T) and water height. Banks meet those sockets without seams. Keep separate topology and direction: straight NS/EW, four corners, source/end and any junctions actually needed by game data; do not invent junction behavior. Runtime flow arrow must follow each tile's local outgoing direction, including bends. Tidecaller changes direction without requiring a repainted tile. Straight/corner overlays must connect on a 3 × 3 test with all rotations, and bridge art must align to the same square edges. Water must visibly end at land; no decorative channel continues through a wall or off a board-mask edge. Existing rules remain: current drifts at most two cells and stops upon first land beyond its end; bridges suppress the underlying hazard. Freeze/water variants share bank geometry. Avoid prominent decorative strokes that read as additional arrows.

Fan direction is a runtime four-way arrow with a clear placement zone; never infer gameplay direction from static blades. The fan base stays fixed while runtime orientation changes. Columns look breakable/topplable, trees combustible, walls solid; no asset extends its apparent blocking footprint beyond its one occupied cell.

## Exact pilot prompts

For each job concatenate the following shared prefix, its subject paragraph, and shared exclusions verbatim. Record model, workflow hash, seed and all node settings with each output. Prompts are proposed for the local ComfyUI pilot, not an instruction to install models or generate now.

**Shared prefix**

> Original tactical game The Last Current, one isolated game sprite, single subject only, complete unclipped silhouette on a perfectly flat pale neutral background for later alpha extraction. Cozy unusual hand-inked painted art, confident imperfect deep petrol contours, simple gouache fills, restrained paper grain within forms, angular exaggerated asymmetrical shapes, broad readable value groups, sparse detail, upper-left soft light. Worn cream stone, sage moss, deep teal cloth, turquoise water accents and muted old brass. Bellwether is a flooded city built around a weather machine. Orthographic elevated front camera looking down about 55 degrees to the ground, upright fronts visible, screen-aligned square-grid world, north up and east right, no perspective convergence. 512 by 512 composition, ground contact centered at x256 y432, generous clear margins, no ground plane. Match the same camera, ink weight, palette and scale as the other pilot sprites.

**1. ally_vanguard — Mara**

> One human harbor keeper called Mara, default facing screen south with a slight turn toward screen east, sturdy angular stance, oversized trapezoid shoulder mantle, short deep-teal work cloak, warm cream shirt, brass harbor clasp, heavy square work boots, expressive small face under an asymmetrical practical hood. One broad cream-and-brass ram guard on her left forearm, her right hand free, no sword. Compact roughly two-and-a-half-head proportions, warm capable presence. Clear forward shoulder and forearm silhouette communicates adjacent ramming and pushing, not ranged attack. Body 0.65 tile wide and 1.10 tile high, feet at shared contact anchor.

**2. ally_tidecaller — Neri**

> One human waterway tender called Neri, default facing screen south with a slight turn toward screen east, narrow bent triangular cream hood and long asymmetrical deep-teal coat, oversized folded cuffs, small thoughtful face, simple brass tide-gauge staff in her right hand with an open hooked head and one muted turquoise inset, left hand extended in a gentle guiding gesture. No floating water effects. Compact roughly two-and-a-half-head proportions, narrow flowing silhouette distinct from the broad Vanguard. Communicates redirecting water, healing and extinguishing rather than combat wizardry. Body 0.55 tile wide and 1.10 tile high, feet at shared contact anchor.

**3. enemy_sentinel — Sentinel**

> One autonomous weather-city sentry machine, narrow angular upright ceramic-and-dark-slate housing, two thin jointed walking legs, offset wedge-shaped head with one small horizontal amber sensor, modest old-brass straight-line emitter built into its front, one worn cream shoulder plate. No human face, no shield, no sword. Slightly off-balance attentive posture, curious but impersonal infrastructure following old orders. Default front toward screen south with a slight turn toward screen east. One clear barrel/emitter silhouette communicates a straight shot. Body 0.55 tile wide and 1.00 tile high, feet at shared contact anchor.

**4. enemy_brute — Breaker**

> One heavy weather-city maintenance machine called Breaker, broad squat trapezoid dark-slate body, two short powerful jointed legs, oversized blunt ram forearms, hunched cream ceramic shoulder housing with three large visible chips, muted old-brass joints, tiny recessed horizontal rust-amber sensor. No horned monster, no human anatomy, no gun. Industrial weight with a slightly lopsided handmade silhouette, clearly larger and wider than the Sentinel, communicates adjacent impact and pushing. Default front toward screen south with slight turn toward screen east. Body 0.82 tile wide and 1.25 tile high, feet at shared contact anchor.

**5. object_tree — Briar tree**

> One small blocking briar tree from a flooded weather city, crooked warm-brown trunk splitting into two unusual angular boughs, three broad asymmetrical sage and deep-teal leaf masses with sparse jagged ink notches, a few thornlike twigs, tiny roots at a compact single-tile base. Soft lively cozy character without face or eyes. Clearly wood and foliage, no stone or metal armor, no magical aura. Canopy 0.85 tile wide and total height 1.45 tiles, trunk base at shared contact anchor, empty gap around lower trunk for clear grounding.

**6. object_column — Column**

> One freestanding old Bellwether masonry column, warm ivory tapering rectangular shaft with an oversized skewed square cap and a compact stepped foot, three bold cracks and a little sage moss on its north side, one modest brass tide-measure fitting. Deliberately unstable and topplable, visually separate from the low wall, no intact building attached. One-cell base 0.50 tile wide, total height 1.30 tiles, base at shared contact anchor. Screen-aligned horizontal and vertical base edges, elevated front camera with top surface visible.

**7. object_wall — Stone wall**

> One low solid square-grid stone barrier block from Bellwether, three large irregular cream masonry stones with dark petrol ink joints, subtly skewed top stones, sparse sage moss and one worn brass repair clamp. Clearly blocks a whole single cell, sturdy but crushable, no doorway, no arch, no stairs, no surrounding ground. Width 0.90 tile, visible height 0.65 tile, base at shared contact anchor. Front edge horizontal on screen, sides aligned to screen north-south, visible shallow top plane, no diamond-shaped base.

**8. object_fan — Directional fan**

> One compact Bellwether weather-control fan machine on a fixed low square cream ceramic pedestal, large circular old-brass protective rim, three broad asymmetrical deep-teal blades, small central cream hub, chunky side support, sparse wear and one practical bolt. Clearly manufactured weather infrastructure, no creature face, no glowing magical energy, no wind streaks. Front visible to the elevated camera, neutral static blades that do not imply a gameplay push direction. Compact one-tile base 0.78 tile wide, height 0.90 tile, base at shared contact anchor. Leave lower front pedestal visually quiet for a separate runtime direction marker.

**Shared exclusions / negative prompt**

> diamond grid, isometric board, rotated ground plane, perspective convergence, multiple subjects, character sheet, duplicate limbs, clipped silhouette, scenery, landscape background, floor tile, pedestal plinth under characters, baked shadow, letters, words, numbers, logo, watermark, UI, health bar, selection ring, direction arrow, spell circle, photorealism, 3D render, glossy plastic, mobile-game polish, candy colors, airbrushed gradients, bloom, rim glow, intricate filigree, dense texture, generic fantasy armor, goblin, demon, pixel art

## Pilot review delivery and stop point

Assemble the eight isolated assets on neutral/light/dark transparency swatches, at matched relative scale; include a 100% close view and actual board-size view. Also assemble a small screen-aligned map using existing rules/data, with a river bend, adjacent units, column, wall, tree and fan; show runtime arrows and health above the art. Label previews outside sprite boundaries. Provide original outputs, derived alpha files, prompts/settings and reject notes. Existing shipped art stays available until review. Do not upscale the catalog, replace production art, generate animation families, install additional production tools, or publish before the user approves this concrete pilot.
