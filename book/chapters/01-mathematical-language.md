# Quantum mathematics without mysticism

**Book:** Rydberg Systems Engineering · **Part:** Foundations · **Status:** original educational text, not new experimental evidence.

## Why this matters in our project

State vectors encode complex amplitudes, not directly observed voltages. A basis {|g⟩,|e⟩} lets us write |ψ⟩=a|g⟩+b|e⟩, |a|²+|b|²=1. Inner products determine probabilities, and a global phase cannot change any measurement. A relative phase can change interference and RF polarisation. Distinguish a Hilbert space dimension from the number of experimentally distinguishable signal channels.

## Worked problem / research exercise

Start with |ψ⟩=(|g⟩+i|e⟩)/√2. The excited-state probability is 1/2, while an X-basis measurement also probes relative phase. Calculate ⟨σ_y⟩=+1 under σ_y=[0,-i;i,0]. A global factor exp(iφ) cancels in every expectation value.

## Lab / solver decision checklist

- Record relevant units, basis, frequency, coordinate frame and exact source version.
- Calculate the expected limiting-case behaviour before running expensive software.
- Keep the experimental or solver-native result separate from a numerical illustration.
- Test at least one independent reference, off-state or convergence criterion.

## Questions (attempt before opening the answer)

**Q. For a state a|g⟩+b|e⟩, why does multiplying both coefficients by exp(iφ) not change the probability of finding |e⟩?**

<details><summary>Reveal worked answer and explanation</summary>

Because |b exp(iφ)|²=|b|². A common phase cancels, but an a-to-b phase difference affects observables in another basis.

</details>

**Advanced discussion.** State the approximations used in the section, which observable could falsify the current explanation, and which source data you would need to validate a stronger claim. Compare this against the relevant source below.

## Troubleshooting pitfall

Confusing a coherent amplitude with measured intensity; using degrees directly inside sin/cos; silently changing basis order.

## Source and extension

Gallagher, Rydberg Atoms (Cambridge University Press, DOI 10.1017/CBO9780511524530). [Read the central book reference ledger](../REFERENCES.md). [Return to the syllabus](../README.md).
