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
        self.log_dir = log_dir

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        while(os.path.exists(os.path.join(log_dir, ('log_' + nr + '.txt')))):
            nr = (int)(nr) + 1
            nr = (str)(nr)
        self.txt_path = os.path.join(log_dir, ('log_' + nr + '.txt'))
        self.csv_path = os.path.join(log_dir, ('performance_' + nr +'.csv'))
        self.fig_path = os.path.join(log_dir, ('fig_performance_' + nr + '.png'))
        self.par_path = os.path.join(log_dir, ('parameters_' + nr + '.txt'))

        self.txt_p_path = os.path.join(log_dir, ('peasant_log_' + nr + '.txt'))
        self.csv_p_path = os.path.join(log_dir, ('peasant_perf_' + nr + '.csv'))
        self.fig_p_path = os.path.join(log_dir, ('fig_peasant_wins_' + nr + '.png'))

        self.txt_l_path = os.path.join(log_dir, ('landlord_log_' + nr + '.txt'))
        self.csv_l_path = os.path.join(log_dir, ('landlord_perf_' + nr + '.csv'))
        self.fig_l_path = os.path.join(log_dir, ('fig_landlord_wins_' + nr + '.png'))

        self.txt_loss_path = os.path.join(log_dir, ('loss_log_' + nr + '.txt'))
        self.csv_loss_path = os.path.join(log_dir, ('loss_perf_' + nr + '.csv'))
        self.fig_loss_path = os.path.join(log_dir, ('fig_loss_' + nr + '.png'))

        self.txt_agent_l_path = os.path.join(log_dir, ('agent_landlord_log_' + nr + '.txt'))
        self.csv_agent_l_path = os.path.join(log_dir, ('agent_landlord_perf_' + nr + '.csv'))
        self.fig_agent_l_path = os.path.join(log_dir, ('fig_agent_landlord_wins_' + nr + '.png'))


        self.txt_agent_p_path = os.path.join(log_dir, ('agent_peasant_log_' + nr + '.txt'))
        self.csv_agent_p_path = os.path.join(log_dir, ('agent_peasant_perf_' + nr + '.csv'))
        self.fig_agent_p_path = os.path.join(log_dir, ('fig_agent_peasant_wins_' + nr + '.png'))


        self.fig_all_path = os.path.join(log_dir, ('fig_all_' + nr + '.png'))
        #parameter file
        self.par_file = open(self.par_path, 'w')

        # episode reward
        self.txt_file = open(self.txt_path, 'w')
        self.csv_file = open(self.csv_path, 'w')

        fieldnames = ['episode', 'reward']
        self.writer = csv.DictWriter(self.csv_file, fieldnames=fieldnames)
        self.writer.writeheader()

        # episode peasant_wins
        self.txt_p_file = open(self.txt_p_path, 'w')
        self.csv_p_file = open(self.csv_p_path, 'w')

        fieldnames_p = ['episode', 'peasant_wins']
        self.writer_p = csv.DictWriter(self.csv_p_file, fieldnames = fieldnames_p)
        self.writer_p.writeheader()

        # episode landlord_wins
        self.txt_l_file = open(self.txt_l_path, 'w')
        self.csv_l_file = open(self.csv_l_path, 'w')

        fieldnames_l = ['episode', 'landlord_wins']
        self.writer_l = csv.DictWriter(self.csv_l_file, fieldnames = fieldnames_l)
        self.writer_l.writeheader()

        # episode agent landlord wins
        self.txt_agent_l_file = open(self.txt_agent_l_path, 'w')
        self.csv_agent_l_file = open(self.csv_agent_l_path, 'w')

        fieldnames_agent_l = ['episode', 'agent_landlord_wins']
        self.writer_agent_l = csv.DictWriter(self.csv_agent_l_file, fieldnames = fieldnames_agent_l)
        self.writer_agent_l.writeheader()


        # episode agent peasant wins
        self.txt_agent_p_file = open(self.txt_agent_p_path, 'w')
        self.csv_agent_p_file = open(self.csv_agent_p_path, 'w')

        fieldnames_agent_p = ['episode', 'agent_peasant_wins']
        self.writer_agent_p = csv.DictWriter(self.csv_agent_p_file, fieldnames = fieldnames_agent_p)
        self.writer_agent_p.writeheader()

        # episode loss
        self.txt_loss_file = open(self.txt_loss_path, 'w')
        self.csv_loss_file = open(self.csv_loss_path, 'w')

        fieldnames_loss = ['episode', 'loss']
        self.writer_loss = csv.DictWriter(self.csv_loss_file, fieldnames = fieldnames_loss)
        self.writer_loss.writeheader()

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

    def log_agent_l(self, text):
        ''' Write the text to log file then print it.
        Args:
            text(string): text to log
        '''
        self.txt_agent_l_file.write(text+'\n')
        self.txt_agent_l_file.flush()
        print(text)

    def log_agent_p(self, text):
        ''' Write the text to log file then print it.
        Args:
            text(string): text to log
        '''
        self.txt_agent_p_file.write(text+'\n')
        self.txt_agent_p_file.flush()
        print(text)
    def log(self, text):
        ''' Write the text to log file then print it.
        Args:
            text(string): text to log
        '''
        self.txt_file.write(text+'\n')
        self.txt_file.flush()
        print(text)

    def log_lo(self, text):
        ''' Write the text to log file then print it.
        Args:
            text(string): text to log
        '''
        self.txt_loss_file.write(text+'\n')
        self.txt_loss_file.flush()
        print(text)


    def log_loss(self, episode, loss):
        ''' Log a point in the curve
        Args:
            episode (int): the episode of the current point
            loss (float): the loss of the current point
        '''
        self.writer_loss.writerow({'episode': episode, 'loss': loss})
        print('')
        self.log_lo('----------------------------------------')
        self.log_lo('  episode    |  ' + str(episode))
        self.log_lo('  loss      |  ' + str(loss))
        self.log_lo('----------------------------------------')

    def log_agent_landlord(self, episode, agent_landlord_wins):
        ''' Log a point in the curve
        Args:
            episode (int): the episode of the current point
            reward (float): the reward of the current point
        '''
        self.writer_agent_l.writerow({'episode': episode, 'agent_landlord_wins': agent_landlord_wins})
        print('')
        self.log_agent_l('----------------------------------------')
        self.log_agent_l('  episode    |  ' + str(episode))
        self.log_agent_l('  agent_landlord_wins      |  ' + str(agent_landlord_wins))
        self.log_agent_l('----------------------------------------')

    def log_agent_peasant(self, episode, agent_peasant_wins):
        ''' Log a point in the curve
        Args:
            episode (int): the episode of the current point
            reward (float): the reward of the current point
        '''
        self.writer_agent_p.writerow({'episode': episode, 'agent_peasant_wins': agent_peasant_wins})
        print('')
        self.log_agent_p('----------------------------------------')
        self.log_agent_p('  episode    |  ' + str(episode))
        self.log_agent_p('  agent_peasant_wins      |  ' + str(agent_peasant_wins))
        self.log_agent_p('----------------------------------------')


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
        if(plots=='loss'):
            plot_loss(self.csv_loss_path, self.fig_loss_path, algorithm)

        if(plots=='agent_peasant_wins'):
            plot_agent_p(self.csv_agent_p_path, self.fig_agent_p_path, algorithm)

        if(plots=='agent_landlord_wins'):
            plot_agent_l(self.csv_agent_l_path, self.fig_agent_l_path, algorithm)


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
        if self.txt_loss_path is not None:
            self.txt_loss_file.close()
        if self.csv_loss_path is not None:
            self.csv_loss_file.close()
        if self.csv_agent_p_path is not None:
            self.csv_agent_p_file.close()
        if self.csv_agent_l_path is not None:
            self.csv_agent_l_file.close()
        if self.par_path is not None:
            self.par_file.close()

    def plot_all(self, algorithm_list, plotlist):

        csv_pathes = []
        save_path = self.fig_all_path


        for plots in plotlist:

            if(plots=='agent_peasant_wins'):
                csv_pathes.append(self.csv_agent_p_path)

            if(plots=='agent_landlord_wins'):
                csv_pathes.append(self.csv_agent_l_path)

            if(plots=='peasant_wins'):
                csv_pathes.append(self.csv_p_path)

            if(plots=='landlord_wins'):
                csv_pathes.append(self.csv_l_path)

            if(plots=='reward'):
                csv_pathes.append(self.csv_path)
        plot_figures_one(csv_pathes, save_path, algorithm_list)


