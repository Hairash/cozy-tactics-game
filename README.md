# Cozy Tactics Game · The Last Current

Play: https://hairash.github.io/cozy-tactics-game/

Source: https://github.com/Hairash/cozy-tactics-game

See [HOWTO.md](HOWTO.md) for local setup, dependencies, tests, art checks, and deployment commands.

The playable static site is in `dist/`. GitHub Pages deploys that folder automatically on pushes to `main`; no build or third-party service is required.

# The Last Current — The Hundred Shores

A silent browser tactics adventure: **100 unlocked missions across ten story acts**, 50 crew roles, 20 enemy types, 39 objects, 21 terrain types, and 16 objective types. No stat upgrades, accounts, dependencies, or build step in the portable edition. Open `dist/index.html`, or serve `dist` with a static server. The GitHub Pages edition is publicly accessible.

## Play
Select a crew member and tap a highlighted destination or ability target. Every crew member has 3 HP, 3 move points, and one action per round. Some temporary effects change movement or absorb a hit. Click intermediate tiles to choose an exact path, or a distant endpoint for automatic routing. Forced movement costs no extra points. Moving then acting closes movement; acting first permits movement afterward. Move–act–move is unavailable.

Click the selected unit/card again, click beyond its movement range, or press Escape to deselect. Hover or keyboard-focus a destination for a route preview. Undo restores the previous input within the current round. End Round plays enemy decisions and environmental effects in sequence; enemies do not forecast attacks.

Right-click any tile for its unit, object, terrain, current direction, and interaction rules. On touchscreens, hold the tile or enable Inspect and tap. Some objects offer a nearby interaction button. Tidecaller, Digger, Puppeteer, and Rigger expose four direction choices; Astronomer exposes four weather choices. Transport, ferry, portals, and stone relocation use two targets. Character dialogue stays visible until Continue, Enter, or Space.

Keys: 1–9 select crew, M move, A ability, Z undo, Enter end round, Escape deselect/close. All 100 missions are available from Campaign, with ten act tabs and search. Completion and last-selected mission are saved in the current browser; refreshing restarts the battle. Existing six-mission completion is retained. There are no campaign locks in this testing edition.

## World and mechanics
The rescue of a flooded city becomes a voyage through an Archive, outer quays, rootworks, furnaces, observatory, divided passenger districts, and a court of remembered storms. Each mission has its own title, briefing, character exchange, and objective. Reinforcements, defection, ruptures, changing water and machinery create midbattle events. Crew sizes range from one to six, including repeated roles and rescued passengers. Twenty map blueprints have different dimensions and cutouts, with district-specific terrain, mechanisms, objectives, and formations. Later operations add guarded relay prerequisites and passenger extraction; approach lanes grow to as much as 13 rows, with cover and safe staging terrain.

Units, objects, and terrain are separate layers. Rivers have entry and exit sides; reversal swaps those sides, including bends. Entering drifts at most two cells, stopping the current on the first land cell beyond the end. Ice, springs and gates can then trigger their own entry effects. Movable objects follow the same rules. Ice slides until it ends or is blocked. Fans, springs and conveyors have their own directions. Bridges cross straight river cells and suppress the current underneath; they cannot be built on bends. Fixed props remain on dry ground. Shields absorb one hit; anchors resist pushing. Charges, fire, carnivorous plants, water pumps, linked portals, bells, pressure plates, mirrors, carts, levers and weather interact. Read the searchable Field guide for every role and rule.

The compact desktop layout gives most of the screen height to the board, with objective, selected crew and controls in a side panel. Mobile fits the field to the screen width and keeps action controls at the bottom. Cells are capped at80px on every device, with the board centered in unused space. Extra campaign, story, crew and transmission information is available through Scenario info; Help contains movement and inspection instructions.

The approved raster art pass uses individual 80×80 PNGs for all 50 crew roles, 20 enemy types, 39 objects and 21 terrain types. Broad colors, simple silhouettes and quiet terrain keep them readable at small cell sizes. The same sprites appear in portraits, dialogue, inspection and the guide. Units and props retain genuine alpha, consistent ground anchors and no added ground shadows. River connectivity, direction arrows, goal markers and status marks remain code so they always match the rules. Ordered action playback adds movement, projectile trails, impact particles, splashes, growth, healing and explosion recoil. Reduced-motion preferences simplify effects. No sound, analytics, purchases, multiplayer or server-side gameplay. Optional fonts fall back to system fonts. HTTPS includes an offline service worker and install manifest, subject to browser support.

