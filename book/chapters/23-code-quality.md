# Scientific software engineering and reproducible computing

**General graduate research textbook.** Cross-disciplinary methods; the original user's experiment histories remain in separate project evidence and research folders.

## Learning objectives

Develop reproducible scientific methods, diagnose invalid conclusions and plan experiments with independent verification and proper uncertainty models.

## 1. A scientific program is a model with a provenance chain

Code is one component of an experimental claim. A reproducible result also needs the exact data, model assumptions, units, package versions, numerical tolerances, hardware/solver environment and output transformation. A script that plots an attractive spectrum without identifying whether its input was measured, simulated or fabricated teaching data is not publication-quality science. Keep the status of each object explicit through filenames, metadata and machine-readable manifests.

## 2. Architecture and separation of concerns

Separate physical constants, model equations, data ingestion, numerical solvers, calibration, plotting and reporting. Pure functions with explicit parameters are easier to test than scripts that mutate global state or rely on the current working directory. An ARC transition table and a RydIQule density-matrix solver should communicate through a clearly defined state/parameter structure, not silent column order and floating-point unit conventions. Type checks and unit libraries reduce accidental mistakes but do not replace physical validation.

## 3. Verification at several levels

Unit tests verify formulas against analytic limits; integration tests verify interfaces; regression tests compare known model cases; source-integrity tests verify preserved raw files; acceptance tests compare simulation and measurement. In a three-level EIT example, test coupling-off and weak-probe limits before full Doppler integration. In an RF inverter, test rank-deficient and extremely ill-conditioned matrices, as well as sign conventions and physicality. A passing test means the tested claim passed, not that all of nature was simulated.

## 4. Numerical convergence is distinct from software correctness

A correct implementation may solve a physically inadequate model. Verify truncation with increased atomic states, velocity classes, mesh elements, spatial sampling and solver tolerances. Check floating-point stability, complex phase and cancellation when a small observable is calculated from large terms. Reproducibility requires recording convergence metrics and source hashes, not merely publishing final PNG files.

## 5. Continuous integration and CI boundaries

Automated jobs can build the handbook, lint code, run numerical fixtures, regenerate figures and check links. They should not download arbitrary untrusted code and run it with write access to confidential data or credentials. A model-generated patch should enter a reviewable pull request with tests and source citations; automatic merge of unverified physics or security-sensitive repository changes is inappropriate. Protect the immutable original research evidence separately from mutable educational documentation.

## 6. Scientific figure standards

Every figure needs a descriptive caption stating the observable, physical units, source provenance, parameter regime, uncertainty and meaning. Avoid using random stock pictures for specialized instruments. Use vector diagrams for concepts and native source links for actual experimental apparatus or solver curves. Explicitly label a model's idealized spectrum as such; a generated curve must not be relabeled as a measured Rydberg receiver.

## 7. Handover and archive strategy

Design the repo so a successor can locate raw runs, figures, scripts, instrument/solver settings and current conclusions quickly. A current-result portal should state which versions supersede old proposals while retaining failed cases. Archive README navigation and change logs should have stable links and avoid hard-coded counts that become stale. A library discovery index does not mean all originals have been imported; track verified byte-level status and checksum.

## Questions and complete explanations

### Question 1. What is the difference between unit and acceptance tests?

<details><summary>Reveal reasoning</summary>

Unit tests check formulas/software components, while acceptance tests check predeclared physical or product criteria under realistic conditions.

</details>

### Question 2. Why do code tests not prove the physics is right?

<details><summary>Reveal reasoning</summary>

They validate selected software behaviors; missing states or wrong apparatus assumptions can remain.

</details>

### Question 3. Why preserve raw and derived data separately?

<details><summary>Reveal reasoning</summary>

Derived figures may lose phase, error or processing history needed for independent review.

</details>

### Question 4. What makes a reproducible numerical figure?

<details><summary>Reveal reasoning</summary>

Original source, units, code, environment, parameters, exact run ID and a validation protocol.

</details>

### Question 5. Why shouldn't AI-generated research patches auto-merge?

<details><summary>Reveal reasoning</summary>

Code and claims may be wrong, unsafe, uncited or scientifically unverified despite passing generic syntax checks.

</details>

### Question 6. How should a historical project archive indicate the current best result?

<details><summary>Reveal reasoning</summary>

A dated evidence-status portal with source-linked most recent verified cases and superseded/failed lineages.

</details>

## Advanced research assignment

Choose a real published experimental or computational method. Create a reproducibility checklist, data/provenance manifest, independent limiting-case test and a claim-to-evidence table. Include a realistic failure case and a diagnostic remedy. Distinguish your own numerical illustration from any published measurement.

## References

Consult [the annotated bibliography](../REFERENCES.md) and discipline-specific journal, instrumentation and software primary sources. Rights to source images and datasets must be checked before release.
