# 数值计算
# 一、梯度下降法
## 1. 梯度
&#8195;  在微积分里面，对多元函数的参数求$∂$偏导数，把求得的各个参数的偏导数以向量的形式写出来，就是梯度。

&#8195;  比如函数$f(x,y)$，分别对$(x,y)$求偏导数，求得的梯度向量就是$(\frac{∂f}{∂x},\frac{∂f}{∂y})^T$，简称$grad f(x,y)$或者$▽f(x,y)$。对于在点$(x_0,y_0)$的具体梯度向量就是$(\frac{∂f}{∂x_0},\frac{∂f}{∂y_0})^T$，如果是3个参数的向量梯度，就是$(\frac{∂f}{∂x},\frac{∂f}{∂y},\frac{∂f}{∂z})^T$，以此类推。

&#8195;  那么这个梯度向量求出来有什么意义呢？他的意义从几何意义上讲，就是函数变化增加最快的地方。具体来说，对于函数$f(x,y)$在点$(x_0,y_0)$，沿着梯度向量的方向就是$(\frac{∂f}{∂x_0},\frac{∂f}{∂y_0})^T$的方向是$f(x,y)$增加最快的地方。或者说，沿着梯度向量的方向，更加容易找到函数的最大值。反过来说，沿着梯度向量相反的方向，也就是 $-(\frac{∂f}{∂x_0},\frac{∂f}{∂y_0})^T$的方向，梯度减少最快，也就是更加容易找到函数的最小值。


## 2. 梯度下降与梯度上升

&#8195;  在机器学习算法中，在最小化损失函数时，可以通过梯度下降法来一步步的迭代求解，得到最小化的损失函数，和模型参数值。反过来，如果我们需要求解损失函数的最大值，这时就需要用梯度上升法来迭代了。

&#8195;  梯度下降法和梯度上升法是可以互相转化的。比如我们需要求解损失函数$f(θ)$的最小值，这时我们需要用梯度下降法来迭代求解。但是实际上，我们可以反过来求解损失函数$-f(θ)$的最大值，这时梯度上升法就派上用场了。


## 3. 梯度下降法算法详解
### 3.1 直观解释

&#8195;  首先来看看梯度下降的一个直观的解释。比如我们在一座大山上的某处位置，由于我们不知道怎么下山，于是决定走一步算一步，也就是在每走到一个位置的时候，求解当前位置的梯度，沿着梯度的负方向，也就是当前最陡峭的位置向下走一步，然后继续求解当前位置梯度，向这一步所在位置沿着最陡峭最易下山的位置走一步。这样一步步的走下去，一直走到觉得我们已经到了山脚。当然这样走下去，有可能我们不能走到山脚，而是到了某一个局部的山峰低处。

&#8195;  从上面的解释可以看出，梯度下降不一定能够找到全局的最优解，有可能是一个局部最优解。当然，如果损失函数是凸函数，梯度下降法得到的解就一定是全局最优解。

