# Changelog

## [1.0.0] 21-10-2026

### Added

I preserved both 2026 disk images, their verified extractions, the matching 1992 ZIP and extracted collection, the running PRG and supplied artifacts. The initial 212-file baseline excludes `.DS_Store`; the subsequently located side 2 image is catalogued separately.

I restored the source with ca65 and ld65, using six explicit 1992 fallbacks. All 8,094 object bytes match. Direct Python, shell, Make and both pinned PlatformIO environments produce the same 15,362-byte PRG, loading at `$0400` and entering at `$1800`.

I added ten regression tests, bounded PAL C16 VICE verification, screenshots, full retained monitor evidence and 44 controlled routine observations. The source and running reference reach gameplay with five lives. Their code, terrain and font match; alien selections differ at wave indices 4–15.

I added build, testing, source, validation, history, artifact, rights and sharing guides, preservation attributes, editor settings, VS Code tasks and a GitHub Actions workflow.

Release tag: `v1.0.0`. Release commit: `v1.0.0^{commit}` (resolve with `git rev-parse`). The annotated tag records the exact commit without a self-referential file hash.

### Known limits

Manual controls, audio, later transitions, all scoring paths, a full play-through and real hardware remain pending. The reason for the running reference's shifted alien pages is unknown. Editable terrain differs from the loader-selected asset in 29 bytes. Packaging advertises three lives, while the source starts with five and displays at most three icons. GitHub CI is checked after publication and is reported separately from local validation.
