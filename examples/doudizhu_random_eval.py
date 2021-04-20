''' An example of learning a Deep-Q Agent on Dou Dizhu
'''

import tensorflow as tf
import os

import rlcard
from rlcard.agents import DQNAgent
from rlcard.agents import RandomAgent
from rlcard.utils import set_global_seed, tournament
from rlcard.utils import Logger

# Make environment
env = rlcard.make('doudizhu', config={'seed': 0})
eval_env = rlcard.make('doudizhu', config={'seed': 0})

# Set the iterations numbers and how frequently we evaluate the performance
evaluate_every = 100
evaluate_num = 100
episode_num = 20000

# The intial memory size
memory_init_size = 100
landlord_score = True

parameter_dict = {}

parameter_dict['episode_num'] = episode_num
parameter_dict['evaluate_every'] = evaluate_every
parameter_dict['evaluate_num'] = evaluate_num
parameter_dict['landlord_score'] = landlord_score
parameter_dict['Agent'] = 'Random Agent'

# The paths for saving the logs and learning curves


# Set a global seed
set_global_seed(0)

with tf.Session() as sess:

    # Initialize a global step
    global_step = tf.Variable(0, name='global_step', trainable=False)

    # Set up the agents
    agent = RandomAgent(action_num=env.action_num)


    random_agent = RandomAgent(action_num=eval_env.action_num)
    env.set_agents([agent, random_agent, random_agent])
    eval_env.set_agents([random_agent, random_agent, random_agent])

    env.set_landlord_score(landlord_score)
    eval_env.set_landlord_score(landlord_score)
    # Initialize global variables
    sess.run(tf.global_variables_initializer())

    # Init a Logger to plot the learning curve
    log_dir = './experiments/doudizhu_random_result/'
    logger = Logger(log_dir)
    logger.log_parameters(parameter_dict)

    for episode in range(episode_num):


        ## dont need these for random agent
        # Generate data from the environment
        #trajectories, _ = env.run(is_training=True)

        # Feed transitions into agent memory, and train the agent
        #for ts in trajectories[0]:
        #    agent.feed(ts)

        # Evaluate the performance. Play with random agents.
        if episode % evaluate_every == 0:
            payoffs, peasant_wins, landlord_wins = tournament(eval_env, evaluate_num)
            logger.log_performance(episode, payoffs[0])
            #print("DQN: ", peasant_wins, " and ", landlord_wins)
            logger.log_peasants(episode, peasant_wins/evaluate_num)
            logger.log_landlord(episode, landlord_wins/evaluate_num)

    # Close files in the logger
    logger.close_files()

    # Plot the learning curve
    logger.plot('Random')

    # Save model

    nr = 0
    nr = (str)(nr)

    save_dir = 'models/doudizhu_random_' + nr
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    else:
        while(os.path.exists(save_dir)):
            nr = (int)(nr) + 1
            nr = (str)(nr)
            save_dir = 'models/doudizhu_random_' + nr +'/'

    saver = tf.train.Saver()
    saver.save(sess, os.path.join(save_dir, 'model'))
