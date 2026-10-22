# Testing

## Regression Tests

```sh
make test
make verify
make probes
```

Ten preservation regression tests cover the PRG header, size and SHA-256; all 8,094 MOS object bytes; exact source priority and the six fallbacks; loader-selected graphics and relocation; the initial input hashes; ZIP contents and the complete catalogue; missing, ambiguous and recursive includes; converter hazards; malformed object records; and malformed or cyclic disk chains.

Three additional analysis tests check exported banks against original payloads, resolve each wave record to a terminated movement stream, and compare reconstructed player pixels against captured original runtime glyphs.

---

## PlatformIO Agreement

I also built through the direct Python command, shell launcher, Makefile and both PlatformIO environments, then compared the PRG bytes. The release and debug environments use the same underlying build. CI repeats the tests, direct build, both PlatformIO builds and byte comparisons. Local emulator checks are separate from CI; the workflow does not claim to test VICE.

---

## VICE Verification

The VICE check selects `c16pal`, 16 KB RAM, PAL and audio off. Each subprocess has a 45-second timeout and a 100,000,000-cycle limit. It loads the rebuilt saved-address PRG, enters `$1800`, stops at `TITTER` after the title has been drawn, captures the screen and RAM, writes `$80` to the original `JFIRE` flag at its existing `BIT` test, then continues through initialization to `LOOP`. It clears the scripted flag there and records a gameplay screenshot and RAM capture. The assertions require `TITLE = 0` and `LIVES = 5`.

The reference check executes the original BASIC-stub decompressor at `$100D`, stops at `$1800` before the original game's first instruction and saves `$0400`–`$3FFF` for comparison. I also ran that decompressed memory through the same original startup and gameplay entry. No game instructions were patched. The original and rebuilt startup screenshots are in `docs/images/`.

The fire-flag write is scripted state injection. It is not a host Return key press, keyboard-mapping test or joystick test. Capturing a gameplay loop entry is not a play-through.

When VICE or its graphical session is unavailable, `--allow-skip` writes a report with `status: skipped`; otherwise verification fails. Check that field before citing a report. A skip can return zero to a caller that explicitly allows it, but is not a pass.

---

## Rule Probes

I ran 48 isolated observations: all sixteen alien selections in each revision, score crossings at 50,000 and 100,000, eight-digit score overflow, the fuel cap, fuel subtraction from zero and one, and full-byte fire-flag comparisons. The overflow case also places a sentinel at `$0186` and confirms the out-of-range final store overwrites it with one. A caller at `$0300` sets `SEI`, `CLD`, A, X and Y, calls the original routine and stops at `$030B`. Named RAM inputs, A/X/Y values, extra memory writes and complete result captures are retained. Calls run sequentially within each loaded revision, resetting the listed inputs rather than pretending every byte of RAM is independently initialized. Interrupt concurrency, full timing and normal reachability of unusual inputs are outside this experiment.

The source selects all sixteen expected 64-byte `BJH` designs. The reference differs for wave indices 4–15. Both versions give an extra life at the tested score crossings, cap fuel at 111, wrap a forced subtraction from zero to 255 without setting death, and set death when fuel decreases from one to zero. These controlled states do not establish that a zero-fuel firing state is normally reachable.

[Source and Validation](docs/SOURCE_AND_VALIDATION.md) links the JSON reports and evidence ZIP. To replace committed evidence after an intentional rerun, I use `python3 scripts/retain_evidence.py` and review the changes.

---

## Documentation Tests

```sh
make docs-check
make test-docs
```

The first regenerates the analysis and graphics in temporary directories and checks that they, and the saved HTML handbook, match their sources. The graphics comparison is byte for byte, so it needs the Pillow version CI pins, 10.3.0. The second covers the handbook's navigation, embedded assets and failure handling.

---

## Verification Limits

I have not manually tested the keyboard or a physical joystick, listened to audio, verified every transition or scoring path, completed all waves and planets, or tested real hardware. Startup screenshots and a few isolated arithmetic probes cannot stand in for those checks. I have not established why the compressed reference's alien pages differ.

See [Build and Run](docs/BUILD_AND_RUN.md) and the [README](README.md).
