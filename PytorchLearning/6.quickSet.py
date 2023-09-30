import torch


# 快速搭建神经网络的方法
net = torch.nn.Sequential (
    torch.nn.Linear (2,10),
    torch.nn.ReLU (),
    torch.nn.Linear (10,2)
)

print (net)