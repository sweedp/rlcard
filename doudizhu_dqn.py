''' An example of learning a Deep-Q Agent on Dou Dizhu
'''

import tensorflow as tf
import os

import rlcard
from dqn_agent import DQNAgent
from rlcard.agents import RandomAgent
from rlcard.utils import set_global_seed, tournament
from rlcard.utils import Logger
## error logging
#tf.logging.set_verbosity(tf.logging.ERROR)
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
# Make environment
env = rlcard.make('doudizhu', config={'seed': 0})
eval_env = rlcard.make('doudizhu', config={'seed': 0})

## save parameters in dictionary
parameter_dict = {}
# Set the iterations numbers and how frequently we evaluate the performance
episode_num = 30000
evaluate_every = 1000
evaluate_num = 1000


## parameters for DQN agent
replay_memory_size=20000
memory_init_size=1000
update_target_estimator_every=1000
discount_factor=0.99
epsilon_start=1.0
epsilon_end=0.1
epsilon_decay_steps=20000
batch_size=32
train_every= 1 # train the agent avery train_every steps
mlp_layers=[512,512]
learning_rate=0.00005
role = 0 # landlord = 0, peasant1 = 1, peasant2 = 2 - only counts if landlord_score = False
landlord_score = True ## if landlord score is True, we dont need role_switching
                      ## because the landlord is not always on position 0 but according to the position with best handcards score

parameter_dict['episode_num'] = episode_num
parameter_dict['evaluate_every'] = evaluate_every
parameter_dict['evaluate_num'] = evaluate_num
parameter_dict['DQN Agent Parameters'] = 'see below:'
parameter_dict['replay_memory_size'] = replay_memory_size
parameter_dict['memory_init_size'] = memory_init_size
parameter_dict['train_every'] = train_every
parameter_dict['update_target_estimator_every'] =  update_target_estimator_every
parameter_dict['discount_factor'] = discount_factor
parameter_dict['epsilon_start'] = epsilon_start
parameter_dict['epsilon_end'] = epsilon_end
parameter_dict['epsilon_decay_steps'] =  epsilon_decay_steps
parameter_dict['batch_size'] =  batch_size
parameter_dict['train_every'] =  train_every
parameter_dict['mlp_layers'] = mlp_layers
parameter_dict['learning_rate'] = learning_rate
parameter_dict['landlord_score'] = landlord_score
if(landlord_score==False):
    if(role==0):
        parameter_dict['always_landlord'] = True
    if(role==1):
        parameter_dict['always_peasant_1'] = True
    if(role==2):
        parameter_dict['always_peasant_2'] = True
# change if you use different agent but this same file
parameter_dict['Agent: '] = 'DQN Agent'

# Set a global seed
set_global_seed(0)


with tf.Session() as sess:

    # Initialize a global step
    global_step = tf.Variable(0, name='global_step', trainable=False)

    # Set up the agents
    agent = DQNAgent(sess,
                     scope='dqn',
                     replay_memory_size=replay_memory_size,
                     replay_memory_init_size=memory_init_size,
                     update_target_estimator_every=update_target_estimator_every,
                     discount_factor=discount_factor,
                     epsilon_start=epsilon_start,
                     epsilon_end=epsilon_end,
                     epsilon_decay_steps=epsilon_decay_steps,
                     batch_size=batch_size,
                     action_num=env.action_num,
                     state_shape=env.state_shape,
                     train_every=train_every,
                     mlp_layers=mlp_layers,
                     learning_rate=learning_rate)


    random_agent = RandomAgent(action_num=eval_env.action_num)
    agent_list = [agent, random_agent, random_agent] # default

    #deactivated at the moment because we might not need it if we use landlord score anyway for switching positions/roles
    '''
    if(landlord_score):
        agent_list = [random_agent, random_agent, random_agent]
    else:
        if(role==0):
            agent_list = [agent, random_agent, random_agent]
            parameter_dict['always landlord'] = True
        elif(role==1):
            agent_list = [random_agent, agent, random_agent]
            parameter_dict['always_peasant_1'] = True
        elif(role==2):
            agent_list = [random_agent, random_agent, agent]
            parameter_dict['always_peasant_2'] = True
    '''
    #set agents in environment
    env.set_agents(agent_list)
    eval_env.set_agents(agent_list)
    env.set_landlord_score(landlord_score)
    eval_env.set_landlord_score(landlord_score)
    eval_env.set_eval_agent(role)
    # Initialize global variables
    sess.run(tf.global_variables_initializer())

    # Init a Logger to plot the learning curve
    log_dir = './results/doudizhu_dqn_result/'
    logger = Logger(log_dir)
    logger.log_parameters(parameter_dict)

    role_counter = role

    for episode in range(episode_num):

        # Generate data from the environment
        trajectories, _ = env.run(is_training=True)

        # Feed transitions into agent memory, and train the agent
        for ts in trajectories[0]:
            agent.feed(ts)

        # Evaluate the performance. Play with random agents.
        if episode % evaluate_every == 0:
            ##payoffs, peasant_wins, landlord_wins = tournament(eval_env, evaluate_num)
            ## new with loss:
            payoffs, peasant_wins, landlord_wins, agent_peasant_wins, agent_landlord_wins = tournament(eval_env, evaluate_num)
            logger.log_performance(episode, payoffs[role_counter])
            #print("DQN: ", peasant_wins, " and ", landlord_wins)
            logger.log_peasants(episode, peasant_wins/evaluate_num)
            logger.log_landlord(episode, landlord_wins/evaluate_num)
            logger.log_loss(episode, agent.get_loss())
            logger.log_agent_peasant(episode, agent_peasant_wins)
            logger.log_agent_landlord(episode, agent_landlord_wins)


    # Close files in the logger
    logger.close_files()

    # Plot the learning curve
    logger.plot('DQN', 'peasant_wins')
    logger.plot('DQN', 'reward')
    logger.plot('DQN', 'landlord_wins')
    logger.plot('DQN', 'loss')
    logger.plot('DQN', 'agent_peasant_wins')
    logger.plot('DQN', 'agent_landlord_wins')

    #algorithm_list = ['peasant_wins', 'reward', 'landlord_wins', 'agent_landlord_wins', 'agent_peasant_wins']
    #plotlist = ['peasant_wins', 'reward', 'landlord_wins','agent_landlord_wins', 'agent_peasant_wins']
    algorithm_list = ['reward', 'agent_landlord_wins', 'agent_peasant_wins']
    plotlist = ['reward', 'agent_landlord_wins', 'agent_peasant_wins']

    logger.plot_all(algorithm_list, plotlist)
    # save the model

    nr = 0
    nr = (str)(nr)

    save_dir = 'models/doudizhu_dqn_' + nr
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    else:
        while(os.path.exists(save_dir)):
            nr = (int)(nr) + 1
            nr = (str)(nr)
            save_dir = 'models/doudizhu_dqn_' + nr +'/'

    saver = tf.train.Saver()
    saver.save(sess, os.path.join(save_dir, 'model'))
