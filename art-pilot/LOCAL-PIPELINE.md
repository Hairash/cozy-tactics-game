# Local pilot operation

Runtime: ../art-runtime
ComfyUI loopback API: http://127.0.0.1:8188
Python: runtime/venv/bin/python. No paid endpoints/API keys are used.

Start ComfyUI from runtime with:
`venv/bin/python ComfyUI/main.py --listen 127.0.0.1 --port 8188 --preview-method none --disable-auto-launch --reserve-vram 2`

From repository:
`../art-runtime/venv/bin/python art-pilot/scripts/worker.py --only enemy-1`
`../art-runtime/venv/bin/python art-pilot/scripts/worker.py` (only this pilot's11jobs)
`../art-runtime/venv/bin/python art-pilot/scripts/process.py`

Queue state is assets.json. Every submission stores prompt_id before waiting. Resume reuses submitted/generating IDs via ComfyUI history, preserves raw files, and skips generated/processed items. If interrupted in the narrow submission-acknowledgement gap (status=submitting), reconcile local /queue and /history before any retry. Never silently resubmit unknown jobs. A failed job remains failed until explicitly revised.

All inputs/outputs remain local. Reference crops are conditioning inputs only, never final exported art. Processing uses Pillow/SciPy and explicit u2net CPU matting, not rembg's differently licensed default model. Master transparent sprites512×512, shared bottom anchor; terrain256×256, opaque.

No production game files may be replaced and no catalog beyond the pilot may run until human approval.

Local preview: serve repository at port4174; open /art-pilot/preview/.

## Current calibrated pilot
DreamShaper XL Turbo with IPAdapter style/composition conditioning is the current model. Character repairs additionally use VAE-encoded original geometric guides (img2img). All workflows, seeds, sources and archived candidates are retained.

Run manifest mutations sequentially: worker, revision, processing and validation are not safe to run concurrently. Use explicit canonical IDs when processing; diagnostic jobs remain for provenance and are excluded from preview. After ordinary processing, run `scripts/tree_matte.py` for the tree: generic u2net erased the fine canopy. Do not rerun prepare.py over calibrated references. `painterly_revision.py` documents the corrected crops but need not be rerun to resume.

The pilot is a static art study. It does not establish animation consistency or production gameplay integration. User review gates mass production; technical validation alone never accepts the art direction.
