# Manufacturing and fabrication record

Engineering design work has included etched double-sided copper polariser structures, Rogers and FR-4 substrate considerations, RF PCB dimensions, artwork and finite-aperture constraints. The imported IEEE manuscript contains a simulation-based two-face switching geometry and its solver figures.

## Fabrication traceability

| Field | Evidence path / recording requirement |
|---|---|
| Board purpose and geometry | Manuscript `main.tex`; HFSS geometry source JSON; historical PCB design notes |
| PCB material and stack-up | Record substrate batch, thickness, εr, copper thickness and manufacturer datasheet |
| Artwork and manufacture output | Save Gerber, drill, stack-up, pick-and-place, assembly drawings, panel revision and fabrication DFM correspondence |
| Manufacture order | Supplier quote, purchase order, invoice, proof of delivery and board photos if available |
| Assembly/inspection | Board IDs, assembly revision, microscopy, shorts/continuity, photos and dimensional results |
| RF measurement | VNA calibration, S-parameters, instrument settings and fixture configuration |

**Current imported evidence** documents design and electromagnetic modelling. It does **not** establish an order for fabrication or a completed final PIN-diode metasurface. Formal manufacturing orders, factory certificates and inspected physical PCB records still require source import if they exist.

The high-value continuation path is to lock a validated geometry and electrical switch model, generate manufacturing outputs with a reproducible BOM and DFM check, then link each built serial number to the corresponding simulation/measurement evidence.
