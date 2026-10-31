from pathlib import Path
import re,json
P=Path(__file__).resolve().parents[1]/'main.tex'
s=P.read_text()
s=s.replace('% V28 thesis-and-journal editorial revision | original evidence updated, 24 Oct 2026.','% V31 independent evidence and publication readability revision | 25 Oct 2026.\n% All new numeric plots are traceable reanalysis of shipped native HFSS-derived matrices.')
s=s.replace(r'\date{ZEIT4501 Final Engineering Thesis Report \quad | \quad 24 October 2026}',r'\date{25 October 2026}')
s=s.replace(r'\title{From Atomic RF Detection to Full-Stokes Microwave Polarimetry: A Reconfigurable L-Band Metasurface for Rydberg Sensing}',r'\title{A Programmable Two-Face Microwave Metasurface for Full-Stokes Analysis at a Fixed Rydberg-Sensor Aperture}')
start=s.index('\\begin{abstract}')
end=s.index('\\end{abstract}',start)+len('\\end{abstract}')
abstract=r'''\begin{abstract}
Polarisation selectivity is essential for a Rydberg microwave receiver that seeks to distinguish the complete transverse state of an incident field. Here we design and numerically characterise a six-state, two-face, 24-mm-period printed metasurface that converts coherent Jones inputs into distinct quadratic receiving observables. The electromagnetic design is grounded in archived laboratory linear-polariser measurements (9.7-dB orientation contrast at approximately 2 GHz) and an Ansys HFSS parameter search of 36 geometries. The optimisation expands the sampled polarimetric acceptance span from 175 to 250 MHz on a 25-MHz discovery grid; independently adapted periodic HFSS solutions give a full-rank Stokes instrument with condition number 9.53 at 1.925 GHz and 0.551\% intermesh matrix difference. We derive a positive-semidefinite receiving-volume operator that maps complex HFSS fields onto the four Stokes coordinates and a corresponding six-measurement least-squares estimator. A finite 82-mm, $3\times3$ panel yields full-rank receiving instruments at 1.850 GHz, but the two completed finite mesh policies give distinct quantitative reconstructions: a fresh, deterministic 1,231-state cross-mesh evaluation has a 95th-percentile full-vector difference of 156.8\% for one calibration direction at a 5-mm receiving plane. This result separates mathematical observability from numerical transfer accuracy. Finally, a velocity- and spatially averaged four-level Rydberg susceptibility model explicitly identifies how local RF projections feed the probe-optical signal. The study establishes a traceable electromagnetic design and calibration framework for metasurface-assisted atomic polarimetry.
\end{abstract}'''
s=s[:start]+abstract+s[end:]
s=s.replace(r'\caption{Optically interrogated rubidium sensor: laboratory apparatus (a) and RF/optical measurement chain (b). Photograph from the author\'s laboratory records\cite{Verghese2026Poster}.}',r'\caption{Laboratory-to-polarimeter architecture. (a) Photograph of the rubidium optical laboratory. (b) Physical RF conditioning geometry ahead of a counterpropagating 780/480-nm optical interrogation, alongside the six-state HFSS-to-Stokes reconstruction chain. The surface position in (b) represents the modelled RF interface, not a component claimed to be in the photographed bench.}')
s=s.replace(r'\caption{Rydberg EIT and RF coupling principle. The conceptual lineshapes illustrate the optical consequence of microwave coupling; no artificial measurements are implied.}',r'\caption{From incident RF field to a modelled optical observable: the ladder scheme, local Rabi coupling and velocity-dependent susceptibility. The quadratic HFSS receiving operator and the atomic probe-transmission model are distinguished explicitly.}')
s=s.replace(r'\caption{The reference split-loop, bandwidth-optimised design and high-band comparator use one substrate with independently dimensioned front and rear copper traces.}',r'\caption{Parametric two-face topology and exact changes to the eleven stored HFSS geometry parameters for the two optimised candidates relative to the reference design. The circuit drawing is a two-dimensional topology projection; the numeric panel is the authoritative geometry comparison.}')
s=s.replace(r'\caption{Finite split-loop array, enlarged 24-mm unit cell and conceptual switched $LC$ circuit. Ideal HFSS bridges mark the proposed diode sites.}',r'\caption{Finite-panel study geometry. (a) Nine 24-mm cells within the modelled 82-mm square panel. (b) Four ideal conducting-gap locations in a schematic trace view. (c) Two copper faces across the dielectric and the downstream 70-by-50-mm field sampling region. Circuit locations denote modelled conducting bridges, not validated diode impedances.}')
s=s.replace(r'\caption{Archived RF polariser measurements: discrete received powers and an original polarisation-angle response plot from the thesis poster.}',r'\caption{Archived laboratory point readings without interpolated or fitted angle-response curves. The 9.7-dB contrast is calculated only from the preferred and rejected measurements; an earlier VNA polariser test used a different apparatus.}')
s=s.replace(r'\caption{HFSS-based Poincar\'e reconstruction and the six distinct responses to horizontal, vertical, diagonal, antidiagonal and circular input states.}',r'\caption{Independent-mesh calibration transfer using the two completed 3-by-3 finite HFSS receiving matrices (1.850 GHz, 5 mm). (a) Projection of 1,231 uniformly sampled fully polarised Stokes states, coloured by reconstruction error for the P24-calibrated/P27-observed calculation. (b) Error distributions for both calibration directions. (c) Corresponding 95th-percentile and maximum full-vector errors. These states are deterministic post-processing of distinct native HFSS matrices, not separate full-wave solves.}')
s=s.replace(r'\caption{Finite $3\times3$ receiving-matrix conditioning at four planes behind the PCB for two HFSS copper-mesh policies.}',r'\caption{Finite HFSS receiver-distance dependence at 1.850 GHz: (a) two-mesh condition numbers, (b) instrument matrix difference, and (c) worst archived deterministic cross-mesh reconstruction discrepancy. Both meshes give rank-four receiving operators at all displayed planes.}')
# insert figure 5 after Fig 4 (not previously in body)
needle=r'\caption{Finite-panel study geometry.'
pos=s.index(needle);after=s.index(r'\end{figure*}',pos)+len(r'\end{figure*}')
insertion=r'''
\begin{figure*}[t]
\centering\includegraphics[width=.98\textwidth]{FINAL_F05_SWITCH_TRUTH.pdf}
\caption{Six calibration states of the four ideal HFSS conducting bridges. Open and closed status is decoded from the archived integer switch masks $3,6,8,10,12,13$, with D1 as the least-significant bit. This mapping fixes the state order used in the instrument matrices.}\label{fig:switchmap}
\end{figure*}
'''
s=s[:after]+'\n'+insertion+s[after:]
# Replace literature table entirely up to \end{table*} preceding research opportunity
pat=r'\\begin\{table\*\}\[t\][\s\S]*?\\end\{table\*\}'
m=re.search(pat,s)
if m:
 table=r'''\begin{table*}[t]
\caption{Representative polarimetry strategies compared by their measurement mechanism and the corresponding design gap. This is a conceptual architecture comparison, not a performance-ranking of incompatible receiver modalities.}\label{tab:context}
\small\centering
\begin{tabular}{p{.18\textwidth}p{.22\textwidth}p{.25\textwidth}p{.23\textwidth}}
\toprule
Research direction & Independent measurement channel & Main capability or dependence & Design implication here\\
\midrule
Atomic EIT/AT electrometry \cite{Sedlacek2012,Sedlacek2013} & RF-induced optical susceptibility/splitting & Atom-referenced field component; optical coherence, RF detuning and selected transition & Optical readout is a spatially sampled dipole projection.\\
Rydberg vector polarimetry \cite{Elgee2024} & Coherent RF references spanning vector components & Experimentally resolved vector fields with reference-field preparation & Provides the primary atomic vector-sensing comparison.\\
Classical instrument-matrix methods \cite{Azzam1988,Tyo2002} & Several independent intensity projections & Reconstruction depends on row independence and noise/calibration statistics & Choose conductor states using full-rank, condition and transfer metrics.\\
Full-Stokes optical metasurfaces \cite{Rubin2019} & Spatially separated polarisation-dependent optical channels & Optical operation through nanostructured anisotropy & Transfer the analysis formalism, not optical-wavelength performance claims.\\
Reconfigurable microwave polarimetry \cite{Chen2025Reconfigurable} & Programmable RF transfer functions & Semiconductor switching enables active polarisation detection & Motivates a compact single-board, sequential receiving projection.\\
\textbf{This work} & \textbf{Six two-face HFSS receiving operators} & \textbf{Periodic and finite apertures; calibration conditioned by receiving position} & \textbf{Tests quantitative full-Stokes observability at a fixed atomic receiving axis.}\\
\bottomrule
\end{tabular}
\end{table*}'''
 s=s[:m.start()]+table+s[m.end():]
