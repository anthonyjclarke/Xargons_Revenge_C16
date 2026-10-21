# Xargon's Revenge – Project Context

## Target and Entry

PAL Commodore C16, 16 KB RAM, TED and 6502-family instructions. VICE `xplus4` 3.10. The preservation PRG loads at `$0400` and enters at `$1800` (`SYS 6144`); it has no BASIC stub. The supplied compressed reference loads at `$1001` and starts its decompressor at `$100D` (`SYS 4109`).

---

## Source and Preservation Rules

Read both D64 images in `Original Source Recovered/2026/` directly and check every extracted payload. Prefer those bytes. Use only the six `INDEX`-validated 1992 fallbacks in `scripts/restore_c16.py`. Never edit, rename, normalize or extract into the preserved collections. Keep their Git text conversion disabled.

The source root is `REVENGE`, in original `.LIB` order. Missing, ambiguous or recursive includes must fail. The rebuilt `$1800`–`$379D` region must match all 8,094 `OBJ` bytes. Do not copy executable bytes from a reference or relax equality for a feature change.

The original loader selects `BJH` (saved `$2000`, relocated `$0400`), `LANDSCAPE-2` (`$1000`) and `FRAK!` (`$3800`). Editable terrain differs in 29 bytes and stays comparison-only. The running reference has shifted alien pages; preserve the complete `BJH` source asset by default.

---

## Build Pipeline and Gotchas

Run `./build.sh` or `python3 scripts/restore_c16.py`. Make and both PlatformIO environments call that same pipeline. Outputs belong in ignored `build/`. `make test`, `make verify` and `make probes` cover regression, bounded VICE startup and controlled routine calls.

The source starts with five lives despite three on the packaging; the display caps icons at three. IRQ routines patch dispatch operands and rewrite glyph RAM. Flags tested with `BIT` use the high bit. Keep label-adjacent operands, alternate entries such as `SCORE+2` and `DELAY+2`, tables and writable code intact.

VICE screenshots need a graphical session. Automated checks disable audio and inject a recorded fire flag; they do not verify manual controls or a full game. Do not turn a skipped emulator check into a pass.

---

## Documentation

Edit Markdown and regenerate `docs/XARGONS_REVENGE.html` with `make docs`. `make docs-check` checks analysis, graphics and handbook freshness. Do not edit generated references in `docs/analysis/` by hand. Keep prose in Anthony's first person, preserve uncertainty and date supplied recollections. Keep this context under 100 lines.
