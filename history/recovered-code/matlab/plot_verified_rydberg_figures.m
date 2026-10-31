%% plot_verified_rydberg_figures.m
% Verified screenshot-derived figures for Ryan Verghese's Rydberg thesis.
% MATLAB R2025a. No specialist toolbox required for plotting.
%
% IMPORTANT:
% 1) The horizontal coordinates visible on the DLC pro are PIEZO SCAN VOLTAGE.
% 2) TOPTICA labels Scan Amp as V pp (peak-to-peak), therefore:
%       59.4 V offset, 11 Vpp -> nominal 53.9 to 64.9 V sweep
%       70.0 V offset,  9 Vpp -> nominal 65.5 to 74.5 V sweep
% 3) Do NOT relabel the axis as wavelength or MHz detuning until the laser
%    scan is independently calibrated. Separate calibration arrays are
%    provided below.
% 4) The single EIT feature is an ENSEMBLE-DERIVED reconstruction from six
%    high-resolution screenshots. It is not a fabricated ideal EIT curve.
%    Each scan was locally modeled as a slowly varying linear grating
%    background plus a positive Lorentzian transparency component; the
%    transparency centers were allowed to shift from scan to scan while a
%    common width was constrained across all six scans. The plotted markers
%    are the baseline-corrected, aligned, binned experimental points.
%
% Use wording such as:
%   "Digitized probe photodetector response"
% and
%   "Ensemble-aligned representative EIT feature"
% rather than claiming an absolute transmission or MHz linewidth without
% dark-reference and frequency calibration data.

clear; clc; close all;
rootDir = fileparts(mfilename('fullpath'));
outDir = fullfile(rootDir,'figures');
if ~exist(outDir,'dir'), mkdir(outDir); end

D780 = readtable(fullfile(rootDir,'digitized_780_verified.csv'));
DEIT = readtable(fullfile(rootDir,'representative_EIT_ensemble.csv'));
DQ   = readtable(fullfile(rootDir,'digitized_EIT_direct_scans.csv'));
FS   = readtable(fullfile(rootDir,'EIT_fit_summary.csv'));

%% ------------------------------------------------------------------------
% OPTIONAL CALIBRATION
% -------------------------------------------------------------------------
% Enter measured wavemeter points only. Keep NaN until measured.
% 780-only absorption scan calibration:
cal780_V  = [NaN NaN];
cal780_nm = [NaN NaN];

% EIT scan calibration. This may NOT be identical to the 780-only scan if
% laser operating conditions differ, so it is deliberately separate.
calEIT_V  = [NaN NaN];
calEIT_nm = [NaN NaN];

% Optional known optical reference wavelength for detuning (nm).
% Use the actual experimental transition/reference, not a guessed value.
lambdaRef780_nm = NaN;
lambdaRefEIT_nm = NaN;

have780cal = all(isfinite(cal780_V)) && all(isfinite(cal780_nm)) && diff(cal780_V)~=0;
haveEITcal = all(isfinite(calEIT_V)) && all(isfinite(calEIT_nm)) && diff(calEIT_V)~=0;

%% ------------------------------------------------------------------------
% STYLE
% -------------------------------------------------------------------------
set(groot,'defaultAxesFontName','Times New Roman');
set(groot,'defaultTextFontName','Times New Roman');
set(groot,'defaultAxesFontSize',9);
set(groot,'defaultAxesLineWidth',0.8);
set(groot,'defaultLineLineWidth',1.2);

%% ========================================================================
% FIGURE 1 — VERIFIED 780-nm PROBE ABSORPTION SCAN
% ========================================================================
V = D780.scan_voltage_V;
Y = D780.photodetector_relative_mV;

% A very light smoothing is used only to suppress screenshot pixelation.
% The CSV is already digitized from the actual blue DLC-pro trace.
Ys = smoothdata(Y,'movmean',7);

if have780cal
    p = polyfit(cal780_V,cal780_nm,1);
    lambda = polyval(p,V);
    if isfinite(lambdaRef780_nm)
        c0 = 299792458;
        X = (c0./(lambda*1e-9) - c0/(lambdaRef780_nm*1e-9))/1e6;
        xlab = 'Probe detuning (MHz)';
    else
        X = lambda;
        xlab = 'Probe wavelength (nm)';
    end
else
    X = V;
    xlab = '780-nm laser piezo scan voltage (V)';
end

f1 = figure('Color','w','Units','centimeters','Position',[2 2 11.5 7.5]);
ax = axes(f1); hold(ax,'on');
plot(ax,X,Ys,'-','LineWidth',1.45);
idx = 1:20:numel(X);
plot(ax,X(idx),Y(idx),'.','MarkerSize',6);

xlabel(ax,xlab);
ylabel(ax,'Probe detector signal relative to display offset (mV)');
title(ax,'780-nm probe absorption scan','FontWeight','normal');
box(ax,'on'); grid(ax,'on'); ax.GridAlpha=0.12; ax.TickDir='out';
xlim(ax,[min(X) max(X)]);

[~,imin] = min(Ys);
plot(ax,X(imin),Ys(imin),'o','MarkerSize',5,'LineWidth',1);

if ~have780cal
    text(ax,0.02,0.05, ...
        'Piezo-voltage axis verified; wavelength/detuning requires calibration', ...
        'Units','normalized','FontSize',7.5,'VerticalAlignment','bottom');
end

exportgraphics(f1,fullfile(outDir,'Fig1_780_verified.pdf'),'ContentType','vector');
exportgraphics(f1,fullfile(outDir,'Fig1_780_verified.png'),'Resolution',600);

