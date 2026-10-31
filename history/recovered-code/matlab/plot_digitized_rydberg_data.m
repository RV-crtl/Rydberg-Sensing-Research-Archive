%% plot_digitized_rydberg_data.m
% Digitized from DLC Pro screenshots supplied on 27 Aug 2026.
% MATLAB R2025a compatible.
%
% IMPORTANT SCIENTIFIC LIMITATION
% --------------------------------
% The screenshots define the PIEZO SCAN VOLTAGE, but they do not provide
% a defensible wavelength-vs-voltage calibration. Therefore the script
% plots scan voltage by default.
%
% To obtain a wavelength or detuning axis, enter TWO wavemeter calibration
% points below. Do not insert an assumed nm/V value unless independently
% measured.
%
% Figure 1:
%   780-nm probe transmission / absorption scan.
%
% Figure 2:
%   Repeated EIT-bearing scans with 780 + 480 nm lasers.
%   The second panel uses vertical offsets only for visibility.
%
% The EIT data are intentionally NOT forced into a Lorentzian fit because
% the supplied screenshots show a strongly variable / periodic grating
% response. A linewidth fit should only be performed on a calibrated,
% isolated EIT resonance or on raw oscilloscope/DAQ data.

clear; clc; close all;

rootDir = fileparts(mfilename('fullpath'));
D780 = readtable(fullfile(rootDir,'digitized_780nm_transmission.csv'));
DEIT = readtable(fullfile(rootDir,'digitized_EIT_repeated_scans.csv'));

%% ========================================================================
% OPTIONAL WAVELENGTH CALIBRATION
% =========================================================================
%
% Enter two measured wavemeter points:
%
%   calibrationVoltage_V = [V1 V2];
%   calibrationLambda_nm = [lambda1 lambda2];
%
% Example structure ONLY:
%   calibrationVoltage_V = [56.0 63.0];
%   calibrationLambda_nm = [NaN NaN];
%
% Leave NaN until you have real wavemeter values.

calibrationVoltage_V = [NaN NaN];
calibrationLambda_nm = [NaN NaN];

% Optional reference wavelength for detuning.
% Replace only with the actual experimental resonance/reference.
lambdaReference_nm = NaN;

haveLambdaCalibration = all(isfinite(calibrationVoltage_V)) && ...
                        all(isfinite(calibrationLambda_nm)) && ...
                        diff(calibrationVoltage_V) ~= 0;

if haveLambdaCalibration
    pLambda = polyfit(calibrationVoltage_V, calibrationLambda_nm, 1);

    lambda780_nm = polyval(pLambda,D780.scan_voltage_V);
    lambdaEIT_nm = polyval(pLambda,DEIT.scan_voltage_V);

    if isfinite(lambdaReference_nm)
        c = 299792458;
        det780_MHz = (c./(lambda780_nm*1e-9) - ...
                      c/(lambdaReference_nm*1e-9))/1e6;
        detEIT_MHz = (c./(lambdaEIT_nm*1e-9) - ...
                      c/(lambdaReference_nm*1e-9))/1e6;
    else
        det780_MHz = [];
        detEIT_MHz = [];
    end
else
    lambda780_nm = [];
    lambdaEIT_nm = [];
    det780_MHz = [];
    detEIT_MHz = [];
end

%% ========================================================================
% GLOBAL FIGURE STYLE
% =========================================================================

set(groot,'defaultAxesFontName','Times New Roman');
set(groot,'defaultTextFontName','Times New Roman');
set(groot,'defaultAxesFontSize',9);
set(groot,'defaultAxesLineWidth',0.8);
set(groot,'defaultLineLineWidth',1.2);

outDir = fullfile(rootDir,'figures');
if ~exist(outDir,'dir')
    mkdir(outDir);
end

%% ========================================================================
% FIGURE 1 — 780-nm PROBE TRANSMISSION
% =========================================================================

f1 = figure('Color','w','Units','centimeters','Position',[2 2 9.0 7.0]);
ax1 = axes(f1);
hold(ax1,'on');

% Main publication curve.
if haveLambdaCalibration
    x1 = lambda780_nm;
    xLabel1 = 'Probe wavelength (nm)';
else
    x1 = D780.scan_voltage_V;
    xLabel1 = '780-nm laser piezo scan voltage (V)';
end

% Sparse markers show the fact that this was digitized from measured data;
% the line is the smoothed baseline-normalized reconstruction.
idxMark = 1:18:height(D780);

plot(ax1,x1,D780.baseline_normalized_transmission,'-');
plot(ax1,x1(idxMark), ...
    D780.baseline_normalized_transmission(idxMark), ...
    '.','MarkerSize',7);

xlabel(ax1,xLabel1);
ylabel(ax1,'Baseline-normalized transmission (a.u.)');

title(ax1,'780-nm probe transmission');

box(ax1,'on');
grid(ax1,'on');
ax1.GridAlpha = 0.12;
ax1.MinorGridAlpha = 0.06;
ax1.TickDir = 'out';

% Mark the strongest absorption minimum.
[~,iMin] = min(D780.baseline_normalized_transmission);
xMin = x1(iMin);
yMin = D780.baseline_normalized_transmission(iMin);

plot(ax1,xMin,yMin,'o','MarkerSize',5,'LineWidth',1.0);

