# Rydberg Systems Engineering — the open research handbook

**Atomic physics · Optics · RF · Rydberg electrometry · Metasurfaces · Scientific computation · Troubleshooting**

This is an original, evolving research handbook authored to accompany the [actual Rydberg RF sensing archive](../README.md). It connects first principles to the user's 780/480 nm Rb-87 receiver, historic field/Zeeman studies, six-state HFSS Stokes analysis and evidence-status decisions.

**Current coverage, 1 November 2026:** 24 conceptual chapters, 1,000 deterministic worked numerical practice cases across 20 mathematical themes, a browser-based reader/quiz/workbench, source-linked original figures, tutorials and a latest-versus-historical research ledger. **It is not yet 1,000 pages of written textbook prose.** The educational workbook has 1,000 separately addressable problems, not a 1,000-page scholarly textbook; expanding to that substantive prose length is an editorial project and requires ongoing scientific peer review.

## Reading path (concept → use → diagnose)

| Part | Chapters | Purpose |
|---|---|---|
| I. Mathematical and quantum tools | [01–04](chapters/01-mathematical-language.md) | Vectors, operators, Hamiltonians, density matrices |
| II. Atomic and Rydberg properties | [05–07](chapters/05-angular-momentum.md) and [13–16](chapters/13-quantum-defect-and-arc.md) | Selection rules, quantum defects, Rb-87 laser access, ARC, RydIQule, Zeeman, Doppler |
| III. Optical RF receiver | [08–09](chapters/08-eit-and-autler-townes.md) and [17](chapters/17-spectroscopy-diagnostics.md) | EIT, Autler–Townes, optical alignment, false-peak controls |
| IV. Microwave and polarisation | [10–12](chapters/10-microwave-fundamentals.md) and [18–22](chapters/18-hfss-metasurface.md) | Antennas, Jones/Stokes, inverse problems, HFSS, finite aperture and information metrics |
| V. Research engineering | [23–24](chapters/23-code-quality.md) | Scientific software, source evidence, novelty and publication |
| VI. Project implementation | [Current state and technical lineage](CURRENT_STATE.md) | Latest evidence, older superseded studies, remaining gates |
| VII. Labs and solutions | [Tutorials](TUTORIAL_LABS.md) · [1,000-case workbook](workbook.mjs) | Repeatable hands-on examples, self-tests and parameter sensitivity |
| VIII. Bibliography | [References](REFERENCES.md) | Peer-reviewed scientific papers, books, official APIs and original project evidence |

Open the [**interactive textbook and worked quiz**](../site/academy.html) and [**parameter explorer/code lab**](../site/lab.html). The website contains original drawings and references to authentic project research photos; never confuse teaching graphics with actual laboratory photographs or HFSS native output.

## Research method and signs of a good chapter

Every chapter should answer: (1) what system is studied, (2) which variables and units are used, (3) how the equations arise, (4) what observable is actually measured or computed, (5) which experiment or solver case can falsify a claim, (6) the most frequent diagnostic failures, (7) review questions with answers and (8) a citable source.

**Explicit scientific limitations:** A project-specific six-state HFSS instrument matrix is not a functioning, fully calibrated Rb-87 four-coordinate optical polarimeter. The earlier linear analyser probes equatorial Stokes coordinates, and finite-panel local-field transfer still needs verification.

## Contribution and safety

Use original prose, authored SVG diagrams, public reference links and sources from our existing research repository. Do not copy a textbook's copyrighted chapter or redistribute licensed figures. The repository is currently **public**: do not commit private lab credentials, personal correspondence, unpublished proprietary designs, quote details or unapproved raw data. Actual laser, RF, electrical, vapour-cell or PCB work requires lab-specific safety approvals and skilled supervision.

[Source-status policy](../docs/traceability/RECORD_STATUS_POLICY.md) · [Research assistant](../scripts/research_assistant.py) · [Research updates](../docs/literature/) · [Complete source archive](../history/README.md).
