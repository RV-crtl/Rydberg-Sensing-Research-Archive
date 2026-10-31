# Poster-ready HFSS text blocks

## Heading
**Programmable metasurface for full-Stokes analysis**

## 55-word version
The V11 MirrorTwist Tetra4 is a single 200×200 mm double-sided PCB containing a centred 3×3 array of mirror-twisted split-ring cells. Two PIN-control bits create four analyser states. HFSS extracts a Jones transmission matrix for each state; the resulting four power projections form a Stokes instrument matrix, P = A S.

## 35-word version
Four PIN-selected metasurface states are designed to span the Poincaré sphere. HFSS converts each state’s Jones transmission into a Stokes analyser row, allowing conditioning, handedness sensitivity and reconstruction noise to be optimized directly.

## Design rationale
V10 increased the number of electronic states but worsened the normalized inversion condition number from 6.72 (V9) to 10.46. V11 returns to the minimum four-state architecture and explicitly targets tetrahedral analyser separation, positive and negative S3 sensitivity, sufficient transmission and low reconstruction error.

## Equation block
For analyser state k:

H_k = T_k^H T_k,    P_k = E^H H_k E

P = A S,    S_hat = A^+ P

where T_k is the HFSS Jones transmission matrix, A is the calibrated Stokes instrument matrix and A^+ is its pseudoinverse.

## Figure caption — unit cell
**MirrorTwist Tetra4 unit cell.** Mirror-related split-ring selectors are patterned on opposite faces of a 1.524 mm RO4350B substrate. Switching the two selector bits produces four polarization-dependent transmission states.

## Figure caption — Poincaré sphere
**Target analyser geometry.** A regular tetrahedron gives the minimum condition number for a four-state Stokes analyser (κ2 = √3), reducing noise amplification in the inversion.

## Figure caption — benchmark
**Design iteration.** V10 remained mathematically rank-4 but had clustered analyser directions and κ2 = 10.46, compared with 6.72 for V9. V11 therefore optimizes four mirror-twisted states directly toward tetrahedral separation and opposite S3 response.

## Status / claim box
**Simulation status:** The V11 geometry and offline mathematical checks pass, but a solved four-state V11 result set is not present in the supplied package. Any V11 S-parameter, field-uniformity or Stokes-performance values should be added only after HFSS produces the four non-empty S4P files and finite-board field export.