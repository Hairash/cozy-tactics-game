# Independent review — first local batch

Inspected `reviews/raw-v1-sheet.jpg` directly. **Reject batch as approved pilot; keep as diagnostic evidence.** No candidate presently establishes the complete target. This is an image review only; no generation or runtime changes made.

## Findings

| Asset | Concrete observation | Decision |
|---|---|---|
| ally-1 | Tall realistically proportioned armored knight, many tiny armor/cloth folds, side-oriented pose, two painted swatches behind head; loses compact harbor-worker personality | Revise subject and proportions |
| ally-2 | Three separate character designs in three panels; at least one usable angular hood idea but narrow realistic legs and rigid frontal mannequin anatomy | Reject sheet; one compact Neri only |
| enemy-1 | Strong ink/shape; left-facing large beak housing, thin long legs, side medallion and smooth bevels; repeats earlier review | Revise camera and compactness |
| enemy-2 | Red/cream skull-headed organic clawed monster, not a maintenance machine; dark torso merges into arm shapes | Reject identity; replace with explicit ceramic machine |
| tree | Legible tree, but realistic dense branch network, broad detailed crown and roots, rectangular picture frame and ground strip | Revise into three big angular leaf masses and bare background |
| column | Main fluted classical column plus six accessory/detail samples; delicate long shaft, excessive ornament | Reject sheet; one squat irregular stone column |
| wall | Multi-panel tileset/ruin kit with many dark openings; no single solid low barrier | Reject sheet; one closed solid block |
| fan | Three tall totem/spear designs; none clearly a compact three-blade weather fan | Reject identity and multiplicity |
| ground | Quiet pale painted surface, potentially useful at board size, but diagonal streaking may imply slope | Provisional material candidate; check seamless repetition and grid overlay |
| grass | Obvious diagonal diamond lattice contradicts screen-aligned square board | Reject pattern; request unmarked moss/grass surface |
| water | Calm horizontally striped teal surface; no bank sockets or current arrow; can only be a fill texture | Provisional fill candidate; never accept as complete connected river tile |

The apparent style-reference influence includes the *layout* of the concept sheet, not only its brushwork: panels, swatches, multiple examples and frame edges recur. Lower adapter weight may help, but must be judged from output; prompt and CFG changes alone do not prove the issue fixed. If multiplicity persists, use a clean single-object style reference prepared for conditioning, never exported as final artwork. The user must receive newly generated original assets, not reference crop exports.

## Short subject-leading prompts

Use one subject paragraph first, then this short shared suffix. Keep the negative input separate and active. Avoid adding “sheet,” “concept board,” “variants,” or lengthy lists of possible shapes to positive prompts.

**Shared suffix**

> One object only, isolated on plain white, full silhouette with clear margins. Compact hand-inked gouache game sprite, unusual angular asymmetry, broad flat muted cream teal sage brass shapes, dark imperfect outline, three values, very sparse interior marks. Elevated front orthographic view, screen south facing, same upper-left light. No ground beneath it.

**ally-1 / Mara**

> One short sturdy human harbor keeper, two-and-a-half heads tall, broad teal triangular work cloak, oversized cream left forearm ram guard, tiny warm face under a practical crooked hood, short square boots, right hand empty. Front facing, both feet visible, simple wedge silhouette, kind capable posture.

**enemy-1 / Sentinel**

> One small upright weather sentry robot, narrow dark slate ceramic body, small wedge head one third of figure height, tiny front horizontal amber sensor, short blunt brass emitter pointing toward viewer, two short simple mechanical legs, cream shoulder patch. Front facing, compact single-cell silhouette.

**enemy-2 / Breaker**

> One squat heavy maintenance ROBOT, broad dark slate trapezoid body, two oversized blunt rectangular ram arms, two short blocky mechanical legs, small recessed horizontal amber sensor in solid cream ceramic housing. Front facing, hunched industrial machine with brass hinges, no face, no weapon held, wider than tall.

**tree**

> One small crooked briar tree, bent brown trunk, exactly three large angular sage leaf masses, a few bold twig notches, short simple roots. Compact broad crown, whimsical lopsided silhouette, no fine branch network, whole tree alone.

**column**

> One freestanding squat ruined stone column, thick tapered ivory square shaft, skewed oversized square cap, compact square foot, three bold cracks, one small sage moss patch. A single simple topplable masonry object, broad clean silhouette, no fluting or ornament.

**wall**

> One low solid stone wall block, three large irregular cream masonry stones, two bold dark joints, shallow flat top, tiny sage moss patch. Closed rectangular barrier, front edge horizontal, square footprint, no opening, no doorway, one block alone.

**fan**

> One compact weather-control FAN machine, one large circular brass rim enclosing exactly three broad teal fan blades and a cream central hub, two chunky supports on a low square ceramic base. Front-facing circular fan clearly visible, short wide machine, no wind effects.

**Shared negative**

> multiple objects, variants, character sheet, contact sheet, panels, frames, border, color swatches, samples, diagrams, extra parts, scenery, floor, text, letters, watermark, isometric, diamond, side view, profile, realistic anatomy, long thin legs, detailed armor, glossy, 3d render, smooth gradients, dense detail, magic glow

**Additional identity negatives where relevant**

- Sentinel: long beak, enormous head, big side fan, claws, hands.
- Breaker: skull, skeleton, bone, flesh, teeth, horns, demon, monster, claws, red cape, gun.
- Column/wall: architectural sheet, inset panels, window, doorway, arch, filigree.
- Fan: spear, staff, totem, pole, character, red eye, blades outside rim.

## Bounded review approach

Test Neri as planned, then one machine and one prop before accepting this prompt setup for remaining revisions. If each is a single subject with compact shapes, continue the bounded pilot. Review all eleven outputs again at matched scale and in an actual square-grid composite; inspect extracted alpha separately. Rejecting this batch does not require changing mechanics, names, story or grid. Human pilot approval remains the production gate.
