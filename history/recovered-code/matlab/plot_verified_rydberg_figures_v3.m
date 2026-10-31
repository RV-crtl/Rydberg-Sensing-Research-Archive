%% plot_verified_rydberg_figures_v3.m
% Experimental Rydberg optical figures reconstructed from DLC-pro photos.
% MATLAB R2025a. Plotting and fitting use base MATLAB only.
%
% IMPORTANT SCIENTIFIC STATUS
% ---------------------------
% FIGURE 1:
%   Directly digitized 780-nm photodetector trace. A smooth
%   "quadratic baseline + two overlapping Gaussian absorption components"
%   is used only as a presentation-quality envelope so screenshot pixel
%   noise does not distort the trough. The Gaussian components are NOT
%   assigned to specific hyperfine transitions without a frequency axis.
%
% FIGURE 2:
%   Six directly digitized EIT-bearing traces were locally baseline
%   corrected and their recurring positive feature was aligned to DeltaV=0.
%   Only the central +/-0.30 V region is compared with a weak-probe
%   three-level ladder-EIT susceptibility model.
%
%   The theoretical weak-probe coherence used is proportional to
%
%       rho_ge/Omega_p =
%         i(gamma_gr - i*delta) /
%         [gamma_ge(gamma_gr - i*delta) + Omega_c^2/4]
%
%   for the probe close to one-photon resonance and the coupling laser
%   scanned through two-photon detuning. Probe transmission is modeled as
%
%       T ~ exp[-OD * Im(rho_ge/Omega_p)].
%
%   Because the DLC piezo voltage has NOT been independently calibrated in
%   MHz, fitted rate-like quantities are shape parameters only. Do not
%   quote gamma or Omega in MHz from this script.
%
% DEFAULT EIT X-AXIS:
%   The supplied EIT screenshots are treated as scans of the 480-nm
%   coupling-laser DLC. If that DLC was actually the 780-nm probe laser,
%   change scannedLaserLabel below before using the figure.

clear; clc; close all;

rootDir = fileparts(mfilename('fullpath'));
outDir = fullfile(rootDir,'figures');
if ~exist(outDir,'dir'), mkdir(outDir); end

D780 = readtable(fullfile(rootDir,'digitized_780_v3.csv'));
DEIT = readtable(fullfile(rootDir,'EIT_theory_guided_reconstruction_v3.csv'));
DRAW = readtable(fullfile(rootDir,'digitized_EIT_v3_scans.csv'));
PK   = readtable(fullfile(rootDir,'EIT_peak_locations_v3.csv'));
FS   = readtable(fullfile(rootDir,'fit_summary_v3.csv'));

scannedLaserLabel = '480-nm coupling-laser';

%% OPTIONAL FREQUENCY CALIBRATION
% Supply measured calibration points only.
% More than two points are preferable because piezo tuning can be nonlinear.
cal780_V   = [NaN NaN];
cal780_nm  = [NaN NaN];

calEIT_V   = [NaN NaN];
calEIT_nm  = [NaN NaN];

have780cal = all(isfinite(cal780_V)) && all(isfinite(cal780_nm));
haveEITcal = all(isfinite(calEIT_V)) && all(isfinite(calEIT_nm));

%% STYLE
set(groot,'defaultAxesFontName','Times New Roman');
set(groot,'defaultTextFontName','Times New Roman');
set(groot,'defaultAxesFontSize',9);
set(groot,'defaultAxesLineWidth',0.8);
set(groot,'defaultLineLineWidth',1.15);

%% ========================================================================
% FIGURE 1 — 780-nm PROBE TRANSMISSION / ABSORPTION FEATURE
% ========================================================================
V = D780.scan_voltage_V;
Y = D780.photodetector_relative_mV;
Yfit = D780.smooth_absorption_fit_mV;

if have780cal
    p = polyfit(cal780_V,cal780_nm,min(numel(cal780_V)-1,2));
    X = polyval(p,V);
    xlab1 = '780-nm probe wavelength (nm)';
else
    X = V;
    xlab1 = '780-nm probe piezo scan voltage (V)';
end

f1 = figure('Color','w','Units','centimeters','Position',[2 2 12.2 7.1]);
ax1 = axes(f1); hold(ax1,'on');

idx = 1:18:numel(X);
plot(ax1,X(idx),Y(idx),'.','MarkerSize',7);
plot(ax1,X,Yfit,'-','LineWidth',1.45);

xlabel(ax1,xlab1);
ylabel(ax1,'Photodetector signal relative to display offset (mV)');
legend(ax1,{'Digitized measurement', ...
    'Smooth overlapping-absorption fit'}, ...
    'Location','best','Box','off','FontSize',8);

box(ax1,'on');
grid(ax1,'on');
ax1.GridAlpha = 0.10;
ax1.TickDir = 'out';
xlim(ax1,[min(X) max(X)]);

