import torch
import torch.nn.functional as F
from torch.autograd import Variable
import matplotlib.pyplot as plt

torch.manual_seed(1)    # 重复次数

x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)  # x data (tensor), shape=(100, 1)
y = x.pow(2) + 0.2*torch.rand(x.size())                 # noisy y data (tensor), shape=(100, 1)


x, y = Variable(x), Variable(y)

plt.scatter(x.data.numpy(), y.data.numpy())
plt.show()


class Net(torch.nn.Module):                     #搭建神经网络
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)   # 隐藏层
        self.predict = torch.nn.Linear(n_hidden, n_output)   # 输出层

    def forward(self, x):
        x = F.relu(self.hidden(x))      # 激活隐藏层
        x = self.predict(x)             # 线性输出
        return x

net = Net(n_feature=1, n_hidden=10, n_output=1)     # 定义神经网络，一个输入输出特征
print(net)  # 网络架构

# plt.ion()   # 将训练过程可视化
# plt.show()

optimizer = torch.optim.SGD(net.parameters(), lr=0.2)           # 优化器优化
loss_func = torch.nn.MSELoss()                                  # 误差计算，均方差

for t in range(200):        #开始训练，训练步数
    prediction = net(x)     # 预测值

    loss = loss_func(prediction, y)     # 预测值与真实值的误差，位置要预测值在前，真实值在后

    optimizer.zero_grad()   # 梯度设置为0
    loss.backward()         # 反向传递, 计算梯度
    optimizer.step()        # 优化梯度

    if t % 5 == 0:
        # 显示每个步骤以及图像
        plt.cla()
        plt.scatter(x.data.numpy(), y.data.numpy())                             #实时数据
        plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=5)           #预测数据
        plt.text(0.5, 0, 'Loss=%.4f' % loss.data.numpy(), fontdict={'size': 20, 'color':  'red'})       #学习时的误差是多少
        plt.pause(0.1)

plt.ioff()
plt.show()