# Source Inventory

## Preserved Collections

I keep `Original Source Recovered/1992/`, `Original Source Recovered/2026/` and `Original Artifacts/` byte for byte. The running copy, `xargons_revenge.prg`, was at the repository root until 23 October 2026 and is now in `Original Artifacts/`, unchanged. `.DS_Store` is excluded from catalogues and comparisons as host metadata. `.gitattributes` disables text conversion and whitespace cleanup for the historical collections; `.editorconfig` disables automatic newline and trailing-space changes there.

The complete [input catalogue](verification/input-catalogue.json) records hashes, sizes and categories. The fresh disk image originally supplied here was side 1 only. The side 2 extraction manifest identified a second image with an apostrophe in its filename; I located that exact capture, checked its SHA-256 and added it unchanged as `Original Source Recovered/2026/Xargon'sRevenge-C16.d64`.

---

## Active Assembly Sets and Fallback Modules

The main assembly root is `REVENGE`. It expands 68 modules in the original include order. Sixty-two are present in the fresh extraction; six come from the 1992 collection through the original `INDEX`. Wildcards resolve against original Commodore names, not escaped host filenames.

| Original module      | 1992 export    |
| -------------------- | -------------- |
| `COMPLETED-SHEET`    | `COMPLETE.TXT` |
| `DATA-LAND/CHARS`    | `DATALAND.TXT` |
| `RASTER-ROUTINES`    | `RASTERRO.TXT` |
| `WHOOPPEE-MESSAGE`   | `WHOOPPEE.TXT` |
| `FIRING-MEGA/CODE`   | `FIRINGME.TXT` |
| `ALI-PRINT&CLEAR`    | `ALIPRINT.TXT` |

The build validates this mapping against `INDEX` rather than selecting similar filenames. Fresh source bytes use CR line endings and uppercase assembler text. The fallback exports use CRLF and lowercase text; the converter normalizes those working copies to uppercase and logical lines, preserving the historical files. The successful object comparison verifies the resulting assembled operands, strings and layout.

---

## Graphics and Reference Inputs

`BJH` is a 1,024-byte alien pool saved at `$2000` and relocated by the original loader to `$0400`. `LANDSCAPE-2` supplies 2,048 bytes at `$1000`. `FRAK!` supplies 2,048 bytes at `$3800`. The runtime ship, alien and explosion glyphs overwrite portions of that font; an initial font atlas alone does not describe the running display.

`ASSEM-GRAPHS`, `CHAR#1-BOT` and `CHAR#1-TOP` assemble the editable terrain for comparison. `LANDSCAPE-1`, `ALIBUM5` through `ALIBUM8`, `TITLE-DATA` and `XARG-SCREEN` are retained alternatives or development material, not silent substitutes. `OBJ` is the original MOS hexadecimal object listing. The separate `O.ALI` listing and the unused `BLOB-MOVE` and `PLANETS` modules are not main-build dependencies.

`ASM.C64`, `EDITOR64`, `DOS5.2`, `MEGA-SUPER`, `SUPER-LOAD`, boot programs and design utilities document the historical development process. They are not a second supported modern toolchain. Side 1's two data fragments and loader do not contain a complete standalone game; they remain preserved without invented replacement files.

The [source manifest](verification/source-manifest.json) lists every disk record, the selected sources, standalone asset addresses and hashes. [Source and Validation](SOURCE_AND_VALIDATION.md) explains the alternatives and the running-reference comparison. [README](../README.md).
