import torch
import torch.utils.data as Data
import torch.nn.functional as F
from torch.autograd import Variable
import matplotlib.pyplot as plt

# 超参数：提前定义要使用的参数
learning_rate = 0.01
BATCH_SIZE = 32
EPOCH = 12

x = torch.unsqueeze (torch.linspace (-1,1,1000),dim=1) # unsqueeze 使数据x增加一个维度
y = x.pow (2) + 0.1*torch.normal (torch.zeros (*x.size ()))

# plt.scatter (x.data.numpy (),y.data.numpy ())
# plt.show ()

torch_dataset = Data.TensorDataset (x,y)
loader = Data.DataLoader (
    dataset=torch_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)
class Net (torch.nn.Module) :
    def __init__ (self,n_input,n_feature,n_output) :
        super (Net,self).__init__ ()
        self.hidden1 = torch.nn.Linear (n_input,n_feature)
        self.hidden2 = torch.nn.Linear (n_feature,n_feature)
        self.predict = torch.nn.Linear (n_feature,n_output)

    def forward (self,x) :
        x = F.relu (self.hidden1 (x))
        x = F.relu (self.hidden2 (x))
        x = self.predict (x)
        return x

net_SGD = Net (1,20,1)
net_Momentum = Net (1,20,1)
net_RMSprop = Net (1,20,1)
net_Adam = Net (1,20,1)
nets = [net_SGD,net_Momentum,net_RMSprop,net_Adam]

opt_SGD = torch.optim.SGD (net_SGD.parameters (),lr=learning_rate)
opt_Momentum = torch.optim.SGD (net_Momentum.parameters (),lr=learning_rate,momentum=0.8)
opt_RMSprop = torch.optim.RMSprop (net_RMSprop.parameters (),lr=learning_rate,alpha=0.9)
opt_Adam = torch.optim.Adam (net_Adam.parameters (),lr=learning_rate,betas=(0.9,0.99))
optimizers = [opt_SGD,opt_Momentum,opt_RMSprop,opt_Adam]

loss_func = torch.nn.MSELoss ()
losses_his = [[],[],[],[]] # 创建一个列表来记录各个优化器的损失

for epoch in range (EPOCH) :
    print ("Epoch:",epoch)
    for step,(batch_x,batch_y) in enumerate (loader) :
        b_x = Variable (batch_x)
        b_y = Variable (batch_y)

        for net,opt,l_his in zip (nets,optimizers,losses_his) :
            output = net (b_x)
            loss = loss_func (output,b_y)

            opt.zero_grad ()
            loss.backward ()
            opt.step ()
            l_his.append (loss.data.numpy ()) # 列表中不能添加tensor的数据，应在转化成numpy

labels = ['SGD','Momentum','RMSprop','Adam']
for i ,l_his in enumerate (losses_his) :
    plt.plot (l_his,label=labels[i])

plt.legend (loc='best')
plt.xlabel ('Steps')
plt.ylabel ('Loss')
plt.ylim ((0,1))
plt.show ()