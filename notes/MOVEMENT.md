# Movement follow-up
- Click selected unit/card again, or an invalid destination, to deselect. Right-click inspection remains independent.
- Three voluntary movement points per round, shared across as many clicks as desired; terrain drift and sliding are free.
- Adjacent ice/current tiles are directly clickable entry points. They animate immediately to their forced landing; remaining points can then be used.
- Distant destination clicks still route automatically; prefer safe routes within the remaining budget. Hover/focus previews the actual route and landing.
- Acting after spending movement closes it. Acting before movement leaves the full movement phase available. All ability/lever actions use the same rule.
- Update UI, regression tests, campaign playthroughs, desktop/mobile QA, and existing private deployment.

Engine and UI implemented. 34 rules checks pass; six campaign missions solved under new movement rules and transcripts replay successfully. Animation input lock preserved. Remaining: browser QA for direct ice entry/remaining points and post-move action closure; mobile layout; deployment.

Browser QA: clicked an out-of-range tile and confirmed no crew selected; clicked an intermediate stop (2/3 points left), then clicked ice directly and watched the slide (1/3 left), then used Ram to close movement. 34 rules checks and all six updated campaign replays pass.

Desktop and 390px browser QA complete: budget updates after every click, direct ice entry slides immediately with points left, out-of-range deselection, and Ram after partial movement displays Movement closed after action. Route preview shows the forced landing and step path. Mobile controls expose remaining points. Ready to publish.

Published successfully: https://the-last-current.groovyray257.chatgpt.site, source 11e25662e983a03e4daa4a729ec2bd0c3879a694, deployment appgdep_6ad9dd405dd8819186891b1a35d4025d. Updated portable ZIP included. New Chrome tab used for live verification because original user tab had an ongoing battle. Device campaign test flag preserved. No remaining movement tasks.