![](https://upload-images.jianshu.io/upload_images/16911112-ee3cc8e0063070bc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 3.2 相关概念
在详细了解梯度下降的算法之前，我们先看看相关的一些概念。

* 1. **步长（Learning rate）**：步长决定了在梯度下降迭代的过程中，每一步沿梯度负方向前进的长度。用上面下山的例子，步长就是在当前这一步所在位置沿着最陡峭最易下山的位置走的那一步的长度。

* 2. **特征（feature）**：指的是样本中输入部分，比如2个单特征的样本$（x^{(0)},y^{(0)}）,（x^{(1)},y^{(1)}）$,则第一个样本特征为$x^{(0)}$，第一个样本输出为$y^{(0)}$。

* 3. **假设函数（hypothesis function）**：在监督学习中，为了拟合输入样本，而使用的假设函数，记为$h_{\theta}(x)$。比如对于单个特征的m个样本$（x^{(i)},y^{(i)}）(i=1,2,...m)$,可以采用拟合函数如下： $h_{\theta}(x) = \theta_0+\theta_1x$。

* 4. **损失函数（loss function）**：为了评估模型拟合的好坏，通常用损失函数来度量拟合的程度。损失函数极小化，意味着拟合程度最好，对应的模型参数即为最优参数。在线性回归中，损失函数通常为样本输出和假设函数的差取平方。比如对于m个样本$(x_i,y_i)(i=1,2,...m)$,采用线性回归，损失函数为：

$$J(\theta_0, \theta_1) = \sum\limits_{i=1}^{m}(h_\theta(x_i) - y_i)^2
$$其中$x_i$表示第i个样本特征，$y_i$表示第i个样本对应的输出，$h_\theta(x_i)$为假设函数。   

### 3.3 详细算法
&#8195;  梯度下降法的算法可以有代数法和矩阵法（也称向量法）两种表示，如果对矩阵分析不熟悉，则代数法更加容易理解。不过矩阵法更加的简洁，且由于使用了矩阵，实现逻辑更加的一目了然。这里先介绍代数法，后介绍矩阵法。

#### 3.3.1 代数方式描述

1. 先决条件： 确认优化模型的假设函数和损失函数。比如对于线性回归，假设函数表示为$h_\theta(x_1, x_2, ...x_n) = \theta_0 + \theta_{1}x_1 + ... + \theta_{n}x_{n}$，其中$θ_i (i = 0,1,2... n)$为模型参数每个样本的n个特征值。这个表示可以简化，我们增加一个特征$x_0 = 1$，这样$h_\theta(x_0, x_1, ...x_n) = \sum\limits_{i=0}^{n}\theta_{i}x_{i}$；
同样是线性回归，对应于上面的假设函数，损失函数为：
$$J(\theta_0, \theta_1..., \theta_n) = \frac{1}{2m}\sum\limits_{j=1}^{m}(h_\theta(x_0^{(j)}, x_1^{(j)}, ...x_n^{(j)}) - y_j)^2$$

2. 算法相关参数初始化：主要是初始化$θ_0,θ_1...,θ_n$，算法终止距离ε以及步长α。在没有任何先验知识的时候，我喜欢将所有的θ初始化为0， 将步长初始化为1。在调优的时候再优化。

3. 算法过程：
    * a. 确定当前位置的损失函数的梯度，对于$θ_i$，其梯度表达式如下：$$\frac{\partial}{\partial\theta_i}J(\theta_0, \theta_1..., \theta_n)$$

    * b. 用步长乘以损失函数的梯度，得到当前位置下降的距离，即$\alpha\frac{\partial}{\partial\theta_i}J(\theta_0, \theta_1..., \theta_n)$对应于前面登山例子中的某一步；

    * c. 确定是否所有的θi,梯度下降的距离都小于ε，如果小于ε则算法终止，当前所有的θi(i=0,1,...n)即为最终结果。否则进入步骤d；

    * d. 更新所有的θ，对于$θ_i$，其更新表达式如下。更新完毕后继续转入步骤a。
$$\theta_i = \theta_i - \alpha\frac{\partial}{\partial\theta_i}J(\theta_0, \theta_1..., \theta_n)$$

4. 下面用线性回归的例子来具体描述梯度下降。假设我们的样本是:
$$(x_1^{(0)}, x_2^{(0)}, ...x_n^{(0)}, y_0), (x_1^{(1)}, x_2^{(1)}, ...x_n^{(1)},y_1), ... (x_1^{(m)}, x_2^{(m)}, ...x_n^{(m)}, y_m)$$

    * a. 损失函数如前面先决条件所述：
$$J(\theta_0, \theta_1..., \theta_n) = \frac{1}{2m}\sum\limits_{j=0}^{m}(h_\theta(x_0^{(j)}, x_1^{(j)}, ...x_n^{(j)})- y_j)^2$$

    * b. 则在算法过程步骤a中对于$θ_i$的偏导数计算如下：
$$\frac{\partial}{\partial\theta_i}J(\theta_0, \theta_1..., \theta_n)= \frac{1}{m}\sum\limits_{j=0}^{m}(h_\theta(x_0^{(j)}, x_1^{(j)}, ...x_n^{(j)}) - y_j)x_i^{(j)}$$

    * c. 由于样本中没有$x_0$上式中，令所有的$x^j_0$为1，步骤d中$θ_i$的更新表达式如下：
$$\theta_i = \theta_i - \alpha\frac{1}{m}\sum\limits_{j=0}^{m}(h_\theta(x_0^{(j)}, x_1^{(j)}, ...x_n^{j}) - y_j)x_i^{(j)}$$

从这个例子可以看出当前点的梯度方向是由所有的样本决定的，加$\frac{1}{m}$是为了好理解。由于步长也为常数，他们的乘积也为常数，所以这里$α \frac{1}{m}$可以用一个常数表示。

#### 3.3.2 矩阵方式描述

1. 先决条件： 和上面类似， 需要确认优化模型的假设函数和损失函数。对于线性回归，假设函数$h_θ(x_1,x_2,...x_n)=θ_0+θ_1 x_1+...+θ_n x_n$的矩阵表达方式为：
$$h_\mathbf{\theta}(\mathbf{X}) = \mathbf{X\theta}$$
其中， 假设函数$h_θ(X)为m\times1$的向量，θ为$(n+1)\times1$的向量，里面有n+1个代数法的模型参数。X为$m\times(n+1)$维的矩阵。m代表样本的个数，n+1代表样本的特征数。
损失函数的表达式为：
$$J(\mathbf\theta) = \frac{1}{2}(\mathbf{X\theta} - \mathbf{Y})^T(\mathbf{X\theta} - \mathbf{Y})$$
其中Y是样本的输出向量，维度为$m\times1$.

2. 算法相关参数初始化: θ向量可以初始化为默认值，或者调优后的值。算法终止距离ε，步长α和(3.1)比没有变化。

3. 算法过程：
    * a. 确定当前位置的损失函数的梯度，对于θ向量,其梯度表达式如下：$\frac{\partial}{\partial\mathbf\theta}J(\mathbf\theta)$；

    * b. 用步长乘以损失函数的梯度，得到当前位置下降的距离，即$\alpha\frac{\partial}{\partial\theta}J(\theta)$对应于前面登山例子中的某一步；

    * c. 确定θ向量里面的每个值,梯度下降的距离都小于ε，如果小于ε则算法终止，当前θ向量即为最终结果。否则进入步骤d；

    * d. 更新θ向量，其更新表达式如下。更新完毕后继续转入步骤1。
$$\mathbf\theta= \mathbf\theta - \alpha\frac{\partial}{\partial\theta}J(\mathbf\theta)$$

还是用线性回归的例子来描述具体的算法过程。损失函数对于θ向量的偏导数计算如下：
$$\frac{\partial}{\partial\mathbf\theta}J(\mathbf\theta) = \mathbf{X}^T(\mathbf{X\theta} - \mathbf{Y}) \Rightarrow \mathbf\theta= \mathbf\theta - \alpha\mathbf{X}^T(\mathbf{X\theta} - \mathbf{Y})$$

### 3.4 算法调优

在使用梯度下降时，需要进行调优。

#### 3.4.1 步长选择
&#8195;  在前面的算法描述中，我提到取步长为1，但是实际上取值取决于数据样本，可以多取一些值，从大到小，分别运行算法，看看迭代效果，如果损失函数在变小，说明取值有效，否则要增大步长。前面说了。步长太大，会导致迭代过快，甚至有可能错过最优解。步长太小，迭代速度太慢，很长时间算法都不能结束。所以算法的步长需要多次运行后才能得到一个较为优的值。

#### 3.4.2 参数的初始值选择
&#8195;  初始值不同，获得的最小值也有可能不同，因此梯度下降求得的只是局部最小值；当然如果损失函数是凸函数则一定是最优解。由于有局部最优解的风险，需要多次用不同初始值运行算法，关键损失函数的最小值，选择损失函数最小化的初值。

#### 3.4.3 归一化
&#8195;  由于样本不同特征的取值范围不一样，可能导致迭代很慢，为了减少特征取值的影响，可以对特征数据归一化，也就是对于每个特征x，求出它的期望$\overline{x}$和标准差$std(x)$，然后转化为：
$$\frac{x - \overline{x}}{std(x)}
$$这样特征的新期望为0，新方差为1，迭代速度可以大大加快。


## 4. 梯度下降法大家族（BGD，SGD，MBGD）
### 4.1 批量梯度下降法（Batch Gradient Descent）
&#8195;  批量梯度下降法，是梯度下降法最常用的形式，具体做法也就是在更新参数时使用所有的样本来进行更新，这个方法对应于前面3.3.1的线性回归的梯度下降算法，也就是说(3.1)的梯度下降算法就是批量梯度下降法。　
$$\theta_i = \theta_i - \alpha\sum\limits_{j=1}^{m}(h_\theta(x_0^{(j)}, x_1^{(j)}, ...x_n^{(j)}) - y_j)x_i^{(j)}
$$由于我们有m个样本，这里求梯度的时候就用了所有m个样本的梯度数据。

### 4.2 随机梯度下降法（Stochastic Gradient Descent）
&#8195;  随机梯度下降法，其实和批量梯度下降法原理类似，区别在与求梯度时没有用所有的m个样本的数据，而是仅仅选取一个样本j来求梯度。对应的更新公式是：
$$\theta_i = \theta_i - \alpha (h_\theta(x_0^{(j)}, x_1^{(j)}, ...x_n^{(j)}) - y_j)x_i^{(j)}$$

&#8195;  随机梯度下降法，和(1)的批量梯度下降法是两个极端，一个采用所有数据来梯度下降，一个用一个样本来梯度下降。自然各自的优缺点都非常突出。
* 对于训练速度来说，随机梯度下降法由于每次仅仅采用一个样本来迭代，训练速度很快，而批量梯度下降法在样本量很大的时候，训练速度不能让人满意。
* 对于准确度来说，随机梯度下降法用于仅仅用一个样本决定梯度方向，导致解很有可能不是最优。对于收敛速度来说，由于随机梯度下降法一次迭代一个样本，导致迭代方向变化很大，不能很快的收敛到局部最优解。

### 4.3 小批量梯度下降法（Mini-batch Gradient Descent）
&#8195;  小批量梯度下降法是批量梯度下降法和随机梯度下降法的折衷，也就是对于m个样本，我们采用x个样子来迭代，1<x<m。一般可以取x=10，当然根据样本的数据，可以调整这个x的值。对应的更新公式是：
$$\theta_i = \theta_i - \alpha \sum\limits_{j=t}^{t+x-1}(h_\theta(x_0^{(j)}, x_1^{(j)}, ...x_n^{(j)}) - y_j)x_i^{(j)}$$


## 5. 梯度下降法和其他无约束优化算法的比较
&#8195;  在机器学习中的无约束优化算法，除了梯度下降以外，还有前面提到的**最小二乘法**，此外还有**牛顿法**和**拟牛顿法**。

### 5.1 梯度下降法和最小二乘法相比

* 梯度下降法需要选择步长，而最小二乘法不需要。
* 梯度下降法是迭代求解，最小二乘法是计算解析解。
* 如果样本量不算很大，且存在解析解，最小二乘法比起梯度下降法要有优势，计算速度很快。
* 但是如果样本量很大，用最小二乘法由于需要求一个超级大的逆矩阵，这时就很难或者很慢才能求解解析解了，使用迭代的梯度下降法比较有优势。

### 5.2 梯度下降法和牛顿法/拟牛顿法相比

* 两者都是迭代求解，不过梯度下降法是梯度求解，而牛顿法/拟牛顿法是用二阶的海森矩阵的逆矩阵或伪逆矩阵求解。
* 使用牛顿法/拟牛顿法收敛更快。
* 每次迭代的时间牛顿法/拟牛顿法比梯度下降法长。

---

# 二、极大似然估计

## 简介
&#8195;  极大似然估计，通俗理解来说，就是**利用已知的样本结果信息，反推最具有可能（最大概率）导致这些样本结果出现的模型参数值**。换句话说，极大似然估计提供了一种给定观察数据来评估模型参数的方法，即：“模型已定，参数未知”。

&#8195;  我们这样想，一当模型满足某个分布，它的参数值我通过极大似然估计法求出来的话。比如正态分布中公式如下：
$$f(x) = \frac{1}{\sqrt{2\pi} \sigma}e^{-\frac{(x-\mu)^{2}}{2\sigma^{2}}}$$

&#8195;  如果我通过极大似然估计，得到模型中参数$\mu$和$\sigma$的值，我们就得到了这个模型的均值和方差以及其它所有的信息。**极大似然估计中采样需满足一个重要的假设，就是所有的采样都是独立同分布的。**

&#8195;  首先看一下似然函数 $P(x|\theta)$，其中x表示某一个具体的数据，$\theta$表示模型的参数。对于函数$P(x|\theta)$：

* 如果$\theta$是已知确定的，x是变量，这个函数叫做概率函数(probability function)，它描述对于不同的样本点x，其出现概率是多少。

* 如果x是已知确定的， $\theta$是变量，这个函数叫做似然函数(likelihood function)，它描述对于不同的模型参数，出现x这个样本点的概率是多少。

    * 举个类似的例子：$f(x,y) = x^y $，即x的y次方；
    * 当x=2时，$f(y) = 2^y$，此时f(y)为指数函数；
    * 当y=2时，$f(x)=x^2$，此时f(x)为二次函数；
    * 同一个数学形式，从不同的变量角度观察，可以有不同的名字。

## 例子1
&#8195;  假如有一个罐子，里面有黑白两种颜色的球，数目多少不知，两种颜色的比例也不知。我们想知道罐中白球和黑球的比例，但我们不能把罐中的球全部拿出来数。

* 现在我们可以每次任意从已经摇匀的罐中拿一个球出来，记录球的颜色，然后把拿出来的球 再放回罐中。
* 这个过程可以重复，我们可以用记录的球的颜色来估计罐中黑白球的比例。
* 假如在前面的一百次重复记录中，有七十次是白球，请问罐中白球所占的比例最有可能是多少？

&#8195;  很多人马上就有答案了：70%。而其后的理论支撑是什么呢？

* 1. 我们假设罐中白球的比例是p，那么黑球的比例就是1-p。因为每抽一个球出来，在记录颜色之后，我们把抽出的球放回了罐中并摇匀，所以每次抽出来的球的颜色**服从同一独立分布**。

* 2. 这里我们把一次抽出来球的颜色称为一次抽样。题目中在一百次抽样中，七十次是白球的,三十次为黑球事件的概率是P(样本结果|Model)。

* 3. 如果第一次抽象的结果记为$x_1$，第二次抽样的结果记为$x_2....$，那么样本结果为$(x_1,x_2.....,x_{100})$。这样，我们可以得到如下表达式：
$$\begin{aligned}
P(x|\theta) & = P(x_1,x_2,...,x_{100}|\theta) \\
 & = P(x_1|\theta)P(x_2|\theta)...P(x_{100}|\theta) \\
 & = P^{70} \cdot (1-p)^{30} \\
\end{aligned}$$

* 4. 我们已经有了观察样本结果出现的概率表达式了。那么我们要求的模型的参数，也就是求的式中的p。从前面的式子中可以知道不同的p，直接导致P（样本结果|Model）的不同。

* 5. 如此一来，p实际上是有无数种分布的。如下所示：

|P(白球的比例)|(1-P)(黑球的比例)|
|:---:|:---:|
|50%|50%|

* p=50%时，那么$\theta = p^{50}\cdot(1-p)^{50}$

|P(白球的比例)|1-P(黑球的比例)|
|:---:|:---:|
|70%|30%|

* p=70%时，那么$\theta = p^{70}\cdot(1-p)^{30}$

&#8195;  既然有无数种分布可以选择，极大似然估计应该按照**让这个样本结果出现的可能性最大**这个原则去选取这个分布，也就是使得$p^{70}(1-p)^{30}$值最大，那么我们就可以看成是p的方程，求导即可！

&#8195;  那么既然事情已经发生了，为什么不让这个出现的结果的可能性最大呢？这也就是最大似然估计的核心。我们想办法让观察样本出现的概率最大，转换为数学问题就是使得：

&#8195;  对$f(p)=p^{70}(1-p)^{30}$求导，使其导数为0，得到的p值带入$f(p)$；

$$\frac{\partial f(p)}{\partial p} = 0 \implies p=0.7$$

$$\quad f(0.7) = (0.7)^{70} \cdot (1-0.7)^{30}$$

这样得到的结果就是f(p)的最大值。

## 例子2
&#8195;  假设我们要统计全国人民的年均收入，首先假设这个收入服从服从正态分布，但是该分布的均值与方差未知。我们没有人力与物力去统计全国每个人的收入。我们国家有10几亿人口呢？

* 1. 我们可以采用极大似然估计。我们比如选取一个城市，或者一个乡镇的人口收入，作为我们的观察样本结果。然后通过最大似然估计来获取上述假设中的正态分布的参数。

* 2. 有了参数的结果后，我们就可以知道该正态分布的期望和方差了。也就是我们通过了一个小样本的采样，反过来知道了全国人民年收入的一系列重要的数学指标量！

* 3. 那么我们就知道了极大似然估计的核心关键就是对于一些情况，样本太多，无法得出分布的参数值，可以采样小样本后，利用极大似然估计获取假设中分布的参数值。

---

# 三、最小二乘法
## 1. 最小二乘法的原理与要解决的问题

&#8195;  最小二乘法是由勒让德在19世纪发现的，原理的一般形式很简单，当然发现的过程是非常艰难的。形式如下式：
$$目标函数 = \sum\limits（观测值-理论值）^2$$

&#8195;  观测值就是我们的多组样本，理论值就是我们的假设拟合函数。目标函数也就是在机器学习中常说的损失函数，我们的目标是得到使目标函数最小化时候的拟合函数的模型。

* 举一个最简单的线性回归的简单例子，比如我们有m个只有一个特征的样本：
$$(x^{(1)},y^{(1)}), (x^{(2)},y^{(2)}),...,(x^{(m)},y^{(m)})$$

* 样本采用下面的拟合函数：
$$h_\theta(x) = \theta_0 + \theta_1 x$$

* 这样我们的样本有一个特征x，对应的拟合函数有两个参数$θ_0$和$θ_1$需要求出。我们的目标函数为：
$$J(\theta_0, \theta_1) = \sum\limits_{i=1}^{m}(y^{(i)} - h_\theta(x^{(i)})^2 = \sum\limits_{i=1}^{m}(y^{(i)} -  \theta_0 - \theta_1 x^{(i)})^2$$

&#8195;  用最小二乘法使$J(θ_0,θ_1)$最小，求出使$J(θ_0,θ_1)$最小时的$θ_0$和$θ_1$，这样拟合函数就得出了。

## 2. 最小二乘法的代数法解法

&#8195;  上面提到要使$J(θ_0,θ_1)$最小，方法就是对$θ_0$和$θ_1$分别来求偏导数，令偏导数为0，得到一个关于$θ_0$和$θ_1$的二元方程组。求解这个二元方程组，就可以得到$θ_0$和$θ_1$的值。下面我们具体看看过程。

### 2.1 一般情况
* $J(θ_0,θ_1)$对$θ_0$求导，得到如下方程：
$$\sum\limits_{i=1}^{m}(y^{(i)} -  \theta_0 - \theta_1 x^{(i)}) = 0$$

* $J(θ_0,θ_1)$对$θ_1$求导，得到如下方程：
$$\sum\limits_{i=1}^{m}(y^{(i)} -  \theta_0 - \theta_1 x^{(i)})x^{(i)} = 0$$

* 将上面两个方程组成一个二元一次方程组，容易求出$θ_0$和$θ_1$的值：
$$
\theta_0 = \sum\limits_{i=1}^{m}\big(x^{(i)})^2\sum\limits_{i=1}^{m}y^{(i)} - \sum\limits_{i=1}^{m}x^{(i)}\sum\limits_{i=1}^{m}x^{(i)}y^{(i)} \Bigg/ m\sum\limits_{i=1}^{m}\big(x^{(i)})^2 - \big(\sum\limits_{i=1}^{m}x^{(i)})^2
$$

$$
\theta_1 = m\sum\limits_{i=1}^{m}x^{(i)}y^{(i)} - \sum\limits_{i=1}^{m}x^{(i)}\sum\limits_{i=1}^{m}y^{(i)} \Bigg/ m\sum\limits_{i=1}^{m}\big(x^{(i)})^2 - \big(\sum\limits_{i=1}^{m}x^{(i)})^2
$$

### 2.2 多样本特征
&#8195;  这个方法可以推广到多个样本特征的线性拟合。 拟合函数表示为 $h_θ(x_1,x_2,...x_n)=θ_0+θ_1x1+...+θ_n x_n$, 其中$θ_i (i = 0,1,2... n)$为模型参数，$x_i (i = 0,1,2... n)$为每个样本的n个特征值。

* 这个表示可以简化，我们增加一个特征$x_0=1$，这样拟合函数表示为：
$$h_\theta(x_0, x_1, ...x_n) = \sum\limits_{i=0}^{n}\theta_{i}x_{i}$$

* 损失函数表示为：
$$J(\theta_0, \theta_1..., \theta_n) = \sum\limits_{j=1}^{m}(h_\theta(x_0^{(j)}), x_1^{(j)}, ...x_n^{(j)})) - y^{(j)}))^2 = \sum\limits_{j=1}^{m}(\sum\limits_{i=0}^{n}\theta_{i}x_{i}^{(j)}- y^{(j)})^2$$

