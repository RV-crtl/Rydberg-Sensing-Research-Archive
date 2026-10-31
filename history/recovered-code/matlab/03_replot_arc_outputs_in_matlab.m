%% 03_replot_arc_outputs_in_matlab.m
% =========================================================================
% OPTIONAL MATLAB RE-PLOTTER FOR THE PYTHON/ARC OUTPUTS
%
% Workflow:
%   1) Run:
%        python 01_arc_rydberg_figures.py
%
%      It produces ./rydberg_tqe_outputs/
%
%   2) Run this MATLAB file.
%
% Purpose:
%   The Python script does the ARC-dependent atomic calculations.
%   This file lets you redraw selected outputs with MATLAB figure rendering.
%
% Expected Python files:
%   rydberg_tqe_outputs/arc_transition_candidates.csv
%   rydberg_tqe_outputs/fig2_zeeman_pathways.csv
%   rydberg_tqe_outputs/fig3_polarisation_fingerprints.csv
%   rydberg_tqe_outputs/fig4_worst_direction_sensitivity.csv
%
% =========================================================================

clear; clc; close all;

SRC = fullfile(pwd,'rydberg_tqe_outputs');
OUT = fullfile(pwd,'matlab_arc_replots');
if ~exist(OUT,'dir'), mkdir(OUT); end

set(groot,'defaultFigureColor','w');
set(groot,'defaultAxesFontName','Times New Roman');
set(groot,'defaultTextFontName','Times New Roman');
set(groot,'defaultAxesFontSize',8);
set(groot,'defaultAxesLineWidth',0.8);
set(groot,'defaultLineLineWidth',1.25);
set(groot,'defaultAxesTickDir','in');
set(groot,'defaultAxesBox','on');
set(groot,'defaultLegendBox','off');

singleW = 8.9;
doubleW = 18.2;

%% A. ARC transition feasibility map
candFile = fullfile(SRC,'arc_transition_candidates.csv');

if exist(candFile,'file')
    T = readtable(candFile,'TextType','string');

    good = isfinite(T.rf_frequency_GHz) & isfinite(T.max_abs_dme_ea0) & ...
           isfinite(T.coupling_wavelength_nm);

    f = figure('Units','centimeters','Position',[2 2 doubleW 7.5]);
    scatter(T.rf_frequency_GHz(good),T.max_abs_dme_ea0(good), ...
            28,T.coupling_wavelength_nm(good),'filled');
    hold on;
    xline(1.0,':'); xline(2.0,':');
    xlabel('RF transition frequency, f_{RF} (GHz)');
    ylabel('Maximum dipole matrix element, |d| (ea_0)');
    cb = colorbar;
    cb.Label.String = 'Coupling wavelength (nm)';
    xlim([0.4 6.4]);
    tqeAxes(gca);
    exportTQE(f,OUT,'arc_transition_feasibility_matlab');

    fprintf('ARC feasibility map re-plotted.\n');
else
    fprintf('Missing %s — run Python ARC script first.\n',candFile);
end

%% B. ARC Zeeman fan
fanFile = fullfile(SRC,'fig2_zeeman_pathways.csv');

if exist(fanFile,'file')
    Z = readtable(fanFile);
    B0 = linspace(0,2.5,251);

    f = figure('Units','centimeters','Position',[2 2 doubleW 7.5]); hold on;

    qVals = [-1 0 1];
    ls = {'-','--','-.'};

    for iq = 1:numel(qVals)
        rows = Z.q == qVals(iq);
        inds = find(rows);
        for k = 1:numel(inds)
            ii = inds(k);
            y = Z.slope_MHz_per_mT(ii)*B0;
            lw = 0.7 + 1.8*abs(Z.dme_ea0(ii))/max(abs(Z.dme_ea0));
            plot(B0,y,ls{iq},'LineWidth',lw);
        end
    end

    yline(0,':');
    xlabel('Magnetic bias, B_0 (mT)');
    ylabel('RF transition shift, \Delta f_Z (MHz)');
    tqeAxes(gca);
    exportTQE(f,OUT,'arc_zeeman_fan_matlab');

    fprintf('ARC Zeeman fan re-plotted.\n');
else
    fprintf('Missing %s — run Python ARC script first.\n',fanFile);
end

%% C. Polarisation-resolved Rydberg spectra
specFile = fullfile(SRC,'fig3_polarisation_fingerprints.csv');

if exist(specFile,'file')
    S = readtable(specFile,'TextType','string');

    names = unique(S.polarisation,'stable');

    f = figure('Units','centimeters','Position',[2 2 doubleW 7.5]); hold on;

    for i = 1:numel(names)
        mask = S.polarisation == names(i);
        [x,ord] = sort(S.probe_detuning_MHz(mask));
        yy = S.T_RF_on(mask);
        yy = yy(ord);
        plot(x,yy,'LineWidth',1.3,'DisplayName',names(i));
    end

    xline(0,':');
    xlabel('Probe detuning, \Delta_p (MHz)');
    ylabel('Relative probe transmission');
    legend('Location','best');
    tqeAxes(gca);
    exportTQE(f,OUT,'arc_polarisation_fingerprints_matlab');

    fprintf('ARC polarisation spectra re-plotted.\n');
else
    fprintf('Missing %s — run Python ARC script first.\n',specFile);
end

%% D. Identifiability heatmap
mapFile = fullfile(SRC,'fig4_worst_direction_sensitivity.csv');

if exist(mapFile,'file')
    raw = readcell(mapFile);

    rf = cell2mat(raw(1,2:end));
    b0 = cell2mat(raw(2:end,1));
    M  = cell2mat(raw(2:end,2:end));

    f = figure('Units','centimeters','Position',[2 2 doubleW 7.5]);
    imagesc(rf,b0,M);
    axis xy;
    xlabel('RF detuning, \Delta_{RF} (MHz)');
    ylabel('Magnetic bias, B_0 (mT)');
    cb = colorbar;
    cb.Label.String = 'Worst-direction polarisation sensitivity';
    tqeAxes(gca);
    exportTQE(f,OUT,'arc_identifiability_heatmap_matlab');

    fprintf('ARC identifiability heatmap re-plotted.\n');
else
    fprintf('Missing %s — run Python ARC script first.\n',mapFile);
end

fprintf('MATLAB ARC replots complete: %s\n',OUT);

%% Local functions
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