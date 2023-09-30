import torch
from torch.autograd import Variable
import torchvision
from torch import nn
import matplotlib.pyplot as plt
import numpy as np

# torch.manual_seed (1)

EPOCH = 300
TIME_STEP = 10
INPUT_SIZE = 1
LR = 0.02

# # show data
# steps = np.linspace (0,np.pi * 2,100,dtype=np.float32)
# # float32 for converting torch FloatTensor
# x_np = np.sin (steps)
# y_np = np.cos (steps)
# plt.plot (steps,y_np,'r-',label='target (cos)')
# plt.plot (steps,x_np,'b-',label='input (sin)')
# plt.legend (loc='best')
# plt.show ()

class RNN (nn.Module) :
    def __init__ (self) :
        super (RNN,self).__init__ ()
        self.rnn = nn.RNN (
            input_size=INPUT_SIZE,
            hidden_size=32,
            num_layers=1,
            batch_first=True
        )
        self.out = nn.Linear (32,1)

    def forward (self,x,h_state) :
        # x (batch,time_step,input_size)
        # h_state (n_layers,batch,hidden_size)
        # r_out (batch,time_step,output_size'即为 hidden_size，因为我们要的得到的输出结果是要将其通过 self.out 转化为一个层)
        r_out,h_state = self.rnn (x,h_state)
        outs = []
        for time_step in range (r_out.size (1)) :
            outs.append (self.out (r_out[:,time_step,:]))
        # calculate ouput for each time step
        # r_out 中含有不同时间序列的输出结果，此步是在每一时间节点中遍历，并将每一次 RNN 输出的结果通过 self.out 进行处理，然后再将处理结果加入 outs 列表中

        return torch.stack (outs,dim=1),h_state
        # torch.stack 将 outs 的列表打包为 torch 的数据格式

        # instead, for simplicity, you can replace above codes by follows
        # r_out = r_out.view(-1, 32) # 使输出结果最里层为32个数据，能输入 out 中
        # outs = self.out(r_out)
        # outs = outs.view(-1, TIME_STEP, 1)
        # return outs, h_state
        
        # or even simpler, since nn.Linear can accept inputs of any dimension 
        # and returns outputs with same dimension except for the last
        # outs = self.out(r_out)
        # return outs



rnn = RNN ()
print (rnn)

h_state = None # 第一次的 h_state 设为 None，会自动生成全为 0 的 h_state

optimizer = torch.optim.Adam (rnn.parameters (),lr=LR)
loss_func = nn.MSELoss ()

plt.figure (1,figsize=(12,5)) # 设置显示数目图片 num，设置每一张图片的长和宽
plt.ion () # 打开交互模式，使图片能够持续更新，但绘图结束后会关闭界面

for step in range (EPOCH) :
    start,end = step * np.pi,(step + 1) * np.pi
    steps = np.linspace (start,end,TIME_STEP,dtype=np.float32)
    x_np = np.sin (steps)
    y_np = np.cos (steps)

    x = torch.from_numpy (x_np[np.newaxis,:,np.newaxis])
    y = torch.from_numpy (y_np[np.newaxis,:,np.newaxis])
    # 为 x 和 y 增加维度

    prediction,h_state = rnn (x,h_state)
    h_state = Variable (h_state.data) # 要把每次输出的 h_state 数据重新打包成torch可接收的形式，现在这步可省略

    loss = loss_func (prediction,y)
    optimizer.zero_grad ()
    loss.backward ()
    optimizer.step ()

    plt.plot (steps,y_np.flatten (),'r-') 
    # flatten (dim) 表示从第dim个维度开始展开，从外往里，将以后的维度转化为一维，没有dim则默认从第0维展开
    plt.plot (steps,prediction.data.numpy ().flatten (),'b-')
    plt.draw ();plt.pause (0.05)

plt.ioff () # 阻塞模式，使图片绘制完不会关闭界面
plt.show ()
