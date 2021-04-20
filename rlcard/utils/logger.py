import os
import csv

class Logger(object):
    ''' Logger saves the running results and helps make plots from the results
    '''

    def __init__(self, log_dir):
        ''' Initialize the labels, legend and paths of the plot and log file.

        Args:
            log_path (str): The path the log files
        '''

        nr = 0
        nr = (str)(nr)
        '''

        nr = (str)(nr)
        self.log_dir = log_dir
        self.txt_path = os.path.join(log_dir, ('log_' + nr + '.txt'))
        self.csv_path = os.path.join(log_dir, ('performance_' + nr +'.csv'))
        self.fig_path = os.path.join(log_dir, ('fig_' + nr + '.png'))
        self.par_path = os.path.join(log_dir, ('parameters_' + nr + '.txt'))

        self.txt_p_path = os.path.join(log_dir, ('peasant_log_' + nr + '.txt'))
        self.csv_p_path = os.path.join(log_dir, ('peasant_perf_' + nr + 'txt'))
        self.fig_p_path = os.path.join(log_dir, ('fig_p_' + nr + '.png'))

        self.txt_l_path = os.path.join(log_dir, ('landlord_log_' + nr + '.txt'))
        self.csv_l_path = os.path.join(log_dir, ('landlord_perf_' + nr + 'txt'))
        self.fig_l_path = os.path.join(log_dir, ('fig_l_' + nr + '.png'))
        '''
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        while(os.path.exists(os.path.join(log_dir, ('log_' + nr + '.txt')))):
            nr = (int)(nr) + 1
            nr = (str)(nr)
        self.txt_path = os.path.join(log_dir, ('log_' + nr + '.txt'))
        self.csv_path = os.path.join(log_dir, ('performance_' + nr +'.csv'))
        self.fig_path = os.path.join(log_dir, ('fig_' + nr + '.png'))
        self.par_path = os.path.join(log_dir, ('parameters_' + nr + '.txt'))

        self.txt_p_path = os.path.join(log_dir, ('peasant_log_' + nr + '.txt'))
        self.csv_p_path = os.path.join(log_dir, ('peasant_perf_' + nr + '.csv'))
        self.fig_p_path = os.path.join(log_dir, ('fig_p_' + nr + '.png'))

        self.txt_l_path = os.path.join(log_dir, ('landlord_log_' + nr + '.txt'))
        self.csv_l_path = os.path.join(log_dir, ('landlord_perf_' + nr + '.csv'))
        self.fig_l_path = os.path.join(log_dir, ('fig_l_' + nr + '.png'))





        self.txt_file = open(self.txt_path, 'w')
        self.csv_file = open(self.csv_path, 'w')
        self.par_file = open(self.par_path, 'w')

        fieldnames = ['episode', 'reward']
        self.writer = csv.DictWriter(self.csv_file, fieldnames=fieldnames)
        self.writer.writeheader()

        self.txt_p_file = open(self.txt_p_path, 'w')
        self.csv_p_file = open(self.csv_p_path, 'w')

        fieldnames_p = ['episode', 'peasant_wins']
        self.writer_p = csv.DictWriter(self.csv_p_file, fieldnames = fieldnames_p)
        self.writer_p.writeheader()

        self.txt_l_file = open(self.txt_l_path, 'w')
        self.csv_l_file = open(self.csv_l_path, 'w')

        fieldnames_l = ['episode', 'landlord_wins']
        self.writer_l = csv.DictWriter(self.csv_l_file, fieldnames = fieldnames_l)
        self.writer_l.writeheader()

    def log_par(self, parameter_text):
        ''' Write the parameter_text to the parameter file.
        Args:
            parameter_text(string): parameter text to log
        '''

        self.par_file.write(parameter_text+'\n')
        self.par_file.flush()
        print(parameter_text)

    def log_parameters(self, parameter_dict):
        ''' Log parameters into txt file
        Args:
            parameter_dict: multiple different parameters in parameter_dict
            dict? list with two dimensions?
        '''
        print('')
        self.log_par('--------------------')
        for key in parameter_dict:
            self.log_par('   ' + key + '  |  ' + str(parameter_dict[key]))
        print('')


    def log_p(self, text):
        ''' Write the text to log file then print it.
        Args:
            text(string): text to log
        '''
        self.txt_p_file.write(text+'\n')
        self.txt_p_file.flush()
        print(text)
    def log_l(self, text):
        ''' Write the text to log file then print it.
        Args:
            text(string): text to log
        '''
        self.txt_l_file.write(text+'\n')
        self.txt_l_file.flush()
        print(text)
    def log(self, text):
        ''' Write the text to log file then print it.
        Args:
            text(string): text to log
        '''
        self.txt_file.write(text+'\n')
        self.txt_file.flush()
        print(text)
    def log_landlord(self, episode, landlord_wins):
        ''' Log a point in the curve
        Args:
            episode (int): the episode of the current point
            reward (float): the reward of the current point
        '''
        self.writer_l.writerow({'episode': episode, 'landlord_wins': landlord_wins})
        print('')
        self.log_l('----------------------------------------')
        self.log_l('  episode    |  ' + str(episode))
        self.log_l('  landlord_wins      |  ' + str(landlord_wins))
        self.log_l('----------------------------------------')

    def log_peasants(self, episode, peasant_wins):
        ''' Log a point in the curve
        Args:
            episode (int): the episode of the current point
            reward (float): the reward of the current point
        '''
        self.writer_p.writerow({'episode': episode, 'peasant_wins': peasant_wins})
        print('')
        self.log_p('----------------------------------------')
        self.log_p('  episode    |  ' + str(episode))
        self.log_p('  peasant_wins       |  ' + str(peasant_wins))
        self.log_p('----------------------------------------')
    def log_performance(self, episode, reward):
        ''' Log a point in the curve
        Args:
            episode (int): the episode of the current point
            reward (float): the reward of the current point
        '''
        self.writer.writerow({'episode': episode, 'reward': reward})
        print('')
        self.log('----------------------------------------')
        self.log('  episode     |  ' + str(episode))
        self.log('  reward       |  ' + str(reward))
        self.log('----------------------------------------')

    def plot(self, algorithm, plots):

        if(plots=='peasant_wins'):
            plot_p(self.csv_p_path, self.fig_p_path, algorithm)
        if(plots=='landlord_wins'):
            plot_l(self.csv_l_path, self.fig_l_path, algorithm)
        if(plots=='reward'):
            plot(self.csv_path, self.fig_path, algorithm)


    def close_files(self):
        ''' Close the created file objects
        '''
        if self.txt_path is not None:
            self.txt_file.close()
        if self.csv_path is not None:
            self.csv_file.close()
        if self.txt_p_path is not None:
            self.txt_p_file.close()
        if self.csv_p_path is not None:
            self.csv_p_file.close()
        if self.txt_l_path is not None:
            self.txt_l_file.close()
        if self.csv_l_path is not None:
            self.csv_l_file.close()

