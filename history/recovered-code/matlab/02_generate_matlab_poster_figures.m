%% 02_generate_matlab_poster_figures.m
% =========================================================================
% RYDBERG POLARIMETRY POSTER FIGURES — MATLAB R2025a
%
% Generates high-quality IEEE/TQE-style figures that do NOT require ARC.
%
% READY NOW:
%   Fig. M1  Reduced-order probe -> EIT -> RF-dressed sequence (MODEL)
%   Fig. M2  Measured 2 GHz linear-polarizer angular response (MEASURED)
%   Fig. M3  Partial linear Stokes reconstruction in S1-S2 plane (MEASURED)
%   Fig. M4  Stokes component summary (MEASURED / S3 not measured)
%   Fig. M5  Normalized single-coil vs Helmholtz-pair axial field (ANALYTIC)
%
% DATA-DEPENDENT:
%   Fig. M6  RHCP/LHCP transmission and circular extinction ratio
%   Fig. M7  Axial ratio / relative phase (if supplied by full-wave solver)
%
% The CP figures are produced only if "cp_fullwave_results.csv" exists.
%
% TQE style:
%   - Times New Roman
%   - approximately 8 pt final figure text
%   - inward ticks, boxed axes
%   - quantity, symbol (unit) axis labels
%   - vector PDF + 600 dpi PNG
%
% IMPORTANT CLAIM BOUNDARY
%   Fig. M1 is a transparent REDUCED-ORDER teaching model, not Rydiqule
%   and not a calibrated digital twin. Use it to explain the mechanism.
%   Figs. M2-M4 use the 19 Aug 2026 measured polarizer readings.
%
% Run:
%   >> 02_generate_matlab_poster_figures
%
% =========================================================================

clear; clc; close all;

OUT = fullfile(pwd,'matlab_tqe_outputs');
if ~exist(OUT,'dir'), mkdir(OUT); end

%% ------------------------ Global TQE style -------------------------------
set(groot,'defaultFigureColor','w');
set(groot,'defaultAxesFontName','Times New Roman');
set(groot,'defaultTextFontName','Times New Roman');
set(groot,'defaultAxesFontSize',8);
set(groot,'defaultAxesLineWidth',0.8);
set(groot,'defaultLineLineWidth',1.25);
set(groot,'defaultAxesTickDir','in');
set(groot,'defaultAxesBox','on');
set(groot,'defaultAxesXGrid','off');
set(groot,'defaultAxesYGrid','off');
set(groot,'defaultLegendBox','off');
set(groot,'defaultLegendFontSize',7);

singleW = 8.9;   % cm ~ IEEE single column
doubleW = 18.2;  % cm ~ IEEE double column

fprintf('\n============================================================\n');
fprintf('MATLAB TQE POSTER FIGURE GENERATOR\n');
fprintf('============================================================\n');

%% ========================================================================
% FIG. M1 — RYDBERG RECEIVER SEQUENCE
% Reduced-order but mathematically transparent.
% ========================================================================

dp = linspace(-30,30,1601);   % MHz

% Broad probe absorption.
Tbase = 0.94 - 0.60*lorentzian(dp,0,10.5);

% EIT transparency.
eitWidth = 1.35;              % MHz, representative
eitAmp   = 0.52;
Teit = min(1, Tbase + eitAmp*lorentzian(dp,0,eitWidth));

% RF-dressed EIT: resonant two-state dressed splitting.
OmegaRF = 7.0;                % MHz, representative model value
deltaRF = 0.0;                % MHz
[pole1,pole2,w1,w2] = dressedPair(deltaRF,OmegaRF);
Trf = Tbase + eitAmp*( ...
      w1*lorentzian(dp,pole1,eitWidth) + ...
      w2*lorentzian(dp,pole2,eitWidth));
Trf = min(1,Trf);

f = figure('Units','centimeters','Position',[2 2 doubleW 8.5]);
plot(dp,Tbase,'-','LineWidth',1.2); hold on;
plot(dp,Teit,'--','LineWidth',1.5);
plot(dp,Trf,'-','LineWidth',1.5);
xline(0,':','LineWidth',0.8);
xlabel('Probe detuning, \Delta_p (MHz)');
ylabel('Normalized probe transmission, T_p');
xlim([-25 25]); ylim([0.25 1.02]);
legend('780 nm probe only','Probe + coupling (EIT)', ...
       'Probe + coupling + resonant RF','Location','best');
tqeAxes(gca);
exportTQE(f,OUT,'figM1_receiver_sequence');

fprintf('Fig. M1: reduced-order probe/EIT/RF sequence written.\n');

