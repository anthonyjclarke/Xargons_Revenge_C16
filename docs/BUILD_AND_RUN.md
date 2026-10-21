# Build and Run

## Requirements

I use Python 3.9 or later, cc65 tools reporting version 2.18 or later, and VICE `xplus4` 3.10 for verification. PlatformIO Core is pinned to `6.1.19` in CI, with `platformio/native@1.2.1` in `platformio.ini`. Node 22 or later is needed for the handbook; Pillow 10.1 or later is needed for the graphics. The recorded local tools are in [tool-checks.json](verification/tool-checks.json). The installed Homebrew cc65 package is 2.19, but its executables report 2.18; I retain the actual output.

Python's standard library handles the build. The catalogue check also needs `unzip` with support for the old Shrunk and Implode ZIP methods. Python's `zipfile` cannot decode those methods. I extract only into a temporary directory for comparison.

```sh
brew install cc65 vice
python3 -m pip install platformio==6.1.19 Pillow==10.3.0
```

---

## One Build Pipeline

```sh
python3 scripts/restore_c16.py
./build.sh
make
pio run -e c16
pio run -e c16_debug
```

Every entry point calls `scripts/restore_c16.py`. Release and debug produce identical PRGs; both retain the symbols needed for study. PlatformIO is an adapter and does not compile a second implementation. The direct output is `build/xargons-revenge.prg`; PlatformIO outputs are under `build/platformio/<environment>/`.

The pipeline reads both original disk images directly, validates the directory and every extracted payload against the capture manifests, adds exactly six `INDEX`-mapped 1992 source modules, expands `.LIB` directives in original order and converts MOS assembler syntax to ca65. Missing, ambiguous and recursive includes fail. The non-ASCII `$AF` byte in a terrain comment is retained through Latin-1 decoding; it is not an instruction or data byte.

`config/c16.cfg` preserves zero page at `$0002`, work allocations at `$0200` and code at `$1800`. `config/terrain.cfg` separately assembles the editable terrain for comparison with the loader-selected binary. The default PRG combines `BJH` relocated from its saved `$2000` to `$0400`, `LANDSCAPE-2` at `$1000`, object-matched code at `$1800` and `FRAK!` at `$3800`. Unspecified output memory is zero-filled. No bytes come from the compressed reference.

Generated assembly, logical-source mappings, listings, labels, maps and debug information are in `build/`. The object region ends at `$379D`, leaving 98 bytes before the font. These bytes are padding, not proof that a new feature will fit safely.

---

## Emulator Launch

```sh
python3 scripts/run_vice.py
python3 scripts/run_vice.py --original
./scripts/run_vice.sh
make run
make run-original
pio run -e c16 -t upload
```

The launcher selects `c16pal` and 16 KB RAM, waits at the reset-ready breakpoint, loads the PRG at its saved address and goes to `$1800`. The rebuilt PRG has no BASIC stub. The original PRG loads at `$1001`; its BASIC stub says `SYS 4109`, so the original launcher goes to `$100D` and lets the original decompressor run.

I can supply a different PRG and explicit `--entry 0x1800` for debugging. This does not create a supported variant build. The launcher keeps its monitor script and emulator log under `build/vice/`. Normal launch allows sound; automated verification uses `+sound` to disable it.

VICE needs a graphical session for screenshots. In a restricted macOS process, it may fail before opening a window. I run local verification with access to the desktop session. A missing emulator or inaccessible graphics session is a skipped or failed check, never evidence of a rendered title.

---

## VS Code and Maintenance

I open the project directory in VS Code, install the recommended extensions from `.vscode/extensions.json` and use the supplied tasks for direct build, PlatformIO builds, launch, tests and VICE checks. Debug builds provide `xargon.labels`, `xargon.map`, `xargon.lst` and `xargon.dbg`; this is not a claim that a VS Code source debugger has been connected to VICE.

`make clean` removes generated `build/` and `.pio/` directories. It does not remove original inputs or committed evidence. [Source Inventory](SOURCE_INVENTORY.md) defines the source priority, and [Testing](../TESTING.md) covers verification.
