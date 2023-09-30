import torch
import torch.nn.functional as F # 神经网络模块
from torch.autograd import Variable
import matplotlib.pyplot as plt 


# fake data
x = torch.linspace (-5,5,200)  #(-5,5)之间的线段取200个点
x = Variable (x)
x_np = x.data.numpy () # variable的数据(torch的数据格式)无法被matplotlib识别，因而要转换成 numpy 的数据形式

# 通过四种方法计算关于x的激励函数图像，前四为线图，softmax作出的为概率图

# 下面为处理数据
y_relu = F.relu (x).data.numpy ()
y_sigmoid = torch.sigmoid (x).data.numpy () # sigmoid 和 tanh 已经独立出 torch.nn.functional，应使用 torch.sigmoid torch.tanh
y_tanh = torch.tanh (x).data.numpy ()
y_softplus = F.softplus (x).data.numpy ()
# y_softmax = F.softmax (x).data.numpy ()

# 具体作图

plt.figure (1,figsize=(8,6))

plt.subplot (221)
plt.plot (x_np,y_relu,c='red',label='relu')
plt.ylim ((-1,5)) # 纵轴长度
plt.legend (loc='best')

plt.subplot (221)
plt.plot (x_np,y_relu,c='red',label='relu')
plt.ylim ((-1,5)) # 纵轴长度
plt.legend (loc='best')

plt.subplot (222)
plt.plot (x_np,y_sigmoid,c='red',label='sigmoid')
plt.ylim ((-0.2,1.2)) # 纵轴长度
plt.legend (loc='best')

plt.subplot (223)
plt.plot (x_np,y_tanh,c='red',label='tanh')
plt.ylim ((-1.2,1.2)) # 纵轴长度
plt.legend (loc='best')

plt.subplot (224)
plt.plot (x_np,y_softplus,c='red',label='softplus')
plt.ylim ((-0.2,6)) # 纵轴长度
plt.legend (loc='best')

plt.show ()