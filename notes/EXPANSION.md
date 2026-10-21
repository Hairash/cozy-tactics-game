# The Last Current — The Hundred Shores expansion
User-authorized scope: compact laptop layout; directional fans; connected bending rivers, Tidecaller direction control; varied crew/enemies/map shapes; 100 unlocked missions; a long story with portrait speech bubbles and midbattle events. Preserve incremental movement, animations, inspection, undo, no enemy forecasts, mobile usability.

## Milestones
1. [complete] Modular content catalog + 100 authored mission/story specifications across 10 acts. Preserve original six as opening chapters, revise rivers and geometry.
2. [complete] Dynamic board bounds/masks, connected river traversal, direction controls, expanded actions/enemy AI/objects/terrain/objectives, event engine.
3. [complete] Compact desktop UI, scrollable sidebars, visual river connections, direction selector, campaign atlas, contextual speech bubbles and full inspection.
4. [complete] Rules tests + legal-input campaign solver/replay validation for all 100; repair unplayable scenarios. Desktop 1366x768/1280x720 and mobile browser QA.
5. [complete] Refresh portable edition, package/publish existing private Site, verify deployment and handoff.

## Architecture / resume
- Existing source checkpoint: checkpoints/game-before-expansion.js. Original six map data: checkpoints/original-missions.json.
- New data.js owns unit/object/terrain/enemy catalogs and imports campaign.js (authored story rows + deterministic map blueprints).
- game.js remains synchronous, captures ordered immutable playback frames; effects.js animates them. ui.js renders compact responsive UI. art.js owns SVG artwork.
- Flow is per tile: follow local outgoing direction at every water step, max 2 cells; once leaving water stop immediately, so never go over 1 land cell past the river end.
- Campaign is always unlocked, independently of earned completion; 100 missions, 10 acts, no stat progression.
- Validation must test real gameplay actions; do not grant victory or weaken objectives in tests.

Checkpoint: data.js has 50 distinct playable roles / 20 enemies / 39 objects / 21 terrains. campaign.js contains 100 explicit title/briefing/dialogue/story-event rows across 10 acts and 20 map blueprints. game.js rewritten with dynamic dimensions/masks, per-segment current traversal, 50 actions, two-stage transport/portal placement, enemy AI, environment, 16 goal types and scripted events. Next: UI/art/effects integration, catalog/geometry validation and campaign solver. Watch for original opening maps' enemy/goal placement and support-only mission solvability.

Validation checkpoint: 76 rules checks pass, including bent/looping/end-of-river flow, all 50 abilities, directional fans, movement order, portals/bridges, and scripted events. First automated campaign batch wins missions 1,3–10; mission 2 needs investigation. Full remaining campaign solver is running with BEAM=8. UI preview works and anchored speech bubbles display. A spurious boss marker on empty cells was fixed. All 50 roles, all 20 enemy types, all 39 objects, and all 21 terrain types are used in campaign layouts/rosters.

Campaign validation pass 1: 85/100 solved. Found real engine bugs: generated boss missions spawned the command unit twice; enemy fire could destroy essential carts/records, and the solver preferred an impossible objective after that. Fixed duplicate boss, armored carts stop shots, essential records survive damage, and destroying a cart now explicitly fails its mission. Marked disarm charges resist gunfire (their fuse still runs). Relay missions now require sealing consoles AND reaching a command exit; the Conductor no longer wins those maps in one click. Pass 2 running for all 100 with BEAM=12 / ROUNDS=20. Mission 12 now wins in 2 rounds after the cart fix.

Validation pass 2/deep search: 93/100 now solved. Remaining failures before balance retest: 17,18,27,29,40,60. (See current tests/campaign-results.json for authoritative list.) Fixed fairness: enemy charges now give one full player turn to escape/disarm instead of exploding immediately; web/silence machines recharge between uses to prevent permanent stun locks; charmed repair/shield enemies now help the crew rather than their former side. Deeper BEAM=48 retest running. Added 100 authored response lines, spoken by another crew member midbattle, and Enter/Space now actually advances speech bubbles. Laptop iframe QA fixture: tests/laptop-preview.html at 1280x720.

Final validation checkpoint: all 100 missions now have winning public-input transcripts, independently replayed with real victory checks; 81 rules tests pass. Support missions 18,29,40,50 have authored flank objectives to prevent guards occupying indispensable pads indefinitely. Story bosses retain Bellkeeper/Foundry/Heart/Auditor abilities. Portal links are pruned if an objective removes an endpoint. Speech now persists until Continue/Enter/Space. Laptop 1280×720 fit and mobile 390px/large-board/portrait speech verified; physical phones not tested. Publication milestone remains in progress until deployment is recorded below.

Published successfully 2026-10-22: source `9e0286419de37040f322689f9152425247d77142`; saved version `appgprj_6ad941cb6a948191b9a41ebec2143981~appgver_43cfdf72ee7c81919cfd684b713c7b6a`; deployment `appgdep_6ada48a7cdd481918a5befed2f8e5711`. URL https://the-last-current.groovyray257.chatgpt.site . Owner-private audience preserved. New Chrome tab 570925964 shows mission 10, separate from existing battle tabs. Live screenshot evidence/hundred-shores-live.png; mobile portrait evidence/expansion-mobile.png. Portable archive refreshed at the-last-current.zip. All milestones complete.
