# Draft thesis methods and results text

This document is written to be adapted, not pasted without review. Confirm all
state labels, apparatus details, and transcribed notebook values against the
original laboratory record before submission.

## Data provenance and evidentiary scope

The retrospective dataset comprised (i) a 21-point coil-current versus magnetic
field calibration, (ii) eleven manually recorded spectral levels acquired in an
ordered 0–20 V coil sweep, (iii) one initial and two final no-voltage reference
levels, and (iv) two LeCroy oscilloscope waveform exports labelled as 1.5 GHz
measurements without coils. The waveform files each contained 102 samples with
a 50 ps sample interval and a 5.05 ns total record duration. The files did not
contain a laser-frequency axis, a photodiode EIT scan, an applied modulation
reference, or a coil-on/off label. Consequently, waveform processing was
restricted to coherent RF-component extraction and was not interpreted as EIT
recovery.

The manually transcribed level was treated as an exploratory scalar observable.
It was not relabelled as EIT height, linewidth, Autler–Townes splitting, or
atomic transmission because the retained record did not establish that metric
definition. This distinction prevents a post-hoc change in the measured
quantity.

## Magnetic-field calibration

The bias field was modelled by ordinary least squares as

\[
B_0 = aI+b,
\]

where \(I\) is coil current in amperes and \(B_0\) is the measured field in
millitesla. The fitted calibration was

\[
B_0=(2.3016\;\mathrm{mT/A})I+0.0278\;\mathrm{mT},
\]

with \(R^2=0.9806\) and residual RMSE 0.1030 mT. The nonzero intercept is
consistent with a residual/background field or magnetometer offset; the
available data do not identify which contribution dominates.

## Dual-phase coherent extraction

For each waveform, a sinusoid at the nominal carrier frequency was estimated by
linear least squares while simultaneously fitting a constant and linear drift:

\[
y(t)=\beta_0+\beta_1\tilde t+I_c\cos(2\pi f_\mathrm{ref}\tilde t)
-Q_c\sin(2\pi f_\mathrm{ref}\tilde t)+\epsilon(t),
\]

where \(\tilde t=t-\bar t\). The recovered peak magnitude and phase were

\[
R=\sqrt{I_c^2+Q_c^2}, \qquad
\phi=\operatorname{atan2}(Q_c,I_c).
\]

The coherent SNR reported by the code is

\[
20\log_{10}\left[\frac{R/\sqrt 2}{\operatorname{RMS}(\epsilon)}\right].
\]

At a fixed 1.5 GHz reference, the recovered amplitudes were 18.53 and
22.40 mV peak, differing by approximately 1.65 dB. The fits explained only
23.3% and 39.4% of waveform variance, with coherent SNR values of approximately
-5.22 and -2.08 dB. A free-frequency fit returned approximately 1.483 and
1.481 GHz, but the record-limited frequency scale was about 198 MHz. These
frequency refinements therefore do not establish a physical shift away from
1.5 GHz. The two fitted phases were not compared because no common phase
reference between acquisitions was retained.

This calculation is mathematically similar to dual-phase lock-in detection but
does not constitute an atomic EIT lock-in measurement. A true retrospective EIT
lock-in requires a sufficiently long photodiode record and a known reference to
a deliberately modulated RF, laser, or magnetic-bias parameter.

## Bias association and robustness analysis

The eleven recorded main levels were regressed against the calibrated bias
field. Because the field was increased monotonically with acquisition order and
there was no replication at each setting, the resulting coefficient was treated
as a descriptive association rather than a causal effect. A two-sided
permutation test was implemented by shuffling the recorded levels relative to
the fixed field values 100,000 times using a fixed random seed.

The raw slope was approximately +1.333 dB/mT, with \(R^2=0.460\) and a
permutation p-value of approximately 0.021. However, the levels across the sweep
spanned 5.23 dB, while the mean of the two final no-voltage references was
-25.28 dBm compared with -29.06 dBm initially. The 3.78 dB reference change was
therefore 72.3% of the complete observed span.

A drift sensitivity analysis linearly interpolated this reference change over
acquisition order and subtracted the estimated drift from each observed level.
This is not asserted to be the true drift trajectory; it tests whether a
plausible trajectory can change the conclusion. Under this sensitivity, the
slope was approximately -0.160 dB/mT, with \(R^2=0.012\) and permutation
\(p\approx0.75\). The constant model was then preferred by corrected AICc over
the linear and quadratic alternatives. Thus, the apparent raw association was
not robust to the independently observed baseline change.

