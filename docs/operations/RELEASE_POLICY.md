# Research integrity and external release policy

**Default assumption:** this archive is a *research handover*, not a blanket public-redistribution licence.

1. **Scientific modality:** keep experimental data separate from simulated HFSS outputs, analytical tests and statistical assumptions.
2. **Provenance:** do not regenerate plots from illustrative values. Retain real source exports, solver settings, checksums, derivative scripts and figure mappings.
3. **Permissions:** confirm institutional IP, research group approval, photographer permissions, IEEE author posting rules and third-party code/template licences before making a public repository.
4. **Privacy and supply chain:** private receipts, serial numbers, personal contact information, contractual quotations and commercially sensitive project communications belong in access-controlled storage.
5. **File sizes:** if complete `.aedt` projects or large raw RF streams are added later, use Git LFS or release artefacts; keep a SHA-256 index and stable download/preservation location.
6. **Licensing:** no blanket MIT/Apache/Creative Commons licence is assigned here because ownership of every scientific/code/media asset is not established. Seek permission, then add compatible per-path licences.
7. **Releases:** use immutable tags, a signed release note, and save the output of `python scripts/verify_archive.py`.

The current package contains manuscripts, lab/presentation files and a third-party publisher template; review redistribution rights before opening a public fork. This policy prevents accidental oversharing without reducing the fidelity of the handover.

## GitHub Pages

The [`pages.yml`](../../.github/workflows/pages.yml) workflow is **manual by design**. After copyright, privacy and research-IP approval, enable **GitHub Pages → Source: GitHub Actions** in repository settings and dispatch the workflow from Actions. It deploys the repository's root so all relative links resolve; because Pages artefacts contain the full repository, do **not** run this action for confidential content or in an uncleared repository.
