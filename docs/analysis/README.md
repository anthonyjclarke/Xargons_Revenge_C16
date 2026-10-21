# Generated Analysis Reference

## Files and Method

I generate `CODE_REFERENCE.md`, `codebase-index.json`, `asset-data.json` and the indexed SVG atlases with `scripts/analyze_codebase.py`. The [Codebase Analysis](../../CODEBASE_ANALYSIS.md) explains the counts and their limits. Byte ownership comes from ca65 listing program counters; variable sizes come from reservations; direct transfers resolve constant expressions. None of these methods establish complete reachability or a dynamic call graph.

The data export retains raw bytes and provenance. Runtime explosion samples come from original-routine memory captures inside `docs/verification/vice-evidence.zip`, not the running-reference asset. `scripts/render_game_graphics.py` builds the illustrations under `graphics/` and records all input/output hashes in its manifest. [Graphics Guide](../GRAPHICS.md) explains layout, palette and timing limits.

---

## Regeneration and Changes

```sh
make docs
make docs-check
```

I edit the original analysis scripts or authored Markdown, then regenerate. I do not hand-edit generated symbol tables or JSON. `make docs-check` generates reference outputs in temporary directories, compares their bytes and checks the complete HTML against its input hashes. A source change that breaks preservation equality is not accepted as an analysis update.

[Code reference](CODE_REFERENCE.md), [codebase index](codebase-index.json), [asset data](asset-data.json), [README](../../README.md).