exportgraphics(f1,fullfile(outDir,'Fig1_780_probe_v3.pdf'), ...
    'ContentType','vector');
exportgraphics(f1,fullfile(outDir,'Fig1_780_probe_v3.png'), ...
    'Resolution',600);

%% ========================================================================
% FIGURE 2 — THEORY-GUIDED REPRESENTATIVE EIT PEAK
% ========================================================================
DV = DEIT.relative_scan_voltage_V;
Ym = DEIT.experimental_median_normalized;
Ylo = DEIT.experimental_p16_normalized;
Yhi = DEIT.experimental_p84_normalized;
Yth = DEIT.three_level_EIT_theory_fit;
use = logical(DEIT.used_for_theory_fit);

if haveEITcal
    % Local first-order conversion around the median measured peak center.
    p = polyfit(calEIT_V,calEIT_nm,min(numel(calEIT_V)-1,2));
    V0 = median(PK.refined_peak_V);
    lam0 = polyval(p,V0);
    lam = polyval(p,V0 + DV);
    c0 = 299792458;
    X2 = (c0./(lam*1e-9) - c0/(lam0*1e-9))/1e6;
    xlab2 = sprintf('Relative %s detuning (MHz)',scannedLaserLabel);
else
    X2 = DV;
    xlab2 = sprintf('Relative %s piezo scan voltage, \\DeltaV (V)', ...
        scannedLaserLabel);
end

f2 = figure('Color','w','Units','centimeters','Position',[2 2 12.2 7.1]);
ax2 = axes(f2); hold(ax2,'on');

Xu = X2(use);
fill(ax2,[Xu;flipud(Xu)],[Ylo(use);flipud(Yhi(use))], ...
    [0.85 0.85 0.85],'EdgeColor','none','FaceAlpha',0.5);

plot(ax2,Xu,Ym(use),'o','MarkerSize',3.8,'LineWidth',0.75);
plot(ax2,Xu,Yth(use),'-','LineWidth',1.45);

xlabel(ax2,xlab2);
ylabel(ax2,'Normalized EIT contrast');
legend(ax2,{'Inter-scan variation (16th--84th percentile)', ...
            'Aligned digitized measurement', ...
            'Weak-probe three-level EIT model'}, ...
    'Location','best','Box','off','FontSize',8);

box(ax2,'on');
grid(ax2,'on');
ax2.GridAlpha=0.10;
ax2.TickDir='out';
xlim(ax2,[min(Xu) max(Xu)]);
ylim(ax2,[-0.15 1.12]);

exportgraphics(f2,fullfile(outDir,'Fig2_EIT_theory_guided_v3.pdf'), ...
    'ContentType','vector');
exportgraphics(f2,fullfile(outDir,'Fig2_EIT_theory_guided_v3.png'), ...
    'Resolution',600);

%% ========================================================================
% FIGURE 3 — APPENDIX/QC: SIX DIRECTLY DIGITIZED EIT-BEARING TRACES
% ========================================================================
f3 = figure('Color','w','Units','centimeters','Position',[2 2 15.5 8.0]);
ax3 = axes(f3); hold(ax3,'on');

for k=1:6
    y = DRAW.(sprintf('scan_%d_normalized',k));
    plot(ax3,DRAW.scan_voltage_V,y + 1.15*(k-1),'LineWidth',0.8);
    xline(ax3,PK.refined_peak_V(k),':','LineWidth',0.7);
end

xlabel(ax3,sprintf('%s piezo scan voltage (V)',scannedLaserLabel));
ylabel(ax3,'Normalized detector signal + offset');
box(ax3,'on');
grid(ax3,'on');
ax3.GridAlpha=0.07;
ax3.TickDir='out';
xlim(ax3,[65.5 74.5]);
yticklabels(ax3,{});

exportgraphics(f3,fullfile(outDir,'Fig3_EIT_raw_repeatability_v3.pdf'), ...
    'ContentType','vector');
exportgraphics(f3,fullfile(outDir,'Fig3_EIT_raw_repeatability_v3.png'), ...
    'Resolution',600);

fprintf('\nRydberg optical reconstruction v3\n');
fprintf('----------------------------------------\n');
fprintf('780 fit R^2 = %.5f\n',FS.absorption_fit_R2(1));
fprintf('780 fit RMSE = %.4f mV\n',FS.absorption_fit_RMSE_mV(1));
fprintf('EIT central line-shape R^2 = %.5f\n',FS.EIT_shape_fit_R2(1));
fprintf('EIT central normalized RMSE = %.4f\n', ...
    FS.EIT_shape_fit_RMSE_normalized(1));
fprintf(['No EIT linewidth or Rabi frequency in MHz is valid until ', ...
         'piezo-to-frequency calibration is supplied.\n']);
fprintf('Figures saved to:\n%s\n\n',outDir);