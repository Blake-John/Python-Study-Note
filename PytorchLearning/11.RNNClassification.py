# RNN : Recurrent Neural Network
import os
import torch
import torchvision
import torch.nn as nn
from torch.autograd import Variable
import torch.utils.data as Data
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import matplotlib.pyplot as plt


# Hyper Parameters
EPOCH = 1 # 训练的轮数
BATCH_SIZE = 64 # 批处理的数目
TIME_STEP = 28 # filter 行进的次数
INPUT_SIZE = 28 # 输入神经网络的图片的大小
LR = 0.01 # 学习速率
DOWNLOAD_MNIST = False

if  not os.path.exists ('./mnist/') or not os.listdir ('./mnist') :
    DOWNLOAD_MNIST = True
# 设定 DOWNLOAD_MNIST 来决定是否下载数据

train_data = dsets.MNIST (
    root='./mnist',
    train=True,
    transform=transforms.ToTensor (),
    download=DOWNLOAD_MNIST
) # 用于训练的数据，因为要将其输入 pytorch 中，故要将其转化为 tensor 的形式
test_data = dsets.MNIST (
    root='./mnist',
    train=False,
    transform=transforms.ToTensor ()
) # 用于测试的数据，故 train 设置为False，同样要输入神经网络中进行测试，故要转化为 tensor 的形式
train_loader = Data.DataLoader (
    dataset=train_data,
    batch_size=BATCH_SIZE,
    shuffle=True
) # 将用于训练的数据加载成适合训练的数据集，同时设置是否进行批处理，是否要将数据打乱进行加载

test_x = test_data.data.type (torch.FloatTensor)[:2000]/255
test_y = test_data.targets[:2000]

class RNN (nn.Module) :
    def __init__ (self) :
        super (RNN,self).__init__ ()
        self.rnn = nn.LSTM (
            input_size=INPUT_SIZE, # 设置输入 LSTM 的数据的大小
            hidden_size=64, # 设置隐藏层的数目
            num_layers=1, # 有几层 RNN Layer，层数越多，训练效果越好，但训练的时间越长
            batch_first=True # 设置此项使得输入和输出是以 batch size 为第一维度的特征集，即 (batch,time_step,input_size)
        ) # 启动LSTM
        self.out = nn.Linear (64,10)

    def forward (self,x) :
        r_out,(h_n,h_c) = self.rnn (x,None) 
        out = self.out (r_out[:,-1,:]) # 取输出结果的最后一层
        return out


rnn = RNN ()
print (rnn)

optimizer = torch.optim.Adam (rnn.parameters (),lr=LR)
loss_func = nn.CrossEntropyLoss ()

for epoch in range (EPOCH) :
    for step,(b_x,b_y) in enumerate (train_loader) :
        b_x = b_x.view (-1,28,28) # reshape x to (batch,time_step,input_step)
        output = rnn (b_x)
        loss = loss_func (output,b_y)
        optimizer.zero_grad ()
        loss.backward ()
        optimizer.step ()

        if step % 50 == 0 :
            test_output = rnn (test_x)
            pred_y = torch.max (test_output,1)[1].data.numpy ().squeeze ()
            # accuracy = (pred_y == test_y).astype (int).sum ()/test_y.size
            accuracy = float ((pred_y == test_y.data.numpy ()).astype (int).sum ()) / float (test_y.size (0))
            print ('Epoch:',epoch,'| train loss: %.4f' % loss.data.numpy (),'| test accuracy: %.4f' % accuracy)


test_output = rnn (test_x[:10].view (-1,28,28))
pred_y = torch.max (test_output,1)[1].data.numpy ()
print (pred_y,'prediction number')
print (test_y[:10],'real number')
