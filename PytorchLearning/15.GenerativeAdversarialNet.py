import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

# Hyper Parameters
EPOCH = 10000     # 训练轮数
BATCH_SIZE = 64   # 批大小
LR_G = 0.0001     # Generator的学习速率
LR_D = 0.0001     # Discriminator的学习速率
N_IDEAS = 5       # 输入Generato的参数大小
ART_COMPONENTS = 15 # Generator输出大小
PAINT_POINTS = np.vstack ([np.linspace (-1,1,ART_COMPONENTS) for _ in range (BATCH_SIZE)])
# vstack 用于打包数据，将括号里的所有数据打包成一个组
# for _ in range (BATCH_SIZE) 是将前面的数据重复 BATCH_SIZE 次，形成 BATCH_SIZE 组数据
# 最后得到了一组维度为 (64,15) 的数据

# # show the painting range
# plt.plot (PAINT_POINTS[0], 2 * np.power (PAINT_POINTS[0],2) + 1 ,c='#74BCFF',lw=3,label='UpBoundary')
# plt.plot (PAINT_POINTS[0], 1 * np.power (PAINT_POINTS[0],2) + 0 ,c='#FF9359',lw=3,label='BottomBoundary')
# plt.legend (loc='upper right')
# plt.show ()

def artist_works () :
    a = np.random.uniform (1,2,size=BATCH_SIZE)[:,np.newaxis] # newaxis插入新维度
    # uniform 在 [1,2) 范围内采样，样本数目为 BATCH_SIZE
    paintings = a * np.power (PAINT_POINTS,2) + (a-1) # power为求方，PAINT_POINTS的2次方
    paintings = torch.from_numpy (paintings).float () # 将numpy的数据形式转化为torch的形式
    return paintings

G = nn.Sequential (
    nn.Linear (N_IDEAS,128),
    nn.ReLU (),
    nn.Linear (128,ART_COMPONENTS),
)

D = nn.Sequential (
    nn.Linear (ART_COMPONENTS,128),
    nn.ReLU (),
    nn.Linear (128,1),
    nn.Sigmoid ()
)

op_G = torch.optim.Adam (G.parameters (),lr=LR_G)
op_D = torch.optim.Adam (D.parameters (),lr=LR_D)

plt.ion ()

for epoch in range (EPOCH) :
    artist_painting = artist_works ()
    
    G_ideas = torch.randn (BATCH_SIZE,N_IDEAS,requires_grad=True)
    # randn 输出均值为0，方差为1的随机数
    # 参数规定输出结果是维度为 (BATCH_SIZE,N_IDEAS) 的数据
    G_paintings = G (G_ideas)
    prob_artist1 = D (G_paintings)
    G_loss = torch.mean (torch.log (1 - prob_artist1))
    # 使G的loss最小，则D判定为G生成的概率要最大，则用 1 - prob_artist1
    
    op_G.zero_grad ()
    G_loss.backward ()
    op_G.step ()

    prob_artist0 = D (artist_painting)
    prob_artist1 = D (G_paintings.detach ()) # detach 将数据从计算图中剥离出来，返回一个没有梯度的tensor数据，使D得到的数据是原始数据
    D_loss = - torch.mean (torch.log (prob_artist0) + torch.log (1 - prob_artist1))
    
    op_D.zero_grad ()
    D_loss.backward (retain_graph=True)
    op_D.step ()

    


    # 可视化
    if epoch % 50 == 0:  # plotting
        plt.cla()
        plt.plot(PAINT_POINTS[0], G_paintings.data.numpy()[0], c='#4AD631', lw=3, label='Generated painting',)
        plt.plot(PAINT_POINTS[0], 2 * np.power(PAINT_POINTS[0], 2) + 1, c='#74BCFF', lw=3, label='upper bound')
        plt.plot(PAINT_POINTS[0], 1 * np.power(PAINT_POINTS[0], 2) + 0, c='#FF9359', lw=3, label='lower bound')
        plt.text(-.5, 2.3, 'D accuracy=%.2f (0.5 for D to converge)' % prob_artist0.data.numpy().mean(), fontdict={'size': 13})
        plt.text(-.5, 2, 'D score= %.2f (-1.38 for G to converge)' % -D_loss.data.numpy(), fontdict={'size': 13})
        plt.ylim((0, 3));plt.legend(loc='upper right', fontsize=10);plt.draw();plt.pause(0.01)

plt.ioff ()
plt.show ()