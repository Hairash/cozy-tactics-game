# Repository privacy review

The published tree was scanned for personal filesystem paths, private configuration filenames, credential/token patterns, authorization headers, authenticated URLs and private contact emails. No credential-pattern findings were detected. This is a targeted audit, not a guarantee that every possible secret format is recognizable.

Cleanup removes personal checkout references, uses relative paths in docs and art manifests, makes the art registration input configurable, excludes obsolete setup logs and local hosting identity, and ignores private configuration and local-only sources. Local originals are preserved but not tracked. scripts/check-repo-privacy.cjs runs in GitHub Actions to catch regressions. Future repository commits use a GitHub no-reply author address.

## Historical exposure requiring a decision

The public history was scanned separately: 790 blobs, 24 containing former personal filesystem paths, no credential-pattern findings, no email addresses in text blobs. Prior Git commit metadata contains a personal author/committer email address. This cleanup commit does not erase earlier commits. Purging the earlier paths and commit identities requires a coordinated history rewrite and force push; this was intentionally not performed without a specific request. Existing clones, forks, and cached copies could retain old data even after such a rewrite. No credential rotation is indicated by this scan.

Public game and repository URLs, GitHub username, version hashes, art prompts, and historical deployment IDs are ordinary project metadata; deployment IDs do not grant account access. Image exports have transparent raster pixels and do not require local generation cache paths. Historical asset specifications are retained as development history and may describe superseded art styles.