# fix mathematical appendix terms and style
s=s.replace(r'\subsection{Passivity of the modeled analyzer and physical feasibility}',r'\subsection{Positive-semidefinite receiving operators and physical admissibility}')
pat=r'\\subsection\{Observability, conditioning and uncertainty transfer\}[\s\S]*?(?=\\subsection\{Derived design tests:)'
new=r'''\subsection{Observability, conditioning and uncertainty transfer}
The six-state instrument $\Avec\in\mathbb R^{6\times4}$ has four independently identifiable Stokes coordinates when $\operatorname{rank}(\Avec)=4$. For an arbitrary positive-definite measurement weighting $W$, define the rectangular least-squares reconstruction operator
\begin{equation}
L_W(\Avec)=(\Avec^{\mathsf T}W\Avec)^{-1}\Avec^{\mathsf T}W,\quad
\widehat{\Svec}=L_W(\widehat{\Avec})\mvec.
\label{eq:weightedls}
\end{equation}
For the deterministic tests reported here $W=I$ and the inverse was calculated using a singular-value decomposition. With actual measured covariance $\Sigma_m$ one can instead use $W=\Sigma_m^{-1}$ when the corresponding statistical model is justified. Defining $\widehat{\Avec}=\Avec+\Delta\Avec$ and $\mvec=\Avec\Svec+\boldsymbol\epsilon$, the full-column-rank identity $L_W(\widehat\Avec)\widehat\Avec=I$ yields
\begin{equation}
\boxed{\widehat{\Svec}-\Svec=
L_W(\widehat{\Avec})(\boldsymbol\epsilon-\Delta\Avec\Svec).}
\label{eq:perturb}
\end{equation}
Consequently,
\begin{equation}
\|\delta\Svec\|_2\le\|L_W(\widehat\Avec)\|_2\left(
\|\boldsymbol\epsilon\|_2+\|\Delta\Avec\|_2\|\Svec\|_2\right).
\label{eq:errorbound}
\end{equation}
When the calibrated matrix is fixed, the first-order measurement covariance is
\begin{equation}
\Sigma_S\simeq L_W(\Avec)\,\Sigma_m\,L_W(\Avec)^{\mathsf T},
\label{eq:covariance}
\end{equation}
with separate terms needed for matrix uncertainty. No detector-noise statistics are inferred from the purely electromagnetic archive. Row-normalised matrices are useful for shape/condition screening, but their use for inversion requires scaling the observation vector by the identical row gains. All new finite cross-mesh tests instead use the complete stored, unnormalised instrument matrices.

The geometric viewpoint is equally useful. Four normalized analyzer vectors define a tetrahedron inside the Poincar\'e unit ball. If their points approach a plane, the smallest singular value collapses and at least one Stokes direction becomes poorly observable; tetrahedral design and conditioning are established polarimetry concepts\cite{Tyo2002,Azzam1988}. We use these principles as design diagnostics. Near-field mesh transfer is quantitatively distinct from a within-mesh condition number.

'''
s,n=re.subn(pat,lambda _:new,s);print('replace inverse',n)
# Replace atomic bridge paragraphs from subsection head to next subsection (design principles)
pat=r'\\subsection\{RF-to-optical measurement transfer\}[\s\S]*?(?=\\subsection\{Design principles and wider applicability\})'
new=r'''\subsection{RF-to-optical measurement transfer}
The metasurface changes the complex microwave field over the atomic receiving volume. To make the receiver coupling explicit, consider the four-level rubidium EIT ladder $|1\rangle\leftrightarrow|2\rangle\leftrightarrow|3\rangle\leftrightarrow|4\rangle$, where the final coupling is microwave-driven. At switch state $k$ and location $\mathbf r$, the RF Rabi coupling is
\begin{equation}
\Omega_{\rm RF,k}(\mathbf r)=\frac{|\mathbf d_{34}\cdot\mathbf E_k(\mathbf r)|}{\hbar}.
\label{eq:opticalbridge}
\end{equation}
In the weak-probe steady-state approximation, the velocity-resolved susceptibility can be represented using complex detuning/decay coefficients $d_{21}(v),d_{31}(v),d_{41}(v)$ as
\begin{equation}
\chi_{k,v}(\Delta_p,\mathbf r)=
\frac{\mathrm i\chi_0}{d_{21}(v)+\dfrac{|\Omega_c|^2}{4\left[d_{31}(v)+\dfrac{|\Omega_{\rm RF,k}(\mathbf r)|^2}{4d_{41}(v)}\right]}}.
\label{eq:fourlevel}
\end{equation}
Here $\chi_0$ is proportional to the optical transition strength and atomic density, while the complex $d_{ij}$ include optical and microwave detunings, decoherence, and Doppler shifts according to the selected ladder and velocity convention. This compact four-level transfer form is consistent with the independently supplied rubidium-receiver theory\cite{Somaweera2025Review}; it is a useful physical model rather than an optical fit to the HFSS data.

Let $F_T(v)$ be the normalised thermal velocity distribution. For a specified optical transverse mode with normalized power weight $W_\perp(\boldsymbol\rho)$, a propagation-sensitive transmission model is
\begin{equation}
T_k(\Delta_p)=\int d^2\boldsymbol\rho\,W_\perp(\boldsymbol\rho)
\exp\!\left[-k_p\int_0^L dz\;\operatorname{Im}\!\left(\int dv\,F_T(v)\chi_{k,v}(\Delta_p,\boldsymbol\rho,z)\right)\right].
\label{eq:opticalvolume}
\end{equation}
Equation~\eqref{eq:opticalvolume} explicitly separates spatial optical averaging, Doppler averaging, and nonlinear field-to-transmission coupling. Its geometry and local $\mathbf E_k(\mathbf r)$ are supplied by the finite HFSS model; its atomic constants, transition selection and fit protocol must be fixed before deriving a predicted measured Stokes error. The matrix $A$ used throughout this paper corresponds to the independently defined RF quadratic proxy, $m_k=\int w|\mathbf e_d\cdot\mathbf E_k|^2dV$. Only when the extracted optical feature is calibrated to be proportional to that proxy can $\mvec=A\Svec$ be applied directly to the atomically measured channel.

For a resolved, on-resonance Autler--Townes doublet of approximately uniform microwave coupling, the usual local relation is
\begin{equation}
\Delta f_{{\rm AT},k}\approx |\mathbf d_{34}\cdot\mathbf E_k|/h.
\label{eq:atsplittransfer}
\end{equation}
For a spatially nonuniform illuminated ensemble, the splitting extracted from an averaged spectrum need not equal the square root of the volume-average squared field. The coupled equations above show which approximation must be tested to turn the present electromagnetic analyser into a full optical polarimeter, without reinterpreting a local HFSS receiving power as a measured atomic observable.

'''
s,n2=re.subn(pat,lambda _:new,s);print('replace transfer',n2)
# Replace Poincare subsection entire, from head to finite section
pat=r'\\subsection\{Poincar\\\'e-sphere reconstruction and physical observability\}[\s\S]*?(?=\\section\{Finite-panel response and near-field coupling\})'
new=r'''\subsection{Poincar\'e-sphere reconstruction and calibration transfer}
The six-state Jones transmission coefficients define an $A\in\mathbb R^{6\times4}$ instrument for each RF model and frequency. Evaluating 1,231 test states against one matrix and inverting the outputs using that same matrix verifies the algebra and basis conventions, but cannot quantify independent calibration accuracy. We therefore use a distinct test: a reconstructed Stokes vector is inferred with one independently meshed finite HFSS instrument while its nominal response is generated using the second finite HFSS instrument.

At the 5-mm receiver plane and 1.850 GHz, the completed P24 and P27 copper-mesh policies both yield rank four; their respective unnormalised condition numbers are 21.93 and 24.72. Using 1,231 deterministic fully polarised states uniformly sampled on the Poincar\'e sphere, $\mvec_{\mathrm{P27}}=A_{\mathrm{P27}}\Svec$ was inverted using $A_{\mathrm{P24}}^{+}$, and vice versa. With the explicitly defined full-vector error $100\|\widehat\Svec-\Svec\|_2/\|\Svec\|_2$, the P24-calibrated/P27-observed direction gives a 95th percentile of 156.8\% and maximum of 165.2\%; the reverse direction gives 72.2\% and 76.6\%. These values follow directly from the archived $6\times4$ matrices and are a new offline numerical post-processing test, not new HFSS solves.

\begin{figure*}[t]
\centering\includegraphics[width=.98\textwidth]{FINAL_F09_STOKES_AND_POINCARE.pdf}
\caption{Independent-mesh calibration transfer using the two completed 3-by-3 finite HFSS receiving matrices (1.850 GHz, 5 mm). (a) Projection of 1,231 uniformly sampled fully polarised Stokes states, coloured by reconstruction error for the P24-calibrated/P27-observed calculation. (b) Error distributions for both calibration directions. (c) Corresponding 95th-percentile and maximum full-vector errors. These states are deterministic post-processing of distinct native HFSS matrices, not separate full-wave solves.}\label{fig:polsphere}
\end{figure*}

The result is revealing: polarisation sensitivity and rank-four observability are already present, while quantitative finite-aperture calibration transfer remains sensitive to the calculated receiving fields. The published-periodic best point at 1.925 GHz and the finite test at 1.850 GHz also answer different simulation questions, so their respective condition numbers are displayed as separate validation stages rather than an assumed finite-board reproduction of the periodic optimum.
'''
s,n3=re.subn(pat,lambda _:new,s);print('replace poincare',n3)
# insert comparative finite table beneath Figure 10 with archive
needle=r'\label{fig:finitecond}\end{figure*}'
pos=s.find(needle)
if pos!=-1:
 pos+=len(needle)
 table=r'''
\begin{table}[h]
\caption{Native finite-panel HFSS matrix stability by receiving-plane distance at 1.850 GHz. The largest error is the archived finite calibration-transfer diagnostic; it differs from the expanded 1,231-state test of Fig.~\ref{fig:polsphere}.}\label{tab:finite}
\centering\small
\begin{tabular}{rrrrr}
\toprule
Plane (mm) & $\kappa_{2.7}$ & $\kappa_{2.4}$ & Drift (\%) & Transfer (\%)\\
\midrule
5 & 24.72 & 21.93 & 6.18 & 76.92\\
10 & 24.82 & 30.17 & 4.85 & 55.09\\
20 & 59.81 & 61.37 & 5.17 & 139.94\\
50 & 209.15 & 176.74 & 3.16 & 202.44\\
\bottomrule
\end{tabular}
\end{table}
'''
 s=s[:pos]+'\n'+table+s[pos:]
