%% analyse_new_polariser_data.m
% Ryan Verghese thesis - 19 Aug 2026 polariser measurements
%
% Purpose
%   1) Convert dBm readings to physically meaningful linear power and
%      relative electric-field amplitude.
%   2) Quantify insertion loss and polarization extinction ratio (PER).
%   3) Compare the three-angle data against a finite-extinction Malus/Jones model.
%   4) Estimate the principal-axis angular offset using the harmonic form
%      P(theta)=a+b*cos(2theta)+c*sin(2theta).
%   5) Summarise the sparse circular-antenna + linear-analyser measurements.
%
% IMPORTANT
%   - Perform Jones/Malus calculations in field amplitude or linear power,
%     never directly in dBm.
%   - There are only three linear-polarizer angular samples. The generalized
%     model has three parameters and therefore fits them exactly; the fitted
%     offset is a plausible interpretation, NOT a statistically validated fit.
%   - If the lab's 0 deg and 90 deg labels are reversed, swap the first and
%     last entries in theta_deg/Ppol_dBm. PER and the magnitude of the axis
%     offset are unchanged.

clear; clc; close all;

%% ----------------------- Raw measurements -------------------------------
noise_dBm = -66.7;

% Horn calibration / setup response
f_GHz       = [1.8, 1.9, 2.0];
Phorn_dBm   = [-20.6, -12.3, -9.8];

% Re-measurement at 2 GHz
P0_dBm      = -8.2;      % no linear polarizer

% Use an internally consistent angle convention:
% 0 deg = nominal pass orientation, 45 deg = intermediate,
% 90 deg = nominal reject orientation.
theta_deg   = [0, 45, 90];
Ppol_dBm    = [-13.9, -15.1, -23.6];

% Circular antenna measurements at 1.8 GHz from the email summary
Pcirc0_dBm  = -31;       % no linear polarizer
PcircPol_dBm = [-34, -33]; % two linear-analyser measurements

%% ----------------------- Unit conversions -------------------------------
dBm2mW = @(x) 10.^(x/10);
mW2dBm = @(x) 10*log10(x);

P0_mW   = dBm2mW(P0_dBm);
Ppol_mW = dBm2mW(Ppol_dBm);

Tpow = Ppol_mW ./ P0_mW; % power transmission relative to no-polarizer case
Erel = sqrt(Tpow);        % field-amplitude ratio because P proportional |E|^2

%% ----------------------- Direct metrics --------------------------------
[~, iPass]   = max(Ppol_dBm);
[~, iReject] = min(Ppol_dBm);

Ppass_dBm   = Ppol_dBm(iPass);
Preject_dBm = Ppol_dBm(iReject);

IL_pass_dB = P0_dBm - Ppass_dBm;
PER_dB     = Ppass_dBm - Preject_dBm;

power_ratio_pass_reject = 10^(PER_dB/10);
field_ratio_pass_reject = 10^(PER_dB/20);

% Ideal 45 deg prediction from the measured pass level only
P45_ideal_dBm = Ppass_dBm + 10*log10(0.5);

% More realistic finite-extinction prediction at 45 deg, assuming the
% nominal pass/reject measurements are exactly the principal axes:
Ppass_mW   = dBm2mW(Ppass_dBm);
Preject_mW = dBm2mW(Preject_dBm);
P45_finite_mW  = 0.5*(Ppass_mW + Preject_mW);
P45_finite_dBm = mW2dBm(P45_finite_mW);

[~, i45] = min(abs(theta_deg - 45));
P45_obs_dBm = Ppol_dBm(i45);

%% -------- Generalized Malus/Jones fit with angular zero offset ----------
% Any linear diattenuator measured by a linear analyzer can be written
%
%   P(theta) = a + b cos(2 theta) + c sin(2 theta)
%
% which is equivalent to
%
%   P(theta) = Pmax cos^2(theta-theta0)
%            + Pmin sin^2(theta-theta0)
%
% Fit in LINEAR POWER.
th = deg2rad(theta_deg(:));
X = [ones(size(th)), cos(2*th), sin(2*th)];
beta = X \ Ppol_mW(:);

a = beta(1);
b = beta(2);
c = beta(3);

Damp = hypot(b,c);
theta0_deg = 0.5*atan2d(c,b);

Pmax_fit_mW = a + Damp;
Pmin_fit_mW = a - Damp;

Pmax_fit_dBm = mW2dBm(Pmax_fit_mW);
Pmin_fit_dBm = mW2dBm(Pmin_fit_mW);
PER_fit_dB   = 10*log10(Pmax_fit_mW/Pmin_fit_mW);

% Distance of fitted principal pass axis from the nearest nominal 0/90 axis.
axis_offset_mag_deg = min(abs(theta0_deg - 90*round(theta0_deg/90)), ...
                          90-abs(theta0_deg - 90*round(theta0_deg/90)));
axis_offset_mag_deg = abs(axis_offset_mag_deg);

% Polarization diattenuation based on fitted principal transmissions.
Diattenuation = (Pmax_fit_mW - Pmin_fit_mW) / ...
                (Pmax_fit_mW + Pmin_fit_mW);

