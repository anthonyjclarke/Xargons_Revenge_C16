# Quick Start

## Build

I install Python 3.9 or later and cc65 (`ca65` and `ld65`). On macOS, my tools are installed through Homebrew; I can install them with `brew install cc65 vice`.

```sh
./build.sh
make test
```

The build checks all 8,094 original object bytes. Output: `build/xargons-revenge.prg`.

---

## Run

```sh
python3 scripts/run_vice.py
python3 scripts/run_vice.py --original
```

I use PAL C16, 16 KB RAM. The rebuilt PRG loads at `$0400` and starts at `$1800`; the original uses its BASIC `SYS 4109` decompressor. Neither launch path assumes that load and entry addresses are the same.

On the title screen, `J` selects joystick, `K` keyboard, `S` sound on and `Q` sound off. Keyboard play uses `S` up, `X` down and Return to fire. Escape aborts; the keyboard matrix maps Space to pause and G to resume. Host key mapping and a physical joystick still need manual testing.

See [Build and Run](docs/BUILD_AND_RUN.md), [Testing](TESTING.md) and the [README](README.md).
