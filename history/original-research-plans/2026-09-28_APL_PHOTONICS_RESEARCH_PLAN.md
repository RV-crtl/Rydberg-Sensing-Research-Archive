> **Archive status: Historical planning document; proposed architecture, literature and potential experiments. Not a completed empirical or HFSS return.**
>
> Source: user's historical research Library file: **APL Photonics paper research plan** (2026-09-28). Imported as original text extracted from the saved research document; embedded sandbox links or old source markers may be inactive. Distinguish *proposed* from verified results. Underlying source JSON/attachments can be separately recovered for exact byte-level archival.

---

# Research plan for the Rydberg–metasurface APL Photonics paper

## The direction I think we should commit to

I think the project should now be reframed from **“find a clever metasurface that enhances the Rydberg signal”** to:

> **A reconfigurable electromagnetic front end that gives a simple, fixed Rydberg vapor-cell sensor polarization diversity and field enhancement, enabling quantitative microwave/RF polarimetry without relying on Zeeman-resolved atomic manipulation.**

That distinction is extremely important.

A passive polarization-selective resonator combined with a Rydberg vapor cell is already established. Anderson, Paradis, and Raithel demonstrated a split resonator integrated with a Rb vapor cell in 2018, obtaining polarization selectivity and an enhancement corresponding to 24 dB in intensity sensitivity. Holloway *et al.* then demonstrated an SRR around a Cs vapor cell at 1.3 GHz with roughly a factor-100 improvement in electric-field measurement sensitivity. More recently, Rydberg electric-field enhancement structures have moved into circular polarization, directional reception, dual-frequency operation, and broadband resonators. So **“Rydberg sensor + resonator + polarization selectivity” is no longer enough for novelty**.

Likewise, **“PIN-diode metasurface that changes polarization” is not enough**. PIN-loaded surfaces have already demonstrated switchable linear/circular polarization transformations, including broadband multifunctional designs, and a 2026 paper demonstrated a single active metasurface capable of broad arbitrary-polarization control. The publishable intersection that still looks genuinely interesting is:

**programmable metasurface-assisted atomic polarimetry** — where the metasurface is not merely an enhancer or polarizer, but becomes the **measurement basis selector** for a single optically interrogated Rydberg sensor.

That gives us a much clearer thesis question:

> **Can a reconfigurable electromagnetic surface map multiple incident RF polarization states onto the fixed sensitive axis of a simple Rydberg vapor-cell sensor, while simultaneously enhancing the local field, such that the incident polarization state can be reconstructed from a sequence of atomic measurements?**

That is the direction I would build around.

One limitation up front: I cannot actually search your complete ChatGPT conversation history from this workspace; there is no cross-chat history connector exposed to me. I therefore treated what you summarized here—Zeeman biasing having become unattractive, a simple Rydberg setup, and the desire for polarization-sensitive metasurface enhancement—as the current state of the project. I **did** inspect the attached AIP archive directly and performed a fresh literature search around the Rydberg/resonator/metasurface problem.

## What the literature says the novelty has to be

The field has moved considerably further than the first version of this idea might suggest.

| Existing capability | What has already been shown | Consequence for us |
|---|---|---|
| Atomic vector electrometry | Rydberg atoms were used for arbitrary microwave-polarization measurements as early as 2013. | We cannot claim “first Rydberg polarization measurement.” |
| Passive polarization-selective enhancement | A vapor-cell resonator provided enhancement **and** polarization selectivity in C-band in 2018. | A fixed anisotropic resonator is insufficient novelty. |
| Strong SRR enhancement | A 1.3-GHz SRR/Rydberg system improved sensitivity by about two orders of magnitude. | “We added an SRR and got more signal” is insufficient. |
| Circular-polarization Rydberg reception | Recent structures produce circularly polarized directional and omnidirectional Rydberg reception; one reported 14.1 dB enhancement at 2.388 GHz, while another reported a 19.2 dB sensitivity improvement at 2.195 GHz. | Simply converting CP to a locally useful field is now prior art. |
| Multifrequency/broadband enhancement | Dual-frequency enhancement at 1.17/1.74 GHz and a later cascaded broadband cavity have been demonstrated. | Bandwidth or dual resonance alone is not enough. |
| Reconfigurable polarization metasurfaces | PIN-diode metasurfaces already switch among linear/circular polarization functions and transmission/reflection states. | The diode/metasurface by itself cannot carry the novelty claim. |
| General arbitrary polarization control | Active metasurfaces now provide highly general polarization conversion independent of Rydberg sensing. | We need an **atom–surface measurement architecture**, not another converter. |

