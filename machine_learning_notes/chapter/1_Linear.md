# 线性回归
# 一、线性回归算法
## 1. 基本形式
&#8195;  给定数据集$D={(x_1, y_1), (x_2, y_2), ... }$，我们试图从此数据集中学习得到一个线性模型，这个模型尽可能准确地反映 $x_i$ 和 $y_i$ 的对应关系。这里的线性模型，就是属性 $x$ 的线性组合的函数，其中 $b$ 表示随机误差，可表示为：
$$f(x)=w_1 x_1 + w_2 x_2 +... + w_n x_n+b $$

* 用向量表示为：
$$f(x)=w^T x +b$$

* 常用的性能度量有均方误差，因此可以试图让均方误差最小化，那么有：
$$f(x_i)=w x_i+b ，使得f(x_i)\approx y_i $$

$$\begin{aligned}(w^{*},b^{*})
&=\mathop{\arg min}\limits_{w,b}\sum_{i=1}^{m}(f(x_i)-y_i)^{2}\\ 
&=\mathop{\arg min}\limits_{w,b}\sum_{i=1}^{m}(y_i-w x_i-b)^{2}\\ 
\end{aligned}$$

* 基于均方误差最小的方法称为"**最小二乘法"(least square method**)，在线性回归中，最小二乘法就是**试图找到一条直线，使得所有样本点到直线上的欧氏距离之和最小**。

* 线性回归求解 $w$ 和 $b$ 使 $E_{(w,b)}=\sum_{i=1}^{m} (y_{i}-w x_i-b)^2$ 最小化的过程，称为线性回归模型的最小二乘法"参数估计"，将 $E_{(w,b)}$ 对 $w$ 和 $b$ 进行求导，那么有：
$$\frac{\partial E_{(w,b)}}{\partial w}=
2\left( w \sum_{i=1}^{m}x_{i}^2 - \sum_{i=1}^{m} (y_{i}-b)x_i \right)$$

$$\frac{\partial E_{(w,b)}}{\partial b}=2\left( mb - \sum_{i=1}^{m} (y_{i}- w x_i) \right)$$

* 令上式为0可得到 $w$ 和 $b$ 最优解的闭式：
$$w= \frac{\sum_{i=1}^{m} y_{i}(x_{i}- \bar x)}{\sum_{i=1}^{m} x_i^{2} - \frac{1}{m}\left( \sum_{i=1}^{m} x_i\right)^2}
$$

$$b=\frac{1}{m}\sum_{i=1}^{m} (y_{i}- w x_i)$$
&#8195;  其中，$\bar x =\frac{1}{m}\sum_{i=1}^{m}x_i$，为 $x$ 的均值。

## 2. 向量形式
* 将 $w$ 进行化简，则有：
$$w = \frac{\sum_{i=1}^{m}y_i(x_i-\bar x)}{\sum_{i=1}^{m}(x_i^2-x_i\bar x)}$$

* 继续变形，则有：

$$w = \frac{\sum_{i=1}^{m}(x_i-\bar x)(y_i-\bar y)}{\sum_{i=1}^{m}(x_i-\bar x)^2}$$

* 令 $X = (x_1,x_2,...,x_m)^T,\; \vec X_d = (x_1-\vec x,x_2-\vec x,...,x_m-\vec x)^T$

* 令 $Y = (y_1,y_2,...,y_m)^T,\; \vec Y_d = (y_1-\vec y,y_2-\vec y,...,y_m-\vec y)^T$

* 最后的 $w$ 变成向量形式：
$$w = \frac{X^T_d \; Y^T_d}{X^T_d \; X_d}$$

---

# 二、多元线性回归
* **多元线性回归**(**multiple linear regression**) 模型的目的是构建一个回归方程，利用多个自变量估计因变量，从而解释和预测因变量的值。多元总体线性回归方程一般形式如下：
$$y=  w_0+ w_1 x_1+ w_2 x_2 + ... + w_n x_n +  b
$$其中，$y$ 为因变量，$x$ 为自变量，上式中共有 $n$ 个自变量和一个常数项。如果有 $m$ 组观测数据，用方程组形式表示为:
$$\begin{cases}
y_1= w_0+ w_1 x_{11}+ w_2 x_{12} + ... + w_n x_{1n}+ b\\
y_2= w_0+ w_1 x_{21}+ w_2 x_{22} + ... + w_n x_{2n}+ b\\
\vdots\\
y_m= w_0+ w_1 x_{m1}+ w_2 x_{m2} + ... + w_n x_{mn}+ b\\
\end{cases}$$