* 利用损失函数分别对$θ_i(i=0,1,...n)$求导,并令导数为0可得：
$$\sum\limits_{j=0}^{m}(\sum\limits_{i=0}^{n}(\theta_{i}x_{i}^{(j)} - y^{(j)})x_i^{(j)} = 0 \quad(i=0,1,...,n)$$

&#8195;  这样我们得到一个N+1元一次方程组，这个方程组有N+1个方程，求解这个方程，就可以得到所有的N+1个未知的θ。这个方法很容易推广到多个样本特征的非线性拟合。原理和上面的一样，都是用损失函数对各个参数求导取0，然后求解方程组得到参数值。

## 3. 矩阵法解法

&#8195;  矩阵法比代数法要简洁，且矩阵运算可以取代循环，所以现在很多书和机器学习库都是用的矩阵法来做最小二乘法。这里用上面的多元线性回归例子来描述矩阵法解法。

* 假设函数$h_\theta(x_1, x_2, ...x_n) = \theta_0 + \theta_{1}x_1 + ... + \theta_{n-1}x_{n-1}$的矩阵表达方式为：
$$h_\mathbf{\theta}(\mathbf{x}) = \mathbf{X\theta}$$

* 其中， 假设函数$h_θ(X)$为$m\times1$的向量，θ为$n\times1$的向量，里面有n个代数法的模型参数。X为$m\times n$维的矩阵。m代表样本的个数，n代表样本的特征数。损失函数定义为：
$$J(\mathbf\theta) = \frac{1}{2}(\mathbf{X\theta} - \mathbf{Y})^T(\mathbf{X\theta} - \mathbf{Y})
$$其中Y是样本的输出向量，维度为$m\times 1$。$\frac{1}{2}$在这主要是为了求导后系数为1，方便计算。

* 根据最小二乘法的原理，我们要对这个损失函数对θ向量求导取0。结果如下式：

$$\frac{\partial}{\partial\mathbf\theta}J(\mathbf\theta) = \mathbf{X}^T(\mathbf{X\theta} - \mathbf{Y}) = 0$$

* 这里面用到了矩阵求导链式法则，和两个个矩阵求导的公式。
  * 公式1：$$ \frac{\partial}{\partial\mathbf{x}}(\mathbf{x^Tx}) =2\mathbf{x}, \quad x为向量$$
  * 公式2：$$ \nabla_Xf(AX+B) = A^T\nabla_Yf,\;\; Y=AX+B,\;\;f(Y)为标量$$

* 对上述求导等式整理后可得：
$$\mathbf{X^{T}X\theta} = \mathbf{X^{T}Y}$$

* 两边同时左乘$(\mathbf{X^{T}X})^{-1}$可得：
$$\mathbf{\theta} = (\mathbf{X^{T}X})^{-1}\mathbf{X^{T}Y}$$

&#8195;  这样我们就一下子求出了θ向量表达式的公式，免去了代数法一个个去求导的麻烦。只要给了数据,我们就可以用$\mathbf{\theta} = (\mathbf{X^{T}X})^{-1}\mathbf{X^{T}Y}$算出θ。


## 4. 局限性和适用场景

&#8195;  从上面可以看出，最小二乘法适用简洁高效，比梯度下降这样的迭代法似乎方便很多。但是这里我们就聊聊最小二乘法的局限性。

* 1. 首先，最小二乘法需要计算$X^TX$的逆矩阵，有可能它的逆矩阵不存在，这样就没有办法直接用最小二乘法了，此时梯度下降法仍然可以使用。当然，我们可以通过对样本数据进行整理，去掉冗余特征。让$X^TX$的行列式不为0，然后继续使用最小二乘法。

* 2. 当样本特征n非常的大的时候，计算$X^TX$的逆矩阵是一个非常耗时的工作（$n\times n$的矩阵求逆），甚至不可行。此时以梯度下降为代表的迭代法仍然可以使用。那这个n到底多大就不适合最小二乘法呢？如果你没有很多的分布式大数据计算资源，建议超过10000个特征就用迭代法吧。或者通过主成分分析降低特征的维度后再用最小二乘法。

* 3. 如果拟合函数不是线性的，这时无法使用最小二乘法，需要通过一些技巧转化为线性才能使用，此时梯度下降仍然可以用。

* 4. 当样本量m很少，小于特征数n的时候，这时拟合方程是欠定的，常用的优化方法都无法去拟合数据。当样本量m等于特征数n的时候，用方程组求解就可以了。当m大于n时，拟合方程是超定的，也就是我们常用与最小二乘法的场景了。

---

# 四、二阶导数与海森矩阵







---

# 五、牛顿法






---

# 六、拟牛顿法





---

# 七、约束优化


---