## Thesis-safe result statement

The magnetic-coil calibration was repeatable over the tested range. The ordered
receiver readings exhibited a nonmonotonic variation and a raw field
association. However, the start-to-end no-voltage reference change was of the
same order as the bias-sweep variation, and a stated drift sensitivity analysis
removed the association. The available data therefore do not uniquely attribute
the observed variation to magnetic bias. They support a feasibility result and
an uncertainty analysis, rather than experimental confirmation of
magnetic-bias-dependent polarization sensing.

## Compact Zeeman–EIT forward model

The supplied MATLAB code implements an illustrative weak-probe four-level model.
For probe, coupling, and RF interactions, the optical coherence is represented
in compact form as

\[
\rho_{ge}\simeq
\frac{i\Omega_p/2}
{\gamma_{ge}-i\Delta_p+\frac{|\Omega_c|^2}{4D_r}},
\]

with

\[
D_r=\gamma_{gr}-i\Delta_2+\frac{|\Omega_{m,q}|^2}{4D_s},
\qquad
D_s=\gamma_{gs}-i\Delta_{3,q}.
\]

The pathway detuning is shifted illustratively according to

\[
\Delta_{3,q}=\Delta_3-q\alpha_Z B_0,
\]

and the plotted transmission is an arbitrary normalized quantity proportional
to

\[
T=\exp[-\mathrm{OD}\,\operatorname{Im}(\chi)].
\]

The model uses interim illustrative values, including
\(\alpha_Z=2.8\;\mathrm{MHz/mT}\). It is not a fitted density-matrix model.
Its defensible use is to demonstrate that Zeeman motion of several transition
pathways can produce a nonmonotonic signal when transmission is sampled at one
fixed detuning. The model should not be used to claim numerical agreement until
the exact Rydberg states, optical/RF detunings, state-dependent dipole moments,
Rabi frequencies, Doppler averaging, and detector transfer function are known.

For specified states, a differential first-order Zeeman coefficient should be
calculated from the participating magnetic sublevels. ARC can supply level
energies and dipole matrix elements; Rydiqule can implement the documented
multilevel steady-state/Doppler model. Parameter selection should be based on
the apparatus record and atomic structure, not chosen to force agreement with
the eleven observed points.

## Polarization-angle estimator

Let the magnetic bias define the spherical basis. For a resolved transition
with component \(q\in\{-1,0,+1\}\), the microwave Rabi frequency satisfies

\[
\Omega_q=\frac{d_q E_q}{\hbar}.
\]

Accordingly, a component-strength proxy must be corrected for the transition
dipole moment:

\[
P_q \propto \left|\frac{\Omega_q}{d_q}\right|^2.
\]

For an ideal linearly polarized field at angle \(\theta\) to the quantization
axis,

\[
P_\pi=\cos^2\theta, \qquad
P_{\sigma+}+P_{\sigma-}=\sin^2\theta,
\]

which gives

\[
\hat\theta=operatorname{atan2}\!\left(
\sqrt{P_{\sigma+}+P_{\sigma-}},\sqrt{P_\pi}\right).
\]

This estimator requires spectrally resolved, pathway-specific strengths. The
present records do not contain those observables, so the estimator is presented
as a theoretical method rather than applied to the experimental points. For a
general elliptical field, component magnitudes alone do not determine the
relative phases. Complete polarization recovery requires additional independent
measurements, such as rotated quantization axes or phase-coherent orthogonal
local-oscillator channels.

## Statements that the present data do not support

Avoid the following claims unless new primary records are recovered:

- “DSP revealed EIT in the two waveform files.”
- “The magnetic bias caused the measured 5.23 dB change.”
- “The 2.4 GHz readings are Zeeman sidebands of the 1.56 GHz feature.”
- “Simulation agrees quantitatively with experiment.”
- “The experiment estimated polarization angle or full Stokes parameters.”
- “A p-value from the ordered sweep controls for drift.”

The stronger and accurate contribution is that the work establishes the
calibration, implements a reproducible analysis, identifies non-identifiability
from drift, and specifies the resolved-transition observables needed for a
future magnetic-bias polarimeter.