def plot(csv_path, save_path, algorithm):
    ''' Read data from csv file and plot the results
    '''
    import matplotlib.pyplot as plt
    with open(csv_path) as csvfile:
        print(csv_path)
        reader = csv.DictReader(csvfile)
        xs = []
        ys = []
        for row in reader:
            xs.append(int(row['episode']))
            ys.append(float(row['reward']))
        fig, ax = plt.subplots()
        ax.plot(xs, ys, label=algorithm)
        ax.set(xlabel='episode', ylabel='reward')
        ax.legend()
        ax.grid()

        save_dir = os.path.dirname(save_path)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        fig.savefig(save_path)
            
def plot_p(csv_path, save_path, algorithm):
    ''' Read data from csv file and plot the results
    '''
    import matplotlib.pyplot as plt
    with open(csv_path) as csvfile:
        print(csv_path)
        reader = csv.DictReader(csvfile)
        xs = []
        ys = []
        for row in reader:
            xs.append(int(row['episode']))
            ys.append(float(row['peasant_wins']))
        fig, ax = plt.subplots()
        ax.plot(xs, ys, label=algorithm)
        ax.set(xlabel='episode', ylabel='peasant_wins')
        ax.legend()
        ax.grid()

        save_dir = os.path.dirname(save_path)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        fig.savefig(save_path)

def plot_l(csv_path, save_path, algorithm):
    ''' Read data from csv file and plot the results
    '''
    import matplotlib.pyplot as plt
    with open(csv_path) as csvfile:
        print(csv_path)
        reader = csv.DictReader(csvfile)
        xs = []
        ys = []
        for row in reader:
            xs.append(int(row['episode']))
            ys.append(float(row['landlord_wins']))
        fig, ax = plt.subplots()
        ax.plot(xs, ys, label=algorithm)
        ax.set(xlabel='episode', ylabel='landlord_wins')
        ax.legend()
        ax.grid()

        save_dir = os.path.dirname(save_path)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        fig.savefig(save_path)
