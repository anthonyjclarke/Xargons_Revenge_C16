# Xargon's Revenge – Modification and Porting Guide

## Scope and Baseline

I would start a derivative from the source and object-listing revision documented in this repository. The preservation target remains unchanged: its 8,094 object bytes must match, its loader-selected assets remain explicit and its PRG hash stays fixed. This guide proposes future work. No native backend, variant build option or portable game engine exists here yet.

The [Codebase Analysis](../CODEBASE_ANALYSIS.md) explains the implementation, and the [Graphics Guide](GRAPHICS.md) describes reusable data. I would keep a behaviour decision log in a future variant rather than editing historical sources or weakening the restoration tests.

---

## Three Different Development Routes

### Same-Platform Derivative

I would add an authored source tree and a separate build target. It could reuse the converter, extracted data and linker conventions, but would have independent expected hashes and tests. The preservation target would continue building only from the original disks and six documented fallbacks.

On the C16 I would budget zero page, stack, work buffers, glyph RAM and raster cycles before adding anything. There are only 98 padding bytes between the object region and font, and they are not a complete free-memory budget. Writable operands, alternate entries, screen-code collision and table adjacency all remain constraints. Moving a routine can alter branches, dispatch offsets and raster timing even when its logic is unchanged.

### Emulator-Hosted Version

I would keep the original machine execution and build a host interface around it. The host would select PAL C16 and 16 KB RAM, wait for reset, load the saved-address PRG and enter `$1800`. It would map normalized host controls onto the C16 matrix or joystick interface, scale pixels and expose snapshots without pretending the game is a native engine.

I would keep the original compressed PRG launch separate because it begins at `$100D` and unpacks itself. Browser or embedded emulator selection would need its own licensing, ROM distribution, timing, audio and input review. This repository does not currently provide such a host.

### Native Reimplementation

I would extract the model and rendering rules, then implement them independently with explicit compatibility choices. A host sprite API alone cannot preserve this game: collision reads character codes, stars draw conditionally into existing cells, and runtime glyph replacement changes every screen cell using a code.

I would begin with an emulated 40 × 25 cell surface and mutable glyph banks inside the new renderer. That provides an understandable bridge from the original rules. A later renderer could use textures or sprites once the desired collision and overlap behaviour had conformance tests.

---

## Compatibility Choices

| Behaviour             | Preservation baseline             | Deliberate alternative          |
| --------------------- | --------------------------------- | ------------------------------- |
| Alien graphics        | Complete loader-selected `BJH`    | Shifted reference pages         |
| Editable terrain      | Loader's `LANDSCAPE-2`            | Editable 29-byte-different art  |
| Starting lives        | Five; three visible icons         | Three as printed on packaging   |
| Fire gate             | Compare whole shifted flag byte   | Boolean press edge or repeat    |
| Zero-fuel subtraction | Wrap to 255 in controlled probe   | Saturate at zero                |
| Full score overflow   | Zero digits; write one to `$0186` | Bounded or wider safe score     |
| Alien collision       | Screen-code intervals             | Rectangles or pixel masks       |
| Alien boundaries      | Left wraps; right clamps          | Symmetric boundaries            |
| Randomness            | TED reads plus four-byte state    | Seeded portable generator       |
| Colour rendering      | Raster-selected TED attributes    | Fixed palette or new artwork    |
| High score            | RAM only; no save file            | Host persistence                |
| Audio                 | Original TED register rules       | Synthesized or sampled effects  |

These alternatives are choices for a future project, not supported switches in this build. I would keep the default source asset choice visible in a port's metadata. The running reference has identical executable bytes but different alien selections at wave indices 4–15; its shifted pages are not proof of intended final artwork.

The source's five lives and the inlay's three are another explicit choice. I would not combine packaging numbers, source code and a few screenshots into an undocumented hybrid. I would also distinguish a safe arithmetic change from an attempt to preserve quirks. The score-overflow write into the stack page is suitable for a conformance test, not a design I would carry into a new host memory model by accident.

---

## Proposed Portable State

I would give a future model an explicit session mode: title, ready, play, paused, dying, wave award, planet award, game over and final choice. These modes would organize the existing flag interactions; they would not imply that the source currently has a single mode variable.

