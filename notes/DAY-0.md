# Day 0 update checkpoint
1. Add snapshot-based action playback: each movement step, impact, projectile and environmental interaction shown sequentially; guard input through playback.
2. Replace locked intentions with enemy decisions made during their own turn (move, then choose a target, then attack). Remove all forecast UI/copy.
3. Inspect every cell's unit/object/terrain via right-click, long press, or Inspect toggle; never spend an action.
4. Device-scoped test campaign flag, independent of earned progress, reversible in Campaign menu. Activation link writes flag only on visited device.
5. Regression checks, campaign solver and browser QA. Publish existing private site and refresh portable edition.

Implementation complete. 20 rules checks and legal-input replays for all six missions pass. Updated campaign solutions finish in 2, 4, 2, 3, 5, 4 rounds. Browser QA verified animated movement/pickup, enemy phase input lock/completion, right-click layered object help, and mobile Inspect toggle/current help. Remaining: publish existing private site, enable flag in user's Chrome game tab, save delivery screenshot.

Published successfully to https://the-last-current.groovyray257.chatgpt.site using source commit 58c92d0ef6f0376f8ee9e143f7da9db3c449db81; deployment appgdep_6ad9c6503bc08191a4dd43bf14bf9a5f. Confirmed updated live game in user's existing Chrome tab; all six chapters enabled via device test flag. Campaign → Restore campaign locks reverses this without changing earned progress. Evidence: evidence/day0-campaign.png. Portable ZIP refreshed. Mobile charge placement, explosion, fire spread and return to round 2 verified in browser. No remaining Day 0 tasks.
