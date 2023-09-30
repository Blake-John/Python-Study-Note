import torch
import torch.nn as nn
import torch.nn.functional as f
import numpy as np
import gym


BATCH_SIZE = 32
LR = 0.01
EPSILON = 0.9
GAMMA = 0.9
TARGET_REPLACE_ITER = 100
MEMORY_CAPACITY = 2000
env = gym.make ('CartPole-v0')
env = gym.unwrapped
N_ACTIONS = env.actioon_space.n
N_STATES = env.observation_space.shape[0]


class Net (nn.Module) :
    def __init__ (self) :
        super (Net,self).__init__ ()
        self.fc1 = nn.Linear (N_STATES,10)
        self.fc1.weight.data.normal_ (0,0.1)
        self.out = nn.Linear (10,N_ACTIONS)
        self.out.weight.data.normal_ (0,0.1)


    def forward (self,x) :
        x = self.fc1 (x)
        x = f.relu (x)
        actions_value = self.out (x)
        return actions_value


class DNQ (object) :
    def __init__ (self) :
        self.eval_net,self.target_net = Net (),Net ()

        self.learn_step_counter = 0
        self.memory_counter = 0
        self.memory = np.zeros ((MEMORY_CAPACITY,N_STATES * 2 + 2))
        self.optimizer = torch.optim.Adam (self.eval_net.parameters (),lr=LR)
        self.loss_func = nn.MSELoss ()

    def choose_action (self,x) :
        x = torch.unsqueeze (torch.FloatTensor (x),0)
        if np.random.uniform () < EPSILON :
            actions_value = self.eval_net.forward (x)
            action = torch.max (actions_value,1)[1].data.numpy ()[0,0]
        else :
            action = np.random.randint (0,N_ACTIONS)

    def store_transition (self,s,a,r,s) :
        pass

    def learn (self) :
        pass