The proposed state would contain player character row and pixel phase, a fixed X footprint, eight score digits or a chosen replacement representation, lives, fuel and refill request, level/sheet/attack counters, one projectile, one pod and sixteen alien slots. Each alien would retain position, pattern cursor, animation bit, explosion phase and active/gone state. Stars would keep their own sixteen positions, speeds and stop groups.

I would preserve a cell surface containing character code and attribute bytes, plus terrain and font banks. I would represent fine-scroll offsets and the five raster bands explicitly. Temporary scratch pointers would become local variables only after proving that no important aliasing or entry-point assumption had been lost.

A compact proposed snapshot could use a versioned JSON envelope:

```json
{
    "schema": "xargon-state-1",
    "compatibility": "source-obj-bjh",
    "tick": 120,
    "mode": "play",
    "player": {"row": 7, "phase": 3},
    "score_digits": [0, 0, 0, 0, 0, 0, 0, 0],
    "lives": 5,
    "fuel": 111,
    "sheet": 0,
    "level": 0,
    "input_trace": "fixture-001"
}
```

This is a proposed interchange format, not an implemented save file. Full fixtures would also contain arrays, cell memory, glyph changes, random/TED-read inputs and phase information. I would not compare only the fields shown in this small example.

---

## Proposed Backend Boundaries

I would keep model stepping separate from a display backend that accepts cell writes, glyph changes, fine-scroll values and band palettes. A timing backend would supply the ordered service phases, an input backend would produce normalized controls and original-style flag history where required, and an audio backend would accept timed TED-register events or named effect commands.

A randomness interface would expose each original hardware-derived read needed by the selected compatibility model. A persistence interface would be optional because the historical game has no durable save system. A trace sink would record both model changes and the rendering memory read by collision.

I would initially keep memory-oriented adapters for original routines such as `ALIDEF`, `SCORE` and `SHOTFL`. These provide small reference tests. I would not expose every assembler label as an API; many are branch targets, data, mid-routine entries or nonlocal stack paths.

---

## Timing and Input

The five raster phases, frame-boundary polling and busy waits must be translated separately. Alien foreground work waits through `RUSRAS`, while ship, fuel, projectile, terrain, stars and sound are distributed through the interrupt services. A single arbitrary delta-time update would change ordering and potentially collision, resource use and sound.

I would first model an ordered PAL frame with the same service sequence and a separately scheduled foreground step. I would record how many foreground iterations occur rather than assuming exactly one. For an emulator-hosted route I would preserve machine timing directly; for a native route I would choose and test a fixed scheduling contract before optimizing it.

Input normalization needs more than left/right/up/down booleans. The original player only moves vertically. `JUP`, `JDOWN` and `JFIRE` are rotated history bytes tested on bit 7, and firing compares the whole `JFIRE` byte with `OLDFIR`. Controlled probes show that `$80` and `$C0` are meaningfully different even though both have the high bit set. A future boolean edge detector would be a deliberate behaviour change.

I would record original matrix/joystick reads and the resulting flag bytes for press, hold, release, simultaneous directions and both port selections. Manual keyboard mapping, real joystick behaviour and a complete input cadence trace remain open work here. Space/G pause/resume and Escape abort also need host tests.

---

## Coordinates, Collision and Rendering

The ship uses a character row and a pixel phase, with a four-by-three-cell footprint. Aliens use two-by-two cells. Stars use four horizontal subpositions per character. Fuel uses horizontal units divided by four for the cell and a low-bit phase to choose artwork, plus vertical pixels divided by eight. These coordinate domains should have named conversions rather than one vaguely defined X/Y pair.

For the first implementation I would preserve source update order and cell writes. I would keep collision against the same numeric intervals: fuel contact 179–185, lethal values 186–220, and effects at 221 and above ignored by the ship test. Alien hit detection looks for laser code 63 in the cells being printed. The star renderer also reads existing cell codes before drawing or erasing.

Only after this worked would I separate collision entities from visible characters. I would then compare trace fixtures around overlapping aliens, a laser crossing an alien, fuel collection, erasure and screen edges. A pretty matching frame is insufficient if the old screen cells produce different collision decisions on the next update.

