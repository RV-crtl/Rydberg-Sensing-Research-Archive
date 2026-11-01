# Australian R&D opportunity and collaboration intelligence

This is the **project-specific** research intelligence folder, separate from the universal [Rydberg Systems Engineering textbook](../book/README.md). It checks the official Australian Research Council (ARC) scheme calendar, Defence technology strategy, government funding pages, Defence Science Institute and Queensland Defence Science Alliance opportunities.

It is designed to reduce missed calls, **not** to autonomously write and submit grant proposals or claim eligibility. All sources are fixed in [official_sources.json](official_sources.json); untrusted URLs and redirects are rejected. Each item stores a documented review date, the original official URL, known historical deadline and specific eligibility caveats. A source's old status is never presented as verified live availability.

## Scheduling and data handling

- [Weekly official-source workflow](../.github/workflows/australian-opportunities.yml): Fridays at 08:15 **Australia/Sydney** using GitHub's timezone-aware scheduler, plus manual run option.
- The workflow obtains an actual HTML response from the approved publisher, saves a short verbatim page context excerpt, reported last-modified header and SHA-256 digest, and creates a dated **human-review issue** plus downloadable Markdown/JSON artifacts.
- Retrieval failure is shown explicitly; a dead source cannot be interpreted as a closed call or a newly opened grant.
- Government pages have higher verification status than unverified social commentary, but **no source** is a guarantee of an applicant's eligibility. Research institutions, nationality, security, IP, partner contributions, deadlines and scheme changes require current official review.
- Application preparation and collaboration outreach must have the researcher's express approval, as well as institutional research-office and Defence-security review if applicable.

## Current source examples, verified on 1 November 2026

- ARC **Industrial Transformation Research Program 2027**, official closing date 25 November 2026 (5 pm AEDT); relevant to research hub/training centre partnerships, not an automatic individual student entitlement.
- ARC **Future Fellowships 2027**, official closing date 6 November 2026 (5 pm AEDT); specific mid-career eligibility applies.
- The **2026 Defence Innovation, Science and Technology Strategy** highlights quantum technology, AI and other priorities. A strategic priority is **not** a grant call.
- QDSA-DIN **Quantum Sensing for Extreme Environments** 2026 call closed on 20 July 2026; monitor a future call rather than advertising the old one as open.
- DSI describes Defence partnership and unsolicited-expression routes; individual calls and restrictions vary. Defence Industry Development Grants generally target eligible SMEs rather than all university researchers.

## Collaborator qualification matrix

For a candidate, require fields: responsible organisation, official URL, verified status/date, geographic/institution eligibility, research capability fit, distinct deliverable, required partners, security/IP sensitivity, funding ceiling and cost-share, supervisor contact route, strategic fit, next action and decision owner. A collaborative idea is a proposal opportunity, not an agreed partnership.

Source-linked opportunities belong under **automation/** and **research_updates/**, not alongside universal textbook physics.

## Optional code-writing AI proposal assistant

The [bounded co-author](AI_EDITORIAL_POLICY.md) can only be invoked manually by the repo owner, after an API secret and model variable are set. It drafts original source in an isolated new branch and raises a human-review PR. The workflow **never autonomously merges, executes its new Python output, submits a funding application or edits original HFSS data**. This review gate is intentional scientific safety, not a missing feature.

## Deadline stale-data guard

The [independent date-and-timezone triage](opportunity_triage.py) evaluates all seeded official opportunities and explicitly classifies expired deadlines as `PAST_RECORDED_DEADLINE`, future source deadlines as `FUTURE_ADVERTISED_DEADLINE_UNVERIFIED`, and undated calls as `REVIEW_CURRENT_SOURCE`. None of those categories guarantees that a funding stream is open or that the researcher qualifies. The CI regression tests include an expired October 2026 grant and a November 2026 future deadline.

Current official examples to review before applying include the [Defence Industry Development Grants Program](https://business.gov.au/grants-and-programs/defence-industry-development-grants-program), whose new guidelines were anticipated for 3 November 2026. The stream-specific rules and eligibility may change; do not use a historic document as a current application form. The [Defence grants portal](https://www.defence.gov.au/about/governance/grants) routes to live GrantConnect opportunities. This is a project-specific intelligence workflow, not part of the general-purpose textbook.