There is a particularly important 2024 result to take seriously: Ding *et al.* built a circularly polarized Rydberg atomic sensor in which an electromagnetic enhancement structure converts an incident circularly polarized field into an appropriate local linearly polarized field for the atomic sensor. That is conceptually very close to what we were informally discussing.

So I would explicitly abandon the novelty claim:

> “Metasurfaces let a Rydberg sensor detect different polarizations.”

Instead the novelty should become something like:

> **“A programmable electromagnetic interface synthesizes multiple polarization-analysis bases around a single fixed Rydberg vapor-cell readout, allowing full polarization reconstruction while retaining resonant field enhancement.”**

I did **not** find in the literature search I ran a peer-reviewed demonstration that combines a reconfigurable multi-state polarization-analysis metasurface with a single Rydberg vapor cell to perform calibrated full-state polarimetry in this manner. That is not proof that none exists, but it is a substantially better-defined research gap than “Rydberg + metasurface.”

### Why this is also the better APL Photonics story

APL Photonics explicitly seeks work representing significant breakthroughs or novel understanding with lasting impact, and explicitly says incremental engineering advances are outside scope. Sensors and quantum photonics are within its stated coverage. That means I would **not** submit a paper whose central result is:

> “Our new SRR gives 18 dB rather than 14 dB enhancement.”

That would look much more like an IEEE antennas paper.

The APL Photonics version is:

> **A new form of programmable RF-to-optical polarization sensing in which a reconfigurable electromagnetic interface transfers the polarization-analysis problem from atomic-state manipulation into a programmable near-field transformation.**

The atoms remain the calibrated RF-to-optical transducer; the surface changes what the atoms measure.

That makes the physics and sensing architecture—not the PCB geometry—the paper.

## The baseline metasurface I would actually start with

This is where I think we can get you unstuck.

I would **not start with PIN diodes**.

And I would **not start by trying to invent a sophisticated metasurface unit cell**.

Start with an intentionally boring structure whose physics we completely understand and that reproduces a known result. Only after that works do we add the feature that creates the paper.

### The baseline ladder

I would treat the electromagnetic design as five successive devices:

| Stage | Device | Purpose |
|---|---|---|
| **B0** | Bare vapor cell | Establish the real field and atomic-response baseline. |
| **B1** | Single passive split-ring / ELC resonator | Reproduce known field enhancement at your \(f_0\); validate the entire EM → atom modelling chain. |
| **B2** | Two orthogonal passive resonant channels | Make \(x\)- and \(y\)-polarized incident fields produce distinguishable enhanced responses. |
| **B3** | Multi-basis passive/ideal-switch model | Demonstrate numerically that combinations of those modes can implement enough independent polarization analyzers to reconstruct polarization. |
| **B4** | Real PIN-diode implementation | Replace the ideal switching with PIN models, bias lines and actual fabrication constraints. |

**B1 is the metasurface design you have been missing.**

Do not ask it to be novel. Its job is to work.

### The B1 geometry

The most defensible starting element is a **strongly subwavelength split-ring or electric-LC resonator whose capacitive hotspot overlaps the Rydberg interrogation volume**.

The resonance is approximately governed by

\[
f_0\approx\frac{1}{2\pi\sqrt{LC}},
\]

so instead of designing against free-space wavelength alone, we have explicit inductive and capacitive knobs:

\[
L \leftarrow \text{loop/path length, trace width, geometry},
\]

\[
C \leftarrow \text{gap width, overlap, loading, cell dielectric environment}.
\]

That is especially useful if your operating frequency is low. Holloway *et al.* already showed why a deeply subwavelength SRR is effective around a vapor cell at 1.3 GHz. More recent work has pushed the resonator-enhancement philosophy into dual-frequency and broader-band architectures rather than requiring conventional wavelength-scale antennas. I would therefore **not force ourselves to build a large periodic “metasurface” if your RF frequency makes that physically stupid**. A loaded resonant surface, small cluster of meta-atoms, or metasurface-inspired resonator may ultimately be the right hardware. The journal will care much more about the sensing capability than whether we can call a \(20\times20\) PCB an array.

### What B1 must optimize

The mistake would be optimizing \(S_{11}\) or far-field gain and calling the job finished.

