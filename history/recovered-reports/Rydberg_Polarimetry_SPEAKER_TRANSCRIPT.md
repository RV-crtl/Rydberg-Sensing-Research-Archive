# Speaker transcript — SET HDR Conference

## Slide 1 — Title

Good morning. I’m Ryan Verghese, and my project asks whether a Rydberg microwave receiver can add polarisation as a useful RF observable. The key idea is simple: frequency and power tell us part of the story, but the electric-field vector contains extra information. I’ll show how our atomic receiver works, why that extra vector information matters, what we can already measure, and how magnetic bias and passive polarisation projections can be combined into a Stokes-space polarimeter.

## Slide 2 — What is a Rydberg microwave receiver?

A Rydberg receiver is an optical transducer for a microwave electric field. The 780-nanometre probe reads rubidium absorption. The 480-nanometre coupling laser opens an EIT window into a highly excited state. When the microwave couples neighbouring Rydberg states, that optical marker moves or splits, and a photodetector records the change. So the information chain is RF to atom to light. The important point for the rest of the talk is that the microwave leaves a spectral fingerprint, not just a single amplitude number.

## Slide 3 — Why add an atomic RF channel?

Why bother with an atomic channel when classical receivers are already excellent? Not because atoms replace everything. The value is that they give us a complementary measurement mechanism. In our wider programme, the same cell has been used from megahertz to gigahertz, mixing extends the accessible RF space, and controlled jamming work shows a different failure mode from an SDR. My thesis adds one more descriptor to that platform: polarisation. So the question becomes whether the atom can preserve useful vector information as well as frequency and power.

## Slide 4 — Polarisation and AoA

Polarisation is useful because two signals can have the same frequency and the same total field magnitude but different vector states. Horizontal, vertical and circular fields can therefore look identical to a scalar amplitude detector. That extra information matters for antenna and field metrology, co-channel separation and direction finding. There is one nuance I want to state clearly: polarisation does not give angle of arrival by itself. For a plane wave, the electric field is transverse to the propagation direction, so measuring the vector narrows the direction problem. A complete AoA solution still needs additional spatial, phase or vector information. Polarisation is therefore a valuable constraint, not a substitute for an array.

## Slide 5 — Thesis architecture

This is the measurement logic I want you to keep in mind. I do not need one atomic spectrum to distinguish every possible state on its own. A linear projection gives the H-versus-V and diagonal information. Magnetic bias gives the atom a reference axis so opposite circular components can couple through different sigma pathways. Those complementary measurements become the three Stokes coordinates. The Stokes sphere is therefore not the novelty. The contribution is the calibrated route from the unknown field, through physically interpretable projections, to an atomic estimate with a conventional reference and uncertainty.

## Slide 6 — Magnetic bias and handedness

Now we can see why magnetic bias is useful. The bias field defines the quantisation axis. In the favourable geometry where the bias is along the propagation direction, right- and left-hand circular components map to opposite sigma transitions. The reduced model therefore predicts different optical spectra for equal-power R and L states. That is the handedness observable. The same model also exposes an important limitation: horizontal and vertical linear states are not separated by this geometry alone. That is why the passive linear analyser is not redundant; the two channels are complementary.

## Slide 7 — Measured linear analyser

The complementary linear channel is already measured. At two gigahertz, the linear selector produced 9.7 decibels of horizontal-to-vertical contrast in the current run. Converting the dBm readings to linear power gives a preliminary linear Stokes estimate with a degree of linear polarisation of about 0.89 and an angle of roughly 12.3 degrees from horizontal. This is not yet a calibrated full result: it is one run, the analyser is treated as ideal, and the 135-degree projection is missing. But it does show the mechanism we need — rotation of the linear analyser changes the measured projection in a predictable way.

## Slide 8 — Stokes coordinates

Stokes parameters are just a compact bookkeeping system for these independent projections. S-one compares horizontal and vertical. S-two compares the two diagonal linear states. S-three compares right and left circular. That is why the measurement architecture matters: the linear selector supplies the first two coordinates, while the handedness-sensitive atomic channel supplies the third. Once those channels are calibrated, every fully polarised state has one unique location in this three-dimensional space.

## Slide 9 — Poincaré sphere

This answers a question that often comes up when people first see a Poincaré sphere: why is there only one point? Because the sphere is the space of all possible states; it does not fill itself automatically. One generated field gives one point. If I continuously rotate a linear source, the point traces the equator. Circular states sit at the poles, and elliptical states lie between. The final experiment is therefore extremely clear: generate known states, reconstruct them atomically, and compare the recovered points against conventional ground truth with uncertainty regions.

## Slide 10 — What can we claim today?

This is the claim boundary I would defend. We have real atomic readout, a measured linear projection chain and a preliminary linear Stokes estimate. We also have a physically grounded selection-rule mechanism that predicts opposite circular handedness will produce different biased spectra. What we do not yet have is the decisive end-to-end atomic Stokes validation. I prefer to state that clearly because it makes the contribution stronger, not weaker: the remaining experiment is now well defined and falsifiable.

## Slide 11 — Why the result matters

If this full-Stokes loop is closed, the benefit is not simply a prettier sphere. It gives the receiver a vector descriptor beside frequency and power. That can constrain direction finding, help separate overlapping signals, support antenna and field metrology, and directly identify circular handedness in applications such as satellite links. The practical message is that atoms do not need to replace conventional antennas; the interesting capability is an independent optical vector measurement that can be fused with them.

## Slide 12 — Next experiments

The remaining work falls naturally into three stages. First, close the circular channel by independently calibrating handedness and repeating biased atomic spectra. Second, validate the complete polarimeter on held-out states against conventional ground truth. Third, test the effects that matter outside the laboratory: temperature, reflections, field enhancement and geometry. That includes the reflector and metasurface work in the wider group and using LIV as a practical RF-signature platform. The goal is not only to recover a state once, but to know when that state estimate remains trustworthy in the field.

## Slide 13 — Takeaway

So the take-home message is this. First, the Rydberg atom gives us an RF-sensitive optical spectrum. Second, complementary analyser channels let us turn polarisation into independent observables: a linear angle-sensitive channel and a bias-defined circular channel. Third, the Stokes representation gives us a clean validation target. The work is not complete full-Stokes atomic polarimetry yet, but the partial measurement is real, the missing channel is physically identified, and the final experiment is now precise enough to succeed or fail unambiguously.

## Slide 14 — Questions

Thank you. I’m happy to discuss the atomic physics, the polarisation measurements, the simulation assumptions, or the broader Quantum RF Sensing programme. The QR code links to the group site and the projects around this receiver platform.