* 我们令：
$$y = \begin{pmatrix} 
y_1\\ y_2\\  \vdots\\  y_m \end{pmatrix},
X=\begin{pmatrix} 
1 & x_{11} & x_{12} & \cdots & x_{1n}\\ 
1 & x_{21} & x_{22} & \cdots & x_{2n}\\ 
\vdots & \vdots & \vdots & \ddots & \vdots \\ 
1 & x_{m1} & x_{m2} & \cdots & x_{mn}\\ 
\end{pmatrix},
w = \begin{pmatrix} 
 w_0\\ w_1\\ w_2\\ \vdots\\ w_n
\end{pmatrix},
b= \begin{pmatrix} 
 b_0\\ b_1\\ b_2\\ \vdots\\ b_n
\end{pmatrix}$$

* 其简化如下所示：
$$y=X  w+  b$$

## 1. 多元线性回归先决条件
* 自变量与因变量之间存在**线性关系**；

* 任意两个观测残差的**协方差为0**，也就是要求自变量间不存在多重共线性；

* 残差 $\varepsilon$ 服从 $N(0,δ^2)$ 正态分布，也就是对自变量的任意一组观测值，因变量 $y$ 具有相同的方差，且**服从正态分布**；

* 残差 $\varepsilon$ 的大小不随所有变量取值水平的改变而改变，即**方差齐性**。

## 2. 最小二乘估计
* 为了便于计算，令 $\hat w = (w; b)=(w_1,w_2,...,w_n;b)$；

* 利用均方误差最小化，使得：
$$\hat  w=argmin(y-X\hat  w)^T(y-X\hat  w)$$

* 令$E_{\hat  w}=(y-X\hat  w)^T(y-X\hat  w)$，对$\hat  w$求导，则有：
$$\frac{\partial E_{\hat w}}{\partial \hat w}=
2X^T(X\hat w-y)$$

* 当$X^TX$为满秩矩阵或者正定矩阵时，令上式为0，那么模型矩阵系数为：
$$\hat w=(X^{T}X)^{-1}X^{T}y$$

* 最后可得多元线性回归方程的最终拟合模型为：
$$\hat X= X^T(X^{T}X)^{-1}X^{T}y$$

---

# 三、L1正则化
&#8195;  线性回归的 **L1正则化** 通常称为 **Lasso回归**，它和一般线性回归的区别是在损失函数上增加了一个 L1 正则化的项，L1正则化的项有一个常数系数 α 来调节损失函数的均方差项和正则化项的权重，具体 `Lasso回归` 的损失函数表达式如下：

$$J(w) = (y - Xw)^T(y-Xw) + \lambda||w||$$

&#8195;  其中 $n$ 为样本个数，$||w||$ 为 L1 范数， $\lambda$ 为常数系数，需要进行调优。Lasso回归可以使得一些特征的系数变小，甚至还是一些绝对值较小的系数直接变为0。增强模型的泛化能力。Lasso回归的求解办法一般有**坐标轴下降法（coordinate descent）**和**最小角回归法（ Least Angle Regression）**。

## 1. 用坐标轴下降法求解Lasso回归
### 1.1 介绍
&#8195;  坐标轴下降法顾名思义，是沿着坐标轴的方向去下降，这和梯度下降不同。梯度下降是沿着**梯度的负方向下降**。不过梯度下降和坐标轴下降的共性就都是迭代法，通过启发式的方式一步步迭代求解函数的最小值。

&#8195;  坐标轴下降法的数学依据主要是这个结论：
一个可微的凸函数 $J(w)$, 其中 $w$ 是 $n\times 1$ 的向量，即有 $n$ 个维度。如果在某一点 $\bar w$，使得 $J(w)$ 在每一个坐标轴 $\bar w_i(i = 1,2,...n)$ 上都是最小值，那么 $J(\bar w_i)$ 就是一个全局的最小值。

