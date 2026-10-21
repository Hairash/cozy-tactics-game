# Illustrated tabletop / AI / difficulty pass

User AFK; authorized graphics/animations overhaul, progressively smarter AI, all-mission playthrough and balance tuning. Existing owner-private Site retained.

Chunks:
1. Baseline assessment and checkpoint (complete). Previous 100 legal winning transcripts saved in checkpoints/polish/campaign-results.json. Original engine, maps, art and effects retained alongside it.
2. Vector art, terrain, effects, stage lighting and role silhouettes (complete).
3. Tiered AI: opening behavior retained; hazards/pathfinding/target priorities/support coordination increase across acts (complete).
4. Late encounter/relay tuning; solve and independently replay every mission, compare difficulty metrics; repair unplayable cases (complete).
5. Desktop/mobile browser QA, portable ZIP, private publication (complete).

Source opening: 9e0286419de37040f322689f9152425247d77142. Existing project appgprj_6ad941cb6a948191b9a41ebec2143981.

Solvability tests use public legal gameplay inputs, not flags to grant victories. Automated difficulty metrics and browser playtests must be clearly distinguished from human play of 100 missions. Preserve no attack forecasts, movement phase rules, all unlocked chapters, compact desktop/mobile layout, inspection, undo and ordered playback.

Checkpoint 2: vector artwork replaced: equipped crew silhouettes/portraits; distinct walkers, drones, heavy machines and reactors; custom illustrated scenery for every object; textured terrain, ambient current/fan/fire/reactor animation; action particles, projectiles, water splashes and explosion recoil. AI tiers implemented in game.js (0 opening, 1 alert, 2 tactical, 3 coordinated, 4 elite). Later maps gain 2–4 approach rows, cover, added sentries, longer hold/survival goals and relay prerequisites for mobility objectives. AI frost now recharges between roots to avoid permanent control locks. First full search underway, with expected balance failures requiring repair; do not publish before full legal replay.

Final balance checkpoint: 100/100 legal winning routes independently replay. 81 core rules + 9 AI/balance checks pass. Full difficulty review at notes/DIFFICULTY-REVIEW.md and tests/difficulty-report.json, including old/new enemy phases, damage/losses, distinct ability use, intended estimates, and weak-search sensitivity. Manual planned public-input routes retained for missions 44 and 59; the latter wins in six rounds without weakening the boss. Late rescue extraction and relay prerequisites are enforced by the engine. Advanced casts have range limits; control recharges; no enemy forecasts.
Browser QA: final art and portraits, large 9×13 map fitted to 1280×720 (End Round bottom 698.5), movement/enemy playback, persistent midbattle speech, and 390px phone layout and elite inspection help. Physical devices not tested. Publication is the final outstanding chunk until its deployment result is recorded.

Final live QA caught a layout timing issue: speech bubbles and movement measured the pre-fit board. render now fits the board synchronously, before effects measure their anchors. This fixes desktop dialogue placement and keeps playback geometry stable. Recheck browser anchors, then publish this UI-only repair.

Anchor repair verified at 1280×720: speaker center and bubble center both x=487; bubble bottom is 12.4px above the speaker; End Round bottom=704.5; body scrollHeight=720. UI-only repair leaves all 100 verified gameplay routes unchanged.

All chunks complete. Published successfully 2026-10-22, owner-private audience preserved. Final source 5544c3282364dd971d874fef23a1f4efaa196ab2; version appgprj_6ad941cb6a948191b9a41ebec2143981~appgver_b75d4d34a42481919e28dc80a8b341fb; deployment appgdep_6ada5568656c8191ac65540ca9b1d414. URL https://the-last-current.groovyray257.chatgpt.site . Live Chrome tab 570925972 verifies the revised art; exact speaker/bubble center x597 with 12.2px vertical gap. Existing battle tabs were preserved. Final screenshot evidence/illustrated-live.png; phone evidence/illustrated-mobile.png. Portable ZIP refreshed.
