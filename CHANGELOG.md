# Changelog

## [1.2.0] 23-10-2026

Structure and documentation release that aligns this repository with my Dork's Dilemma, Tycoon Tex, Xargon Wars and Xargon's Revenge v2 repositories. The game build is unchanged (SHA-256 `32c13c88…adce33`).

### Added

- `docs/GREMLIN_ARCHIVE.md`, the chapter shared with my other Micro Projects reconstructions, with a project section on `DISK9` and the earlier development disks.
- A "Related Repositories" section in the README that points to `Xargons_Revenge_C16_v2`, which explains the alien difference and builds both game versions.
- Local README badges in `docs/images/badges/`.
- History and Credits sections on the Gremlin Archive and the book, and on how this repository relates to the template and to v2.
- Documentation tests that check the saved handbook is current and that the full handbook has its chapters, badges and images.

### Changed

- The running copy `xargons_revenge.prg` moved from the repository root to `Original Artifacts/`, unchanged. The build, input catalogue and recorded input hashes use the new path.
- README, Quick Start, Testing, Rights, Sharing on GitHub, `src/README.md` and the guide headings follow the common structure; the handbook uses the common chapter order, with the README first.
- The handbook generator and template are shared with my other restorations; game wording now lives in `docs/handbook.json`.
- The GitHub Actions workflow follows the common layout and also runs the documentation tests.
- Links to Dork's Dilemma's history point at its renamed `docs/HISTORY_AND_CREDITS.md`.
- Work happens on `dev`, with verified checkpoints merged into `main`. Common `.gitignore` across the restorations.

### Removed

- A planning note at the repository root, which isn't historical material. Its entry was dropped from `docs/verification/original-inputs.json`.

---

## [1.1.0] 21-10-2026

### Added

I added the codebase analysis, generated code reference and index, raw asset/table exports, ten decoded graphics references and a practical guide to same-platform derivatives, emulator hosts and native ports. The analysis records 68 active modules, 682 symbol definitions and 515 statically resolvable direct transfers, with method limits stated.

I added the nineteen-chapter offline HTML handbook, configured through `docs/handbook.json`, reusing the Tycoon Tex generator, templates and licensed Marked/Mermaid dependencies. Images, styles, controls and diagram rendering are embedded. Markdown remains the source of truth. Make targets cover generation, watch mode, freshness and tests.

I added three asset/composition tests and seven handbook tests. The complete suite now has thirteen Python tests and seven Node tests. I extended the isolated observations from 44 to 48 to check full-byte fire flags and confirm the score-overflow store at `$0186` with a sentinel. The preservation PRG bytes are unchanged.

### Changed

I expanded source/asset classification and provenance, retained the additional probe evidence and documented the original graphics alternatives, runtime glyph replacement and source-versus-reference choices. I recorded the successful GitHub Actions run for `v1.0.0` separately from local VICE checks. I reviewed the authored prose using the humanizer skill while keeping facts, uncertainty and reference material intact.

Release tag: `v1.1.0`. Release commit: `v1.1.0^{commit}` (resolve with `git rev-parse`). The annotated tag records the exact release commit.

### Fixed

I corrected the pause instructions to Space/G from the actual keyboard matrix. The initial guide's Shift Lock statement was wrong. The preserved game instructions have not been changed.

### Known limits

The in-app browser blocked local file previews under its URL security policy. Desktop/narrow browser rendering, runtime reader controls, Mermaid rendering and print preview remain pending; static generation, link, embedding and freshness tests pass. Manual gameplay controls, audible sound, later transitions, full progression and real hardware remain pending. The cause of the running reference's shifted alien pages is unknown.

---

## [1.0.0] 21-10-2026

### Added

I preserved both 2026 disk images, their verified extractions, the matching 1992 ZIP and extracted collection, the running PRG and supplied artifacts. The initial 212-file baseline excludes `.DS_Store`; the subsequently located side 2 image is catalogued separately.

I restored the source with ca65 and ld65, using six explicit 1992 fallbacks. All 8,094 object bytes match. Direct Python, shell, Make and both pinned PlatformIO environments produce the same 15,362-byte PRG, loading at `$0400` and entering at `$1800`.

I added ten regression tests, bounded PAL C16 VICE verification, screenshots, full retained monitor evidence and 44 controlled routine observations. The source and running reference reach gameplay with five lives. Their code, terrain and font match; alien selections differ at wave indices 4–15.

I added build, testing, source, validation, history, artifact, rights and sharing guides, preservation attributes, editor settings, VS Code tasks and a GitHub Actions workflow.

Release tag: `v1.0.0`. Release commit: `f058dc8900558280c4e52188346c02e7426a6b5f`. The annotated tag records the exact commit without a self-referential file hash.

### Known limits

Manual controls, audio, later transitions, all scoring paths, a full play-through and real hardware remain pending. The reason for the running reference's shifted alien pages is unknown. Editable terrain differs from the loader-selected asset in 29 bytes. Packaging advertises three lives, while the source starts with five and displays at most three icons. GitHub CI is checked after publication and is reported separately from local validation.