The renderer needs mutable glyph data. `PRSHIP` rebuilds twelve glyphs, fuel uses six, laser uses one, terrain animation replaces two, `TVPIC` alters terrain bytes, and alien/explosion setup replaces a runtime font region. The 16 KB machine also mirrors the RAM interrupt vectors into the font tail; a memory-compatible backend must account for that alias. Bank-address placement can become logical asset IDs on a native host, but the shared-code effects must remain intentional.

---

## Assets, Audio, Randomness and Persistence

I would consume the documented JSON data and verify its hashes before converting it into a new asset format. Multi-byte table pointers are little-endian; movement streams use `$FF` terminators; packed title bytes contain two nibble codes. Character bytes are eight rows per glyph, and multicolour uses four two-bit pairs widened horizontally. Ordinary aliens use hires attributes, while the ship and many effects use multicolour.

The exported explosion samples come from the unchanged original `CALEXP` routine under recorded TED state. They are useful fixtures, not a unique canonical explosion animation. A native port could replay captured masks for a test or implement the original masking rule with a controlled hardware-read stream. It should not quietly label one random sample as the entire effect.

For audio I would first log register writes with service phase and cycle/frame context, then implement the two TED voices, noise selection and volume rules or choose a replacement sound design. I would test the low-fuel channel alongside firing, collection and death because the effect state shares bits and register fields. The current automated checks disable audio, so a listening review is still needed.

A four-byte random seed does not capture direct TED reads or the carry state entering every routine. I would use an explicit hardware-read fixture stream for exact tests, and a separately specified generator for ordinary native play. Terrain rejection of the last motif and weighted `LOOKUP` colour choices should be included in that contract.

The original high score lives in `TPBUFF` RAM. Host persistence would need a format, validation, migration and reset policy. I would preserve original copyright and publication notices, and establish rights separately before distributing a new game or embedded ROMs.

---

## First Playable Slice and Milestones

I would make the first playable slice a fixed first-wave scene: draw the HUD and original landscape, move the ship vertically using source phases, fire one projectile and hit one stationary alien. I would use the original `BJH` frame bytes and keep screen-code collision initially. Fuel could be fixed for that slice, clearly identified as temporary development behaviour.

Next I would add ordered raster-style phases, procedural terrain, stars and a sixteen-slot alien wave. I would then add pod movement, fuel drain and refill, scoring, explosion generation and death/restart. Completion, planet awards, high score and the final restart/end choice would follow, with traces for each transition. Audio, host input refinement, persistence and presentation would come after model comparisons were stable.

Each milestone would leave the preservation target passing unchanged. A native target would have its own fixtures and compatibility identifier. I would not expose unfinished ports as options in the historical launcher or imply that a proposed target already builds.

---

## Trace and Conformance Tests

I would use JSON Lines for event traces, with schema version, compatibility choice, frame, service phase, event type and named fields. Binary memory fixtures would carry a start address, length and SHA-256 in an adjacent JSON manifest. Asset tests would record source module/line or disk filename and input hash. Trace timestamps would be logical phase counters, not host wall time.

The first conformance set would replay the existing `ALIDEF`, score and fuel observations. It would add fire press/hold/release history, ship boundaries and phase transitions, cell-code collision boundaries, all movement pattern terminators, quota/regeneration limits, fuel-pod collection, high-score ties and the first completion/death transitions. I would explicitly test `SCORE+2` and other alternate-entry conventions before replacing them with native functions.

For pictures I would compare glyph indices, attributes and band scroll state before comparing RGB output. The decoded diagrams use an explicit VICE colodore TED palette; current startup screenshots use VICE's internal default colours. A palette change must not be mistaken for a model difference. Pixel comparisons would state the chosen renderer and crop.

The remaining work includes manual controls, audible sound, later transitions, complete progression, stack/concurrency review and real-hardware checks. Those limits should travel with any derivative's evidence until the corresponding tests are actually completed.

[README](../README.md), [Testing](../TESTING.md), [Source and Validation](SOURCE_AND_VALIDATION.md).
