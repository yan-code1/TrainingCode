close all; clear; clc;

result_parent_dir = './results';
result_dir = {
%      'dqn_agent__UGV2_20211126_224503',...
%      'dqn_agent__UGV3_20211126_224503',...
%      'dqn_agent__UGV4_20211126_224503',...
%      'dqn_agent__UGV5_20211126_224503',...
%      'dqn_agent__UGV6_20211126_224503',...
'atpc_agent__UGV1_20211127_121051'...
'atpc_agent__UGV2_20211127_121051'...
'atpc_agent__UGV3_20211127_121051'...
'atpc_agent__UGV4_20211127_121051'...
'atpc_agent__UGV6_20211127_121051'...
'atpc_agent__UGV7_20211127_121051'...

     
};
result_algorithms = {
  
     
%             'DQN',...
%                'WIFI',...
%               'DQN UAV1',...
%               'DQN UAV2',...
%               'DQN UAV3',...
%               'DQN UAV4',...
%               'DQN UAV5',...
              'ATPC UAV1',...
              'ATPC UAV2',...
              'ATPC UAV3',...
              'ATPC UAV4',...
              'ATPC UAV5',...
              'ATPC UAV6',...

                
            
};

result_number = length(result_dir);

figure_titles = {
   'frame_loss', ...
   'Date latency (s)', ...
   'Power (dBm)', ...
};
figure_plot_data = {
    'frame_loss', ...
    'latency', ...
    'power',...
};

figure_number = length(figure_titles);

plot_handlers = gobjects(figure_number, result_number);

double_cell = cell(1, figure_number);
[double_cell{:}] = deal('double');
T = table(...
    'Size', [result_number, figure_number], ...
    'VariableTypes', double_cell, ...
    'VariableNames', figure_plot_data, ...
    'RowNames', result_algorithms);

move_destination_table = zeros(4,result_number);
channel_table = zeros(2,result_number);
for result_idx = 1:result_number
    result_path = sprintf('%s/%s/results.mat', result_parent_dir, result_dir{result_idx});
    load(result_path);
    latency = data_latency./(51.*ones(1,800)-packet_loss);
    frame_loss = packet_loss/50;
    for fig_idx = 1:figure_number
        
        plot_data = eval(figure_plot_data{fig_idx});
        
        plot_handlers(fig_idx, result_idx) = plot_one_figure(fig_idx, plot_data(1,1:500));
%          T(result_idx, fig_idx) = {mean(plot_data(10:100,:), 'all')};
         T(result_idx, fig_idx) = {mean(plot_data(1:500), 'all')};
    end
    
%     move_destination_table(1,result_idx) = sum(move_destination == 0, 'all');
%     move_destination_table(2,result_idx) = sum(move_destination == 2, 'all');
%     move_destination_table(3,result_idx) = sum(move_destination == 4, 'all');
%     move_destination_table(4,result_idx) = sum(move_destination == 6, 'all');
%     move_destination_table = move_destination_table';
    channel_table(1,result_idx) = 800%sum(channel == 1, 'all');
    channel_table(2,result_idx) = 0%sum(channel == 6, 'all');
%     channel_table = channel_table'
end

for fig_idx = 1:figure_number
    figure(fig_idx);
    legend(plot_handlers(fig_idx, :), result_algorithms);
    xlabel('time slot.');
    ylabel(figure_titles{fig_idx});
end


figure; hold on;
bar([1,6],channel_table);
legend(result_algorithms, 'location', 'southeast');
xticks([1,6]);
xlabel('Channel');
ylabel('Switch times');

% figure; hold on;
% bar([0,2,4,6],move_destination_table);
% legend(result_algorithms, 'location', 'southeast');
% xticks([0, 2, 4 ,6]);
% xlabel('Move destination');
% ylabel('Switch times');


figure_number = figure_number + 1;

T

% for fig_idx = 1:figure_number
%     figure(fig_idx);
%     saveas(gcf, sprintf('figures/%d.emf', fig_idx));
% end














