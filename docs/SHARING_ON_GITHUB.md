# Sharing on GitHub

## Repository and Releases

I authorised public publication at [anthonyjclarke/Xargons_Revenge_C16](https://github.com/anthonyjclarke/Xargons_Revenge_C16). The verified preservation release is `v1.0.0`; documentation, analysis, graphics and the handbook are released as `v1.1.0`. Each release uses an annotated tag. I never move a published tag; any later correction needs a new version.

The changelog records the release's commit reference and tag. I resolve a tag to its exact commit with:

```sh
git rev-parse 'v1.0.0^{commit}'
git rev-parse 'v1.1.0^{commit}'
git ls-remote --tags origin
```

---

## Publication Checks

I run the build, historical-input tests, both PlatformIO environments and byte comparisons before publication. The GitHub Actions workflow repeats those checks. Once the handbook is present it also checks generated analysis and graphics freshness, Markdown links and the handbook tests. It does not run graphical VICE verification; the retained local evidence records that separately.

For a future release I review `git status`, run the relevant checks, update `CHANGELOG.md`, commit with a `type(scope): description` message, create a new annotated tag and push the branch and tag. I inspect the actual Actions result for that commit and report it separately from local checks. A successful local build is not a GitHub CI pass.

Historical inputs and intentional documentation fixtures stay in Git. Generated build products, caches and scratch work do not. I keep the checkout alongside the HTML when following source-file links. [Rights and Preservation](../RIGHTS.md) explains the notices; public hosting does not add a licence.

[README](../README.md).
