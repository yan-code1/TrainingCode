function [p] = plot_one_figure(fig_idx, plot_data)

figure(fig_idx); hold on;

% plot_data = mean(plot_data);
% plot_data = smooth(plot_data,50);
p = plot(plot_data);