The Rydberg atoms do not care that your antenna has a beautiful return loss. They care about the **local electric field in the laser–atom interaction volume**.

Define an optical interrogation volume \(V_\mathrm{opt}\), ideally weighted by the probe/coupling beam intensities, and make the principal metric

\[
G_E =
\frac{
\left\langle
|\mathbf E(\mathbf r)\cdot\hat{\mathbf d}|
\right\rangle_{V_\mathrm{opt}}
}{
|E_\mathrm{inc}|
},
\]

where \(\hat{\mathbf d}\) is the RF transition's effective sensitive direction.

Then separately quantify the field nonuniformity,

\[
U_E=
\frac{\sigma_{V_\mathrm{opt}}(|E_\mathrm{sens}|)}
{\langle|E_\mathrm{sens}|\rangle_{V_\mathrm{opt}}}.
\]

That second metric matters because an enormous field in a tiny corner of the cell is not necessarily useful. The atoms sampled by the laser see a spatial distribution of Rabi frequencies or Stark shifts; excessive nonuniformity can broaden or distort the optical spectrum rather than simply increasing signal.

The electromagnetic optimization target is therefore:

> **large \(G_E\), small \(U_E\), correct field orientation, optical access, and manageable \(Q\).**

That is a much better baseline design problem than “make a high-performing metasurface.”

### Then turn B1 into B2

Make a second copy of the resonant channel, rotated by \(90^\circ\), so that the structure has two independently excitable modes:

\[
M_x:\quad E_x^{\mathrm{inc}}\rightarrow
G_x E_\mathrm{local},
\]

\[
M_y:\quad E_y^{\mathrm{inc}}\rightarrow
G_y E_\mathrm{local}.
\]

The important engineering trick is that we do **not merely want two orthogonal hotspots**. Ideally, both channels ultimately generate a strong field component along the **same atomic sensing axis** at the same laser interrogation volume.

In other words, we want the RF structure to behave somewhat like a polarization-diverse antenna feeding a common detector.

That immediately gives the paper an interesting co-design problem:

> How do two different incident polarization components couple into one atomic measurement volume with large and approximately equal enhancement?

That is already more purposeful than inventing an elaborate meta-atom.

## How the reconfigurable version should work

Once B2 exists, the PIN diodes acquire a very specific job: **select the polarization basis being interrogated**.

This is the central conceptual step.

### Stop thinking “polarization converter”; think “programmable analyzer”

Represent the incident field as

\[
\mathbf E_\mathrm{inc}
=
\begin{bmatrix}
E_x\\
E_y
\end{bmatrix}.
\]

For switch state \(k\), the electromagnetic front end implements some calibrated complex projection

\[
u_k=
\mathbf a_k^\dagger
\mathbf E_\mathrm{inc},
\]

and the atoms measure a quantity related to

\[
m_k\propto |u_k|
\]

or, after conversion to an intensity-like quantity,

\[
I_k\propto
|\mathbf a_k^\dagger\mathbf E_\mathrm{inc}|^2.
\]

The exact calibration between spectral splitting/shift and \(m_k\) depends on whether your simple Rydberg setup is operating resonantly through Autler–Townes splitting or off-resonantly through Stark response; the electromagnetic architecture itself does not require us to commit prematurely to one atomic operating regime. Rydberg electric-field measurements have been demonstrated through optical EIT-based microwave coupling as well as off-resonant field-induced level shifts. Now the surface states can implement analyzer bases analogous to conventional optical polarimetry.

A six-state version would be:

\[
H,\quad V,\quad D,\quad A,\quad R,\quad L,
\]

corresponding to horizontal, vertical, \(+45^\circ\), \(-45^\circ\), right circular and left circular analysis.

Then, ideally,

\[
S_0=I_H+I_V,
\]

\[
S_1=I_H-I_V,
\]

\[
S_2=I_D-I_A,
\]

\[
S_3=I_R-I_L.
\]

Now we have a very concrete objective:

> **Build a reconfigurable RF metasurface whose switch states approximate six independent polarization analyzers, each concentrating the selected component into the Rydberg interrogation region.**

This is radically clearer than “design a metasurface for different polarizations.”

And it fits beautifully with the fact that polarization is already routinely manipulated by PIN-loaded surfaces. The reconfigurable-metasurface literature proves the electromagnetic primitives exist; our research contribution would be using them as a **measurement basis generator for an atomic optical sensor**, not merely as a communications polarizer. ### We do not actually need six states initially

