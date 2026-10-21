# Development how-to

Run the commands below from the repository root unless stated otherwise. The game is a static HTML/CSS/JavaScript application: no build step, npm packages, database, API keys, or backend are required to play.

## Get the code

```sh
git clone https://github.com/Hairash/cozy-tactics-game.git
cd cozy-tactics-game
```

If you already have a checkout, open a terminal in that folder instead.

## Required tools

- A modern browser to play.
- Python 3 for the local HTTP server.
- Node.js for the automated tests and asset assembly. GitHub Actions currently runs the checks with Node.js 24.
- Git to clone, commit, and push changes.

Check the installed tools:

```sh
python3 --version
node --version
git --version
```

There is no `package.json`, so there is no `npm install`, `npm start`, or `npm test` command. The JavaScript tools use Node's built-in libraries.

## Run the game locally

```sh
python3 -m http.server 8000 --bind 127.0.0.1 --directory dist
```

Open <http://localhost:8000>. Stop the server with **Ctrl+C**. If port 8000 is occupied, use another port, such as 8001, and change the browser URL to match.

Edit files in `dist/` and refresh the browser. A hard refresh can help if older scripts or images remain cached. Progress is saved in browser storage for the current origin; different hosts or ports have separate progress. Refreshing restarts the current battle.

### Test on a phone over the same Wi-Fi

```sh
python3 -m http.server 8000 --bind 0.0.0.0 --directory dist
```

Open `http://<computer-LAN-IP>:8000` on the phone, replacing the placeholder with your computer's local network address. Allow the local server through the firewall if prompted. This makes the server reachable on your network; stop it with **Ctrl+C** when finished. HTTPS-only install/offline features may be unavailable over a phone's plain HTTP connection.

## Run automated checks

Run these individually, or paste the complete block. No Python packages are needed for these checks.

```sh
node scripts/check-repo-privacy.cjs
node tests/drone-art.cjs
node tests/rules.cjs
node tests/terrain-regressions.cjs
node tests/blade-regressions.cjs
node tests/ai.cjs
node tests/replay.cjs
```

These are the same checks used by `.github/workflows/pages.yml` before deployment:

| Command | Checks |
| --- | --- |
| `check-repo-privacy.cjs` | Tracked text for personal paths, private configuration filenames, and common credential/contact patterns; does not audit old Git commits. |
| `drone-art.cjs` | Separate artwork for the Beekeeper, friendly worker drone, and enemy drone; actual summon rendering choice. |
| `rules.cjs` | Core mechanics, content, geometry, and animation events. |
| `terrain-regressions.cjs` | Rivers, bridges, placement, object transport, and status effects. |
| `blade-regressions.cjs` | Contiguous Bulldozer pushes, delivery carriers, and weather. |
| `ai.cjs` | Enemy behavior and balance-related rules. |
| `replay.cjs` | Legal winning action transcripts for all 100 missions. Writes `tests/replay-report.json`. |

The privacy check scans tracked files. Stage new files with `git add` before running it if you want them included. A clean scan is a useful safeguard, not a guarantee that every possible secret format will be detected.

### JavaScript syntax checks

There is no configured linter or formatter. Node can check syntax without running the files:

```sh
for file in dist/*.js scripts/*.cjs tests/*.cjs; do
  node --check "$file" || exit 1
done
```

## Browser and responsive checks

Serve the repository root so the test pages can load the game:

```sh
python3 -m http.server 8001 --bind 127.0.0.1
```

Open:

- <http://localhost:8001/dist/> — normal game.
- <http://localhost:8001/tests/visual-qa.html> — choose a viewport, then **Render all 100**; the final report should have an empty `failures` array.
- <http://localhost:8001/tests/terrain-ui-qa.html> — interactive river, bridge, effects, path, weather, and drone fixtures; **Measure** reports layout/state checks.
- <http://localhost:8001/tests/art-gallery.html> — runtime image gallery.

Check laptop and phone widths, image loading, move/ability highlights, route contours, and interactions. These are manual browser tools, not headless tests. Stop the server with **Ctrl+C**.

## Optional Python libraries for art tools

Only the image-processing/review scripts need **Pillow**. Keep it in a repository-local virtual environment:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install Pillow
```

The `.venv/` folder is ignored by Git. There is no need to activate it when using the explicit interpreter paths below. Historical ComfyUI experiments are optional and are not required to play, test, or deploy the game.

### Assemble and validate art

Processed production assets and accepted pilot exports are the inputs to assembly. Runtime images belong in `dist/assets/art/`; raster masters are 80×80 pixels.

```sh
node scripts/assemble-art.cjs
.venv/bin/python scripts/check-art.py
node scripts/finalize-art.cjs
```

- Assembly copies the selected exports and generates `dist/asset-catalog.js` and `art-production/assembly-status.json`.
- The Python check writes `art-production/qa-report.json` and contact sheets in `reviews/full-raster/`. Inspect the report: `missing` and `errors` must be empty. The Python script reports findings but does not itself fail with a nonzero exit code for image-quality findings.
- Finalization assembles again, checks the saved integrity report, and regenerates `dist/sw.js` for offline caching. Run the Python check first so its report is current.

After changing assets or release cache behavior, update the cache version in `scripts/finalize-art.cjs`. The art helper/catalog URLs are versioned in `dist/index.html` and the browser fixture; keep these versions consistent when changing them. Then rerun the checks and inspect the game in a browser.

Raw generation outputs, local-only inputs, and credentials should remain ignored. See [the art brief](art-production/BRIEF.md), [drone provenance](art-production/companions/README.md), and [privacy review](notes/REPOSITORY-PRIVACY.md).

## Advanced campaign tools

These tools generate or change reports/transcripts; they are not needed for normal regression testing.

```sh
node tests/assess.cjs
```

Replays campaigns and writes difficulty-assessment reports. To search for new legal winning routes for selected missions:

```sh
ONLY=24,44 BEAM=16 ROUNDS=20 TIME=90 node tests/campaign.cjs
node tests/replay.cjs
```

`ONLY` uses one-based mission numbers. `FROM` is a zero-based start index and `TO` is an exclusive end index. `TIME` is the search time budget per mission in seconds. The solver writes `tests/campaign-results.json`; review its diff before committing and always verify with `replay.cjs`. Use a separate output file for experiments:

```sh
ONLY=24 BEAM=16 TIME=90 OUTPUT=campaign-experiment.json node tests/campaign.cjs
```

The output filename is relative to `tests/`. Do not commit failed experimental results over the canonical winning routes.

## Commit and deploy

After reviewing your changes and running the checks:

```sh
git status --short
git add HOWTO.md
# Stage other intended files explicitly as needed.
node scripts/check-repo-privacy.cjs
git diff --cached
git commit -m "Describe the change"
git push origin main
```

Pushes to `main` run the tests and deploy **only `dist/`** to GitHub Pages. Check the result at <https://github.com/Hairash/cozy-tactics-game/actions>.

Public game: <https://hairash.github.io/cozy-tactics-game/>.