%% ========================================================================
% FIGURE 2 — SINGLE REPRESENTATIVE EIT FEATURE
% ========================================================================
% DEIT markers are actual digitized experimental points after:
%   (i) local linear-background subtraction,
%   (ii) amplitude normalization,
%   (iii) scan-to-scan peak alignment,
%   (iv) binning across the six screenshots.
% The dashed line is the jointly constrained phenomenological Lorentzian.

DV = DEIT.relative_scan_voltage_V;
Ymed = DEIT.measured_median;
Y16  = DEIT.measured_p16;
Y84  = DEIT.measured_p84;
Yfit = DEIT.joint_lorentzian_fit;

if haveEITcal
    % Convert relative piezo voltage to local optical frequency shift using
    % the measured linear wavelength-vs-voltage calibration around the
    % fitted EIT center. This is a local first-order conversion only.
    pE = polyfit(calEIT_V,calEIT_nm,1);
    Vc = median(FS.fit_center_voltage_V);
    lam0 = polyval(pE,Vc);
    lamDV = polyval(pE,Vc + DV);
    c0 = 299792458;
    X2 = (c0./(lamDV*1e-9)-c0/(lam0*1e-9))/1e6;
    xlab2 = 'Relative probe detuning (MHz)';
else
    X2 = DV;
    xlab2 = 'Relative piezo scan voltage, \DeltaV (V)';
end

f2 = figure('Color','w','Units','centimeters','Position',[2 2 11.5 7.5]);
ax2 = axes(f2); hold(ax2,'on');

% uncertainty envelope
fill(ax2,[X2; flipud(X2)],[Y16; flipud(Y84)], ...
    [0.85 0.85 0.85],'EdgeColor','none','FaceAlpha',0.55);
plot(ax2,X2,Ymed,'o','MarkerSize',4.2,'LineWidth',0.8);
plot(ax2,X2,Yfit,'--','LineWidth',1.45);

xlabel(ax2,xlab2);
ylabel(ax2,'Normalized EIT transparency component (a.u.)');
title(ax2,'Ensemble-aligned representative EIT feature','FontWeight','normal');
legend(ax2,{'16--84% scan-to-scan envelope','Digitized ensemble median', ...
            'Joint phenomenological Lorentzian'}, ...
       'Location','south','Box','off','FontSize',8);
box(ax2,'on'); grid(ax2,'on'); ax2.GridAlpha=0.12; ax2.TickDir='out';
xlim(ax2,[min(X2) max(X2)]); ylim(ax2,[0 1.12]);

if ~haveEITcal
    text(ax2,0.02,0.95, ...
        sprintf('Common fitted width = %.3f V (piezo coordinate only)',FS.common_FWHM_piezo_V(1)), ...
        'Units','normalized','FontSize',7.5,'VerticalAlignment','top');
else
    text(ax2,0.02,0.95,'Frequency-calibrated local detuning axis', ...
        'Units','normalized','FontSize',7.5,'VerticalAlignment','top');
end

exportgraphics(f2,fullfile(outDir,'Fig2_representative_EIT.pdf'),'ContentType','vector');
exportgraphics(f2,fullfile(outDir,'Fig2_representative_EIT.png'),'Resolution',600);

%% ========================================================================
% FIGURE 3 — QUALITY-CONTROL / APPENDIX VIEW OF THE SIX EIT SCANS
% ========================================================================
% This figure is intentionally not the main presentation figure. It exists
% to show that the representative peak above is derived from real variable
% scans rather than from an ideal curve invented afterward.

f3 = figure('Color','w','Units','centimeters','Position',[2 2 15.5 8.5]);
ax3 = axes(f3); hold(ax3,'on');
scanNames = compose('scan_%d_normalized',1:6);
for k=1:6
    y = DQ.(scanNames{k});
    y = smoothdata(y,'movmean',5);
    plot(ax3,DQ.scan_voltage_V,y + 1.15*(k-1),'LineWidth',0.9);
end
xlabel(ax3,'Laser piezo scan voltage (V)');
ylabel(ax3,'Normalized detector signal + offset');
title(ax3,'Repeated EIT-bearing scans used in the ensemble reconstruction', ...
      'FontWeight','normal');
box(ax3,'on'); grid(ax3,'on'); ax3.GridAlpha=0.08; ax3.TickDir='out';
xlim(ax3,[65.5 74.5]); yticklabels(ax3,{});
for k=1:6
    xline(ax3,FS.fit_center_voltage_V(k),':','LineWidth',0.7);
end
exportgraphics(f3,fullfile(outDir,'Fig3_EIT_repeatability_QC.pdf'),'ContentType','vector');
exportgraphics(f3,fullfile(outDir,'Fig3_EIT_repeatability_QC.png'),'Resolution',600);

fprintf('\nVerified Rydberg figures written to:\n%s\n',outDir);
fprintf('780 nominal scan span: %.3f to %.3f V\n',min(D780.scan_voltage_V),max(D780.scan_voltage_V));
fprintf('EIT nominal scan span: %.3f to %.3f V\n',min(DQ.scan_voltage_V),max(DQ.scan_voltage_V));
fprintf('Joint EIT phenomenological FWHM: %.4f V (NOT MHz until calibrated)\n', ...
        FS.common_FWHM_piezo_V(1));
fprintf('Joint local-fit R^2: %.5f\n\n',FS.joint_fit_R2(1));