%% ========================================================================
% FIG. M2 — MEASURED LINEAR POLARIZER ANGULAR RESPONSE
% ========================================================================

P0_dBm    = -8.2;
theta_deg = [0 45 90];
P_dBm     = [-13.9 -15.1 -23.6];
noise_dBm = -66.7;

P0_mW = dbm2mw(P0_dBm);
PmW = dbm2mw(P_dBm);

% Direct measured metrics.
Ppass_dBm = max(P_dBm);
Prej_dBm  = min(P_dBm);
PER_dB = Ppass_dBm - Prej_dBm;
ILpass_dB = P0_dBm - Ppass_dBm;

% Finite-extinction Malus/Jones power model based strictly on measured
% principal pass/reject levels.
Ppass_mW = dbm2mw(Ppass_dBm);
Prej_mW  = dbm2mw(Prej_dBm);
th = linspace(0,90,721);
Pmodel_mW = Ppass_mW*cosd(th).^2 + Prej_mW*sind(th).^2;
Pmodel_rel_dB = 10*log10(Pmodel_mW/P0_mW);
Pmeas_rel_dB = P_dBm - P0_dBm;

f = figure('Units','centimeters','Position',[2 2 singleW 6.7]);
plot(th,Pmodel_rel_dB,'-','LineWidth',1.35); hold on;
plot(theta_deg,Pmeas_rel_dB,'o','MarkerSize',5.5,'LineWidth',1.2);
xline(0,':','LineWidth',0.7);
xlabel('Polarizer angle, \theta (deg)');
ylabel('Relative received power (dB)');
xlim([0 90]);
xticks([0 45 90]);
ylim([min(Pmeas_rel_dB)-2, -4]);
legend('Finite-extinction model','Measured','Location','southwest');
tqeAxes(gca);

txt = sprintf('PER = %.1f dB\\newlineIL_{pass} = %.1f dB',PER_dB,ILpass_dB);
text(0.98,0.97,txt,'Units','normalized','HorizontalAlignment','right', ...
    'VerticalAlignment','top','FontSize',7);

exportTQE(f,OUT,'figM2_measured_linear_polarizer');
fprintf('Fig. M2: measured linear-polarizer response written.\n');

%% ========================================================================
% FIG. M3 — PARTIAL LINEAR STOKES RECONSTRUCTION
% ========================================================================

I0  = dbm2mw(-13.9);
I45 = dbm2mw(-15.1);
I90 = dbm2mw(-23.6);

S0 = I0 + I90;
S1 = I0 - I90;
S2 = 2*I45 - S0;

s1 = S1/S0;
s2 = S2/S0;
linearMag = hypot(s1,s2);
psi_deg = 0.5*atan2d(S2,S1);

phi = linspace(0,2*pi,721);

f = figure('Units','centimeters','Position',[2 2 singleW 7.0]);
plot(cos(phi),sin(phi),'-','LineWidth',1.0); hold on;
xline(0,':','LineWidth',0.7);
yline(0,':','LineWidth',0.7);

% Measured point, and direction-only unit-vector projection.
plot([0 s1],[0 s2],'-','LineWidth',1.2);
plot(s1,s2,'o','MarkerSize',6,'LineWidth',1.3);

if linearMag > 0
    s1u = s1/linearMag;
    s2u = s2/linearMag;
    plot([s1 s1u],[s2 s2u],'--','LineWidth',0.9);
    plot(s1u,s2u,'s','MarkerSize',5,'LineWidth',1.0);
end

text(1.02,0,'H','HorizontalAlignment','left');
text(-1.02,0,'V','HorizontalAlignment','right');
text(0,1.03,'+45^\circ','HorizontalAlignment','center','VerticalAlignment','bottom');
text(0,-1.03,'-45^\circ','HorizontalAlignment','center','VerticalAlignment','top');

xlabel('Normalized Stokes parameter, s_1');
ylabel('Normalized Stokes parameter, s_2');
axis equal;
xlim([-1.12 1.12]); ylim([-1.12 1.12]);
tqeAxes(gca);

txt = sprintf('Measured: (%.3f, %.3f)\\newline|s_L| = %.3f\\newline\\psi = %.1f^\\circ', ...
              s1,s2,linearMag,psi_deg);
text(0.03,0.97,txt,'Units','normalized','VerticalAlignment','top','FontSize',7);

legend('Linear-state equator','Axes','Measured direction','Measured point', ...
       'Direction-only projection','Normalized direction', ...
       'Location','southoutside','NumColumns',2);

