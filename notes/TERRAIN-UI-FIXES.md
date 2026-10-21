# Terrain and interface fixes — 2026-10-24

Requested changes are implemented in the existing game; story, rosters and all 100 unlocked missions remain.

## Rendering and controls

- River channels use the approved calm raster water inside ink-and-stone banks. Entry and exit meet exact cell borders, and every channel is clipped to its own cell. Bends reverse by swapping entry and exit, including top-to-left becoming left-to-top.
- Cells never exceed 80 px. The board is centered with spare space around it. ResizeObserver handles changing available width; the mobile scrollbar gutter is stable to avoid a late scrollbar making the field too wide.
- Movement and ability targets have explicit tinted/bordered overlays above opaque terrain images. These no longer depend on an inset shadow hidden by a PNG.
- The new horizontal80 px bridge sprite is centered, grid-aligned and rotated 90° for a vertical crossing. It crosses perpendicular to straight current. Existing bridge art is preserved under sibling-before-horizontal files.
- Tidecaller has separate entry and exit edge choices. Global abilities use an immediate Apply button and keyboard A; weather choices are visible without tile targeting.
- Effect indicators are separate grid items beginning at the unit’s upper left. Both teams use the same effect list. Context inspection describes all current effects and any underlying fixture beneath a movable object.

## Rules and campaign compatibility

- Fixed objects are never left on water. Loaded incompatible props move deterministically to nearby safe land; quest objects and portal links are preserved. A drain instead creates a dry outlet at its existing location. If no safe land exists, the fixed object retains its location on a dry island.
- Bridges can only be built on empty straight river segments. Existing legacy bridges retain their location with a straight river underneath, preserving routes.
- Crates, bombs, barrels, boulders, carts and oil use the same entry resolver as units: ice, two-step river drift, launch springs and woven gates. Chains are bounded; collisions and objectives are preserved. Bomb fuse coordinates follow each animation state.
- Walkable fixtures survive beneath moving objects and reappear when the object leaves or is destroyed. Object movement, current, sliding, spring and gate transport all animate.
- Ten affected example winning routes were repaired with the existing legal-action solver. No victory/legality assertions were weakened. The Bridgewright fixture now uses straight water instead of its obsolete pit target.

## Verification

- 81 core rules tests, 39 terrain regressions and 9 AI/balance tests pass.
- 100/100 strict legal winning mission replays pass.
- All 100 maps render without failures at 1280×720, 1024×600, 390×844 and 1920×1080. Checks include 80 px cap, centering, clipped river art, loaded images, no overflow or clipped desktop controls.
- Browser fixture tests verify top-to-left creation, reversal, both bridge rotations, visible ability targets, immediate Conductor with no pending cell target, 24 simultaneous effect indicators across both teams without overlap, and a crate moving through a current into a woven gate while preserving the gate.
- 130/130 art exports pass size/alpha checks. Portable ZIP and offline cache v11 refreshed.

Evidence: evidence/terrain-ui-fixes/. Repeatable browser fixtures: tests/terrain-ui-qa.html and tests/visual-qa.html. Mechanics checkpoint: checkpoints/terrain-bugfix/CHECKPOINT.md. Sources and exact bridge prompt remain in art-production/objects/; large raw images remain locally preserved as before. Mobile validation uses responsive browser layouts, not physical handset hardware.

Published successfully at https://the-last-current.groovyray257.chatgpt.site on 2026-10-24. Source commit: 4e2b7b7fdeb47b4663eb1e65a62f2e15075ec248. Version: appgver_2b1cd7f9c7a48191a3193aed5a6a7654. Deployment: appgdep_6adbf6451b488191a5e2d45a58fb2185 (succeeded). Live battlefield and loaded artwork verified; evidence/terrain-ui-fixes/live-game.png. Existing private access preserved.
