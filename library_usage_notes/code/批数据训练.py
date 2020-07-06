
import torch
import torch.utils.data as Data

torch.manual_seed(1)    # reproducible

BATCH_SIZE = 5          # 抽取5批数据
# BATCH_SIZE = 8        # 此时第二批数据小于8

x = torch.linspace(1, 10, 10)       # this is x data (torch tensor)
y = torch.linspace(10, 1, 10)       # this is y data (torch tensor)

torch_dataset = Data.TensorDataset(x, y)        #将数据导入
loader = Data.DataLoader(
    dataset=torch_dataset,      # torch 训练的数据来源
    batch_size=BATCH_SIZE,      # 最小batch size
    shuffle=True,               # 让数字随机
    num_workers=2,              # 为数据开启多线程
)


def show_batch():
    for epoch in range(3):   # 训练三次
        for step, (batch_x, batch_y) in enumerate(loader):  # 对每次训练的操作
            # train your data...
            print('Epoch: ', epoch, '| Step: ', step, '| batch x: ',
                  batch_x.numpy(), '| batch y: ', batch_y.numpy())


if __name__ == '__main__':
    show_batch()