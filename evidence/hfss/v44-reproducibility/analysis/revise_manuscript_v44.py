from pathlib import Path
import re
R=Path(__file__).resolve().parent.parent
p=R/'main_access.tex';s=p.read_text()

def remove_between(start,end):
    global s
    a=s.index(start);b=s.index(end,a+len(start))
    s=s[:a]+s[b:]

# Remove an overview table that duplicates the comparative literature prose.
remove_between(r'\begin{table*}[t]'+ '\n'+r'\caption{Major polarimetry approaches',r'\subsection{Research opportunity}')
# Research objectives currently repeats the Introduction and the Methods section.
remove_between(r'\section{Research objectives and design strategy}',r'\section{Electromagnetic modelling and verification}')
# Unneeded parameter-percentage plot: same copper geometry already in figure 5.
remove_between(r'\begin{figure}[tb]'+ '\n'+r'\centering\includegraphics[width=\columnwidth]{F03_NATIVE_OPTIMISED_UNIT_CELL.pdf}',r'\subsection{Optimisation history and candidate selection}')
# Same apparatus context already explained once in physics foundation and intro.
remove_between(r'\subsection{Laboratory architecture and measurement chain}',r'\subsection{A measurement example: why amplitude alone is insufficient}')
remove_between(r'\subsection{A measurement example: why amplitude alone is insufficient}',r'\section{Related work and research opportunity}')
# Remove repeated philosophy at end: discussed in the main discussion and conclusion.
remove_between(r'\section{Interpretation, Scope, and Reproducibility}',r'\section{Conclusion}')
# Move archival equation-verification *table* out of main results, retain calculation in appendix with no duplicated prose.
a=s.index(r'\subsection{Independent-source verification of the Stokes algebra}')
b=s.index(r'\section{Conclusion}',a)
eq_section=s[a:b]
s=s[:a]+s[b:]
# Condense remaining main first-page scientific narrative a little.
s=s.replace('The useful question is therefore not simply whether a metal pattern transmits or rejects one polarisation.',
'The design question is therefore not whether a metal pattern transmits or rejects one polarisation.')
s=s.replace('The distinctive results are a physically specified six-state analyser, an exhaustive four-state subset comparison, and a gain-aware state-criticality test that turns abstract matrix conditioning into concrete RF switching priorities.',
'The main results are a source-defined six-state analyser, exhaustive four-state comparisons, and gain-aware state-selection laws.')
# Strengthen claim boundary in abstract and opening; include new fixed-budget result.
s=s.replace('A gain-aware extension quantifies the distinction between normalised polarimetric leverage and absolute HFSS receiving amplitude, providing an explicit design priority for eventual diode selection and RF loss management.',
'A gain-aware extension separates polarimetric leverage from absolute HFSS receiving amplitude. Under a stated fixed-duration measurement model, optimal dwell allocation reduces the inverse-trace uncertainty metric by 40.8\\% relative to equal-time six-state acquisition, and reveals when a four-state schedule is preferable.')
s=s.replace('We further show how weak circular-Stokes sensitivity and state-dependent receiving gain constrain calibration, thereby establishing a reproducible, information-aware design method for microwave polarimetric front ends.',
'The finite-array analysis identifies weak circular sensitivity and calibration-transfer instability, defining a quantitative route from the verified periodic architecture to a physical polarimeter.')
# Correct potentially overconfident 'fabrication-ready' phrasing.
s=s.replace('fabrication-ready topology','fabrication-oriented copper topology')
s=s.replace('provides a credible PCB fabrication pathway','provides a manufacturable starting geometry subject to PCB design-rule and switching-network validation')
# Insert fixed-budget principle before the weaker finite-noise section, after existing gain-aware analysis.
marker=r'\subsection{Circular-channel strength and a projected angular-uncertainty bound}'
new=r'''
\subsection{Fixed-budget acquisition: when four states can outperform six}
\label{sec:fixedbudget}
A sixth calibrated response adds information when the measurement duration of all other states is held constant. It does not follow that six states are always best when \emph{total} acquisition time is fixed. Let $w_k=t_k/T$ be the fraction of an available integration budget $T$ allocated to mask $k$, with $\sum_{k\in\mathcal K}w_k=1$. Assume independent unbiased raw-output errors whose variance decreases inversely with dwell time, $\operatorname{Var}(m_k)=\sigma_0^2/w_k$. For an HFSS matrix $A_{\mathcal K}$, the resulting information and dimensionless A-optimal design objective are
\begin{equation}
\mathcal I_T=\sigma_0^{-2}A_{\mathcal K}^{\mathsf T}\operatorname{diag}(w_k)A_{\mathcal K},\qquad
J_T=\operatorname{tr}\!\left[(A_{\mathcal K}^{\mathsf T}\operatorname{diag}(w_k)A_{\mathcal K})^{-1}\right].
\label{eq:dwell_information}
\end{equation}
The common factor $\sigma_0^2$ cancels from comparisons of schedules. We enumerated all $\binom64=15$ four-state, six five-state and one six-state subsets and minimised $J_T$ subject to $w_k\ge0.02$ for each selected state. This 2\% dwell floor is a declared design assumption, not a measurement of diode switching or atomic settling time. The same calculation was checked with an analytical gradient and independent finite differences.

\begin{figure*}[t]
\centering\includegraphics[width=.87\textwidth]{V44_FIXED_BUDGET.pdf}
\caption{Fixed-budget comparison of four-, five- and six-state C033 schedules at 1.925~GHz. (a) Best subset under equal or optimised dwell, normalised to equal-time six-state operation. (b) A-optimal dwell fractions for the full six-state set. Independent equal raw-output noise per unit integration time is assumed.}\label{fig:fixedbudget}
\end{figure*}

For the full set, equal dwell gives $J_T=1764.54$ in arbitrary inverse-gain units and the optimised schedule gives $1044.82$, a 40.8\% reduction. The four-state set $\{03,06,08,13\}$ achieves $J_T=1020.33$ with approximately 19.4\%, 45.7\%, 14.7\% and 20.2\% of the budget assigned to its four masks. Its modest advantage over the constrained six-state schedule comes from avoiding minimum-dwell allocation to less informative states. This result is \emph{not} an accuracy prediction for a vapour-cell experiment: real switching dead time, correlated noise and drift can change the optimum. It does show that information quality and acquisition cost can be optimised together using the existing complex HFSS results, providing a practical state-selection criterion beyond rank and $\kappa_2$.

'''
s=s.replace(marker,new+marker)
# Add benchmark presentation without pretending external matched geometry: a clean explicit comparison in discussion.
s=s.replace(r'\section{Discussion: design insight and engineering contribution}',r'''\section{Discussion: design insight and engineering contribution}
The strongest matched internal benchmark is not a differently fabricated polarimeter, but the same C033 geometry operated with different choices and allocations of switch states. All the subsets in Fig.~\ref{fig:fixedbudget} use the identical six HFSS-calculated responses at 1.925 GHz; their performance differences therefore follow from the measurement design rather than an uncontrolled change in frequency or aperture. This isolates a transferable result: a well-conditioned polarimetric basis can be engineered in the \emph{space of measurements}, after the electromagnetic geometry has been simulated. Comparisons with the published electronically reconfigurable microwave polarimeter \cite{Chen2025Reconfigurable} remain qualitative until matching measurements at the same frequency and receiving geometry are available.
''')
# Introduce evidence level table to avoid repeating in paragraphs? Already references archived.
# Fix ugly scattered subheading above full geometry and theoretical labels, reduce caption language.
s=s.replace(r'\caption{HFSS geometry and equivalent circuit: (a) finite array, (b) C033 copper meta-atom with D1--D4 at exact native conducting-bridge polygon positions, and (c) qualitative coupled-resonator topology.}',
            r'\caption{C033 geometry: (a) $3\times3$ finite panel, (b) native copper with ideal bridge sites D1--D4, and (c) topology-level coupled-resonator model.}')