## AI and difficulty
The first ten missions retain their original simple patrol policy. Five stages increase across the story: Dormant (1–10), Alert (11–30), Tactical (31–60), Coordinated (61–90), and Elite (91–100). Later machines route around obstacles and hazards, avoid imminent charges, choose vulnerable/mission-critical targets, and position repair/shield units to support one another. Coordinated patrols act in a useful support order. Advanced control, ignition, lure and charge abilities require a target within 4 tiles; mortars reach 6. Web/silence/frost control recharges between uses. Enemies still decide on their turn, without attack forecasts or extra level-based statistics.

[The complete difficulty review](notes/DIFFICULTY-REVIEW.md) assesses every mission using independently replayed legal routes, incoming damage, crew losses, ability use, and a second search policy. The first act averages the same 1.9 enemy phases as before. The final two acts average 4.6 phases per winning route, up from about 2.2. Winning routes are examples, not minimum-turn proofs. Difficulty labels are design estimates; a human playtest cohort remains valuable.

## Validation and continuation
- `node tests/rules.cjs`: 81 mechanics, content, geometry, animation-event and regression checks.
- `node tests/terrain-regressions.cjs`:39 river, bridge, movable-object, placement and status regressions.
- `node tests/ai.cjs`: 9 AI, range, relay and extraction checks.
- `node tests/assess.cjs`: independently replays both the previous and revised campaign and generates the per-mission difficulty report.
- `node tests/replay.cjs`: replays winning transcripts for **all 100 missions**, using legal player inputs and requiring actual victory.
- `node tests/campaign.cjs`: legal-action beam search, writes reproducible transcripts to `tests/campaign-results.json`. Focused runs: `ONLY=18,29 BEAM=16 ROUNDS=20 node tests/campaign.cjs`. Optional `FROM`/`TO` are zero-based start and exclusive end.
- Browser QA: 1280×720 laptop layout, large 9×9 map, campaign unlocks, portrait dialogue, direction controls, and 390px mobile layout. Mobile QA is responsive browser testing, not physical iOS/Android hardware. Automated winning routes establish solvability, not a substitute for ongoing human difficulty tuning.

`notes/POLISH-AI.md` records the current graphics/AI/balance checkpoints. `notes/EXPANSION.md` preserves the earlier expansion history. Source is split into catalogs (`data.js`), authored campaign (`campaign.js`), synchronous rules (`game.js`), UI (`ui.js`), raster registry and rendering (`asset-catalog.js`, `art.js`), ordered animations (`effects.js`), and styles. Original six-map data and pre-expansion code remain in `checkpoints/`.

### Dusk expedition visual edition

Original painted campaign vista; dark teal/brass interface; material-shaded vector crew and machines; map previews for all 100missions; illustrated field guide, inspection and deployment roster. Hover paths now draw their actual trace. Melee arcs, casting motes, impact flashes, active-actor outlines and turn banners make action playback easier to follow. Header controls choose 1×/1.5×/2× playback and reduced ambient motion; preferences persist on this device. System reduced-motion is honored. The guide includes keyboard shortcuts and a motion toggle on mobile.

Visual regression fixture: `tests/visual-qa.html`. All 100mission layouts checked at 1280×720, 1024×600 and390×844. Gameplay regression:81 rules +9 AI checks and100 winning transcript replays pass. Generated art provenance/prompt: `notes/ART-ASSETS.md`.

### Field-first UI

The battlefield fills the available laptop height and phone width. Only the objective, selected unit and action controls remain on the battle screen, with readable 16px body text. Open Scenario info for crew status, story and radio history; open Help for movement rules, inspection and animation settings. All 100missions remain unlocked.

## Raster art sources and rollback

[The production notes](notes/RASTER-ART-RELEASE.md) describe provenance, exports, review and deployment. `art-production/` preserves the inventory, exact prompts, original generated sources, category manifests and restart checkpoints. `scripts/assemble-art.cjs` assembles the runtime; `scripts/check-art.py` checks dimensions and transparency and creates 80/40 px review sheets. `tests/art-gallery.html` checks every runtime image in a browser. The previous complete playable build remains in `checkpoints/before-approved-raster-art/`; accepted and earlier pilot options remain in `art-pilot/`.

[Terrain/UI correction notes](notes/TERRAIN-UI-FIXES.md) record the current river, bridge, highlight, status and global-action fixes and their verification.