% Principal transmission coefficients relative to no-polarizer baseline
Tmax_fit = Pmax_fit_mW/P0_mW;
Tmin_fit = Pmin_fit_mW/P0_mW;
tmax_fit = sqrt(Tmax_fit);
tmin_fit = sqrt(Tmin_fit);

%% ----------------------- Circular-analyser summary ----------------------
circ_loss_dB = Pcirc0_dBm - PcircPol_dBm; % positive = attenuation
circ_Tpow = 10.^((PcircPol_dBm-Pcirc0_dBm)/10);

%% ----------------------- Console report --------------------------------
fprintf('\n============================================================\n');
fprintf('19 AUG 2026 LINEAR POLARIZER ANALYSIS\n');
fprintf('============================================================\n');
fprintf('2 GHz no-polarizer baseline            : %6.2f dBm\n', P0_dBm);
fprintf('Nominal pass                           : %6.2f dBm\n', Ppass_dBm);
fprintf('Nominal reject                         : %6.2f dBm\n', Preject_dBm);
fprintf('Pass insertion loss                    : %6.2f dB\n', IL_pass_dB);
fprintf('Direct pass/reject extinction (PER)    : %6.2f dB\n', PER_dB);
fprintf('Power ratio, pass/reject               : %6.2f : 1\n', power_ratio_pass_reject);
fprintf('Field ratio, pass/reject               : %6.2f : 1\n', field_ratio_pass_reject);
fprintf('\n');
fprintf('Observed nominal 45 deg level          : %6.2f dBm\n', P45_obs_dBm);
fprintf('Ideal lossless Malus prediction        : %6.2f dBm\n', P45_ideal_dBm);
fprintf('Finite-extinction 45 deg prediction    : %6.2f dBm\n', P45_finite_dBm);
fprintf('45 deg residual vs finite-ext model    : %+6.2f dB\n', ...
        P45_obs_dBm-P45_finite_dBm);
fprintf('\n');
fprintf('Generalized finite-extinction fit:\n');
fprintf('  fitted principal maximum             : %6.2f dBm\n', Pmax_fit_dBm);
fprintf('  fitted principal minimum             : %6.2f dBm\n', Pmin_fit_dBm);
fprintf('  implied principal PER                : %6.2f dB\n', PER_fit_dB);
fprintf('  principal-axis offset magnitude      : %6.2f deg\n', axis_offset_mag_deg);
fprintf('  fitted diattenuation                 : %6.3f\n', Diattenuation);
fprintf('  fitted field transmission t_parallel : %6.3f\n', tmax_fit);
fprintf('  fitted field transmission t_perp     : %6.3f\n', tmin_fit);
fprintf('\n');
fprintf('Noise floor                            : %6.2f dBm\n', noise_dBm);
fprintf('Reject point above noise               : %6.2f dB\n', Preject_dBm-noise_dBm);
fprintf('2 GHz calibration -> remeasurement shift: %+5.2f dB\n', ...
        P0_dBm-Phorn_dBm(end));
fprintf('\n');
fprintf('Circular source, 1.8 GHz:\n');
fprintf('  no polarizer                         : %6.2f dBm\n', Pcirc0_dBm);
for k = 1:numel(PcircPol_dBm)
    fprintf('  analyser reading %d                   : %6.2f dBm  (loss %.2f dB)\n', ...
        k, PcircPol_dBm(k), circ_loss_dB(k));
end
fprintf(['  NOTE: near-3-dB attenuation with weak angle dependence is qualitatively\n' ...
         '  compatible with circular/elliptical polarization, but these sparse\n' ...
         '  data do not establish handedness or axial ratio, especially because\n' ...
         '  the analyzer insertion loss at 1.8 GHz was not independently measured.\n']);
fprintf('============================================================\n\n');

%% ----------------------- Table ------------------------------------------
Results = table(theta_deg(:), Ppol_dBm(:), Tpow(:), Erel(:), ...
    Ppol_dBm(:)-noise_dBm, ...
    'VariableNames', {'Angle_deg','Measured_dBm','PowerTransmission', ...
                      'FieldAmplitudeRatio','dB_Above_Noise'});
disp(Results);

%% ----------------------- Figure style ----------------------------------
set(groot, 'defaultAxesFontName', 'Times New Roman');
set(groot, 'defaultTextFontName', 'Times New Roman');
set(groot, 'defaultAxesFontSize', 9);
set(groot, 'defaultLineLineWidth', 1.25);
set(groot, 'defaultFigureColor', 'w');

%% Figure 1: horn/system frequency response
figure('Units','centimeters','Position',[2 2 9.0 6.5]);
plot(f_GHz, Phorn_dBm, 'o-', 'MarkerFaceColor','w');
hold on;
plot(2.0, P0_dBm, 's', 'MarkerFaceColor','w');
xlabel('Frequency (GHz)');
ylabel('Received power (dBm)');
legend('Calibration sweep','2 GHz remeasurement','Location','southeast');
box on;
grid on;
exportgraphics(gcf,'horn_frequency_response.pdf','ContentType','vector');
exportgraphics(gcf,'horn_frequency_response.png','Resolution',600);