Four calibrated states are mathematically enough for the four Stokes parameters.

For example:

\[
H,\;V,\;D,\;R.
\]

An ideal system gives

\[
S_0=I_H+I_V,
\]

\[
S_1=I_H-I_V,
\]

\[
S_2=2I_D-S_0,
\]

\[
S_3=2I_R-S_0.
\]

But I would ultimately prefer six states because the system is not ideal. Then we formulate the real sensor as

\[
\mathbf m=\mathbf A\mathbf S+\boldsymbol\epsilon ,
\]

where

\[
\mathbf m=
\begin{bmatrix}
m_1&m_2&\ldots&m_N
\end{bmatrix}^{T},
\]

\(\mathbf A\) is a **calibrated metasurface–atom measurement matrix**, and \(\mathbf S\) is the incident Stokes vector.

For \(N>4\),

\[
\hat{\mathbf S}
=
(\mathbf A^{T}\mathbf W\mathbf A)^{-1}
\mathbf A^{T}\mathbf W\mathbf m ,
\]

or the corresponding constrained estimator.

That makes one of the most important metasurface design metrics something antenna papers rarely optimize:

\[
\boxed{\kappa(\mathbf A)}
\]

—the condition number of the polarization measurement matrix.

Two designs with the same field enhancement may differ dramatically in their ability to reconstruct polarization. **That is potentially a very nice intellectual contribution in its own right.**

### What the PIN architecture could physically look like

My first candidate would be:

**two orthogonal resonant receiving channels feeding a common high-field sensing region, with switches controlling channel activation and relative electrical path.**

Conceptually:

```text
                     y-polarized mode
                           │
                           │
                     [resonator Y]
                           │
                      switch / phase
                           │
                           ▼
                   ┌─────────────┐
x-polarized mode → │ common RF   │ → enhanced local E along
 [resonator X]     │ hotspot     │   the atomic sensitive axis
      │             └─────────────┘
 switch / phase           │
                          │
                    Rydberg atoms
                  + optical beams
```

The states would evolve approximately as:

| State | X channel | Y channel | Relative phase | Effective analysis |
|---|---:|---:|---:|---|
| A | on | off | — | \(H\) |
| B | off | on | — | \(V\) |
| C | on | on | \(0^\circ\) | \(D\) |
| D | on | on | \(180^\circ\) | \(A\) |
| E | on | on | \(+90^\circ\) | \(R/L\) |
| F | on | on | \(-90^\circ\) | opposite handedness |

PIN diodes are excellent for the on/off pieces. Creating a clean \(90^\circ\) relative phase with only a single diode state may require switched electrical lengths or reactive loading rather than just short/open connections. That should be treated as an electromagnetic design problem rather than assumed.

And importantly, we should simulate this initially with **ideal switches**.

Only after it works electromagnetically do we introduce:

\[
Z_\mathrm{PIN,on}\approx R_s+j\omega L_s,
\]

and an off-state parasitic model of the form

\[
Z_\mathrm{PIN,off}\approx
j\omega L_s+
\left(
R_p\parallel\frac{1}{j\omega C_j}
\right).
\]

Then add the DC bias lines, RF chokes/stubs, vias and finite array. The reconfigurable-metasurface literature shows precisely why the bias network cannot be treated as electromagnetically invisible; sophisticated designs explicitly engineer biasing to avoid ruining the RF response. That is why I strongly recommend **PINs at B4, not B1**.

## The simulation and experimental program

This is the actual work map I would use for the thesis from here.

### Electromagnetic work package

The first full-wave model should contain the **actual vapor-cell geometry**, not just a unit cell in free space.

The sequence should be:

**Bare cell → passive resonator + cell → dual-channel structure → ideal switching → real switches → complete finite prototype.**

For every candidate structure we should save the same dataset:

\[
S_{11},S_{21},f_0,Q,
\]

\[
\mathbf E(\mathbf r,f),
\]

\[
G_E(f),
\]

\[
U_E(f),
\]

polarization selectivity,

\[
\mathrm{PER}
=
20\log_{10}
\frac{|E_\mathrm{desired}|}
{|E_\mathrm{orthogonal}|},
\]

angular response,

and the resulting measurement-matrix conditioning,

\[
\kappa(\mathbf A).
\]

The key design space should be the geometry **seen by the atoms**, rather than only the geometry of an infinite periodic surface.

