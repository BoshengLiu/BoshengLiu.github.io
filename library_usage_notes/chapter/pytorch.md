# torch使用

## Pytorch基础

* numpy和torch对比
```
np_data = np.arange(6).reshape((2,3))
torch_data = torch.from_numpy(np_data)  # numpy转换成torch
tensor2array = torch_data.numpy()   # torch转换成numpy

data = [-1, 1, -2, 2]
tensor = torch.FloatTensor(data)    # 转换成32bit
torch.abs(tensor)
np.abs(data)    # 两个绝对值运算

data = [[1,2], [3,4]]
tensor = torch.FloatTensor(data)
np.matmul(data,data)
torch.mm(tensor, tensor)    # 矩阵相乘
```
        
        
* Variable变量

```
tensor = torch.FloatTensor([[1,2],[3,4]])
variable = Variable(tensor, required_grad=True)

t_out = torch.mean(tensor*tensor)
v_out = torch.mean(variable*variable)   # 求均值

v_out.backward()
print(variable.grad)    # 反向传递   
```


* 激励函数

---

## 建造神经网络

* 回归

* 分类

* 快速搭建法

* 保存提取

* 批训练

* 加速神经网络训练

* 优化器


---

## 高级神经网络结构

* 卷积神经网络(CNN)

* 循环神经网络(RNN)-回归

* 循环神经网络(RNN)-分类

* 自编码/非监督学习

* DQN强化学习

* 生成对抗网络(GAN)

---

## 高阶内容

* 关于Torch是动态

* GPU加速

* 过拟合(overfitting)

* 缓解过拟合(dropout)

* 批标准化