&#8195;  于是我们的优化目标就是在 $w$ 的 $n$ 个坐标轴上(或者说向量的方向上)对损失函数做迭代的下降，当所有的坐标轴上的 $w_i(i = 1,2,...n)$ 都达到收敛时，我们的损失函数最小，此时的 $w$ 即为我们要求的结果。

### 1.2 算法流程
1. 首先，我们把 $w$ 向量随机取一个初值。记为 $w^{(0)}$，上面的括号里面的数字代表我们迭代的轮数，当前初始轮数为0。
2. 对于第 $k$ 轮的迭代。我们从$w^{(k)}_1$开始，到$w^{(k)}_n$为止，依次求$w^{(k)}_i$。$w^{(k)}_i$的表达式如下：
$$
 w_i^{(k)}  \in \underbrace{argmin}_{ w_i} J( w_1^{(k)},  w_2^{(k)}, ...  w_{i-1}^{(k)},  w_i,  w_{i+1}^{(k-1)}, ...,  w_n^{(k-1)})
$$也就是说$ w_i^{(k)}$时使得$J( w_1^{(k)},  w_2^{(k)}, ...  w_{i-1}^{(k)},  w_i,  w_{i+1}^{(k-1)}, ...,  w_n^{(k-1)})$最小化时候的$w_i$的值。此时 $J(w)$ 只有$w^{(k)}_i$是变量，其余均为常量，因此最小值容易通过求导或者一维搜索求得。具体一点，在第$k$轮，$w$向量的$n$个维度的迭代式如下：

$$w_1^{(k)}  \in \underbrace{argmin}_{ w_1} J( w_1,  w_2^{(k-1)}, ... ,  w_n^{(k-1)})$$

$$w_2^{(k)}  \in \underbrace{argmin}_{ w_2} J( w_1^{(k)},  w_2,  w_3^{(k-1)}... ,  w_n^{(k-1)})$$

$$\vdots $$

$$w_n^{(k)}  \in \underbrace{argmin}_{ w_n} J( w_1^{(k)},  w_2^{(k)}, ... ,  w_{n-1}^{(k)},  w_n)$$

3. 检查$w^{(k)}$向量和$w^{(k-1)}$向量在各个维度上的变化情况，如果在所有维度上变化都足够小，那么$w^{(k)}$即为最终结果，否则转入2，继续第$k+1$轮的迭代。

### 1.3 和梯度下降的比较
1. 坐标轴下降法在每次迭代中在当前点处沿一个坐标方向进行一维搜索 ，固定其他的坐标方向，找到一个函数的局部极小值。而梯度下降总是沿着梯度的负方向求函数的局部最小值。
2. 坐标轴下降优化方法是一种**非梯度优化算法**。在整个过程中依次循环使用不同的坐标方向进行迭代，一个周期的一维搜索迭代过程相当于一个梯度下降的迭代。
3. **梯度下降是利用目标函数的导数来确定搜索方向的，该梯度方向可能不与任何坐标轴平行。而坐标轴下降法法是利用当前坐标方向进行搜索，不需要求目标函数的导数，只按照某一坐标方向进行搜索最小值**。
4. 两者都是迭代方法，且每一轮迭代，都需要$O(mn)$的计算量($m$ 为样本数，$n$为系数向量的维度)

## 2. 用最小角回归法求解Lasso回归
### 2.1 前向选择（`Forward Selection`）算法
* 前向选择算法的原理是一种典型的贪心算法。要解决的问题是对于:
  * $y=Xw$ 这样的线性关系，如何求解系数向量$w$的问题。其中 $y$ 为 $m\times 1$ 的向量，$X$为 $m\times n$ 的矩阵，$w$ 为 $n\times 1$ 的向量。$m$ 为样本数量，$n$ 为特征维度。

