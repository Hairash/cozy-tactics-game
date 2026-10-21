# Mature crew correction — Astra low

User rejected raster80-v1 because Mara had mobile-game rendering while Neri was childlike, with a white enclosed background fragment; fan pedestal lost cream color. User explicitly requested Astra with low effort for the critical part.

Astra-low agent designed matched adult composition guides and critically reviewed both generations. Guide sources/script and exact recommendations live in reference/mature-crew/ and scripts/mature_crew_guides.py. These are conditioning only, not final vector exports. Main used local DreamShaperXL Turbo raster img2img, then80px export. No new model downloads/paid services. Unchanged robots/terrain/other props.

First matched .56denoise pair rejected by Astra for rounded child faces, modern baseball cap and hoodie strings. Second pair uses IDENTICAL .44denoise/.20style/.95composition/CFG2.5/8steps/dpmpp_sde/karras/seed428613. Both use the same clean paired style reference and common prompt. Workflow/history/seed/reference hashes and archived candidates retained. No independent percharacter drift-inducing denoise/style tuning.

Result: compact adult faces, horizontal ink eyes, longer bent limbs, shared palette/outline density, no tiny hair/clothes details or rendered highlights. Mara warmrust shield silhouette; Neri teal/ivory hookedstaff silhouette. Astra accepted the pair for human pilot review; Mara's eyes remain broader wedges than Neri's strokes and Mara's crown/fist are softer. Final face readability is necessarily reduced at40px. This is a static pilot, not full gameplay acceptance.

Matting: crew now removes enclosed neutral-white regions as well as edge-connected background; cream paint is warm and retained. Checked both crew on dark/sage at80/64/40 in reviews/mature-crew-comparison.png. Fan repaired from ORIGINAL raster RGB with closed-ink silhouette alpha (fix_fan_matte.py); reviews/fan-alpha-repaired.png demonstrates restored opaque cream base on two contrasting grounds. Do not run generic u2net processing on fan afterward: it removes pale pedestal paint again.

Archives: archive/schematic80 is the complete consistent vector pilot requested by user; archive/raster80-v1 preserves the rejected raster pass. No live/dist changes or publishing. Current assets remain80px PNG; vector guides are only references. Current phase mature-crew-pilot-review, human approval before mass production.

Rebuild: mature_crew_guides.py → mature_crew_revision.py (first calibration only) → revise.py paired-refinement.json → worker.py --only ally-1 ally-2 → raster80_process.py --only ally-1 ally-2. Reapply fan fix separately if needed. Then crew_comparison.py, raster80_sheet.py, validate.py. Use exact current manifest to reproduce accepted second graph; do NOT blindly rerun the earlier first-calibration prep over accepted prompts. Sequential manifest writers only.
