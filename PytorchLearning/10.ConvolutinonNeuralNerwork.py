import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.utils.data as Data
import torchvision
import matplotlib.pyplot as plt
import os


# Hyper Parameters
EPOCH = 1
BATCH_SIZE  = 50
Learning_Rate = 0.001
DOWNLOAD_MNIST = False

if not os.path.exists ('./mnist') or not os.listdir ('./mnist') :
    DOWNLOAD_MNIST = True

train_data = torchvision.datasets.MNIST (
    root='./mnist', # 保存的目录
    train=True, # 设置是否为训练的数据
    transform=torchvision.transforms.ToTensor (), # 把下载的数据转化成tensor的形式
    download=DOWNLOAD_MNIST # 设置是否下载
) # 用于训练的数据， train 参数设置为 True

# 查看下载的数据
# print (train_data.train_data.size ())
# print (train_data.train_labels.size ())
# plt.imshow (train_data.train_data[0].numpy (),cmap='gray')
# plt.title ('%i' % train_data.train_labels[0])
# plt.show ()

train_loader = Data.DataLoader (
    dataset=train_data,
    batch_size=BATCH_SIZE,
    shuffle=True,
    # num_workers=2
) # 将要用于训练的数据加载成一个数据集，用于后续训练

test_data = torchvision.datasets.MNIST (
    root='./mnist', # 保存的目录
    train=False, # 设置是否为训练的数据
) # 训练完成后用于测试神经网络模型的数据
test_x = (Variable (torch.unsqueeze (test_data.data,dim=1)).type (torch.FloatTensor))[:2000]/255
# /255 是为了使 test_x 的数据处于 (0,1) 的范围内，因为黑白图片像素点的数据从0到255
test_y = test_data.targets[:2000]
# [:2000] 是从开始选取前2000个数据，选2000是为了减少测试，训练的量


class CNN (nn.Module) :
    def __init__ (self) :
        super (CNN,self).__init__ ()
        self.conv1 = nn.Sequential (
            nn.Conv2d (        # (1,28,28) 图片的维度，1为层高，28，28为长宽
                in_channels=1, # 输入数据的层高度，如黑白图片为一层，彩色图片有RGB三个层
                out_channels=16, # 设置多少个输出通道，即有多少个filter同时扫描，是输出后的层高度
                kernel_size=5, # 设置filter的长宽
                stride=1, # 设置步幅，即filter每次移动的长度
                padding=2 # 设置填充，即在图片周围填上一圈颜色为0(黑色)的区域宽度
                # stride 希望减少输入参数的数目，减少计算量
                # padding 希望每个输入方块能作为卷积窗口(filter)的中心，即在扫描方框的中心
                # if stride == 1,padding = (kernel_size - 1)/2
            ), # 卷积层，利用filter提取图片中的各种信息
            # 经过第一层卷积，图片的维度变成 (16,28,28) ,kernel_size=5,stride=1,padding=2使得图片长宽不变
            nn.ReLU (),   # 神经网络激励层
            nn.MaxPool2d (kernel_size=2) # 池化层,继续往下筛选重要的部分，取区域内最大值作为筛选特征
            # 2*2的范围内只选取一个点，则减小为一半，此时输出层维度为 (16,14,14)
        )
        self.conv2 = nn.Sequential ( # 输入层维度 (16,14,14)
            nn.Conv2d (16,32,5,1,2), # 如果不标注会按参数默认排列顺序填充 
            # 此时输出层维度为 (32,14,14)
            nn.ReLU (),
            nn.MaxPool2d (2) # AvgPool 会选择区域内的均值输出 
            # 此时输出层维度为 (32,7,7)
        )
        self.out = nn.Linear (32 * 7 * 7,10) # 把上一个卷积层输出的数据展平为二维的
    
    def forward (self,x) :
        x = self.conv1 (x)
        x = self.conv2 (x)  # (batch,32,7,7) 数据本身有考虑batch，只不过上面不涉及
        x = x.view (x.size (0),-1)  
        # x.size (0) 是把数据的 batch 保留，-1 是把(32,7,7)展平成(32 * 7 * 7)，即(batch,32 * 7 * 7)
        # 确切地说，这里 x.view (x.size (0),-1) 是要将该数据重新转化维度，这里有两个参数则转化为二维数据
        # 以 batch 为最外围，-1代表自动填充下一维度并保证数据总量不变
        output = self.out (x)
        return output ,x # return x for visualization


def main () :
    cnn = CNN ()
    print (cnn)

    optimizer = torch.optim.Adam (cnn.parameters (),lr=Learning_Rate)
    loss_func = nn.CrossEntropyLoss () # 分类使用 CrossEntropyLoss 作损失函数

    # following function (plot_with_labels) is for visualization, can be ignored if not interested
    from matplotlib import cm
    try: from sklearn.manifold import TSNE; HAS_SK = True
    except: HAS_SK = False; print('Please install sklearn for layer visualization')
    def plot_with_labels(lowDWeights, labels):
        plt.cla()
        X, Y = lowDWeights[:, 0], lowDWeights[:, 1]
        for x, y, s in zip(X, Y, labels):
            c = cm.rainbow(int(255 * s / 9)); plt.text(x, y, s, backgroundcolor=c, fontsize=9)
        plt.xlim(X.min(), X.max()); plt.ylim(Y.min(), Y.max()); plt.title('Visualize last layer'); plt.show(); plt.pause(0.01)

    plt.ion()

    for epoch in range (EPOCH) :
        for step,(x,y) in enumerate (train_loader) : # enumerate 使训练的数据集带上索引，用于 step 的计数
            b_x = Variable (x)
            b_y = Variable (y)

            output = cnn (b_x)[0] # 取神经网络输出时返回的的第一个结果，此时神经网络返回 output,x ，这里 [0] 取output
            loss = loss_func (output,b_y) # 利用 loss_func 来计算神经网络输出值和实际值之间的损失

            optimizer.zero_grad () # 将神经网络中所有节点的梯度设为 0
            loss.backward () # 将计算得到的损失值向前传递，为每一个节点计算出梯度
            optimizer.step () # 以lr为学习速率优化每个节点的梯度，把计算得到的参数留在节点中

            if step % 50 == 0 :
                test_output,last_layer = cnn (test_x) # test_output 是神经网络输出的结果，x 是最后输入的一层数据
                pred_y = torch.max (test_output,1)[1].data.numpy () # 在test_output 中选取最大值作为预测值
                accuracy = float ((pred_y == test_y.data.numpy ()).astype (int).sum ()) / float (test_y.size (0))
                # 计算预测的准确率
                print (test_output)
                print ('Epoch:',epoch,'| train loss: %.4f' % loss.data.numpy (),'| test accuracy: %.4f' % accuracy)
                
                if HAS_SK:
                    # Visualization of trained flatten layer (T-SNE)
                    tsne = TSNE(perplexity=30, n_components=2, init='pca', n_iter=5000)
                    plot_only = 500
                    low_dim_embs = tsne.fit_transform(last_layer.data.numpy()[:plot_only, :])
                    labels = test_y.numpy()[:plot_only]
                    plot_with_labels(low_dim_embs, labels)
    plt.ioff ()


    test_output,_ = cnn (test_x[:10]) # 选取数据集前10个数进入神经网络进行预测
    pred_y = torch.max (test_output,1)[1].data.numpy ()
    # 提取神经网络的输出结果
    print (pred_y,'prediction number')
    print (test_y[:10].numpy (),'real number')




if __name__ == '__main__' :
    main ()