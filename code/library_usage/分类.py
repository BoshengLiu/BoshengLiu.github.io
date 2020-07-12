
import torch
import torch.nn.functional as F
from torch.autograd import Variable
import matplotlib.pyplot as plt

# torch.manual_seed(1)    # reproducible

# make fake data
n_data = torch.ones(100, 2)
x0 = torch.normal(2*n_data, 1)              # class0 x 取值范围
y0 = torch.zeros(100)                       # class0 y 取值范围
x1 = torch.normal(-2*n_data, 1)             # class1 x 取值范围
y1 = torch.ones(100)                        # class1 取值范围
x = torch.cat((x0, x1), 0).type(torch.FloatTensor)      # x 合并在一起作为数据，FloatTensor = 32-bit floating
y = torch.cat((y0, y1), ).type(torch.LongTensor)        # y 合并在一起作为标签，LongTensor = 64-bit integer

# x, y = Variable(x), Variable(y)
#
# plt.scatter(x.data.numpy()[:, 0], x.data.numpy()[:, 1], c=y.data.numpy(), s=100, lw=0, cmap='RdYlGn')
# plt.show()            #可视化图形

class Net(torch.nn.Module):             # 搭建神经网络
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)      # 隐藏层
        self.out = torch.nn.Linear(n_hidden, n_output)          # 输出层

    def forward(self, x):
        x = F.relu(self.hidden(x))      #  # 激活隐藏层
        x = self.out(x)
        return x

net = Net(n_feature=2, n_hidden=10, n_output=2)     # 定义神经网络，两个输入输出特征
print(net)  # net architecture

optimizer = torch.optim.SGD(net.parameters(), lr=0.02)      # 优化器优化
loss_func = torch.nn.CrossEntropyLoss()                     # 误差计算

plt.ion()   # 训练过程可视化

for t in range(100):             # 开始训练，训练步数
    out = net(x)                 # 输出X的预测值
    loss = loss_func(out, y)     # must be (1. nn output, 2. target), the target label is NOT one-hotted

    optimizer.zero_grad()   # 梯度设置为0
    loss.backward()         # 反向传递, 计算梯度
    optimizer.step()        # 优化梯度

    if t % 2 == 0:
        # 每两步出一次图
        plt.cla()
        prediction = torch.max(out, 1)[1]       #最大概率值的位置
        pred_y = prediction.data.numpy()        #
        target_y = y.data.numpy()
        plt.scatter(x.data.numpy()[:, 0], x.data.numpy()[:, 1], c=pred_y, s=100, lw=0, cmap='RdYlGn')
        accuracy = float((pred_y == target_y).astype(int).sum()) / float(target_y.size)
        plt.text(1.5, -4, 'Accuracy=%.2f' % accuracy, fontdict={'size': 20, 'color':  'red'})
        plt.pause(0.1)

plt.ioff()
plt.show()