%% Figure 2: polarizer angular response in normalized power
thetaFine = linspace(0,180,721);

PfitFine_mW = a + b*cosd(2*thetaFine) + c*sind(2*thetaFine);
PfitFine_norm = PfitFine_mW/P0_mW;

% Zero-offset finite-extinction reference built only from nominal
% pass/reject values.
PrefFine_mW = Ppass_mW*cosd(thetaFine).^2 + ...
              Preject_mW*sind(thetaFine).^2;
PrefFine_norm = PrefFine_mW/P0_mW;

figure('Units','centimeters','Position',[2 2 9.0 6.8]);
plot(thetaFine, 10*log10(PfitFine_norm), '-', 'LineWidth',1.5);
hold on;
plot(thetaFine, 10*log10(PrefFine_norm), '--', 'LineWidth',1.0);
plot(theta_deg, 10*log10(Tpow), 'o', ...
     'MarkerSize',6,'MarkerFaceColor','w','LineWidth',1.25);
xlabel('Nominal polarizer angle (deg)');
ylabel('Relative received power (dB)');
xlim([0 180]);
xticks(0:45:180);
legend(sprintf('Generalized fit (axis offset \\approx %.1f^\\circ)',axis_offset_mag_deg), ...
       'Finite-extinction Malus, zero offset', ...
       'Measured', 'Location','best');
box on;
grid on;
exportgraphics(gcf,'linear_polarizer_angular_response.pdf','ContentType','vector');
exportgraphics(gcf,'linear_polarizer_angular_response.png','Resolution',600);

%% Figure 3: measured transmission in linear power
figure('Units','centimeters','Position',[2 2 9.0 6.5]);
stem(theta_deg, Tpow, 'filled', 'LineWidth',1.2);
xlabel('Nominal polarizer angle (deg)');
ylabel('Power transmission relative to no polarizer');
xlim([-5 95]);
xticks([0 45 90]);
ylim([0 max(Tpow)*1.25]);
box on;
grid on;
exportgraphics(gcf,'linear_polarizer_transmission.pdf','ContentType','vector');
exportgraphics(gcf,'linear_polarizer_transmission.png','Resolution',600);

%% Figure 4: circular antenna + linear analyser, sparse result
figure('Units','centimeters','Position',[2 2 9.0 6.5]);
vals = [Pcirc0_dBm PcircPol_dBm];
bar(1:numel(vals), vals);
hold on;
yline(noise_dBm,'--','Noise floor');
set(gca,'XTick',1:numel(vals), ...
    'XTickLabel',{'No analyser','Analyser A','Analyser B'});
ylabel('Received power (dBm)');
title('Circular-antenna measurements at 1.8 GHz');
box on;
grid on;
exportgraphics(gcf,'circular_antenna_sparse_analyser_test.pdf','ContentType','vector');
exportgraphics(gcf,'circular_antenna_sparse_analyser_test.png','Resolution',600);

%% ----------------------- Optional Jones matrix --------------------------
% A simple non-ideal linear polarizer Jones matrix in its principal basis is
%
%   J0 = [t_parallel   0
%         0            t_perp*exp(1j*delta)]
%
% and at angle theta:
%
%   J(theta) = R(-theta)*J0*R(theta)
%
% where R is a 2-D rotation matrix.
%
% With no phase information in the present power-only data, delta cannot be
% estimated. Set delta=0 only for a first-order diattenuator model.
delta = 0;
J0 = [tmax_fit, 0; 0, tmin_fit*exp(1j*delta)];

fprintf('Estimated first-order principal-basis Jones matrix (delta assumed 0):\n');
disp(J0);

%% ----------------------- Thesis-ready numerical summary -----------------
fprintf('\nTHESIS-READY SUMMARY (edit wording after checking angle labels):\n');
fprintf(['At 2.0 GHz, insertion of the linear polarizer produced a nominal pass\n' ...
         'level of %.1f dBm and reject level of %.1f dBm relative to a %.1f dBm\n' ...
         'no-polarizer reference. This corresponds to %.1f dB pass insertion loss\n' ...
         'and %.1f dB direct polarization extinction. The nominal 45-degree\n' ...
         'measurement was %.1f dBm, lying %.1f dB above the finite-extinction\n' ...
         'Malus prediction. A generalized Jones/Malus representation can account\n' ...
         'for the three points with an approximately %.1f-degree angular-zero\n' ...
         'offset and an implied principal extinction of %.1f dB; however, with\n' ...
         'only three angular measurements the model has zero residual degrees of\n' ...
         'freedom and should be treated as a physical interpretation rather than\n' ...
         'a statistically validated fit.\n'], ...
         Ppass_dBm, Preject_dBm, P0_dBm, IL_pass_dB, PER_dB, ...
         P45_obs_dBm, P45_obs_dBm-P45_finite_dBm, ...
         axis_offset_mag_deg, PER_fit_dB);