def plot_figures(csv_pathes, save_path, algorithm_list):
    ''' Read data from csv files and plot the results
    '''
    import matplotlib.pyplot as plt

    fig, axs = plt.subplots(len(csv_pathes), sharex=True, sharey=True)

    for i in range(len(csv_pathes)):
        csv_path = csv_pathes[i]
        algorithm = algorithm_list[i]

        print("csv path: ", csv_path)
        print("algorithm: ", algorithm)

        with open(csv_path) as csvfile:
            print(csv_path)
            reader = csv.DictReader(csvfile)
            xs = []
            ys = []
            for row in reader:
                xs.append(int(row['episode']))
                ys.append(float(row[algorithm]))


            axs[i].plot(xs, ys, label=algorithm)
            axs[i].set(xlabel='episode', ylabel='reward')
            axs[i].legend()
            axs[i].grid()

        save_dir = os.path.dirname(save_path)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

    fig.savefig(save_path)



def plot_figures_one(csv_pathes, save_path, algorithm_list):
    ''' Read data from csv files and plot the results
    '''
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()

    for i in range(len(csv_pathes)):
        csv_path = csv_pathes[i]
        algorithm = algorithm_list[i]

        print("csv path: ", csv_path)
        print("algorithm: ", algorithm)

        with open(csv_path) as csvfile:
            print(csv_path)
            reader = csv.DictReader(csvfile)
            xs = []
            ys = []
            for row in reader:
                xs.append(int(row['episode']))
                ys.append(float(row[algorithm]))


            ax.plot(xs, ys, label=algorithm)
            ax.set(xlabel='episode', ylabel='reward')
    ax.legend()
    #ax.grid()

    save_dir = os.path.dirname(save_path)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    fig.savefig(save_path)



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

def plot_loss(csv_path, save_path, algorithm):
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
            ys.append(float(row['loss']))
        fig, ax = plt.subplots()
        ax.plot(xs, ys, label=algorithm)
        ax.set(xlabel='episode', ylabel='loss')
        ax.legend()
        ax.grid()

        save_dir = os.path.dirname(save_path)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        fig.savefig(save_path)

def plot_agent_l(csv_path, save_path, algorithm):
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
            ys.append(float(row['agent_landlord_wins']))
        fig, ax = plt.subplots()
        ax.plot(xs, ys, label=algorithm)
        ax.set(xlabel='episode', ylabel='agent_landlord_wins')
        ax.legend()
        ax.grid()

        save_dir = os.path.dirname(save_path)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)


        fig.savefig(save_path)
def plot_agent_p(csv_path, save_path, algorithm):
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
            ys.append(float(row['agent_peasant_wins']))
        fig, ax = plt.subplots()
        ax.plot(xs, ys, label=algorithm)
        ax.set(xlabel='episode', ylabel='agent_peasant_wins')
        ax.legend()
        ax.grid()

        save_dir = os.path.dirname(save_path)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        fig.savefig(save_path)
