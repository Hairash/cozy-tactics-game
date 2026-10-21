# Terrain mechanics bugfix — complete

Owned changes: dist/game.js and tests/terrain-regressions.cjs. No UI, CSS, campaign or art changes by this worker.

API:
- riverSides(x,y) returns {entry,exit,incoming,bend}. Both vectors point outward from this cell. Entry points upstream, exit downstream. Existing S.flow is the exit. S.riverIn stores explicit entry vectors. Legacy entry inferred from adjacent water pointing into the cell, stable DIR order excluding exit; missing upstream defaults opposite exit. Forks retain incoming list; a single stable primary entry defines the segment and reverses with it.
- reverseRiver(x,y) swaps entry and exit. All sides are snapshotted before multi-cell reversal/rotation, so bends reverse correctly.
- setDirection(index), setRiverEntry(index), getRiverChoice()->{entry:index,exit:index}. Defaults west to east. Equal choices auto-adjust the other edge to its opposite. Channel uses both explicit choices. Dig first entry uses the chosen edge, interior segments connect along the dug line, and last exit uses chosen direction.
- applyGlobalAction(u) immediately performs a global action at its actor coordinate. Browser keyboard A also immediately applies globals; ordinary abilities enter targeting mode.
- unitEffects(u) -> [{icon,name,text}], shared by inspection and UI for allies/enemies. Includes shield, roots, sleep, charm, cooldown, movement bonus/closure, runway, fragment, passenger, temporary drone, action spent, evacuation and adjacent anchor.

Forced movement:
- Shared entryPreview resolves units and movable objects through ice, water, springs and paired portals. Two water drift steps maximum; first land exit ends drift. Bounded visited states prevent spring loops, portal pair used once.
- Movable objects: crate, bomb, barrel, boulder, cart, oil. Underlying walkable fixtures retained in S.objectUnder and restored as objects leave. Objective collectibles cannot be overwritten. Bomb coordinates/fuse follow every animation state. Conveyors/fans/wind also push movable objects.
- terrainAt recognizes an underlying bridge even while occupied by a movable object.

Normalization:
- All loaded fixed river objects relocate to nearest safe unoccupied land, deterministic distance then row/column ordering. Portal links and directions follow. With no safe land, keep the objective and make a ground island beneath it.
- Legacy bridges stay in place to preserve map routes; underlying terrain is normalized to straight water. New bridge actions require empty straight water only.
- Channel/dig and water setters normalize immediately. Generated fixed vines and new portals cannot be placed on water.

Verification:
- node --check dist/game.js
- node tests/terrain-regressions.cjs — 28 pass
- node tests/rules.cjs — 81 pass (Bridgewright fixture updated by replay worker)
- node tests/ai.cjs — 9 pass
- Replay worker reports node tests/replay.cjs — 100/100 strict legal victories after updating nine changed routes.

All originals remain in repository history / existing backup. Parent owns UI integration and release packaging.

## Release edge-case follow-up

- Fixed-wall relocation already rejected water; added explicit wall-vs-boulder regression.
- Leaving water ends current drift on first land, then resolves landing spring/portal/ice for units and objects; waterSteps stays capped at2 through the whole entry.
- Destroying movable objects now calls liftObject to restore a covered fixture; destroying the fixture itself clears any stale objectUnder entry and portal links.
- Added unit/object river-to-portal, river-to-spring, river-to-ice, bomb/crate-over-portal destruction regressions.
- 37 terrain regressions, 81 rules, 9 AI pass. First strict replay99/100; mission29 transcript repair delegated to replay worker because restored landing effects change legal movement.

## Parent integration / final verification

All requested UI and art integration complete. River SVG channel is filled with raster water and clipped exactly per cell; bridge now horizontal centered raster with90degree perpendicular crossing rotation. Explicit overlays restore move/ability highlights. Cell cap80px across devices; field centered; ResizeObserver+stable mobile gutter fix scrollbar width race. Effect badges use independent grid slots, all descriptions shared with inspection; underlying fixtures are rendered and inspectable. Direct Apply control andkeyboardA execute global actions without a tile; weather selector remains visible.

Parent followups preserve drain as a dry outlet, list root+nearbyanchor effects independently, and give precise root description. Movable-object current/slide/spring/portal animations updated; fixture survives underneath and after destruction.39terrain+81rules+9AI+100strict winning replay checks pass. Four viewport sweeps each100maps pass (1280x720,1024x600,390x844,1920x1080), covering max80cell, centeredfield, clippedrivers, allimagesloaded, nooverflow/clippedcontrols. Browserfunctionalfixturespassed directConductor, TidecallerentryNexitW, reversedbends, two bridge rotations,24effects withoutoverlap/overflow, and cratecurrent->woven-gateanimation. Evidence evidence/terrain-ui-fixes.

All130art exports passdimensions/alpha. Cachev11/portableZIPupdated (1,121,449bytes). Sameowner-privateSiteverifiedtoday:owneronly,0externalvisitors,0groups. Freshsourcehelperopeningfromcommit5071b7dee25bc2f98f11bee33fd2a67513a61779 recorded for the authenticated publishing session. Next: sourcehelperpackageoutsidecheckout ../terrain-ui-release.tar.gz, publishnativeprivate, record terminalsuccess, liveproof, stopownedlocalserver session91384. No requiredimplementationworkremains.


## Publication complete
Source 4e2b7b7fdeb47b4663eb1e65a62f2e15075ec248; deployment appgdep_6adbf6451b488191a5e2d45a58fb2185 succeeded. Live private URL verified and screenshot saved at evidence/terrain-ui-fixes/live-game.png. No outstanding implementation or publication tasks.
