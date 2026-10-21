# The Last Current — independent pilot review

Review the assembled pilot against this sheet without seeing its generating seed or preferred candidate first. The reference is `art-pilot/reference/Tactical Fantasy Worlds Concept Board.png`; implementation mechanics are defined by current `dist/data.js` and `README.md`. Review style resemblance and game readability separately. Attractive art alone does not pass.

## Hard gates: every item must pass

- Exactly the requested eight identities: Mara/Vanguard, Neri/Tidecaller, Sentinel, Breaker (`brute`), Briar tree, Column, Stone wall, Directional fan. No renamed roles or changed rules.
- Bellwether weather-machine story survives: humans are crew, enemies are legible infrastructure, scenery uses reclaimed stone/brass/nature. No replacement goblin/demon setting.
- Board is screen-aligned squares with horizontal/vertical grid edges; never diamond isometric. All assets share elevated camera and upper-left light.
- Anchors coincide at (256,432) on 512 px masters. One-cell bases fit; figures stand in their actual cells. No unintended obstruction of neighboring feet, flow markers, or status UI.
- Clean alpha after extraction: no pale/black fringe, opaque background, missing staff/branches, clipped boots or phantom shadow. Check on cream, teal and charcoal.
- No baked text, health, selection rings, movement arrows or direction claims. Runtime overlays remain legible. Fan's four directions and river bends are truthful to data.
- River sockets join exactly; no seams or false crossings; banks/bridges do not imply extra passable terrain. Source/end and bend clearly read. Current changes can be drawn without repainting the terrain.
- User approval is explicitly obtained for this pilot before catalog generation, production replacement, installation or publishing.

## Score each dimension 0–4

0 = absent/broken; 1 = major rework; 2 = usable with visible compromise; 3 = matches target; 4 = unusually strong execution. Record evidence with a crop or exact preview coordinate.

| Dimension | What to examine | Pass target |
|---|---|---|
| Silhouette and role | At actual game size and in grayscale: broad ram guard vs narrow hooked staff; thin ranged Sentinel vs heavy blunt Breaker; distinct tree/column/wall/fan | >=3 |
| Hand-painted character | Imperfect decisive ink, broad opaque paint, sparse marks, unusually angular exaggerated shapes; no shiny uniform capsule forms | >=3 |
| Cozy atmosphere | Humane crew, tactile quiet palette and small expressive faces; enemy machines retain purposeful tension | >=3 |
| Cohesion | Same scale, line density, camera, value structure, upper-left light, brass/cream/teal material vocabulary across all eight | >=3 |
| Tactical clarity | Unit/object bases map to cells, river direction and fan marker visible, health legible, no apparent false blockers or walkable features | >=3 |
| Edge quality | Clean fine elements, consistent outline thickness at board size, no extraction halo, blur or eroded contour | >=3 |
| Material economy | Wood, ceramic, stone, brass and cloth separable through shape and two or three paint values, without texture noise | >=3 |

Acceptance requires all hard gates plus every score at least 3. A reviewer may still reject for an unlisted concrete issue; explain the observable defect. Do not average away a gameplay-readability failure.

## Required review views

1. Eight assets as one scale lineup, neutral background; verify anchors with a temporary external guide.
2. Individual sprites on three transparency swatches at master size and reduced to 48, 64 and 96 px visible height. Read silhouettes without labels first, then compare identities.
3. Small actual-game-size board with all eight present; units next to obstacles, clear square-grid boundaries, river straight/bend/end, and fan runtime arrows in N/E/S/W states. Use existing mechanic values rather than decorative guesses.
4. Grayscale board and silhouette-only lineup. Confirm allegiance and role do not depend on color alone.
5. Connectivity zoom: all relevant river socket pairs and corners, bridge crossing, water-to-land end and board edge. Also check frozen/water bank alignment if such variants are included.

## Fidelity spot checks

- Mara visibly rams; a sword must not replace her adjacent push identity. Data: 1 damage and 1-tile push; crushes walls, topples columns.
- Neri guides water with her own narrow identity; no giant offensive spell. Data: choose flow direction, make/redirect river, heal or extinguish.
- Sentinel reads as a mobile straight-line shooter, not a melee guard. Breaker reads as heavier adjacent impact/push machine, not another shooter.
- Tree looks combustible; wall looks solid; column has a distinct toppling silhouette. Tall art must not imply a larger blocked footprint or a preselected falling direction.
- Fan can rotate mechanically in all four runtime directions; the static image must not contradict its arrow.

## Reviewer record

- Candidate/output identifiers and workflow hash:
- Preview sizes and board coordinates checked:
- Hard-gate failures (or “none”):
- Seven scores, with brief evidence:
- Three strongest traits:
- Required corrections in priority order:
- Decision: reject / revise / ready for user review.
- User decision and approved candidate(s): pending.

“Ready for user review” is not mass-production authorization. Preserve rejected candidates and settings for comparison; request a focused correction rather than silently drifting the whole style.
