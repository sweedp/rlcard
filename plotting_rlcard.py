import os
import csv
from logger import *

# need to rewrite this to log some graphs into one graphs
# just say how to name them in graph = algorithm_list[]
# and give their csv path to csv_list[] ]
log_dir = './results/'
log_dir_dqn = './results/doudizhu_dqn_result'
log_dir_ddqn = './results/doudizhu_ddqn_result'
log_dir_dddqn = './results/doudizhu_dueling_ddqn_result'
log_dir_random = './results/doudizhu_random_agent_result'

save_path_performance= log_dir + '/general_performance_figure'

# EDIT ALGORITHM and CSV List for other plots together
algorithm_list = ['DQN', 'DDQN', 'Dueling DDQN', 'Random']
what_plot = 'reward' # agent_landlord_wins; agent_peasant_wins
# performance
csv_list_performance = [ log_dir_dqn + '/performance_0.csv', log_dir_ddqn + '/performance_1.csv', log_dir_dddqn + '/performance_2.csv', log_dir_random + '/performance_0.csv']

plot_figures_one(csv_list_performance, save_path_performance, algorithm_list, what_plot)


save_path_agent_l = log_dir + 'landlord_performance_figure'
what_plot = 'agent_landlord_wins'
csv_list_agents_landlord_wins = [log_dir_dqn + '/agent_landlord_perf_0.csv', log_dir_ddqn + '/agent_landlord_perf_1.csv', log_dir_dddqn + '/agent_landlord_perf_2.csv', log_dir_random +'/agent_landlord_perf_0.csv']
plot_figures_one(csv_list_agents_landlord_wins, save_path_agent_l,algorithm_list, what_plot)


save_path_agent_p = log_dir + 'peasant_performance_figure'
what_plot = 'agent_peasant_wins'
csv_list_agents_peasant_wins = [log_dir_dqn + '/agent_peasant_perf_0.csv', log_dir_ddqn + '/agent_peasant_perf_1.csv', log_dir_dddqn + '/agent_peasant_perf_2.csv', log_dir_random +'/agent_peasant_perf_0.csv']
plot_figures_one(csv_list_agents_peasant_wins, save_path_agent_p, algorithm_list, what_plot)
