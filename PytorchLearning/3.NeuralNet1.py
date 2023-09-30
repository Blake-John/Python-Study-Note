import torch 
from torch.autograd import Variable
import torch.nn.functional as F
import matplotlib.pyplot as plt 

epoch = 1000

x = torch.unsqueeze (torch.linspace (-1,1,100),dim=1) 
# 套上unsqueeze是为了把数据转化成二维的，因为在torch的网络中的数据是有维度的，pytorch只能处理二维的数据
y = x.pow (2)  + 0.2*torch.rand (x.size ()) 
# y为x的二次方再加一些噪点的影响
# rand 返回了一个张量，包含了从 [0,1) 中的均匀分布中抽取的一组随机数，张量的形状由size定义

x,y = Variable (x),Variable (y) # pytorch的神经网络中只能输入 Variable 的形式

# x，y的图
# plt.scatter (x.data.numpy (),y.data.numpy ()) 
# plt.show ()

# 定义一个神经网络
class Net (torch.nn.Module) : # 继承torch中的一个神经网络模块
    def __init__ (self,n_feature,n_hidden,n_output) :
        super (Net,self).__init__ ()
        self.hidden = torch.nn.Linear (n_feature,n_hidden) 
        # 一层神经网络，需要规定又多少个输入口，多少个输出口
        self.predict = torch.nn.Linear (n_hidden,n_output) # 另一层神经网络

    def forward (self,x) : # 神经网络前向传递的过程
        x = F.relu (self.hidden (x))
        # 使用激励函数激活信息，并用hidden层来加工数据x
        x = self.predict (x)
        return x

net = Net (1,10,1) # 一个输入口，10个隐藏层，1个输出口
print (net)

plt.ion ()
plt.show ()


# 优化神经网络
optimizer = torch.optim.SGD (net.parameters (),lr=0.15) # net.parameters ()代表了网络的所有参数，lr 是学习的速率
loss_func = torch.nn.MSELoss () # MSELoss() 是利用均方差来处理回归问题

# 开始训练
for i in range (epoch) :
    prediction = net (x) # 预测值为神经网络输出的结果

    loss = loss_func (prediction,y) # 计算误差 prediction为预测值，y为真实值

    optimizer.zero_grad () # 把所有参数梯度圈全部降为0
    loss.backward () # 反向传递，为每一个节点计算出梯度
    optimizer.step () # 以0.5的学习效率优化计算出的梯度

    if i % 5 == 0 :
        # 每五步重新打印一次结果
        plt.cla ()
        plt.scatter (x.data.numpy (),y.data.numpy ()) # 原数据的图，scatter 输出的是点图
        plt.plot (x.data.numpy (),prediction.data.numpy (),'r-',lw=5) # plot 输出的是线图
        plt.text (0.5,0,'Loss=%.4f' % loss.data,fontdict={'size':20,'color':'red'})
        plt.pause (0.1)


plt.ioff ()
plt.show ()