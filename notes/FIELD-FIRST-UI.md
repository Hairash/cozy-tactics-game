# Field-first interface · 2026-10-23

Request: remove persistent crew roster/log/campaign exposition; enlarge fonts; maximize battlefield; move optional details into Scenario info and Help.

Implemented:
- Header contains mission title (desktop), Scenario info, Help, Campaign.
- Main field contains only tactical tiles, objects, units, routes and action feedback; removed board top/bottom bars, round counter, field peek, route captions, legend and inspect toggle.
- Desktop uses the full available height below a 56px header, with one 304px sidebar for objective, selected unit and action controls.
- Phones use 98% of available width for the field. Objective and selected unit are below it; fixed action dock remains reachable.
- 16px objective/ability body text,14px secondary labels; larger modal/guide text too.
- Scenario info: mission story, round/weather, expandable campaign story, crew status/selection, radio history, field notes, restart.
- Help: movement/action logic, inspection activation, keyboard controls, animation settings and field guide.
- Campaign picker has no campaign prose/banner.
- Service worker v9 includes battle-ui.css.

Verification:
- 81 rules + 9 AI/balance tests pass.
- 100 winning mission transcripts still replay successfully.
- All 100missions rendered at 1280×720,1024×600,390×844: no horizontal overflow, no clipped desktop End round controls, no old field text wrappers, objective>=16px. Phone field width>=96% and objective visible.
- Opening movement across ice, melee push/current animation, scenario crew selection and optional inspection manually checked in browser; no console errors.
- Browser phone sample: client width 375px, field 369px (98%); objective 16px; fixed End round bottom 835px in 844px viewport.

Publication pending. Source gameplay unchanged.

## Published
Source:9d5336477150d70de15b0ac1041af01c3b1a3f77
Version:appgprj_6ad941cb6a948191b9a41ebec2143981~appgver_49c08b30e5408191b223024c8f671353
Deployment:appgdep_6adb46e59afc8191acfeb6b4dbee1c16 (succeeded 2026-10-23T11:37:22Z).
URL:https://the-last-current.groovyray257.chatgpt.site
Existing private audience preserved. Live battle verified, no console errors.
Evidence:evidence/field-first-live.png and evidence/field-first-mobile.png.
Completed; no pending work.
