# Xargon's Revenge C16

![Release v1.2.0](docs/images/badges/release.svg)
![Platform Commodore 16 / Plus/4](docs/images/badges/platform.svg)
![Byte match 8,094 of 8,094](docs/images/badges/byte-match.svg)
![Toolchain cc65](docs/images/badges/toolchain.svg)
![PlatformIO 6.1](docs/images/badges/platformio.svg)
![Emulator VICE 3.10](docs/images/badges/emulator.svg)
![Status preservation](docs/images/badges/status.svg)

I wrote Xargon's Revenge at Micro Projects in 1985 for the Commodore 16 and Plus/4. This project preserves my recovered disks, reassembles the surviving source and provides a baseline for studying and developing the game.

I keep the history, build guides, validation, analysis, graphics and porting advice in the [complete offline HTML handbook](docs/XARGONS_REVENGE.html). It is generated from the Markdown sources; `make docs` regenerates the build, analysis, illustrations and reader. [Maintaining the HTML Documentation](docs/HTML_DOCUMENTATION.md) has the details.

![Original cassette artwork](Original%20Artifacts/Xargons%20Revenge%20Image.jpg)

---

## Related Repositories

This is my first restoration of the game, released as v1.0.0 and v1.1.0 on 21 October 2026. It builds one PRG from my 2026 disk images and records the different alien graphics in the running copy as unexplained.

[Xargons_Revenge_C16_v2](https://github.com/anthonyjclarke/Xargons_Revenge_C16_v2) carries the work on from the same preserved inputs. It explains the alien difference by the cassette loader, builds both the game as I wrote it and the game as it was sold, compares six downloaded copies and adds sector copies of all three development disks. Its game v1 is byte-identical to this repository's build. I keep this repository as the record of the first restoration.

[Xargon Wars C16](https://github.com/anthonyjclarke/Xargon_Wars_C16) is the game this one follows on from.

---

## Verified Build

All **8,094 bytes** recorded in the surviving `OBJ` listing match the assembled code and embedded data. The rebuild uses the 2026 disk sources and six explicitly mapped 1992 fallbacks. Graphics come from preserved standalone assets named by the original loader. I have copied no executable or graphical bytes out of the running PRG to complete this build.

![Rebuilt title in VICE](docs/images/restored-title.png)

The title renders and the original control flow reaches gameplay on a 16 KB PAL C16 in VICE, with sound disabled and a scripted fire flag. This verifies startup, not a complete game. Manual controls, audio, later transitions, a full play-through and real hardware remain untested.

The running reference decompresses to identical code and embedded data, but has different alien graphics in waves 5–16. Both binaries start with five lives; the packaging says three and the display shows at most three icons. I preserve that source behaviour. [Source and Validation](docs/SOURCE_AND_VALIDATION.md) explains every compared memory region and the controlled probes.

---

## Build and Run

I build the preserved version with Python 3.9 or later and the cc65 tools (`ca65` and `ld65`), plus VICE (`xplus4`) to run it:

```sh
brew install cc65 vice
./build.sh
python3 scripts/run_vice.py
```

The result is `build/xargons-revenge.prg`, a 15,362-byte saved-address PRG. It loads at `$0400` and enters at `$1800` (`SYS 6144`); it has no BASIC `RUN` stub. The launcher waits for the emulated machine's reset before loading it. I use VICE `xplus4` 3.10, model `c16pal`, with 16 KB RAM. `python3 scripts/run_vice.py --original` runs the compressed running copy through its own BASIC stub.

With PlatformIO Core, or from the PlatformIO terminal in VS Code:

```sh
pio run -e c16
pio run -e c16 -t upload
```

`pio run -e c16_debug` gives identical program bytes plus debug files. [Quick Start](QUICKSTART.md) and [Build and Run](docs/BUILD_AND_RUN.md) cover setup, VS Code and the original running program.

---

## Preserved Inputs

`Original Source Recovered/` holds my 2026 disk images and their extractions in `2026/`, and the 1992 export (the Gremlin archive's `DISK9`) in `1992/`. The build reads both D64 images directly and takes six modules from `1992/` through the original `INDEX`. `Original Artifacts/` holds the cassette artwork, screenshots, the compilation leaflet and the compressed running copy, `xargons_revenge.prg`.

Generated assembly, extracted working copies and build reports all go into `build/`, and the original inputs stay byte for byte as they were. The [Source Inventory](docs/SOURCE_INVENTORY.md) records source priority, fallbacks and unused material, and the [Artifact Catalogue](docs/ARTIFACTS.md) identifies the supplied images by content.

---

## History and Recovery Background

I was a fan of Scramble and wanted to make a scrolling game. I used the same C64 and shared-1541 development setup for all my C16 games. [History and Credits](docs/HISTORY_AND_CREDITS.md) records what I remember and what the sources say, and [Gremlin Archive and the Book](docs/GREMLIN_ARCHIVE.md) covers Mark Hardisty's book and archive.

My original development setup and the source-recovery story are documented in [Dorks Dilemma C16](https://github.com/anthonyjclarke/Dorks_Dilemma_C16), particularly its [History and Credits](https://github.com/anthonyjclarke/Dorks_Dilemma_C16/blob/main/docs/HISTORY_AND_CREDITS.md). This project adapts the disk reader, source converter, build and documentation tooling from that work and [Tycoon Tex](https://github.com/anthonyjclarke/Tycoon_Tex_C16). The addresses, assets and validation results here belong to Xargon's Revenge.

---

## Learning, Modification, and Ports

[Codebase Analysis](CODEBASE_ANALYSIS.md) traces the actual routines, state, timing and modification constraints. [Illustrated Graphics](docs/GRAPHICS.md) reconstructs the ship, all alien variants, terrain and effects from preserved data. The [Porting Guide](docs/PORTING_GUIDE.md) proposes separate derivative, emulator-hosted and native routes, with explicit compatibility choices and conformance tests. These guides describe future work; no new targets have been implemented.

The [generated code reference](docs/analysis/CODE_REFERENCE.md), [codebase index](docs/analysis/codebase-index.json) and [asset export](docs/analysis/asset-data.json) provide addresses, logical source lines, sizes and provenance.

---

## Tests and Sharing

```sh
make test
make verify
make probes
```

[Testing](TESTING.md) describes the regression checks, emulator evidence and rule probes. [Source and Validation](docs/SOURCE_AND_VALIDATION.md) links the machine-readable reports and retained monitor logs and memory captures, and the preservation release's [GitHub CI result](docs/verification/ci-results.json) is recorded separately from local VICE evidence. The graphics freshness check needs Pillow 10.3.0, the version CI pins.

[Sharing on GitHub](docs/SHARING_ON_GITHUB.md) covers branches, checks and tags. [Rights and Preservation](RIGHTS.md) preserves the historical notices without inventing a licence. Changes are recorded in the [Changelog](CHANGELOG.md).