exportTQE(f,OUT,'figM3_partial_stokes_plane');
fprintf('Fig. M3: partial Stokes plane written.\n');

%% ========================================================================
% FIG. M4 — STOKES COMPONENT SUMMARY
% ========================================================================

f = figure('Units','centimeters','Position',[2 2 singleW 5.8]);

% S3 is deliberately NaN because it was not independently measured.
vals = [s1 s2 0];
b = bar(1:3,vals,0.62); hold on;
% Add a crossed marker / label instead of pretending S3=0 was measured.
plot(3,0,'x','MarkerSize',9,'LineWidth',1.4);
text(3,0.08,'not measured','HorizontalAlignment','center','FontSize',7);

yline(0,'-','LineWidth',0.7);
set(gca,'XTick',1:3,'XTickLabel',{'s_1','s_2','s_3'});
ylabel('Normalized Stokes component');
ylim([-1.05 1.05]);
tqeAxes(gca);
exportTQE(f,OUT,'figM4_stokes_components');
fprintf('Fig. M4: Stokes component summary written.\n');

%% ========================================================================
% FIG. M5 — SINGLE COIL VS HELMHOLTZ PAIR FIELD UNIFORMITY
%
% Analytic on-axis circular-loop field. The geometry is dimensionless and
% therefore general: z/R is the axial coordinate normalized by coil radius.
% Helmholtz condition: coil separation = R.
% ========================================================================

zR = linspace(-1.25,1.25,1501);
R = 1;                   % normalized radius
sep = R;                 % Helmholtz separation
zc = sep/2;

% Common prefactor cancels after normalization.
Bsingle = 1 ./ (R^2 + (zR+zc).^2).^(3/2);
Bpair = 1 ./ (R^2 + (zR-zc).^2).^(3/2) + ...
        1 ./ (R^2 + (zR+zc).^2).^(3/2);

Bsingle = Bsingle / interp1(zR,Bsingle,0);
Bpair = Bpair / interp1(zR,Bpair,0);

f = figure('Units','centimeters','Position',[2 2 doubleW 7.5]);
plot(zR,Bsingle,'--','LineWidth',1.25); hold on;
plot(zR,Bpair,'-','LineWidth',1.5);
xline(0,':','LineWidth',0.7);
yline(1,':','LineWidth',0.7);

% Illustrative central interaction region only; edit to match cell/R.
xregion = 0.25;
yl = [min([Bsingle Bpair])-0.02, max([Bsingle Bpair])+0.02];
patch([-xregion xregion xregion -xregion],[yl(1) yl(1) yl(2) yl(2)], ...
      [0.8 0.8 0.8],'FaceAlpha',0.10,'EdgeColor','none');
uistack(findobj(gca,'Type','line'),'top');

xlabel('Axial position, z/R');
ylabel('Normalized magnetic field, B(z)/B(0)');
xlim([-1.25 1.25]);
legend('Single coil','Helmholtz pair','Location','best');
tqeAxes(gca);

% Uniformity over the illustrative |z/R|<=0.25 region.
mask = abs(zR)<=xregion;
uSingle = 100*(max(Bsingle(mask))-min(Bsingle(mask)))/mean(Bsingle(mask));
uPair   = 100*(max(Bpair(mask))-min(Bpair(mask)))/mean(Bpair(mask));
text(0.02,0.05,sprintf('\\DeltaB/\\bar{B} over |z/R|<=0.25:\\newline single %.2f%%; pair %.2f%%', ...
     uSingle,uPair),'Units','normalized','FontSize',7);

exportTQE(f,OUT,'figM5_helmholtz_uniformity');
fprintf('Fig. M5: analytic field-uniformity comparison written.\n');

%% ========================================================================
% FIGS. M6-M7 — CIRCULAR POLARIZER / METASURFACE
%
% REQUIRED CSV:
% cp_fullwave_results.csv
%
% Minimum columns:
%   frequency_GHz, RHCP_dB, LHCP_dB
%
% Optional:
%   axial_ratio_dB, relative_phase_deg
%
% IMPORTANT: These should come from CST/HFSS/MATLAB full-wave simulation or
% calibrated measurement. This script does not invent CP performance.
% ========================================================================

cpFile = fullfile(pwd,'cp_fullwave_results.csv');

