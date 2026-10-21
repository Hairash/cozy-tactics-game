# Independent review: enemy-1, first local benchmark

Decision: **revise; reject as the approved Sentinel sprite**. Preserve this image as a useful shape exploration. Review performed directly on `raw/enemy-1.png` (768 × 768), against the inspected concept board and `REVIEW_RUBRIC.md`. Local SDXL-Lightning 8 steps with IPAdapter style 0.75 reported by parent; full workflow not independently inspected.

## What works

Strong asymmetrical angular silhouette, confident dark outline, restrained slate/brass/cream palette, and an unmistakably mechanical ranged weapon. The long wedge emitter and narrow legs could become a memorable Sentinel identity. Blank background makes extraction plausible. No text, interface or magical fantasy motif. These are traits worth retaining.

## Concrete failures

1. **Facing and camera fail.** Emitter points screen-left in a predominantly lateral profile. The required south-facing front with only a slight east turn is absent. The enormous broad side panel is the focal plane. Its large top face and receding edges read as a close three-quarter object drawing, not the compact consistent elevated-front battlefield view in the reference.
2. **Proportions fail.** Head/housing occupies approximately the upper half of the entire image and almost its whole width; small torso and long thin dangling legs create a birdlike side-profile mascot. It does not read as the reference's compact upright sentry. The huge forward beak would visually claim neighboring cells when placed at useful height.
3. **Sprite scale/anchor fail.** Visible artwork runs roughly x67–725, y48–735. Ground contact is near y731 instead of a normalized y648 at this 768 master size. This is fixable during extraction/export, but cannot be accepted as already satisfying the common-anchor contract. Long lateral muzzle makes optical centering differ substantially from foot centering.
4. **Detail and finish need reduction.** Orange fan medallion, multiple concentric joint rings, hand claws, shoe panels, edge bevels and orange accent striping compete at board size. Smooth broad highlights and clean bevel bands lean toward polished illustrated product design; reference sprites use simpler dark shapes, fewer internal marks and less glossy volume. Preserve the ink but flatten surfaces.
5. **Weather-machine identity is only partial.** Brass and housing communicate machinery, but the large visible side fan dominates and could confuse this shooter with the directional-fan object. A small horizontal amber sensor and short front emitter would communicate Sentinel more directly. No need to add dense gauges or decorative gears.
6. **Raw background is opaque.** This is acceptable as an intermediate raw output, but the alpha hard gate remains untested until processing. Fine claw wires and overlapping leg lines risk extraction damage; simplify them rather than treating extraction as a cure.

## Provisional scores

| Dimension | Score | Evidence |
|---|---:|---|
| Silhouette and role | 2/4 | Shooter clear; oversized profile head overwhelms single-cell sentry identity |
| Hand-painted character | 2/4 | Strong ink/angularity; smooth beveled surfaces and dense small mechanics |
| Cozy atmosphere | 3/4 | Curious nonviolent maintenance-machine character, warm subdued ground |
| Cohesion | Not scored | Only one benchmark available; facing already violates contract |
| Tactical clarity | 1/4 | Broad lateral muzzle and large housing likely encroach neighboring cells |
| Edge quality | Not scored | Raw opaque image only; processed alpha and actual-size board not reviewed |
| Material economy | 2/4 | Slate/brass distinct, but too many rings, panels and bevel highlights |

No acceptance average is appropriate: facing/scale gates fail. Do not infer complete pilot rejection or mass-production readiness from this one image.

## Bounded prompt revision

Keep the shared style/palette prompt and change the subject block to:

> One compact upright Bellwether Sentinel maintenance shooter, full body FRONT VIEW facing the viewer at screen south, only a very slight turn toward screen east. Symmetrical visible short feet under a narrow torso; two short simple jointed legs, no hands. Modest wedge-shaped dark slate head only one third of total figure height, one tiny horizontal amber sensor centered on its FRONT, one SHORT blunt brass emitter projecting toward the viewer from its front, no long side-pointing beak. Small worn cream ceramic shoulder plate. Narrow single-tile silhouette, width about half its total height, broad flat opaque painted shapes, one shadow per surface, just three or four interior ink marks. Small functional weather-city machine, curious and impersonal. Upper-left light, elevated-front orthographic camera, feet at the shared anchor. Maintain angular asymmetry through the shoulder plate and housing corners, not an enlarged head.

Add to exclusions:

> side view, profile, left-facing, right-facing, long beak, enormous head, large side fan emblem, large orange medallion, long legs, dangling arms, hand claws, concentric joint rings, polished bevels, glossy highlights, product rendering, huge muzzle, camera close-up

Treat this as one focused candidate revision. Prompt language cannot guarantee camera or footprint; compare the new silhouette against this benchmark and the reference before any broad rerun. Independent review of the remaining pilot remains necessary.