s=s.replace(r'\caption{HFSS optimisation across 36 geometry candidates. The dashed reference is the original 175-MHz sampled passing span.}',
            r'\caption{HFSS search across 36 candidate geometries; dashed line marks the 175-MHz reference screening span.}')
# Put equation-verification subsection in appendix before summary derived laws.
append_marker=r'\subsection{Derived design tests: admissibility, information bandwidth, and calibration transfer}'
s=s.replace(append_marker,eq_section+'\n'+append_marker)
# Fix 17 references? retained.
# Briefly revise official repeat conclusion to include new approach.
s=s.replace('The design also admits a fixed-budget acquisition trade-off', 'The design also admits a fixed-budget acquisition trade-off')
s=s.replace('The central positive result is', 'The principal simulation result is')
# Add formal biography and AI disclosure before final refs, keeping user-provided academic credentials unclaimed.
s=s.replace(r'\input{ieee_references.tex}',r'''\section*{Acknowledgment and manuscript preparation}
The author acknowledges the experimental and simulation environment supporting the study. OpenAI ChatGPT (GPT-6) assisted with manuscript drafting, scientific-language editing, figure-layout code and offline analysis code. All numerical results attributed to HFSS are taken from the preserved native records; model-based post-processing is identified as such. The author must verify this disclosure and all source references before submission.

\input{ieee_references.tex}
\begin{IEEEbiographynophoto}{Ryan N. Verghese}
Ryan N. Verghese is affiliated with the School of Engineering and Technology, UNSW Canberra, Australia. His research interests include microwave polarimetry, electromagnetic metasurfaces and Rydberg-atom radio-frequency sensing.
\end{IEEEbiographynophoto}''')
# placeholder metadata blanks remain in official template, not fake
p.write_text(s)
print('Length before/after', 'n/a',len(s),'references moved:',len(eq_section))