if exist(cpFile,'file')
    C = readtable(cpFile);

    req = {'frequency_GHz','RHCP_dB','LHCP_dB'};
    assert(all(ismember(req,C.Properties.VariableNames)), ...
        'cp_fullwave_results.csv is missing one of: frequency_GHz, RHCP_dB, LHCP_dB');

    CER = C.RHCP_dB - C.LHCP_dB;

    f = figure('Units','centimeters','Position',[2 2 doubleW 7.3]);
    plot(C.frequency_GHz,C.RHCP_dB,'-','LineWidth',1.4); hold on;
    plot(C.frequency_GHz,C.LHCP_dB,'--','LineWidth',1.4);
    xlabel('Frequency, f (GHz)');
    ylabel('Transmission magnitude (dB)');
    legend('RHCP channel','LHCP channel','Location','best');
    tqeAxes(gca);
    exportTQE(f,OUT,'figM6_cp_rhcp_lhcp_transmission');

    f = figure('Units','centimeters','Position',[2 2 singleW 6.0]);
    plot(C.frequency_GHz,CER,'-','LineWidth',1.4); hold on;
    yline(0,':','LineWidth',0.7);
    xlabel('Frequency, f (GHz)');
    ylabel('Circular extinction ratio (dB)');
    tqeAxes(gca);
    exportTQE(f,OUT,'figM6b_circular_extinction_ratio');

    if ismember('axial_ratio_dB',C.Properties.VariableNames)
        f = figure('Units','centimeters','Position',[2 2 singleW 6.0]);
        plot(C.frequency_GHz,C.axial_ratio_dB,'-','LineWidth',1.4); hold on;
        yline(3,'--','3 dB criterion','LabelHorizontalAlignment','left');
        xlabel('Frequency, f (GHz)');
        ylabel('Axial ratio (dB)');
        tqeAxes(gca);
        exportTQE(f,OUT,'figM7_cp_axial_ratio');
    else
        fprintf(['SKIP Fig. M7 axial ratio: cp_fullwave_results.csv does not contain ' ...
                 'axial_ratio_dB.\n']);
    end

    if ismember('relative_phase_deg',C.Properties.VariableNames)
        f = figure('Units','centimeters','Position',[2 2 singleW 6.0]);
        plot(C.frequency_GHz,C.relative_phase_deg,'-','LineWidth',1.4); hold on;
        yline(90,'--','+90^\circ');
        yline(-90,'--','-90^\circ');
        xlabel('Frequency, f (GHz)');
        ylabel('Relative phase, \Delta\phi (deg)');
        tqeAxes(gca);
        exportTQE(f,OUT,'figM7b_cp_relative_phase');
    else
        fprintf(['SKIP Fig. M7b relative phase: cp_fullwave_results.csv does not contain ' ...
                 'relative_phase_deg.\n']);
    end

    fprintf('CP full-wave figures written from supplied CSV.\n');
else
    fprintf('\nDATA REQUIRED — CP FIGURES NOT GENERATED\n');
    fprintf('Create cp_fullwave_results.csv with columns:\n');
    fprintf('frequency_GHz, RHCP_dB, LHCP_dB');
    fprintf(', axial_ratio_dB, relative_phase_deg\n');
    fprintf('The code intentionally refuses to fabricate CP performance.\n\n');
end

%% ------------------------ Numeric summary -------------------------------
fprintf('Measured polarizer: PER = %.2f dB; pass IL = %.2f dB\n',PER_dB,ILpass_dB);
fprintf('Partial Stokes: s1 = %.4f, s2 = %.4f, |sL| = %.4f, psi = %.2f deg\n', ...
    s1,s2,linearMag,psi_deg);
fprintf('Outputs: %s\n',OUT);
fprintf('============================================================\n');

%% ========================================================================
% LOCAL FUNCTIONS
% ========================================================================

function y = lorentzian(x,c,w)
    y = 1 ./ (1 + ((x-c)./w).^2);
end

function [low,high,wLow,wHigh] = dressedPair(delta,Omega)
    root = sqrt(delta.^2 + Omega.^2);
    low  = delta/2 - root/2;
    high = delta/2 + root/2;
    safe = max(root,eps);
    wLow  = 0.5*(1 + delta/safe);
    wHigh = 0.5*(1 - delta/safe);
end

function x = dbm2mw(dBm)
    x = 10.^(dBm/10);
end

function tqeAxes(ax)
    ax.FontName = 'Times New Roman';
    ax.FontSize = 8;
    ax.LineWidth = 0.8;
    ax.TickDir = 'in';
    ax.Box = 'on';
    ax.XMinorTick = 'on';
    ax.YMinorTick = 'on';
    ax.Layer = 'top';
end

function exportTQE(fig,outDir,stem)
    exportgraphics(fig,fullfile(outDir,[stem '.pdf']),'ContentType','vector');
    exportgraphics(fig,fullfile(outDir,[stem '.png']),'Resolution',600);
end