* 把矩阵$X$看做 $n$ 个 $m\times 1$ 的向量$X_i(i=1,2,...n)$，在 $y$ 的 $X$ 变量 $X_i(i =1,2,...n)$ 中，选择和目标 $y$ 最为接近(余弦距离最大)的一个变量 $X_k$，用$X_k$ 来逼近 $y$，得到下式：
$$\overline{{y}} = {X_k w_k}
$$其中${ w_k}= {\frac{<X_k, y>}{||X_k||_2}}$,即：$\bar y$是 $y$ 在$X_k$上的投影。

* 那么，可以定义残差(`residual`)：$y_{res}=y−\bar y$。

* 由于是投影，所以很容易知道 $y_{res}$和$X_k$是正交的。再以$y_{res}$为新的因变量，去掉$X_k$后，剩下的自变量的集合$X_i(i=1,2,...k,k+1,...n)$ 为新的自变量集合，重复刚才投影和残差的操作，直到残差为0，或者所有的自变量都用完了，才停止算法。

![](https://upload-images.jianshu.io/upload_images/16911112-65b2b9d2c86c1240.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

* 当 $X$ 只有2维时，例子如上图，和 $y$ 最接近的是 $X_1$，首先在 $X_1$ 上面投影，残差如上图长虚线。此时 $X_1 w_1$ 模拟了 $y$，$w_1$模拟了 $w$ (仅仅模拟了一个维度)。接着发现最接近的是 $X_2$，此时用残差接着在 $X_2$ 投影，残差如图中短虚线。由于没有其他自变量了，此时 $X_1 w_1+X_2 w_2$ 模拟了 $y$,对应的模拟了两个维度的 $w$ 即为最终结果。

* 此算法对每个变量只需要执行一次操作，效率高，速度快。但也容易看出，当自变量不是正交的时候，由于每次都是在做投影，所有算法只能给出一个局部近似解。因此，这个简单的算法太粗糙，还不能直接用于我们的Lasso回归。

### 2.2 前向梯度（Forward Stagewise）算法
* 在 $y$ 的 $X$ 变量 $X_i(i =1,2,...n)$ 中，选择和目标 $y$ 最为接近(余弦距离最大)的一个变量 $X_k$，用 $X_k$ 来逼近 $y$，但是前向梯度算法不是粗暴的用投影，而是每次在最为接近的自变量 $X_t$ 的方向移动一小步，然后再看残差 $y_{res}$ 和哪个 $X_i(i =1,2,...n)$ 最为接近。

* 此时我们也不会把 $X_t$ 去除，因为我们只是前进了一小步，有可能下面最接近的自变量还是 $X_t$。如此进行下去，直到残差 $y_{res}$ 减小到足够小，算法停止。

![](https://upload-images.jianshu.io/upload_images/16911112-d3a66b1d7fdb5c6d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

&#8195;  $X$ 只有2维时，例子如上图，和 $y$ 最接近的是 $X_1$，首先在 $X_1$ 上面走一小段距离，此处 $ε$ 为一个较小的常量，发现此时的残差还是和 $X_1$ 最接近。那么接着沿 $X_1$ 走，一直走到发现残差不是和 $X_1$ 最接近，而是和 $X_2$ 最接近，此时残差如上图长虚线。接着沿着 $X_2$ 走一小步，发现残差此时又和 $X_1$ 最接近，那么开始沿着 $X_1$ 走，走完一步后发现残差为0，那么算法停止。此时y由刚才所有的所有步相加而模拟，对应的算出的系数 $w$ 即为最终结果。

* 当算法在 $ε$ 很小的时候，可以很精确的给出最优解，当然，其计算的迭代次数也是大大的增加。和前向选择算法相比，前向梯度算法更加精确，但是更加复杂。

### 2.3 最小角回归(Least Angle Regression， LARS)算法
&#8195;  最小角回归法对前向梯度算法和前向选择算法做了折中，保留了前向梯度算法一定程度的精确性，同时简化了前向梯度算法一步步迭代的过程。具体算法如下：　

* 首先，将所有系数 $\theta$ 设为0，找到与因变量 $y$ 最接近或者相关度最高的自变量比如 $X_1$；

* 然后在这个方向上前进尽可能大的一步（需要调节相关系数$\theta$），直到出现第二个变量比如 $X_2$，使得 $X_1$ 和 $y_{res}$ 的相关度和 $X_2$ 与 $y_{res}$ 的相关度是一样的；

* 此时残差 $y_{res}$ 就在 $X_1$ 和 $X_2$ 的角平分线方向上，我们开始沿着这个残差角平分线走，直到出现第三个变量 $X_3$ 和 $y_{res}$ 的相关度足够大的时候，即 $X_3$ 到当前残差 $y_{res}$ 的相关度和 $X_1$，$X_2$ 与 $y_{res}$ 的一样。

* 将 $X_3$ 其也加入到 $y$ 的逼近特征集合中，并用 $y$ 的逼近特征集合的共同角分线，作为新的逼近方向。以此循环，直到 $y_{res}$ 足够的小，或者说所有的变量都已经取完了，算法停止。此时对应的系数$w$即为最终结果。

![](https://upload-images.jianshu.io/upload_images/16911112-5bac4ef39b580d20.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

&#8195;  当 $w$ 只有2维时，例子如上图，和$y$最接近的是$X_1$，首先在$X_1$上面走一段距离，一直到残差在$X_1$和$X_2$的角平分线上，此时沿着角平分线走，直到残差最够小时停止，此时对应的系数 $β$ 即为最终结果。最小角回归法是一个适用于高维数据的回归算法。

* 完整的求解过程请参考：[**最小角回归(Least Angle Regression)**](https://keson96.github.io/2016/10/26/2016-10-26-Least-Angle-Regression/)

* 主要优点
    * 特别适合于特征维度 $n$ 远高于样本数m的情况。
    * 算法的最坏计算复杂度和最小二乘法类似，但是其计算速度几乎和前向选择算法一样。
    * 可以产生分段线性结果的完整路径，这在模型的交叉验证中极为有用。

* 主要缺点
    * 由于LARS的迭代方向是根据目标的残差而定，所以该算法对样本的噪声极为敏感。

## 3. 总结
&#8195;  Lasso回归是在ridge回归的基础上发展起来的，如果模型的特征非常多，需要压缩，那么Lasso回归是很好的选择。一般的情况下，普通的线性回归模型就够了。

---

# 四、L2正则化
&#8195;  线性回归的L2正则化通常称为**Ridge回归**，它和一般线性回归的区别是在损失函数上增加了一个L2正则化的项，和Lasso回归的区别是Ridge回归的正则化项是L2范数，而Lasso回归的正则化项是L1范数。

* 具体Ridge回归的损失函数表达式如下：
$$J(w) = (y-Xw)^T(y-Xw) + \lambda||w||^2$$
其中 $\lambda$ 为常数系数，需要进行调优，$||w||^2$为L2范数。

* Ridge回归在不抛弃任何一个特征的情况下，缩小了回归系数，使得模型相对而言比较的稳定，但和Lasso回归比，这会使得模型的特征留的特别多，模型解释性差。Ridge回归的求解比较简单，一般用最小二乘法。这里给出用最小二乘法的矩阵推导形式，和普通线性回归类似。

* 令$J(w)$的导数为0，得到下式：
$$ {X^T(X w - y) + \lambda w} = 0$$

* 整理即可得到最后的 $w$ 的结果：
$$ { w = (X^TX + \lambda E)^{-1}X^Ty}$$
其中 $E$为单位矩阵。除了上面这两种常见的线性回归正则化，还有一些其他的线性回归正则化算法，区别主要就在于正则化项的不同，和损失函数的优化方式不同。

* 至于详细的推导过程以及 $\lambda$ 的选择可以参考下面：
    * [*岭回归、LASSO回归*](https://blog.csdn.net/qq_36523839/article/details/82931559)
    * [*岭回归和LASSO回归*](https://blog.csdn.net/weixin_43374551/article/details/83688913)

---

# 五、总结
### 优点
* 建模速度快，不需要很复杂的计算，在数据量大的情况下依然运行速度很快。  
* 可以根据系数给出每个变量的理解和解释.

### 缺点
* 不能很好地拟合非线性数据。所以需要先判断变量之间是否是线性关系。
