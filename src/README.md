# Source Workspace

## Preservation Assembly

I generate readable assembly from the original modules with `python3 scripts/restore_c16.py`. The editable working output is `build/xargon.s`; the original module and logical source-line mapping is `build/xargon-source-lines.json`. Listings, labels, maps and debug data sit beside it. Editing generated assembly does not change the next preservation build.

The active source is the two read-only D64 images plus six explicit 1992 fallback modules. `config/c16.cfg` preserves the original allocation origins. `config/terrain.cfg` builds the editable terrain separately for comparison. The standalone loader-selected assets remain authoritative for this preservation target.

---

## Future Changes

I have not created a variant target. Before modifying the game, I would create a separate source tree and target with its own expected hashes and tests. The preservation target must retain original operands, source order, data and object equality. See [Source Inventory](../docs/SOURCE_INVENTORY.md), [Build and Run](../docs/BUILD_AND_RUN.md) and the [README](../README.md).
