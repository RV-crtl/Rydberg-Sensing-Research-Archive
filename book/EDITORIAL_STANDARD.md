# Editorial standard — route to a publishable Rydberg graduate textbook

**Status:** first substantial draft, 1 November 2026. The original 1,033-page workbook is **not** evidence that 1,000 original textbook prose pages exist. A publisher-grade monograph requires scientific editorial work beyond a long page count.

## Required editorial criteria for each finished chapter

1. **5,000–10,000 substantively unique words**, organised as a structured learning progression from fundamental physical intuition through derivations and limiting cases. These are target word counts, not automatically achieved.
2. **At least 3 original, technically accurate, accessible figures** with full alt text, source traceability and independent visual review. A source photograph must actually show the labelled apparatus. Use vector concept diagrams for abstract physics, not stock/random visual decoration.
3. **At least 10–20 varied questions with separate full derivations**, plus conceptual misconception checks, numerical calculations and open-ended research-design tasks. Variation of one formula's parameters is *not* a unique graduate learning objective.
4. **Citations close to factual claims**, supported by original research papers, authoritative monographs or official numerical API documentation. Verify title/DOI, versions, sign/phase conventions and whether a claim is measured, simulated or only theoretical.
5. **Two independent technical reviews** when feasible: subject-matter scientist plus pedagogy/editorial reviewer, with a reproducible corrections/errata ledger. An AI review alone does not count as independent scholarly peer review.
6. **Code and mathematics checked against independent limits**, with exact units, numerical convergence, test environments, source links, errors/uncertainty and licence review.
7. **Research generality**: the main exposition must apply beyond one user's current Rb-87 HFSS project. Project cases belong in the project's own docs and research evidence.

## Actual and target maturity

| Deliverable | This edition | Publication target |
|---|---|---|
| Original conceptual chapters | **36** | Expand and peer-review each |
| Conceptual prose | **Tens of thousands of words**, see [machine-readable metrics](../site/data/book-catalog.json) | At least 180,000–300,000 original words for an extensive graduate treatise |
| Q&A | Original end-of-chapter explanations + 1,000 parameterised numerical exercises | 10–20 distinct, full derivation answers/chapter, proof-checked |
| Original diagrams | Initial source-linked original SVGs | 3+ per chapter, reviewed for physical correctness |
| ARC/RydIQule practical science | Real scripts with offline tests, actual-package run optional | Fully reproduced state/temperature/field cases and source archives |
| Reference accuracy | Core bibliography and primary source links | Full checked journal/monograph metadata and citations per section |
| Print/PDF | >1,000-page worked problem *workbook* automatically generated | Separate coherent monograph volume and exercise/solution manual |
| Scientific review | Automated source/math checks | Human expert review, rights review, errata and publishing QA |

## What the build verifies and what it cannot

GitHub CI checks chapter-to-web parity, source links, basic formula tests, original research integrity, and PDF page count. It cannot guarantee scientific novelty, mathematical completeness or accuracy in every derived equation. A model-generated source contribution is a draft with a GitHub PR requiring human approval; it is not certified original experimental evidence.

## Editorial expansion plan

**Volume I:** quantum mathematics, angular momentum, atomic spectroscopy and coherent/open-system dynamics. **Volume II:** Rydberg energy levels, quantum defect, Stark/Zeeman, EIT/AT, optical laser technology and sensor calibration. **Volume III:** RF electromagnetism, polarimetry, finite fields, metrology, device fabrication. **Volume IV:** tweezers, blockade, cavity QED, interacting arrays, molecular physics and ionisation. **Volume V:** experimental construction, inference, reproducibility, interdisciplinary applications and comprehensive advanced problems.

For each volume, do an independent accuracy audit before incorporating current journal claims into permanent background prose. Never present placeholders, repeated exercises, auto-generated commentary or zero-source figures as publication-ready material. Track open issues in GitHub. 

## Focused deep-reference expansion (1 November 2026)

Added three original cross-platform field guides: [experiment design from zero](field-guides/COMPLETE_EXPERIMENT_DESIGN.md), [ARC/RydIQule computational verification](field-guides/ARC_RYDIQULE_MODEL_VERIFICATION.md), and [universal fault isolation](field-guides/UNIVERSAL_DIAGNOSTIC_ATLAS.md). These increase real educational coverage without pretending that 36 chapters have been fully developed into a peer-reviewed publisher manuscript. The existing editorial audit continues to report deficiencies in core chapters. A publisher-grade expansion requires sustained subject-specific original derivations, independent scientific review, visual inspection, rights/licence checks, and a complete errata and citation verification cycle.
