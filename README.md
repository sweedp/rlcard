# DRL and Dou Dizhu
### Deep Reinforcement Learning Semester Project @ UOS

This is the main repository for our semester project of creating a deep reinforcement learning agent to play the game Dou Dizhu.
It contains a modified copy of the RLCard toolkit repository.
We had to make a lot of changes to environment files for data logging and keeping our code running,
so we could not delete any of the other games inside the toolkit. We even had to use a second repository as the changes
that were needed for the PPO agent and the DQN agent overlapped partly.
The PPO repository can be found at https://github.com/tmhatton/Deep-Dou-Dizhu.

### Content & Usage

To make the agents better visible we moved them to the main directory.
The main script to train the agent is under ``doudizhu_dqn.py``.
As the names suggest, ``dqn_agent.py``contains the DQN Agent, ``ddqn_agent.py``the DDQN Agent, and ``dueling_ddqn_agent.py``the Dueling DDQN Agent.
The training results can be found in the folder ``results``.
The trained models are in ``models``.

### Usage

Open ``doudizhu_dqn.py`` and choose the name of the agent you want to train.
The comments in the code help you choose the specific parameters.
Run the script from this directory by calling
``python doudizhu_dqn.py``.

### Environment

RLCard needs Python=<3.7 and Tensorflow 1.

We set up an environment yml for Windows and MacOS.
If they do not work, please set up an environment that includes the following:
- python==3.7
- tensorflow==1.15
- rlcard==0.2.8

### Credits

All credits regarding the rlcard library go to the original authors, we do not claim any ownership. 

Zha, D., Lai, K. H., Cao, Y., Huang, S., Wei, R., Guo, J., & Hu, X. (2019). Rlcard: A toolkit for reinforcement learning in card games. arXiv preprint arXiv:1910.04376.

https://github.com/datamllab/rlcard