A useful multi-objective problem is therefore conceptually

\[
\underset{\mathbf p}{\mathrm{maximize}}
\quad
\{
G_E,\,
\mathrm{PER},\,
1/\kappa(\mathbf A),\,
1/U_E
\},
\]

subject to

\[
f_k\approx f_0,
\]

optical-access constraints, fabrication limits and switch/bias constraints.

This gives you a principled answer when a supervisor asks:

> “What exactly are you optimizing?”

We are optimizing **atomic field enhancement and information recoverability simultaneously**.

### Atom–electromagnetic co-model

Do not stop at a COMSOL/CST/HFSS electric-field map.

The RF interaction enters through

\[
\Omega_\mathrm{RF}(\mathbf r)
=
\frac{
|\mathbf d_{rr'}\cdot\mathbf E(\mathbf r)|
}{\hbar}.
\]

So every full-wave field map can be converted into a spatial RF Rabi-frequency map over the laser beams.

For a resonant AT measurement,

\[
\Delta f_\mathrm{AT}
\propto \Omega_\mathrm{RF},
\]

subject to the usual atomic calibration.

The important next step is to spatially integrate the predicted optical response over the probe/coupling overlap rather than simply quoting \(E_\mathrm{max}\).

That lets the paper make a much stronger statement:

> **The metasurface was co-designed against the atomic optical readout, not merely against an RF scattering metric.**

That is exactly the sort of connection that can elevate the work above a straightforward antenna paper.

### The first simulation that should be done

I would literally make the first new project:

**“Single-resonator Rydberg field-enhancement benchmark.”**

It should answer only four questions:

1. Can we place a resonant hotspot at the actual laser–cell interaction volume at \(f_0\)?
2. What enhancement does the real vapor cell permit?
3. How uniform is that enhancement over the optical interaction region?
4. Does the local field point in the direction the chosen atomic transition can efficiently sense?

Once those four are answered, duplicate and rotate that channel.

That is the point at which the “novel metasurface” problem becomes manageable.

### The passive dual-polarization experiment

Before putting a single diode onto the board, demonstrate experimentally:

\[
H\rightarrow\text{strong response channel X},
\]

\[
V\rightarrow\text{strong response channel Y}.
\]

Measure response versus polarization angle,

\[
\theta=0^\circ\rightarrow180^\circ,
\]

and compare

\[
E_\mathrm{atom}(\theta)
\]

to full-wave predictions.

The bare-cell experiment is the control.

This alone tells us whether the front-end strategy works with the real vapor cell and optical setup.

### Then the active experiment

Once switching is included:

1. illuminate the sensor with known polarization states;
2. cycle the metasurface through \(N\) configurations;
3. extract one atomic RF response \(m_k\) for each configuration;
4. construct or calibrate \(\mathbf A\);
5. reconstruct \(\mathbf S\);
6. compare against the known polarization;
7. repeat over amplitude, frequency and incidence angle.

The killer figure would be measured input and reconstructed states on a **Poincaré sphere**.

For example:

```text
Known RF polarization
        ↓
 reconfigurable
 RF metasurface
        ↓
 enhanced fixed-axis
 local electric field
        ↓
 Rydberg vapor cell
        ↓
 optical EIT spectrum
        ↓
 {m1,m2,...,mN}
        ↓
 calibrated inversion
        ↓
 reconstructed
 (S0,S1,S2,S3)
```

That is a paper.

### Provisional go/no-go metrics

These should initially be treated as **engineering targets**, not claims about what APL Photonics mandates.

| Metric | Initial target |
|---|---:|
| Resonance alignment with atomic \(f_0\) | tunable to experimental transition |
| Local field enhancement | clearly \(>1\), preferably enough for a \(\gtrsim10\) dB measurable sensitivity advantage |
| Linear-polarization discrimination | preferably \(>15\)–20 dB |
| Interaction-volume field nonuniformity | aim for \(<10\)–15% if achievable |
| Independent analyzer states | minimum 4; preferred 6 |
| Measurement-matrix condition number | drive toward unity; provisional \(<5\) |
| State-to-state resonance movement | as small as possible; ideally a few percent or less |
| Polarization reconstruction | aim for a few-degree error over representative test states |
| Validation | bare cell + passive baseline + active device all measured |

I would not obsess over beating every published enhancement number. Recent Rydberg resonator papers are already producing strong sensitivity enhancements. **Our primary win should be functionality.**

Enhancement makes it useful; programmable polarimetry makes it new.

## What the eventual APL Photonics paper should contain

The paper should be designed from the figures backward.

### The five-figure paper

**Figure 1 — Concept and physics**

Show the vapor cell, lasers, incident arbitrary-polarization RF wave, metasurface states and the RF-to-optical readout. Introduce

\[
\mathbf m=\mathbf A\mathbf S.
\]

This figure establishes immediately that the paper is about **programmable atomic polarimetry**, not merely a PCB.

**Figure 2 — Electromagnetic co-design**

Show the unit/resonator structure, currents, electric-field hotspot, actual cell, optical interaction volume, \(x/y\) resonant modes, and calculated \(G_E\), PER and uniformity.

This is where the simple SRR baseline evolves into the novel structure.

**Figure 3 — Atomic field-enhancement validation**

Bare cell versus passive resonator versus active metasurface. Show measured EIT/AT or Stark spectra, simulated versus measured enhancement, frequency response, and uncertainty.

Existing Rydberg/resonator work has already established that simulation–measurement agreement is expected to be scrutinized carefully. **Figure 4 — Programmable polarization states**

For each metasurface configuration, plot response against incident linear-polarization angle and circular/elliptical states. Show the experimental measurement matrix \(\mathbf A\).

This figure proves that the surface is genuinely changing the **measurement basis** rather than simply switching gain.

**Figure 5 — Reconstructed polarimetry**

Poincaré sphere or equivalent Stokes plots: truth versus reconstruction for a library of input states, with error statistics.

Then add sensitivity/polarization error versus RF amplitude, frequency and angle.

That is the figure that I think makes the paper APL Photonics-level rather than “another resonator.”

A sixth figure could compare the device against the prior-art landscape in enhancement, polarization functionality, reconfigurability and atomic complexity.

### The likely manuscript argument

I would write the eventual Results/Discussion logic in this order:

**Introduction**

Rydberg atoms provide optically interrogated RF electrometry and can perform vector electrometry. Resonators can improve sensitivity and impose polarization selectivity. Recent structures support circular polarization, directional reception, dual-frequency and broader-band enhancement. But existing enhancement structures are predominantly designed as fixed electromagnetic interfaces, while conventional polarization-diverse atomic approaches place more complexity on the atomic preparation/readout.

**Gap**

A simple fixed-axis vapor-cell sensor lacks a programmable external mechanism for selecting arbitrary polarization-analysis bases.

**Idea**

Move that complexity into a reconfigurable resonant electromagnetic front end.

**Principle**

Each metasurface state maps one incident polarization projection onto an enhanced local RF mode that the same Rydberg transition reads optically.

**Result**

Multiple switch states generate a calibrated analyzer matrix from which the incident Stokes vector can be recovered.

**Significance**

Polarization diversity and sensitivity enhancement are achieved without changing the core atomic/optical sensor configuration.

That is the central scientific narrative I would protect throughout the project.

### What not to claim

I would explicitly avoid these claims unless the data become genuinely exceptional:

> “First polarization-sensitive Rydberg sensor.”

Not true; polarization-sensitive and vector Rydberg sensing predates this project. > “First metasurface to improve Rydberg sensitivity.”

Also not true; resonant structures and related enhancement approaches are well established. > “Novel PIN-diode polarization metasurface.”

That literature is crowded. The potentially defensible claim is much narrower and better:

> **A reconfigurable polarization-analysis electromagnetic interface co-designed with a Rydberg optical readout for enhanced full-state RF polarimetry using a single fixed vapor-cell sensor.**

That is what we should try to prove.

## How I would execute the project from here

The sequence below is deliberately set up so that every stage produces useful thesis content even if the ambitious reconfigurable device eventually has problems.

### First lock the sensor definition

Before any “novel metasurface” optimization, freeze a one-page specification:

\[
f_0=\text{target RF frequency},
\]

\[
\text{cell dimensions and material},
\]

\[
\text{probe/coupling beam axes and waist},
\]

\[
\hat{\mathbf d}=\text{effective RF-sensitive axis},
\]

\[
\text{available RF illumination geometry},
\]

\[
\text{available PCB/device volume}.
\]

The absolute geometry cannot rationally be finalized until those are fixed.

This is especially important because the real question is **not** “what metasurface works around 2 GHz?” It is:

> “What resonant current distribution gives the required electric field inside this particular glass cell at the particular location sampled by these lasers?”

### Then reproduce a boring resonator

Scale/design a single SRR or ELC to the chosen \(f_0\).

Model:

**free space → vapor cell → resonator + vapor cell.**

Generate:

\[
S(f),\quad E(\mathbf r),\quad G_E,\quad U_E.
\]

Do parameter sweeps for gap, trace length, resonator–cell spacing and interrogation location.

At this point we deliberately do **zero novelty chasing**.

This stage establishes a trustworthy model.

### Then solve the polarization problem passively

Create two approximately degenerate orthogonal coupling modes.

Optimize them so that

\[
G_x\approx G_y,
\]

while unwanted cross-coupling is suppressed.

Characterize

\[
R_x(\theta),\quad R_y(\theta).
\]

Now we know whether the physical principle of polarization-selective coupling survives the actual vapor cell.

### Then formulate the polarimeter before adding hardware

Define the desired analyzer vectors:

\[
\mathbf a_H,\mathbf a_V,\mathbf a_D,
\mathbf a_A,\mathbf a_R,\mathbf a_L.
\]

Determine through full-wave simulation which surface states can approximate them.

Construct

\[
\mathbf A_\mathrm{sim}.
\]

Optimize

\[
\kappa(\mathbf A_\mathrm{sim}).
\]

This step is critical because it tells us **what the switches must accomplish**.

Otherwise we would be designing PIN topology first and inventing its purpose afterward.

### Then add ideal switches

Put ideal open/closed elements into the geometry.

Ask whether four or six sufficiently independent analyzer states are possible at the same \(f_0\).

If the answer is no, redesign the resonator architecture now—while switches are still ideal.

Only when

\[
\mathrm{rank}(\mathbf A)=4
\]

and its conditioning is acceptable should we proceed.

### Then add the real PIN network

Introduce diode parasitics and the DC network.

Evaluate the degradation:

\[
\Delta G_E,
\]

\[
\Delta f_0,
\]

\[
\Delta\mathrm{PER},
\]

\[
\Delta\kappa(\mathbf A).
\]

This itself becomes useful scientific content because it quantifies how active loading affects an atom-coupled resonant electromagnetic interface.

### Then fabricate the passive version first

I would fabricate B1/B2 before the full active board unless the fabrication cost makes simultaneous production trivial.

That gives us:

- VNA validation;
- resonance shift caused by fabrication/cell;
- field enhancement;
- polarization selectivity;
- comparison with simulation;
- first Rydberg spectra.

If those do not agree, debugging a PIN-loaded metasurface would be painful.

### Then fabricate the active system

At this point the reconfigurable board is an extension of a known working resonator rather than a blind first prototype.

The experimental sequence becomes:

\[
\text{known RF state}
\rightarrow
\text{switch state}
\rightarrow
\text{atomic spectrum}
\rightarrow
m_k
\rightarrow
\hat{\mathbf S}.
\]

That produces the data set around which the journal paper is written.

### The decision tree I would use

```text
Does B1 give useful enhancement in the actual interrogation volume?
        │
        ├── No → redesign resonator/cell coupling.
        │        Do not proceed to PINs.
        │
        └── Yes
             │
             ▼
Can B2 discriminate two orthogonal incident polarizations?
             │
             ├── No → solve modal symmetry/coupling first.
             │
             └── Yes
                  │
                  ▼
Can ideal switching produce ≥4 independent analyzer states?
                  │
                  ├── No → change topology / phase paths.
                  │
                  └── Yes
                       │
                       ▼
Does real PIN loading preserve enhancement and conditioning?
                       │
                       ├── No → alternative switch/bias strategy.
                       │
                       └── Yes
                            │
                            ▼
Can atomic measurements reconstruct unknown polarization?
                            │
                            ├── No → calibration/noise/atomic-model work.
                            │
                            └── Yes → journal result.
```

That is the cleanest way I can see of preventing us from disappearing into months of arbitrary metasurface optimization.

## How this maps onto APL Photonics and the attached template

There is one important housekeeping correction from your attachment.

The archive you uploaded is an **old generic AIP REVTeX package**, not the current APL Photonics submission template. I inspected `aiptemplate.tex`; its own header identifies it as the AIP REVTeX 4.1 distribution dated **9 October 2009**, and it uses

```latex
\documentclass[aip,graphicx]{revtex4-1}
```

with the older generic AIP skeleton.

I would therefore **not build the thesis paper around that package**.

Current AIP instructions recommend the maintained AIP Publishing Overleaf LaTeX template, and initial submission is now a single compiled manuscript PDF. For APL Photonics specifically, Research Articles do not have a fixed word limit, whereas Letters are capped at 3500 words; non-Letter manuscripts should use section headings. Current AIP guidance also requires a one-paragraph abstract of up to 250 words, a CRediT author-contribution statement, and a data-availability statement. For this project I would target a **Research Article**, not a Letter. We are going to need enough space to establish:

\[
\text{atomic principle}
+
\text{EM design}
+
\text{calibration}
+
\text{experimental validation}
+
\text{polarimetry}.
\]

The eventual working manuscript skeleton should therefore be:

```text
TITLE
Reconfigurable metasurface-assisted Rydberg polarimetry ...
    or
Programmable polarization analysis with a Rydberg atomic RF sensor ...

ABSTRACT

I. INTRODUCTION
    Rydberg RF sensing
    Existing vector electrometry
    Resonator enhancement
    Recent polarization-enhancement structures
    Gap: programmable external polarization analysis
    Contribution of this paper

II. PRINCIPLE OF METASURFACE-ASSISTED ATOMIC POLARIMETRY
    Atomic RF-to-optical transduction
    Polarization projection
    Stokes reconstruction
    Measurement matrix

III. RESONANT ELECTROMAGNETIC INTERFACE
    Baseline resonator
    Dual-polarized modes
    Interaction-volume optimization
    Active switching topology
    PIN/bias model

IV. EXPERIMENTAL SYSTEM
    Vapor cell and lasers
    RF source and reference polarization generation
    Metasurface hardware
    Switching/control
    Calibration procedure

V. RESULTS
    Passive field enhancement
    Polarization selectivity
    Reconfigurable analyzer states
    Atomic spectra
    Stokes reconstruction
    Sensitivity and uncertainty
    Frequency/angular robustness

VI. DISCUSSION
    Comparison with existing Rydberg resonators
    Why external programmability matters
    Limitations
    Scaling/bandwidth

VII. CONCLUSION

SUPPLEMENTARY MATERIAL
    Full geometry
    Diode equivalent circuits
    Bias network
    Additional field maps
    Optical/atomic model
    Calibration matrix
    Uncertainty derivation
    Additional polarization states

AUTHOR DECLARATIONS
DATA AVAILABILITY
REFERENCES
```

That structure also aligns better with APL Photonics' editorial positioning. The journal says it wants photonics-anchored fundamental/applied research representing significant advances rather than incremental engineering. So my honest assessment is:
**APL Photonics is plausible, but only under the stronger version of this project.**

A paper that ends at

\[
\text{new resonator}+\text{better }E\text{-field}
\]

probably belongs more naturally in an antennas/microwave or applied-physics venue.

A paper that demonstrates

\[
\boxed{
\text{programmable metasurface}
\rightarrow
\text{controlled RF polarization projection}
\rightarrow
\text{enhanced Rydberg interaction}
\rightarrow
\text{optical readout}
\rightarrow
\text{full polarization reconstruction}
}
\]

has a much stronger case for APL Photonics because the electromagnetic surface is enabling a **new optically read quantum-sensing modality**, rather than constituting an incremental antenna improvement. APL Photonics' current scope explicitly includes sensors and quantum photonics while rejecting incremental engineering advances. The core plan I would therefore lock in is:

\[
\boxed{
\begin{array}{c}
\textbf{First:}~\text{make one simple resonator work extremely well with the real cell}\\[4pt]
\downarrow\\[4pt]
\textbf{Then:}~\text{create two polarization-diverse resonant channels}\\[4pt]
\downarrow\\[4pt]
\textbf{Then:}~\text{turn polarization sensing into a calibrated matrix problem}\\[4pt]
\downarrow\\[4pt]
\textbf{Then:}~\text{use ideal switches to synthesize the required analyzer states}\\[4pt]
\downarrow\\[4pt]
\textbf{Then:}~\text{implement those states with PIN diodes}\\[4pt]
\downarrow\\[4pt]
\textbf{Finally:}~\text{demonstrate enhanced full-Stokes Rydberg polarimetry experimentally.}
\end{array}}
\]

That gives us a baseline we can actually start from, a sequence in which every step has a measurable purpose, and—most importantly—a novelty claim that survives contact with the existing Rydberg and metasurface literature.
