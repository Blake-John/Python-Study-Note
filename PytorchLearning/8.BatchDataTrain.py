import torch
import torch.utils.data as Data

BATCH_SIZE = 8 # 一批数据的个数

x = torch.linspace (1,10,10)
y = torch.linspace (10,1,10)

torch_dataset = Data.TensorDataset (x,y) # 把数据加载进数据集里
loader = Data.DataLoader (
    dataset=torch_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True,
    # num_workers=2 # 设置线程，当数据极其简单时线程越少越好，此处单线比多线更快
) # 再用DataLoader分批提取数据
def main () :
    for epoch in range (3) :
        for step,(batch_x,batch_y) in enumerate (loader) : # enumerate 为提取loader时设计索引
            print ('Epoch:',epoch,'|Step:',step,'|batch x:',batch_x.numpy (),'|batch y:',batch_y.numpy ())
        
if __name__ == '__main__' :
    main ()