# remove original inconsistent claim where source Fig 9 says self reconstruction, now new results
s=s.replace('Figure~\\ref{fig:polsphere} shows why complementary measurements are required.','Figure~\\ref{fig:polsphere} shows how cross-mesh calibration changes full-vector reconstruction.')
# remove redundant scope wording / inaccurate description of changed figure
s=s.replace('Figure~\\ref{fig:linearresults} retains these contexts and uses the original thesis poster plot without inventing unreported samples.','Figure~\\ref{fig:linearresults} displays the original archived point values directly without interpolated measurements or a fitted angle curve.')
# put shorter conclusion with finite error and atomic transfer, no unjustified claims
pat=r'\\section\{Conclusion\}[\s\S]*?(?=\\section\{Future integration and research handover\})'
new=r'''\section{Conclusion}
A single programmable two-face RF metasurface can generate multiple independent quadratic responses to an incident microwave Jones field, supporting four-coordinate Stokes observability from a fixed receiving axis. The design links a measured 9.7-dB laboratory linear polariser contrast to an RF-engineering route toward polarisation-sensitive optical sensing. The native HFSS search across 36 candidate geometries increases the sampled polarimetric discovery span by 42.9\%, while separate dual-mesh periodic calculations give a rank-four six-state instrument with condition number 9.53 at 1.925 GHz.

More revealing than the zero-residual same-matrix algebraic inversion is the finite-panel calibration transfer. For the completed 82-mm panel at 1.850 GHz, the full-rank receiver response depends on mesh policy and detector distance; at 5 mm the expanded 1,231-state cross-mesh test reaches 156.8\% 95th-percentile full-vector error in one calibration direction. Thus the work distinguishes the existence of polarization information from the stability of its numerical recovery. The derived Jones-to-Stokes receiving operator, its six-state estimator and the spatially averaged four-level atomic susceptibility provide a direct, reproducible route from microwave structure to optical feature design. The strongest research outcome is a physically grounded, auditable workflow for metasurface-conditioned Rydberg polarimetry, with quantitative finite-field refinement identified as the decisive remaining engineering validation.
'''
s,n4=re.subn(pat,lambda _:new,s);print('replace conclusion',n4)
# remove over-defensive author research-scope footer duplicating points discussed
s=s.replace(r'\textbf{Research scope.} Simulations are electromagnetic-only and contain no synthetic detector noise. No completed Rydberg optical readout response or experimental full-Stokes data are reported.','')
# body text terminology use full rank but finite sample calibrated 
s=s.replace('The six-state response map is scientifically more informative than a near-zero ideal inversion error: it shows why complementary measurements are required.','The cross-mesh calibration test is more informative than a near-zero same-matrix residual: it measures how quantitative inversion changes when the independently calculated electromagnetic response changes.')
s=s.replace('The two circular states have identical $S_0,S_1,S_2$ but opposite $S_3$; their different predicted receiving responses demonstrate sensitivity to phase handedness.','The two circular input states differ only in $S_3$, so phase-quadrature sensitivity follows from the nonzero fourth instrument column, subject to the stated receiving-axis convention.')
# avoid 'fully verified' language, and update file
P.write_text(s)
