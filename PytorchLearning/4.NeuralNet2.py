import torch
import torch.nn.functional as F
from torch.autograd import Variable
import matplotlib.pyplot as plt

epoch = 5000
x = torch.unsqueeze (torch.linspace (-1,1,100),dim=1)
y = x.pow (3) + 0.1*torch.rand (x.size ())
x,y = Variable (x),Variable (y)

class Net (torch.nn.Module) :
    def __init__ (self,n_input,n_features,n_output) :
        super(Net,self).__init__ ()
        self.hidden1 = torch.nn.Linear (n_input,n_features)
        self.hidden2 = torch.nn.Linear (n_features,n_features)
        self.predict = torch.nn.Linear (n_features,n_output)

    def forward (self,x) :
        x = F.relu(self.hidden1 (x))
        x = F.relu (self.hidden2 (x))
        x = self.predict (x)
        return x

net = Net (1,20,1)
print (net)

optimizer = torch.optim.SGD (net.parameters (),lr=0.5)
loss_func = torch.nn.MSELoss ()

plt.ion () # 设置打开交互模式，可画动态图片
plt.show ()

for i in range (epoch) :
    prediction = net (x)
    loss = loss_func (prediction,y)

    optimizer.zero_grad ()
    loss.backward ()
    optimizer.step ()

    if i % 2 == 0 :
        plt.cla ()
        plt.scatter (x.data.numpy (),y.data.numpy ())
        plt.plot (x.data.numpy (),prediction.data.numpy (),'r-',lw=5)
        plt.text (0.5,0,'Loss = %.4f' % loss.data,fontdict={'size':20,'color':'red'})
        plt.pause (0.05)

plt.ioff () # 阻塞模式，关闭交互，让图像停留，否则交互完毕后图像就会关闭
plt.show () # 使用 plt.plot 需要使用 plt.show 才能显示图像