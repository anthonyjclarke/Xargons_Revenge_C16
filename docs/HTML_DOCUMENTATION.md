# Maintaining the Offline Handbook

## Source and Output

I edit the Markdown, not `docs/XARGONS_REVENGE.html`. `docs/handbook.json` defines the chapter order: history, artifacts, quick start, build, testing, validation, analysis, graphics, porting, then reference and maintenance. The generator uses the existing Tycoon Tex implementation and reader templates, adapted for this game.

```sh
make docs
make docs-html
make docs-watch
make docs-check
make test-docs
```

`make docs` refreshes the preservation build, static analysis, graphics and HTML. `make docs-html` rebuilds only the reading copy. `make docs-watch` polls the Markdown, images, templates and relevant directories for changes. `make docs-check` regenerates analysis and graphics in temporary directories, compares expected outputs, checks local document links and requires the saved handbook to match all current input hashes. It does not rerun VICE. `make test-docs` checks navigation, image embedding, determinism, staleness rejection, broken links, raw HTML escaping and watch mode.

I use Python 3.9 or later with Pillow 10.3.0 for the recorded graphics, and Node 22 or later for the reader. `scripts/vendor/` pins Marked 17.0.5 and Mermaid 10.9.3 and retains the [Marked licence](../scripts/vendor/MARKED-LICENSE.md) and [Mermaid licence](../scripts/vendor/MERMAID-LICENSE). There are no runtime CDNs.

---

## Offline Reading and Source Links

The HTML embeds images, styles, reader controls, diagram renderer and library licences. Chapter links remain internal. Search filters chapters by their text; image enlargement opens a local dialog. Print controls expand sections and use the print stylesheet. A content-security policy blocks network connections and remote media.

I can copy the HTML alone to read its embedded content without internet access. To follow links to source files, JSON data, the evidence ZIP, the original PDF or Markdown, I keep the repository directory alongside it in its original structure: the HTML remains under `docs/`. External repository and project links naturally need a connection.

The embedded provenance block records input SHA-256 hashes and a digest, not a build timestamp. A Markdown, image, template, renderer or configuration change makes the handbook stale. Current local file links and Markdown section anchors must resolve; broken current links fail generation. Original commissioning text and preserved source files are linked as repository material, not interpreted as build instructions.

---

## Browser Checks and Limits

The browser review should inspect the reading copy at desktop and narrow widths and in print layout. It should check internal navigation, Mermaid completion, image decoding, chapter search, enlargement, overflow and offline network requests. The in-app browser blocked the local `file://` preview under its URL security policy, so those runtime and layout checks remain pending. I have not worked around that policy or reported a browser pass. Static Node tests and freshness checks complement that inspection; neither alone proves that a browser rendered the page correctly.

The [browser check report](verification/browser-checks.json) records the blocked preview and the completed static checks. CI repeats generator tests and freshness checks, but does not claim a graphical VICE run or manual gameplay test. [Testing](../TESTING.md) separates those scopes.

I add a new authored chapter to `docs/handbook.json` and link it from the README or another current chapter. Generated symbol reference content belongs in the generator. Historical sources, artwork and the original project brief remain unchanged.

[README](../README.md).