if haveLambdaCalibration
    text(ax1,xMin,yMin, ...
        sprintf('  %.6f nm',xMin), ...
        'VerticalAlignment','bottom', ...
        'FontSize',8);
else
    text(ax1,xMin,yMin, ...
        sprintf('  %.3f V',xMin), ...
        'VerticalAlignment','bottom', ...
        'FontSize',8);
end

% Optional detuning axis is deliberately not fabricated.
if haveLambdaCalibration && isfinite(lambdaReference_nm)
    % Add detuning information as a small annotation rather than a second
    % physical axis, avoiding ambiguity from the wavelength-frequency
    % nonlinearity.
    detMin = det780_MHz(iMin);
    text(ax1,0.03,0.04, ...
        sprintf('\\Delta/2\\pi at minimum = %.1f MHz',detMin), ...
        'Units','normalized', ...
        'FontSize',8);
elseif ~haveLambdaCalibration
    text(ax1,0.03,0.04, ...
        'Wavelength axis requires two wavemeter calibration points', ...
        'Units','normalized', ...
        'FontSize',7.5);
end

exportgraphics(f1,fullfile(outDir,'F_780nm_probe_transmission.pdf'), ...
    'ContentType','vector');
exportgraphics(f1,fullfile(outDir,'F_780nm_probe_transmission.png'), ...
    'Resolution',600);

%% ========================================================================
% FIGURE 2 — REPEATED EIT-BEARING SCANS
% =========================================================================

scanNames = compose('scan_%d_normalized',1:6);

if haveLambdaCalibration
    x2 = lambdaEIT_nm;
    xLabel2 = 'Probe wavelength (nm)';
else
    x2 = DEIT.scan_voltage_V;
    xLabel2 = 'Laser piezo scan voltage (V)';
end

f2 = figure('Color','w','Units','centimeters','Position',[2 2 18.0 11.0]);
tl = tiledlayout(f2,2,1,'TileSpacing','compact','Padding','compact');

% ------------------------------------------------------------------------
% Panel (a): all scans on the same normalized scale
% ------------------------------------------------------------------------
ax2 = nexttile(tl,1);
hold(ax2,'on');

for k = 1:numel(scanNames)
    y = DEIT.(scanNames{k});
    plot(ax2,x2,y,'LineWidth',0.9);
end

xlabel(ax2,xLabel2);
ylabel(ax2,'Normalized transmission (a.u.)');
title(ax2,'Repeated EIT-bearing scans: 780 + 480 nm');

box(ax2,'on');
grid(ax2,'on');
ax2.GridAlpha = 0.10;
ax2.TickDir = 'out';

legend(ax2,compose('Scan %d',1:6), ...
    'Location','eastoutside', ...
    'Box','off');

% ------------------------------------------------------------------------
% Panel (b): vertically stacked traces
% This makes the repeating / phase-shifting structure obvious without
% averaging it away.
% ------------------------------------------------------------------------
ax3 = nexttile(tl,2);
hold(ax3,'on');

offsetStep = 1.15;

for k = 1:numel(scanNames)
    y = DEIT.(scanNames{k});
    yOff = y + (k-1)*offsetStep;
    plot(ax3,x2,yOff,'LineWidth',1.0);

    text(ax3,x2(1), ...
        median(yOff(1:min(30,end))), ...
        sprintf('  Scan %d',k), ...
        'FontSize',8, ...
        'VerticalAlignment','middle');
end

xlabel(ax3,xLabel2);
ylabel(ax3,'Normalized transmission + offset');
title(ax3,'Same scans stacked to expose the periodic grating response');

box(ax3,'on');
grid(ax3,'on');
ax3.GridAlpha = 0.08;
ax3.TickDir = 'out';
yticklabels(ax3,{});

% Figure-level note.
annotation(f2,'textbox',[0.56 0.01 0.42 0.045], ...
    'String', ...
    ['Digitized from DLC Pro display. No EIT linewidth is extracted ', ...
     'because the resonance is not independently frequency calibrated.'], ...
    'EdgeColor','none', ...
    'HorizontalAlignment','right', ...
    'FontName','Times New Roman', ...
    'FontSize',7.5);

exportgraphics(f2,fullfile(outDir,'F_EIT_repeated_grating_scans.pdf'), ...
    'ContentType','vector');
exportgraphics(f2,fullfile(outDir,'F_EIT_repeated_grating_scans.png'), ...
    'Resolution',600);

%% ========================================================================
% NUMERICAL SUMMARY
% =========================================================================

fprintf('\nDIGITIZED RYDBERG DATA FIGURES\n');
fprintf('---------------------------------------------\n');
fprintf('780 scan: %.3f to %.3f V\n', ...
    min(D780.scan_voltage_V),max(D780.scan_voltage_V));
fprintf('EIT scans: %.3f to %.3f V\n', ...
    min(DEIT.scan_voltage_V),max(DEIT.scan_voltage_V));

if haveLambdaCalibration
    fprintf('Wavelength calibration active.\n');
    fprintf('780 wavelength span: %.9f to %.9f nm\n', ...
        min(lambda780_nm),max(lambda780_nm));
else
    fprintf(['No wavelength calibration applied. Add two wavemeter ', ...
        'points at the top of this script.\n']);
end

fprintf('Figures written to:\n%s\n\n',outDir);