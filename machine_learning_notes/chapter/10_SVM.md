# 支持向量机(SVM)
# 一、简介
1. 支持向量机(`support vector machines： SVM`）是一种二分类模型。它是定义在特征空间上的、间隔最大的线性分类器。
    * 间隔最大使得支持向量机有别于感知机。如果数据集是线性可分的，那么感知机获得的模型可能有很多个，而支持向量机选择的是间隔最大的那一个。
    * 支持向量机还支持核技巧，从而使它成为实质上的非线性分类器。
    
2. 支持向量机支持处理线性可分数据集、非线性可分数据集。
    * 当训练数据线性可分时，通过硬间隔最大化，学习一个线性分类器，即线性可分支持向量机（也称作硬间隔支持向量机）。
    * 当训练数据近似线性可分时，通过软间隔最大化，学习一个线性分类器，即线性支持向量机（也称为软间隔支持向量机）。
    * 当训练数据不可分时，通过使用核技巧以及软间隔最大化，学习一个非线性分类器，即非线性支持向量机。
    
3. 当输入空间为 [*欧氏空间*](https://zh.wikipedia.org/wiki/%E6%AC%A7%E5%87%A0%E9%87%8C%E5%BE%97%E7%A9%BA%E9%97%B4) 或离散集合、特征空间为 [*希尔伯特空间*](https://zh.wikipedia.org/wiki/%E5%B8%8C%E5%B0%94%E4%BC%AF%E7%89%B9%E7%A9%BA%E9%97%B4) 时，将输入向量从输入空间映射到特征空间，得到特征向量。支持向量机的学习是在特征空间进行的。
    * 线性可分支持向量机、线性支持向量机假设这两个空间的元素一一对应，并将输入空间中的输入映射为特征空间中的特征向量。
    * 非线性支持向量机利用一个从输入空间到特征空间的非线性映射将输入映射为特征向量。
        * 特征向量之间的内积就是核函数，使用核函数可以学习非线性支持向量机。
        * 非线性支持向量机等价于隐式的在高维的特征空间中学习线性支持向量机，这种方法称作核技巧。
        
4. 欧氏空间是有限维度的，希尔伯特空间为无穷维度的。
    * 欧式空间 $\subseteq$ 希尔伯特空间 $\subseteq$ 内积空间 $\subseteq$ 赋范空间。
        * 欧式空间，具有很多美好的性质。
        * 若不局限于有限维度，就来到了希尔伯特空间。从有限到无限是一个质变，很多美好的性质消失了，一些非常有悖常识的现象会出现。
        * 如果再进一步去掉完备性，就来到了内积空间。
        * 如果再进一步去掉"角度"的概念，就来到了赋范空间。此时还有“长度”和“距离”的概念。
    * 越抽象的空间具有的性质越少，在这样的空间中能得到的结论就越少
    * 如果发现了赋范空间中的某些性质，那么前面那些空间也都具有这个性质。

---

# 二、线性SVM
## 1. 函数间隔与几何间隔
&#8195;  在正式介绍SVM的模型和损失函数之前，我们还需要先了解下函数间隔和几何间隔的知识。
* 在分离超平面固定为 $w^T +b =0$ 的时候，$|w^Tx + b |$ 表示点 x 到超平面的相对距离。

* 通过观察 $w^Tx+b$ 和 y 是否同号，我们判断分类是否正确。这里我们引入函数间隔的概念，定义函数间隔 γ′为：
$$\gamma^{'} = y(w^Tx + b)$$

* 可以看到，它就是感知机模型里面的误分类点到超平面距离的分子。对于训练集中 m 个样本点对应的 m 个函数间隔的最小值，就是整个训练集的函数间隔。

* 函数间隔并不能正常反应点到超平面的距离，在感知机模型里我们也提到，当分子成比例的增长时，分母也是成倍增长。为了统一度量，我们需要对法向量w加上约束条件，这样我们就得到了几何间隔 γ，定义为：
$$\gamma = \frac{y(w^Tx + b)}{||w||_2}= \frac{\gamma^{'}}{||w||_2}$$
几何间隔才是点到超平面的真正距离，感知机模型里用到的距离就是几何距离。

## 2. 支持向量
&#8195;  在感知机模型中，我们可以找到多个可以分类的超平面将数据分开，并且优化时希望所有的点都被准确分类。但是实际上离超平面很远的点已经被正确分类，它对超平面的位置没有影响。我们最关心是那些离超平面很近的点，这些点很容易被误分类。如果我们可以让离超平面比较近的点尽可能的远离超平面，最大化几何间隔，那么我们的分类效果会更好一些。SVM的思想起源正起于此。
 
&#8195;  如下图所示，分离超平面为$w^Tx+b=0$，如果所有的样本不光可以被超平面分开，还和超平面保持一定的函数距离（下图函数距离为1），那么这样的分类超平面是比感知机的分类超平面优的。可以证明，这样的超平面只有一个。和超平面平行的保持一定的函数距离的这两个超平面对应的向量，我们定义为支持向量，如下图虚线所示。

![](https://upload-images.jianshu.io/upload_images/16911112-81f2039d96198401.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

&#8195;  支持向量到超平面的距离为$1/||w||_2$，两个支持向量之间的距离为$2/||w||_2$。

## 3. SVM模型目标函数与优化
* SVM的模型是让所有点到超平面的距离大于一定的距离，也就是所有的分类点要在各自类别的支持向量两边。用数学式子表示为：
$$
max \;\; \gamma = \frac{y(w^Tx + b)}{||w||_2}  \;\; s.t \;\; y_i(w^Tx_i + b) = \gamma^{'(i)} \geq \gamma^{'} (i =1,2,...m)
$$

* 一般我们都取函数间隔γ′为1，这样我们的优化函数定义为：

$$max \;\; \frac{1}{||w||_2}  \;\; s.t \;\; y_i(w^Tx_i + b)  \geq 1 (i =1,2,...m)$$

* 也就是说，我们要在约束条件$y_i(w^Tx_i + b)  \geq 1 (i =1,2,...m)$下，最大化$\frac{1}{||w||_2}$。可以看出，这个感知机的优化方式不同，感知机是固定分母优化分子，而SVM是固定分子优化分母，同时加上了支持向量的限制。

* 由于$\frac{1}{||w||_2}$的最大化等同于$\frac{1}{2}||w||_2^2$的最小化。这样SVM的优化函数等价于：
$$min \;\; \frac{1}{2}||w||_2^2  \;\; s.t \;\; y_i(w^Tx_i + b)  \geq 1 (i =1,2,...m)$$

* 由于目标函数$\frac{1}{||w||_2}$是凸函数，同时约束条件不等式是仿射的，根据凸优化理论，我们可以通过拉格朗日函数将我们的优化目标转化为无约束的优化函数，具体的，优化函数转化为：
$$L(w,b,\alpha) = \frac{1}{2}||w||_2^2 - \sum\limits_{i=1}^{m}\alpha_i[y_i(w^Tx_i + b) - 1] \; 满足\alpha_i \geq 0$$

* 由于引入了朗格朗日乘子，我们的优化目标变成：
$$\underbrace{min}_{w,b}\; \underbrace{max}_{\alpha_i \geq 0} L(w,b,\alpha)$$

* 和最大熵模型一样的，我们的这个优化函数满足KKT条件，也就是说，我们可以通过拉格朗日对偶将我们的优化问题转化为等价的对偶问题来求解。也就是说，现在我们要求的是：
$$\underbrace{max}_{\alpha_i \geq 0} \;\underbrace{min}_{w,b}\;  L(w,b,\alpha)$$

* 从上式中，我们可以先求优化函数对于w和b的极小值。接着再求拉格朗日乘子α的极大值。
  * 首先我们来求$L(w,b,\alpha)$基于w和b的极小值，即$\underbrace{min}_{w,b}\;  L(w,b,\alpha)$。

  * 这个极值我们可以通过对w和b分别求偏导数得到：
$$\frac{\partial L}{\partial w} = 0 \;\Rightarrow w = \sum\limits_{i=1}^{m}\alpha_iy_ix_i \quad  \frac{\partial L}{\partial b} = 0 \;\Rightarrow \sum\limits_{i=1}^{m}\alpha_iy_i = 0$$

* 从上两式子可以看出，我们已经求得了w和α的关系，只要我们后面接着能够求出优化函数极大化对应的α，就可以求出我们的w了，至于b，由于上两式已经没有b，所以最后的b可以有多个。

* 好了，既然我们已经求出w和α的关系，就可以带入优化函数$L_{(w,b,α)}$消去w了。我们定义:
$$\psi(\alpha) = \underbrace{min}_{w,b}\;  L(w,b,\alpha)$$

* 现在我们来看将w替换为α的表达式以后的优化函数ψ(α)的表达式：

$$
\begin{aligned}
\psi(\alpha) 
& =  \frac{1}{2}||w||_2^2 - \sum\limits_{i=1}^{m}\alpha_i[y_i(w^Tx_i + b) - 1] \\
& = \frac{1}{2}w^Tw-\sum\limits_{i=1}^{m}\alpha_iy_iw^Tx_i - \sum\limits_{i=1}^{m}\alpha_iy_ib + \sum\limits_{i=1}^{m}\alpha_i \\
& = \frac{1}{2}w^T\sum\limits_{i=1}^{m}\alpha_iy_ix_i -\sum\limits_{i=1}^{m}\alpha_iy_iw^Tx_i - \sum\limits_{i=1}^{m}\alpha_iy_ib + \sum\limits_{i=1}^{m}\alpha_i \\
& = \frac{1}{2}w^T\sum\limits_{i=1}^{m}\alpha_iy_ix_i - w^T\sum\limits_{i=1}^{m}\alpha_iy_ix_i - \sum\limits_{i=1}^{m}\alpha_iy_ib + \sum\limits_{i=1}^{m}\alpha_i  \\
& = - \frac{1}{2}w^T\sum\limits_{i=1}^{m}\alpha_iy_ix_i - \sum\limits_{i=1}^{m}\alpha_iy_ib + \sum\limits_{i=1}^{m}\alpha_i  \\
& = - \frac{1}{2}w^T\sum\limits_{i=1}^{m}\alpha_iy_ix_i - b\sum\limits_{i=1}^{m}\alpha_iy_i + \sum\limits_{i=1}^{m}\alpha_i \\
& = -\frac{1}{2}(\sum\limits_{i=1}^{m}\alpha_iy_ix_i)^T(\sum\limits_{i=1}^{m}\alpha_iy_ix_i) - b\sum\limits_{i=1}^{m}\alpha_iy_i + \sum\limits_{i=1}^{m}\alpha_i  \\
& = -\frac{1}{2}\sum\limits_{i=1}^{m}\alpha_iy_ix_i^T\sum\limits_{i=1}^{m}\alpha_iy_ix_i - b\sum\limits_{i=1}^{m}\alpha_iy_i + \sum\limits_{i=1}^{m}\alpha_i \\
& = -\frac{1}{2}\sum\limits_{i=1}^{m}\alpha_iy_ix_i^T\sum\limits_{i=1}^{m}\alpha_iy_ix_i + \sum\limits_{i=1}^{m}\alpha_i \\& = -\frac{1}{2}\sum\limits_{i=1,j=1}^{m}\alpha_iy_ix_i^T\alpha_jy_jx_j + \sum\limits_{i=1}^{m}\alpha_i \\
& = \sum\limits_{i=1}^{m}\alpha_i - \frac{1}{2}\sum\limits_{i=1,j=1}^{m}\alpha_i\alpha_jy_iy_jx_i^Tx_j  \end{aligned}
$$

* 从上面可以看出，通过对w,b极小化以后，我们的优化函数ψ(α)仅仅只有α向量做参数。只要我们能够极大化ψ(α)，就可以求出此时对应的α，进而求出w,b。

* 对ψ(α)求极大化的数学表达式如下:
$$
\underbrace{max}_{\alpha} -\frac{1}{2}\sum\limits_{i=1}^{m}\sum\limits_{j=1}^{m}\alpha_i\alpha_jy_iy_j(x_i \bullet x_j) + \sum\limits_{i=1}^{m} \alpha_i
$$

$$
s.t. \; \sum\limits_{i=1}^{m}\alpha_iy_i = 0, \quad \alpha_i \geq 0  \; i=1,2,...m
$$

* 那么我们根据$w = \sum\limits_{i=1}^{m}\alpha_iy_ix_i$，可以求出对应的w的值：

$$w^{*} = \sum\limits_{i=1}^{m}\alpha_i^{*}y_ix_i$$

* 注意到，对于任意支持向量$(x_x,y_s)$，都有：
$$
y_s(w^Tx_s+b) = y_s(\sum\limits_{i=1}^{m}\alpha_iy_ix_i^Tx_s+b) = 1
$$

* 假设我们有S个支持向量，则对应我们求出S个$b^∗$,理论上这些$b^∗$都可以作为最终的结果， 但是我们一般采用一种更健壮的办法，即求出所有支持向量所对应的$b^∗$，然后将其平均值作为最后的结果。注意到对于严格线性可分的SVM，b的值是有唯一解的，也就是这里求出的所有$b^∗$都是一样的。

* 根据KKT条件中的对偶互补条件：
$$\alpha_{i}^{*}(y_i(w^Tx_i + b) - 1) = 0$$
    * 如果$α_i>0$，则有$y_i(w^Tx_i + b) =1$即点在支持向量上；
    
    * 如果$α_i=0$，则有$y_i(w^Tx_i + b) \geq 1$，即样本在支持向量上或者已经被正确分类。


## 4. 算法过程
* 输入是线性可分的m个样本:${(x_1,y_1), (x_2,y_2), ...,(x_m,y_m),}$，其中x为n维特征向量，y为二元输出，值为1或-1。

* 输出是分离超平面的参数$w^∗$和$b^∗$和分类决策函数。

### 算法过程
1. 构造约束优化问题：

$$
\underbrace{min}_{\alpha} \frac{1}{2}\sum\limits_{i=1}^{m}\sum\limits_{j=1}^{m}\alpha_i\alpha_jy_iy_j(x_i \bullet x_j) -  \sum\limits_{i=1}^{m} \alpha_i
$$

$$
s.t. \; \sum\limits_{i=1}^{m}\alpha_iy_i = 0 \quad \alpha_i \geq 0  \; i=1,2,...m
$$

2. 用SMO算法求出上式最小时对应的α向量的值$α^∗$向量：

3. 计算$w^{*} = \sum\limits_{i=1}^{m}\alpha_i^{*}y_ix_i$

4. 找出所有的S个支持向量,即满足$α_s>0$对应的样本$(x_s,y_s)$；

5. 通过$y_s(\sum\limits_{i=1}^{m}\alpha_iy_ix_i^Tx_s+b) = 1$；

    * a. 计算出每个支持向量$(x_x,y_s)$对应的$b^∗_s$；
    
    * b. 计算出$b_s^{*} = y_s - \sum\limits_{i=1}^{m}\alpha_iy_ix_i^Tx_s$；
    * c. 所有的$b^∗_s$对应的平均值即为最终的$b^{*} = \frac{1}{S}\sum\limits_{i=1}^{S}b_s^{*}$。

6. 这样最终的分类超平面为：
$$w^{*} \bullet x + b^{*} = 0$$

7. 最终的分类决策函数为：
$$f(x) = sign(w^{*} \bullet x + b^{*})$$

---

# 三、线性SVM软间隔最大化模型
## 1. 面临的问题
&#8195;  时候本来数据的确是可分的，也就是说可以用 线性分类SVM的学习方法来求解，但是却因为混入了异常点，导致不能线性可分，比如下图，本来数据是可以按下面的实线来做超平面分离的，可以由于一个橙色和一个蓝色的异常点导致我们没法按照上一节中的方法来分类。

![](https://upload-images.jianshu.io/upload_images/16911112-6bd5ac6075a9c8d3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

&#8195;  另外一种情况没有这么糟糕到不可分，但是会严重影响我们模型的泛化预测效果，比如下图，本来如果我们不考虑异常点，SVM的超平面应该是下图中的红色线所示，但是由于有一个蓝色的异常点，导致我们学习到的超平面是下图中的粗虚线所示，这样会严重影响我们的分类模型预测效果。

![](https://upload-images.jianshu.io/upload_images/16911112-b5134d358a6de840.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 2. 软间隔最大化
* 所谓的软间隔，是相对于硬间隔说的，我们可以认为上一个线性分类SVM的学习方法属于硬间隔最大化。回顾下硬间隔最大化的条件：
$$min\;\; \frac{1}{2}||w||_2^2  \;\; s.t \;\; y_i(w^Tx_i + b)  \geq 1 (i =1,2,...m)$$

* 接着我们再看如何可以软间隔最大化呢？SVM对训练集里面的每个样本$(x_i,y_i)$引入了一个松弛变量$ξ_i≥0$,使函数间隔加上松弛变量大于等于1，也就是说：
$$y_i(w\bullet x_i +b) \geq 1- \xi_i$$

* 对比硬间隔最大化，可以看到我们对样本到超平面的函数距离的要求放松了，之前是一定要大于等于1，现在只需要加上一个大于等于0的松弛变量能大于等于1就可以了。当然，松弛变量不能白加，这是有成本的，每一个松弛变量ξi, 对应了一个代价$ξ_i$，这个就得到了我们的软间隔最大化的SVM学习条件如下：
$$min\;\; \frac{1}{2}||w||_2^2 +C\sum\limits_{i=1}^{m}\xi_i$$

$$s.t.  \;\; y_i(w^Tx_i + b)  \geq 1 - \xi_i \;\;(i =1,2,...m)$$

$$\xi_i \geq 0 \;\;(i =1,2,...m)$$

* 这里C>0为惩罚参数，可以理解为我们一般回归和分类问题正则化时候的参数。C越大，对误分类的惩罚越大，C越小，对误分类的惩罚越小。
也就是说，我们希望$\frac{1}{2}||w||^2_2$尽量小，误分类的点尽可能的少。C是协调两者关系的正则化惩罚系数。在实际应用中，需要调参来选择。

&#8195;  这个目标函数的优化和上一篇的线性可分SVM的优化方式类似，我们下面就来看看怎么对线性分类SVM的软间隔最大化来进行学习优化。

## 3. 目标函数的优化
* 和线性可分SVM的优化方式类似，我们首先将软间隔最大化的约束问题用拉格朗日函数转化为无约束问题如下：
$$L(w,b,\xi,\alpha,\mu) = \frac{1}{2}||w||_2^2 +C\sum\limits_{i=1}^{m}\xi_i - \sum\limits_{i=1}^{m}\alpha_i[y_i(w^Tx_i + b) - 1 + \xi_i] - \sum\limits_{i=1}^{m}\mu_i\xi_i$$
其中$μ_i≥0,α_i≥0,$均为拉格朗日系数。

* 也就是说，我们现在要优化的目标函数是：
$$\underbrace{min}_{w,b,\xi}\; \underbrace{max}_{\alpha_i \geq 0, \mu_i \geq 0,} L(w,b,\alpha, \xi,\mu)$$

* 这个优化目标也满足KKT条件，也就是说，我们可以通过拉格朗日对偶将我们的优化问题转化为等价的对偶问题来求解如下：
$$\underbrace{max}_{\alpha_i \geq 0, \mu_i \geq 0,} \; \underbrace{min}_{w,b,\xi}\; L(w,b,\alpha, \xi,\mu)$$

* 我们可以先求优化函数对于w,b,ξ的极小值, 接着再求拉格朗日乘子α和 μ的极大值。首先我们来求优化函数对于w,b,ξ的极小值，这个可以通过求偏导数求得：
$$\frac{\partial L}{\partial w} = 0 \;\Rightarrow w = \sum\limits_{i=1}^{m}\alpha_iy_ix_i$$

$$\frac{\partial L}{\partial b} = 0 \;\Rightarrow \sum\limits_{i=1}^{m}\alpha_iy_i = 0$$

$$\frac{\partial L}{\partial \xi} = 0 \;\Rightarrow C- \alpha_i - \mu_i = 0$$

* 接下来，利用上面的三个式子去消除w和b。具体过程如下：
$$\begin{aligned} L(w,b,\xi,\alpha,\mu) & = \frac{1}{2}||w||_2^2 +C\sum\limits_{i=1}^{m}\xi_i - \sum\limits_{i=1}^{m}\alpha_i[y_i(w^Tx_i + b) - 1 + \xi_i] - \sum\limits_{i=1}^{m}\mu_i\xi_i\\
&= \frac{1}{2}||w||_2^2 - \sum\limits_{i=1}^{m}\alpha_i[y_i(w^Tx_i + b) - 1 + \xi_i] + \sum\limits_{i=1}^{m}\alpha_i\xi_i\\& = \frac{1}{2}||w||_2^2 - \sum\limits_{i=1}^{m}\alpha_i[y_i(w^Tx_i + b) - 1]\\
& = \frac{1}{2}w^Tw-\sum\limits_{i=1}^{m}\alpha_iy_iw^Tx_i - \sum\limits_{i=1}^{m}\alpha_iy_ib + \sum\limits_{i=1}^{m}\alpha_i\\
& = \frac{1}{2}w^T\sum\limits_{i=1}^{m}\alpha_iy_ix_i -\sum\limits_{i=1}^{m}\alpha_iy_iw^Tx_i - \sum\limits_{i=1}^{m}\alpha_iy_ib + \sum\limits_{i=1}^{m}\alpha_i\\
& = \frac{1}{2}w^T\sum\limits_{i=1}^{m}\alpha_iy_ix_i - w^T\sum\limits_{i=1}^{m}\alpha_iy_ix_i - \sum\limits_{i=1}^{m}\alpha_iy_ib + \sum\limits_{i=1}^{m}\alpha_i\\
& = - \frac{1}{2}w^T\sum\limits_{i=1}^{m}\alpha_iy_ix_i - \sum\limits_{i=1}^{m}\alpha_iy_ib + \sum\limits_{i=1}^{m}\alpha_i\\
& = - \frac{1}{2}w^T\sum\limits_{i=1}^{m}\alpha_iy_ix_i - b\sum\limits_{i=1}^{m}\alpha_iy_i + \sum\limits_{i=1}^{m}\alpha_i \\
& = -\frac{1}{2}(\sum\limits_{i=1}^{m}\alpha_iy_ix_i)^T(\sum\limits_{i=1}^{m}\alpha_iy_ix_i) - b\sum\limits_{i=1}^{m}\alpha_iy_i + \sum\limits_{i=1}^{m}\alpha_i \\
& = -\frac{1}{2}\sum\limits_{i=1}^{m}\alpha_iy_ix_i^T\sum\limits_{i=1}^{m}\alpha_iy_ix_i - b\sum\limits_{i=1}^{m}\alpha_iy_i + \sum\limits_{i=1}^{m}\alpha_i \\& = -\frac{1}{2}\sum\limits_{i=1}^{m}\alpha_iy_ix_i^T\sum\limits_{i=1}^{m}\alpha_iy_ix_i + \sum\limits_{i=1}^{m}\alpha_i \\& = -\frac{1}{2}\sum\limits_{i=1,j=1}^{m}\alpha_iy_ix_i^T\alpha_jy_jx_j + \sum\limits_{i=1}^{m}\alpha_i \\& =\sum\limits_{i=1}^{m}\alpha_i - \frac{1}{2}\sum\limits_{i=1,j=1}^{m}\alpha_i\alpha_jy_iy_jx_i^Tx_j \end{aligned}$$

* 仔细观察可以发现，这个式子和我们前面线性可分SVM的一样。唯一不一样的是约束条件。现在我们看看我们的优化目标的数学形式：
$$\underbrace{ max }_{\alpha} \sum\limits_{i=1}^{m}\alpha_i - \frac{1}{2}\sum\limits_{i=1,j=1}^{m}\alpha_i\alpha_jy_iy_jx_i^Tx_j$$

$$
s.t. \; \sum\limits_{i=1}^{m}\alpha_iy_i = 0, \quad C- \alpha_i - \mu_i = 0
$$

$$
\alpha_i \geq 0 \;(i =1,2,...,m), \quad \mu_i \geq 0 \;(i =1,2,...,m)
$$

* 对于$C−α_i−μ_i=0，α_i≥0，μ_i≥0$这3个式子，我们可以消去$μ_i$，只留下$α_i$，也就是说$0≤α_i≤C$。 同时将优化目标函数变号，求极小值，如下：
$$\underbrace{ min }_{\alpha}  \frac{1}{2}\sum\limits_{i=1,j=1}^{m}\alpha_i\alpha_jy_iy_jx_i^Tx_j - \sum\limits_{i=1}^{m}\alpha_i$$

$$
s.t. \; \sum\limits_{i=1}^{m}\alpha_iy_i = 0, \quad 0 \leq \alpha_i \leq C
$$

&#8195;  这就是软间隔最大化时的线性可分SVM的优化目标形式，和前面的硬间隔最大化的线性可分SVM相比，我们仅仅是多了一个约束条件$0≤α_i≤C$。我们依然可以通过SMO算法来求上式极小化时对应的α向量就可以求出w和b了。

## 4. 支持向量
&#8195;  在硬间隔最大化时，支持向量比较简单，就是满足$y_i(w^T x_i+b)−1=0$就可以了。根据KKT条件中的对偶互补条件$α^∗_i(y_i(w^T x_i+b)−1)=0$，如果$α^∗_i>0$，则有$y_i(w^T x_i+b)=1$即点在支持向量上，否则如果$α^∗_i=0$，则有$y_i(w^T x_i+b)≥1$，即样本在支持向量上或者已经被正确分类。

&#8195;  在软间隔最大化时，则稍微复杂一些，因为我们对每个样本$(x_i,y_i)$引入了松弛变量$ξ_i$。我们从下图来研究软间隔最大化时支持向量的情况，第i个点到对应类别支持向量的距离为$\frac{ξ_i}{||w||_2}$。根据软间隔最大化时KKT条件中的对偶互补条件$α^∗_i(y_i(w^T x_i+b)−1+ξ^∗_i)=0$我们有：

* 如果α=0,那么$y_i(w^T x_i+b)−1≥0$，即样本在间隔边界上或者已经被正确分类。如图中所有远离间隔边界的点。

* 如果0<α<C，那么$ξ_i=0，y_i(w^T x_i+b)−1=0$，即点在间隔边界上。

* 如果α=C，说明这是一个可能比较异常的点，需要检查此时$ξ_i$：
  * a. 如果$0≤ξ_i≤1$，那么点被正确分类，但是却在超平面和自己类别的间隔边界之间。如图中的样本2和4。
  * b. 如果$ξ_i=1$，那么点在分离超平面上，无法被正确分类。
  * c. 如果$ξ_i>1$，那么点在超平面的另一侧，也就是说，这个点不能被正常分类。如图中的样本1和3。

![](https://upload-images.jianshu.io/upload_images/16911112-2905c122a6aa219e.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 5. 算法过程
* 输入是线性可分的m个样本$(x_1,y_1),(x_2,y_2),...,(x_m,y_m)$，其中x为n维特征向量。y为二元输出，值为1，或者-1；

* 输出是分离超平面的参数$w^∗$和$b^∗$和分类决策函数。

### 算法过程
1. 选择一个惩罚系数C>0, 构造约束优化问题：

$$\underbrace{ min }_{\alpha}  \frac{1}{2}\sum\limits_{i=1,j=1}^{m}\alpha_i\alpha_jy_iy_jx_i^Tx_j - \sum\limits_{i=1}^{m}\alpha_i$$

$$s.t. \; \sum\limits_{i=1}^{m}\alpha_iy_i = 0, \quad 0 \leq \alpha_i \leq C$$

2. 用SMO算法求出上式最小时对应的α向量的值α∗向量：

3. 计算$w^{*} = \sum\limits_{i=1}^{m}\alpha_i^{*}y_ix_i$。

4. 找出所有的S个支持向量对应的样本$(x_s,y_s)$，通过$y_s(\sum\limits_{i=1}^{m}\alpha_iy_ix_i^Tx_s+b) = 1$；

    * 计算每个支持向量$(x_x,y_s)$对应的$b^∗_s$，
    
    * 计算这些$b_s^{*} = y_s - \sum\limits_{i=1}^{m}\alpha_iy_ix_i^Tx_s$，
    * 所有的$b^∗_s$对应的平均值即为最终的$b^{*} = \frac{1}{S}\sum\limits_{i=1}^{S}b_s^{*}$。

5. 这样最终的分类超平面为：
$$w^{*} \bullet x + b^{*} = 0$$

6. 最终的分类决策函数为：
$$f(x) = sign(w^{*} \bullet x + b^{*})$$

## 6. 合页损失函数
&#8195;  线性支持向量机还有另外一种解释如下：
$$\underbrace{ min}_{w, b}[1-y_i(w \bullet x + b)]_{+} + \lambda ||w||_2^2$$

&#8195;  其中$L(y(w∙x+b))=[1−y_i(w∙x+b)]_+$称为合页损失函数(hinge loss function)，下标+表示为：
$$[z]_{+}= \begin{cases} z & {z >0}\\ 0& {z\leq 0} \end{cases}$$

&#8195;  也就是说，如果点被正确分类，且函数间隔大于1，损失是0，否则损失是1−y(w∙x+b)，如下图中的绿线。我们在下图还可以看出其他各种模型损失和函数间隔的关系：对于0-1损失函数，如果正确分类，损失是0，误分类损失1， 如下图黑线，可见0-1损失函数是不可导的。对于感知机模型，感知机的损失函数是$[−y_i(w∙x+b)]_{+}$，这样当样本被正确分类时，损失是0，误分类时，损失是$−y_i(w∙x+b)$，如下图紫线。对于逻辑回归之类和最大熵模型对应的对数损失，损失函数是$log[1+exp(−y(w∙x+b))]$, 如下图红线所示。

![](https://upload-images.jianshu.io/upload_images/16911112-47844da273255e04.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

&#8195;  线性可分SVM通过软间隔最大化，可以解决线性数据集带有异常点时的分类处理，但是现实生活中的确有很多数据不是线性可分的，这些线性不可分的数据也不是去掉异常点就能处理这么简单。

---

# 四、线性不可分支持向量机与核函数
## 1. 回顾多项式回归
* 在之前的多项式回归中，如何将多项式回归转化为线性回归。比如一个只有两个特征的p次方多项式回归的模型：
$$h_\theta(x_1, x_2) = \theta_0 + \theta_{1}x_1 + \theta_{2}x_{2} + \theta_{3}x_1^{2} + \theta_{4}x_2^{2} + \theta_{5}x_{1}x_2$$

* 我们令$x_0 = 1, x_1 = x_1, x_2 = x_2, x_3 =x_1^{2}, x_4 = x_2^{2}, x_5 =  x_{1}x_2$，这样我们就得到了下式：
$$h_\theta(x_1, x_2) = \theta_0 + \theta_{1}x_1 + \theta_{2}x_{2} + \theta_{3}x_3 + \theta_{4}x_4 + \theta_{5}x_5$$

* 可以发现，我们又重新回到了线性回归，这是一个五元线性回归，可以用线性回归的方法来完成算法。

* 对于每个二元样本特征$(x_1,x_2)$，我们得到一个五元样本特征$(1,x_1,x_2,x^2_1,x^2_2,x_1x_2)$，通过这个改进的五元样本特征，我们重新把不是线性回归的函数变回线性回归。可以发现，我们又重新回到了线性回归，这是一个五元线性回归，可以用线性回归的方法来完成算法。对于每个二元样本特征$(x1,x2)$，我们得到一个五元样本特征$(1,x_1,x_2,x^2_1,x^2_2,x_1x_2)$，通过这个改进的五元样本特征，我们重新把不是线性回归的函数变回线性回归。

* 也就是说，对于二维的不是线性的数据，我们将其映射到了五维以后，就变成了线性的数据。

* 这给了我们启发，也就是说对于在低维线性不可分的数据，在映射到了高维以后，就变成线性可分的了。这个思想我们同样可以运用到SVM的线性不可分数据上。也就是说，对于SVM线性不可分的低维特征数据，我们可以将其映射到高维，就能线性可分，此时就可以运用前两篇的线性可分SVM的算法思想了。

## 2. 核函数的引入
* 前面讲到线性不可分的低维特征数据，我们可以将其映射到高维，就能线性可分。现在我们将它运用到我们的SVM的算法上。回顾线性可分SVM的优化目标函数：
$$\underbrace{ min }_{\alpha}  \frac{1}{2}\sum\limits_{i=1,j=1}^{m}\alpha_i\alpha_jy_iy_jx_i \bullet x_j - \sum\limits_{i=1}^{m}\alpha_i$$

$$s.t. \; \sum\limits_{i=1}^{m}\alpha_iy_i = 0, \quad 0 \leq \alpha_i \leq C$$

* 注意到上式低维特征仅仅以内积$x_i∙x_j$的形式出现，如果我们定义一个低维特征空间到高维特征空间的映射ϕ，将所有特征映射到一个更高的维度，让数据线性可分，我们就可以继续按前两篇的方法来优化目标函数，求出分离超平面和分类决策函数了。也就是说现在的SVM的优化目标函数变成：

$$\underbrace{ min }_{\alpha}  \frac{1}{2}\sum\limits_{i=1,j=1}^{m}\alpha_i\alpha_jy_iy_j\phi(x_i) \bullet \phi(x_j) - \sum\limits_{i=1}^{m}\alpha_i$$

$$s.t. \; \sum\limits_{i=1}^{m}\alpha_iy_i = 0 \quad 0 \leq \alpha_i \leq C$$

* 可以看到，和线性可分SVM的优化目标函数的区别仅仅是将内积xi∙xj替换为$ϕ(x_i)∙ϕ(x_j)$。
* 看起来似乎这样我们就已经完美解决了线性不可分SVM的问题了，但是事实是不是这样呢？我们看看，假如是一个2维特征的数据，我们可以将其映射到5维来做特征的内积，如果原始空间是三维，可以映射到到19维空间，似乎还可以处理。但是如果我们的低维特征是100个维度，1000个维度呢？那么我们要将其映射到超级高的维度来计算特征的内积。这时候映射成的高维维度是爆炸性增长的，这个计算量实在是太大了，而且如果遇到无穷维的情况，就根本无从计算了。

* 这时候就需要核函数了，假设ϕ是一个从低维的输入空间χ（欧式空间的子集或者离散集合）到高维的希尔伯特空间的H映射。那么如果存在函数K(x,z)，对于任意x,z∈χ，都有：
$$K(x, z) = \phi(x) \bullet \phi(z)
$$
那么我们就称$K(x,z)$为核函数。

* 从上面的式子乍一看还是不明白核函数怎么帮我们解决线性不可分的问题的。仔细观察上式可以发现，$K(x,z)$的计算是在低维特征空间来计算的，它避免了在刚才我们提到了在高维维度空间计算内积的恐怖计算量。也就是说，我们可以好好享受在高维特征空间线性可分的红利，却避免了高维特征空间恐怖的内积计算量。

* 至此，我们总结下线性不可分时核函数的引入过程：
  * 我们遇到线性不可分的样例时，常用做法是把样例特征映射到高维空间中去(如上一节的多项式回归）但是遇到线性不可分的样例，一律映射到高维空间，那么这个维度大小是会高到令人恐怖的。此时，核函数就体现出它的价值了，核函数的价值在于它虽然也是将特征进行从低维到高维的转换，但核函数好在它在低维上进行计算，而将实质上的分类效果（利用了内积）表现在了高维上，这样避免了直接在高维空间中的复杂计算，真正解决了SVM线性不可分的问题。

## 3. 核函数的介绍
&#8195;  事实上，核函数的研究非常的早，要比SVM出现早得多，当然，将它引入SVM中是最近二十多年的事情。对于从低维到高维的映射，核函数不止一个。那么什么样的函数才可以当做核函数呢？这是一个有些复杂的数学问题。这里不多介绍。由于一般我们说的核函数都是正定核函数，这里我们直说明正定核函数的充分必要条件。一个函数要想成为正定核函数，必须满足他里面任何点的集合形成的Gram矩阵是半正定的。也就是说,对于任意的$xi∈χ，i=1,2,3...m, K(x_i,x_j)$对应的Gram矩阵$K=[K(x_i,x_j)]$是[*半正定矩阵*](https://baike.baidu.com/item/%E5%8D%8A%E6%AD%A3%E5%AE%9A%E7%9F%A9%E9%98%B5/2152711?fr=aladdin)，则K(x,z)是正定核函数。

&#8195;  从上面的定理看，它要求任意的集合都满足Gram矩阵半正定，所以自己去找一个核函数还是很难的，怎么办呢？还好牛人们已经帮我们找到了很多的核函数，而常用的核函数也仅仅只有那么几个。下面我们来看看常见的核函数, 选择这几个核函数介绍是因为scikit-learn中默认可选的就是下面几个核函数。

### 3.1线性核函数
* 线性核函数（Linear Kernel）其实就是我们前两篇的线性可分SVM，表达式为：
$$K(x, z) = x \bullet z
$$也就是说，线性可分SVM我们可以和线性不可分SVM归为一类，区别仅仅在于线性可分SVM用的是线性核函数。

### 3.2 多项式核函数
* 多项式核函数（Polynomial Kernel）是线性不可分SVM常用的核函数之一，表达式为：
$$K(x, z) = （\gamma x \bullet z  + r)^d
$$其中，γ,r,d都需要自己调参定义。

### 3.3 高斯核函数
* 高斯核函数（Gaussian Kernel），在SVM中也称为径向基核函数（Radial Basis Function,RBF），它是非线性分类SVM最主流的核函数。libsvm默认的核函数就是它。表达式为：
$$K(x, z) = exp(-\gamma||x-z||^2)$$

### 3.4 Sigmoid核函数
* Sigmoid核函数（Sigmoid Kernel）也是线性不可分SVM常用的核函数之一，表达式为：
$$K(x, z) = tanh（\gamma x \bullet z  + r)$$
其中，γ,r都需要自己调参定义。

## 4. 分类SVM的算法小结
&#8195;  引入了核函数后，我们的SVM算法才算是比较完整了。现在我们对分类SVM的算法过程做一个总结。不再区别是否线性可分。

* 输入：m个样本$(x_1,y_1),(x_2,y_2),...,(x_m,y_m)$，其中x为n维特征向量。y为二元输出，值为1或-1；

* 输出：分离超平面的参数$w^∗$和$b^∗$和分类决策函数。

### 算法过程
1. 选择适当的核函数K(x,z)和一个惩罚系数C>0, 构造约束优化问题；

$$
\underbrace{ min }_{\alpha}  \frac{1}{2}\sum\limits_{i=1,j=1}^{m}\alpha_i\alpha_jy_iy_jK(x_i,x_j) - \sum\limits_{i=1}^{m}\alpha_i
$$

$$s.t. \; \sum\limits_{i=1}^{m}\alpha_iy_i = 0，\quad 0 \leq \alpha_i \leq C$$

2. 用SMO算法求出上式最小时对应的α向量的值$α^∗$向量；

3. 得到$w^{*} = \sum\limits_{i=1}^{m}\alpha_i^{*}y_i\phi(x_i)$，此处可以不直接显式的计算$w^∗$。

4. 找出所有的S个支持向量,即满足$0<α_s<C$对应的样本$(x_s,y_s)$，通过$y_s(\sum\limits_{i=1}^{m}\alpha_iy_iK(x_i,x_s)+b) = 1$，
    * 计算每个支持向量$(x_s,y_s)$对应的$b^∗_s$，
    
    * 计算这些$b_s^{*} = y_s - \sum\limits_{i=1}^{m}\alpha_iy_iK(x_i,x_s)$。

5. 所有的$b∗s$对应的平均值即为最终的$b^{*} = \frac{1}{S}\sum\limits_{i=1}^{S}b_s^{*}$。

6. 这样最终的分类超平面为：
$$\sum\limits_{i=1}^{m}\alpha_i^{*}y_iK(x, x_i)+ b^{*} = 0$$

7. 最终的分类决策函数为：
$$f(x) = sign(\sum\limits_{i=1}^{m}\alpha_i^{*}y_iK(x, x_i)+ b^{*})$$

---

# 五、SMO算法原理
&#8195;  在SVM的前三篇里，我们优化的目标函数最终都是一个关于 α 向量的函数。而怎么极小化这个函数，求出对应的 α 向量，进而求出分离超平面我们没有讲。本篇就对优化这个关于 α 向量的函数的SMO算法做一个总结。

## 1. 回顾SVM优化目标函数
* 首先回顾下我们的优化目标函数：
$$\underbrace{ min }_{\alpha} \frac{1}{2}\sum\limits_{i=1,j=1}^{m}\alpha_i\alpha_jy_iy_jK(x_i,x_j) - \sum\limits_{i=1}^{m}\alpha_i$$

$$s.t. \; \sum\limits_{i=1}^{m}\alpha_iy_i = 0，\quad0 \leq \alpha_i \leq C$$

* 我们的解要满足的 KKT 条件的对偶互补条件为：
$$\alpha_{i}^{*}(y_i(w^Tx_i + b) - 1 + \xi_i^{*}) = 0$$

* 根据这个 KKT 条件的对偶互补条件，我们有：
$$\alpha_{i}^{*} = 0 \Rightarrow y_i(w^{*} \bullet \phi(x_i) + b) \geq 1$$

$$0 <\alpha_{i}^{*} < C  \Rightarrow y_i(w^{*} \bullet \phi(x_i) + b) = 1$$

$$\alpha_{i}^{*}= C \Rightarrow y_i(w^{*} \bullet \phi(x_i) + b) \leq 1$$

* 由于
$$w^{*} = \sum\limits_{j=1}^{m}\alpha_j^{*}y_j\phi(x_j)$$

* 我们令
$$g(x) = w^{*} \bullet \phi(x) + b =\sum\limits_{j=1}^{m}\alpha_j^{*}y_jK(x, x_j)+ b^{*}$$

* 则有：
$$\alpha_{i}^{*} = 0 \Rightarrow y_ig(x_i) \geq 1$$

$$0 < \alpha_{i}^{*} < C  \Rightarrow y_ig(x_i)  = 1$$

$$\alpha_{i}^{*}= C \Rightarrow y_ig(x_i)  \leq 1$$

## 2. SMO算法的基本思想
&#8195;  上面这个优化式子比较复杂，里面有m个变量组成的向量α需要在目标函数极小化的时候求出。直接优化时很难的。SMO算法则采用了一种启发式的方法。它每次只优化两个变量，将其他的变量都视为常数。由于$\sum\limits_{i=1}^{m}\alpha_iy_i = 0$，假如将$α_3,α_4,...,α_m$固定，那么$α_1,α_2$之间的关系也确定了。这样SMO算法将一个复杂的优化算法转化为一个比较简单的两变量优化问题。

* 为了后面表示方便，我们定义：$K_{ij} = \phi(x_i) \bullet \phi(x_j)$

* 由于$α_3,α_4,...,α_m$都成了常量，所有的常量我们都从目标函数去除，这样我们上一节的目标优化函数变成下式：
$$
\underbrace{ min }_{\alpha_1, \alpha_1} \frac{1}{2}K_{11}\alpha_1^2 + \frac{1}{2}K_{22}\alpha_2^2 +y_1y_2K_{12}\alpha_1 \alpha_2 -(\alpha_1 + \alpha_2) +y_1\alpha_1\sum\limits_{i=3}^{m}y_i\alpha_iK_{i1} + y_2\alpha_2\sum\limits_{i=3}^{m}y_i\alpha_iK_{i2}
$$

$$s.t. \;\;\alpha_1y_1 +  \alpha_2y_2 = -\sum\limits_{i=3}^{m}y_i\alpha_i = \varsigma$$

$$\quad 0 \leq \alpha_i \leq C \;\; i =1,2$$

## 3. SMO算法目标函数的优化
&#8195;  为了求解上面含有这两个变量的目标优化问题，我们首先分析约束条件，所有的$α_1,α_2$都要满足约束条件，然后在约束条件下求最小。

&#8195;  根据上面的约束条件$\alpha_1y_1 +  \alpha_2y_2  = \varsigma\;\;0 \leq \alpha_i \leq C \;\; i =1,2$，又由于$y_1,y_2$均只能取值1或者-1, 这样$α_1,α_2$在[0,C]和[0,C]形成的盒子里面，并且两者的关系直线的斜率只能为1或者-1，也就是说$α_1,α_2$的关系直线平行于[0,C]和[0,C]形成的盒子的对角线，如下图所示：

![](https://upload-images.jianshu.io/upload_images/16911112-128b775514292f6b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

* 由于$α_1,α_2$的关系被限制在盒子里的一条线段上，所以两变量的优化问题实际上仅仅是一个变量的优化问题。不妨我们假设最终是$α_2$的优化问题。
  * 由于我们采用的是启发式的迭代法，假设我们上一轮迭代得到的解是$α^{old}_1,α^{old}_2$；
  
  * 假设沿着约束方向$α_2$未经剪辑的解是$α^{new,unc}_2$；
  * 本轮迭代完成后的解为$α^{new}_1,α^{new}_2$；
  * 由于$α^{new}_2$必须满足上图中的线段约束；
  * 假设L和H分别是上图中$α^{new}_2$所在的线段的边界。
  
* 那么很显然我们有：
$$L \leq \alpha_2^{new} \leq H$$

* 而对于L和H，我们也有限制条件如果是上面左图中的情况，则：
$$L = max(0, \alpha_2^{old}-\alpha_1^{old}) \;\;\;H = min(C, C+\alpha_2^{old}-\alpha_1^{old})$$

* 如果是上面右图中的情况，我们有：
$$L = max(0, \alpha_2^{old}+\alpha_1^{old}-C) \;\;\; H = min(C, \alpha_2^{old}+\alpha_1^{old})$$

* 也就是说，假如我们通过求导得到的$α^{new,unc}_2$，则最终的$α^{new}_2$应该为：
$$\alpha_2^{new}= \begin{cases} H& { \alpha_2^{new,unc} > H}\\ \alpha_2^{new,unc}& {L \leq \alpha_2^{new,unc} \leq H}\\ L& {\alpha_2^{new,unc} < L} \end{cases}$$

* 至于如何求出$α^{new,unc}_2$呢？很简单，我们只需要将目标函数对$α_2$求偏导数即可。首先我们整理下我们的目标函数，为了简化叙述，我们令：
$$E_i = g(x_i)-y_i = \sum\limits_{j=1}^{m}\alpha_j^{*}y_jK(x_i, x_j)+ b - y_i$$

* 其中：
$$g(x) = w^{*} \bullet \phi(x) + b =\sum\limits_{j=1}^{m}\alpha_j^{*}y_jK(x, x_j)+ b^{*}$$

* 我们令：
$$v_i = \sum\limits_{j=3}^{m}y_j\alpha_jK(x_i,x_j) = g(x_i) -  \sum\limits_{j=1}^{2}y_j\alpha_jK(x_i,x_j) -b$$

* 这样我们的优化目标函数进一步简化为：
$$W(\alpha_1,\alpha_2) = \frac{1}{2}K_{11}\alpha_1^2 + \frac{1}{2}K_{22}\alpha_2^2 +y_1y_2K_{12}\alpha_1 \alpha_2 -(\alpha_1 + \alpha_2) +y_1\alpha_1v_1 +  y_2\alpha_2v_2$$

* 由于$α_1y_1+α_2y_2=ς$，并且$y^{2}_i=1$，可以得到$α_1$用$α_2$表达的式子为：
$$\alpha_1 = y_1(\varsigma  - \alpha_2y_2)$$

* 将上式带入我们的目标优化函数，就可以消除$α_1$，得到仅仅包含$α_2$的式子。
$$W(\alpha_2) = \frac{1}{2}K_{11}(\varsigma  - \alpha_2y_2)^2 + \frac{1}{2}K_{22}\alpha_2^2 +y_2K_{12}(\varsigma - \alpha_2y_2) \alpha_2 - (\varsigma  - \alpha_2y_2)y_1 -  \alpha_2 +(\varsigma  - \alpha_2y_2)v_1 +  y_2\alpha_2v_2$$

* 通过求偏导数来得到$α^{new,unc}_2$，即：
$$\frac{\partial W}{\partial \alpha_2} = K_{11}\alpha_2 +  K_{22}\alpha_2 -2K_{12}\alpha_2 -  K_{11}\varsigma y_2 + K_{12}\varsigma y_2 +y_1y_2 -1 -v_1y_2 +y_2v_2 = 0$$

* 整理上式有：
$$(K_{11} +K_{22}-2K_{12})\alpha_2 = y_2(y_2-y_1 + \varsigma  K_{11} - \varsigma  K_{12} + v_1 - v_2)$$

$$= y_2(y_2-y_1 + \varsigma  K_{11} - \varsigma  K_{12} + (g(x_1) -  \sum\limits_{j=1}^{2}y_j\alpha_jK_{1j} -b ) -(g(x_2) -  \sum\limits_{j=1}^{2}y_j\alpha_jK_{2j} -b))$$

* 将$ς=α_1y_1+α_2y_2$带入上式，我们有：
$$(K_{11} +K_{22}-2K_{12})\alpha_2^{new,unc}
= y_2((K_{11} +K_{22}-2K_{12})\alpha_2^{old}y_2 +y_2-y_1 +g(x_1) - g(x_2)) $$

$$= (K_{11} +K_{22}-2K_{12}) \alpha_2^{old} + y_2(E_1-E_2)$$

* 我们得到了$α^{new,unc}_2$的表达式：
$$\alpha_2^{new,unc} = \alpha_2^{old} + \frac{y_2(E_1-E_2)}{K_{11} +K_{22}-2K_{12})}$$

* 利用上面讲到的$α^{new,unc}_2和α^{new}_2$的关系式，我们就可以得到我们新的$α^{new}_2$了。利用$α^{new}_2$和$α^{new}_1$的线性关系，我们也可以得到新的$α^{new}_1$。

## 4. SMO算法两个变量的选择
&#8195;  SMO算法需要选择合适的两个变量做迭代，其余的变量做常量来进行优化，那么怎么选择这两个变量呢？

### 4.1 第一个变量的选择
&#8195;  SMO算法称选择第一个变量为外层循环，这个变量需要选择在训练集中违反KKT条件最严重的样本点。

* 对于每个样本点，要满足的KKT条件： 
$$\alpha_{i}^{*} = 0 \Rightarrow y_ig(x_i) \geq 1$$

$$0 < \alpha_{i}^{*} < C  \Rightarrow y_ig(x_i)  =1$$

$$\alpha_{i}^{*}= C \Rightarrow y_ig(x_i)  \leq 1$$

* 一般来说，我们首先选择违反$0 < \alpha_{i}^{*} < C  \Rightarrow y_ig(x_i)  =1$这个条件的点。如果这些支持向量都满足KKT条件，再选择违反$\alpha_{i}^{*} = 0 \Rightarrow y_ig(x_i) \geq 1$和$\alpha_{i}^{*}= C \Rightarrow y_ig(x_i)  \leq 1$的点。

### 4.2 第二个变量的选择
&#8195;  SMO算法称选择第二一个变量为内层循环，假设我们在外层循环已经找到了$α_1$, 第二个变量$α_2$的选择标准是让$|E_1−E_2|$有足够大的变化。由于$α_1$定了的时候，$E_1$也确定了，所以要想$|E_1−E_2|$最大，只需要在$E_1$为正时，选择最小的$Ei$作为$E_2$， 在$E_1$为负时，选择最大的$E_i$作为$E_2$，可以将所有的$E_i$保存下来加快迭代。

&#8195;  如果内存循环找到的点不能让目标函数有足够的下降，可以采用遍历支持向量点来做$α_2$,直到目标函数有足够的下降， 如果所有的支持向量做$α_2$都不能让目标函数有足够的下降，可以跳出循环，重新选择$α_1$。

### 4.3 计算阈值b和差值$E_i$
* 在每次完成两个变量的优化之后，需要重新计算阈值b。当$0<α^{new}_1<C$时，我们有：
$$y_1 - \sum\limits_{i=1}^{m}\alpha_iy_iK_{i1} -b_1 = 0$$

* 于是新的$b^{new}_1$为：
$$b_1^{new} = y_1 - \sum\limits_{i=3}^{m}\alpha_iy_iK_{i1} - \alpha_{1}^{new}y_1K_{11} - \alpha_{2}^{new}y_2K_{21}$$

* 计算出$E_1$为：
$$E_1 = g(x_1) - y_1 = \sum\limits_{i=3}^{m}\alpha_iy_iK_{i1} + \alpha_{1}^{old}y_1K_{11} + \alpha_{2}^{old}y_2K_{21} + b^{old} -y_1$$

* 可以看到上两式都有$y_1 - \sum\limits_{i=3}^{m}\alpha_iy_iK_{i1}$,因此可以将$b^{new}_1$用$E_1$表示为：
$$b_1^{new} = -E_1 -y_1K_{11}(\alpha_{1}^{new} - \alpha_{1}^{old}) -y_2K_{21}(\alpha_{2}^{new} - \alpha_{2}^{old}) + b^{old}$$

* 同样的，如果$0<α^{new}_2<C$, 那么有：
$$b_2^{new} = -E_2 -y_1K_{12}(\alpha_{1}^{new} - \alpha_{1}^{old}) -y_2K_{22}(\alpha_{2}^{new} - \alpha_{2}^{old}) + b^{old}$$

* 最终的$b^{new}$为：
$$b^{new} = \frac{b_1^{new} + b_2^{new}}{2}$$

* 得到了$b^{new}$我们需要更新$E_i$:
$$E_i = \sum\limits_{S}y_j\alpha_jK(x_i,x_j) + b^{new} -y_i
$$其中，S是所有支持向量$x_j$的集合。

## 5. SMO算法总结
* 输入m个样本$(x_1,y_1),(x_2,y_2),...,(x_m,y_m)$，其中x为n维特征向量；

* y为二元输出，值为1或-1，精度e。输出是近似解α。
###  算法流程
1. 取初值$α_0=0,k=0$；

2. 根据(4)中的方法选择$α^k_1$和$α^k_2$，求出新的$α^{new,unc}_2$；

$$\alpha_2^{new,unc} = \alpha_2^{k} + \frac{y_2(E_1-E_2)}{K_{11} +K_{22}-2K_{12})}$$

3. 按照下式求出$α^{k+1}_2$；

$$
\alpha_2^{k+1}= \begin{cases} H& {L \leq \alpha_2^{new,unc} > H}\\
 \alpha_2^{new,unc}& {L \leq \alpha_2^{new,unc} \leq H}\\ 
L & {\alpha_2^{new,unc} < L} \end{cases}
$$

4. 利用$α^{k+1}_2$和$α^{k+1}_1$的关系求出$α^{k+1}_1$；

5. 按照4.3的方法计算$b^{k+1}$和$E_i$；

6. 在精度e范围内检查是否满足如下的终止条件：

$$\sum\limits_{i=1}^{m}\alpha_iy_i = 0, \quad 0 \leq \alpha_i \leq C, i =1,2...m$$

$$\alpha_{i}^{k+1} = 0 \Rightarrow y_ig(x_i) \geq 1$$

$$0 <\alpha_{i}^{k+1} < C  \Rightarrow y_ig(x_i)  = 1$$

$$\alpha_{i}^{k+1}= C \Rightarrow y_ig(x_i)  \leq 1$$

7. 如果满足则结束，返回$α^{k+1}$,否则转到步骤2。

---

# 六、线性支持回归
## 1. 模型的损失函数度量
&#8195;  回顾下我们前面SVM分类模型中，我们的目标函数是让$\frac{1}{2}||w||_2^2$最小，同时让各个训练集中的点尽量远离自己类别一边的的支持向量，即$y_i(w \bullet \phi(x_i )+ b) \geq 1$。

&#8195;  如果是加入一个松弛变量$ξ_i≥0$，则目标函数是$\frac{1}{2}||w||_2^2 +C\sum\limits_{i=1}^{m}\xi_i$，对应的约束条件变成：$y_i(w \bullet \phi(x_i ) + b )  \geq 1 - \xi_i$。

&#8195;  但是我们现在是回归模型，优化目标函数可以继续和SVM分类模型保持一致为$\frac{1}{2}||w||_2^2$，但是约束条件呢？不可能是让各个训练集中的点尽量远离自己类别一边的的支持向量，因为我们是回归模型，没有类别。对于回归模型，我们的目标是让训练集中的每个点$(x_i,y_i)$,尽量拟合到一个线性模型$y_i =w∙ϕ(x_i)+b$。对于一般的回归模型，我们是用均方差作为损失函数，但是SVM不是这样定义损失函数的。

&#8195;  SVM需要我们定义一个常量ϵ>0,对于某一个点$(x_i,y_i)$：
如果$|y_i−w∙ϕ(x_i)−b|≤ϵ$，则完全没有损失；如果$|y_i−w∙ϕ(x_i)−b|>ϵ$，则对应的损失为$|y_i−w∙ϕ(x_i)−b|−ϵ$。这个均方差损失函数不同，如果是均方差，那么只要$y_i−w∙ϕ(x_i)−b≠0$，那么就会有损失。

如下图所示，在蓝色条带里面的点都是没有损失的，但是外面的点的是有损失的，损失大小为红色线的长度。

![](https://upload-images.jianshu.io/upload_images/16911112-c8f1953b2e5aae76.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

总结下，我们的SVM回归模型的损失函数度量为：
$$
err(x_i,y_i) =  \begin{cases} 0 & {|y_i - w \bullet \phi(x_i ) -b| \leq \epsilon}\\ 
|y_i - w \bullet \phi(x_i ) -b| - \epsilon & {|y_i - w \bullet \phi(x_i ) -b| > \epsilon} \end{cases}
$$

## 2. 模型的目标函数的原始形式
* 前面已经得到了我们的损失函数的度量，现在可以可以定义我们的目标函数如下：
$$min\;\; \frac{1}{2}||w||_2^2  \;\; s.t \;\; |y_i - w \bullet \phi(x_i ) -b| \leq \epsilon (i =1,2,...m)$$

* 和SVM分类模型相似，回归模型也可以对每个样本$(x_i,y_i)$加入松弛变量$ξ_i≥0$, 但是由于我们这里用的是绝对值，实际上是两个不等式，也就是说两边都需要松弛变量，我们定义为$ξ^∨_i,ξ^∧_i,$ 则我们SVM回归模型的损失函数度量在加入松弛变量之后变为：
$$min\;\; \frac{1}{2}||w||_2^2 + C\sum\limits_{i=1}^{m}(\xi_i^{\lor}+ \xi_i^{\land})$$

$$s.t. \;\;\; -\epsilon - \xi_i^{\lor} \leq y_i - w \bullet \phi(x_i ) -b \leq \epsilon + \xi_i^{\land}$$

$$\xi_i^{\lor} \geq 0, \;\; \xi_i^{\land} \geq 0 \;(i = 1,2,..., m)$$

* 依然和SVM分类模型相似，我们可以用拉格朗日函数将目标优化函数变成无约束的形式，也就是拉格朗日函数的原始形式如下：
$$
L(w,b,\alpha^{\lor}, \alpha^{\land}, \xi_i^{\lor}, \xi_i^{\land}, \mu^{\lor}, \mu^{\land}) = \frac{1}{2}||w||_2^2 + C\sum\limits_{i=1}^{m}(\xi_i^{\lor}+ \xi_i^{\land}) + \sum\limits_{i=1}^{m}\alpha^{\lor}(-\epsilon - \xi_i^{\lor} -y_i + w \bullet \phi(x_i) + b) \\ +
 \sum\limits_{i=1}^{m}\alpha^{\land}(y_i - w \bullet \phi(x_i ) - b -\epsilon - \xi_i^{\land}) - \sum\limits_{i=1}^{m}\mu^{\lor}\xi_i^{\lor} - \sum\limits_{i=1}^{m}\mu^{\land}\xi_i^{\land}$$
 其中$μ^∨≥0,μ^∧≥0,α^∨_i≥0,α^∧_i≥0$均为拉格朗日系数。

## 3. 模型的目标函数的对偶形式
* 前面讲到了SVM回归模型的目标函数的原始形式,我们的目标是：
$$\underbrace{min}_{w,b,\xi_i^{\lor}, \xi_i^{\land}}\quad \underbrace{max}_{\mu^{\lor} \geq 0, \mu^{\land} \geq 0, \alpha_i^{\lor} \geq 0, \alpha_i^{\land} \geq 0}\;L(w,b,\alpha^{\lor}, \alpha^{\land}, \xi_i^{\lor}, \xi_i^{\land}, \mu^{\lor}, \mu^{\land})$$

* 和SVM分类模型一样，这个优化目标也满足KKT条件，也就是说，我们可以通过拉格朗日对偶将我们的优化问题转化为等价的对偶问题来求解如下：
$$\underbrace{max}_{\mu^{\lor} \geq 0, \mu^{\land} \geq 0, \alpha_i^{\lor} \geq 0, \alpha_i^{\land} \geq 0}\quad\underbrace{min}_{w,b,\xi_i^{\lor}, \xi_i^{\land}}\;L(w,b,\alpha^{\lor}, \alpha^{\land}, \xi_i^{\lor}, \xi_i^{\land}, \mu^{\lor}, \mu^{\land})$$

* 我们可以先求优化函数对于$w,b,ξ^∨_i,ξ^∧_i$的极小值, 接着再求拉格朗日乘子$α^∨,α^∧,μ^∨,μ^∧$的极大值。

* 首先我们来求优化函数对于$w,b,ξ^∨_i,ξ^∧_i$的极小值，这个可以通过求偏导数求得：
$$\frac{\partial L}{\partial w} = 0 \;\Rightarrow w = \sum\limits_{i=1}^{m}(\alpha_i^{\land} - \alpha_i^{\lor})\phi(x_i)$$

$$\frac{\partial L}{\partial b} = 0 \;\Rightarrow  \sum\limits_{i=1}^{m}(\alpha_i^{\land} - \alpha_i^{\lor}) = 0$$

$$\frac{\partial L}{\partial \xi_i^{\lor}} = 0 \;\Rightarrow C-\alpha^{\lor}-\mu^{\lor} = 0$$

$$\frac{\partial L}{\partial \xi_i^{\land}} = 0 \;\Rightarrow C-\alpha^{\land}-\mu^{\land} = 0$$

* 把上面4个式子带入$L(w,b,α^∨,α^∧,ξ^∨_i,ξ^∧_i,μ^∨,μ^∧)$去消去$w,b,ξ^∨_i,ξ^∧_i$。最终得到的对偶形式为：
$$\underbrace{ max }_{\alpha^{\lor}, \alpha^{\land}}\; -\sum\limits_{i=1}^{m}(\epsilon-y_i)\alpha_i^{\land}+ (\epsilon+y_i)\alpha_i^{\lor}) - \frac{1}{2}\sum\limits_{i=1,j=1}^{m}(\alpha_i^{\land} - \alpha_i^{\lor})(\alpha_j^{\land} - \alpha_j^{\lor})K_{ij}$$

$$s.t. \; \sum\limits_{i=1}^{m}(\alpha_i^{\land} - \alpha_i^{\lor}) = 0$$

$$0 < \alpha_i^{\lor} < C \; (i =1,2,...m)$$

$$0 < \alpha_i^{\land} < C \; (i =1,2,...m)$$

* 对于这个目标函数，我们依然可以用第四篇讲到的SMO算法来求出对应的$α^∨,α^∧$，进而求出我们的回归模型系数w,b。

## 4. 模型系数的稀疏性
* 在SVM分类模型中，我们的KKT条件的对偶互补条件为： $α^∗_i(y_i(w∙ϕ(x_i)+b)−1+ξ^∗_i)=0$，而在回归模型中，我们的对偶互补条件类似如下：
$$\alpha_i^{\lor}(\epsilon + \xi_i^{\lor} + y_i - w \bullet \phi(x_i ) - b ) = 0$$

$$\alpha_i^{\land}(\epsilon + \xi_i^{\land} - y_i + w \bullet \phi(x_i ) + b ) = 0$$

* 根据松弛变量定义条件，如果$|y_i - w \bullet \phi(x_i ) -b| < \epsilon$，我们有$ξ^∨_i=0,ξ^∧_i=0$，此时：$\epsilon + \xi_i^{\lor} + y_i - w \bullet \phi(x_i ) - b \neq 0, \epsilon + \xi_i^{\land} - y_i + w \bullet \phi(x_i ) + b \neq 0$

* 这样要满足对偶互补条件，只有：$\alpha_i^{\lor} = 0, \alpha_i^{\land} = 0 \quad $

* 我们定义样本系数系数：
$$\beta_i =\alpha_i^{\land}-\alpha_i^{\lor}$$

* 根据上面w的计算式$w = \sum\limits_{i=1}^{m}(\alpha_i^{\land} - \alpha_i^{\lor})\phi(x_i)$，我们发现此时$β_i=0$，也就是说w不受这些在误差范围内的点的影响。对于在边界上或者在边界外的点，$α^∨_i≠0,α^∧_i≠0$，此时$β_i≠0$。

---

# 七、小结
## 主要优点
* 解决高维特征的分类问题和回归问题很有效,在特征维度大于样本数时依然有很好的效果；

* 仅仅使用一部分支持向量来做超平面的决策，无需依赖全部数据；
* 有大量的核函数可以使用，从而可以很灵活的来解决各种非线性的分类回归问题；
* 样本量不是海量数据的时候，分类准确率高，泛化能力强。

## 主要缺点
* 如果特征维度远远大于样本数，则SVM表现一般。

* SVM在样本量非常大，核函数映射维度非常高时，计算量过大，不太适合使用。
* 非线性问题的核函数的选择没有通用标准，难以选择一个合适的核函数。
* SVM对缺失数据敏感。

---

# 八、SVM常见问题
## 1. SVM是什么及其优化目标是什么？
&#8195;  SVM的基本模型是一个**二分类模型**，是定义在**特征空间**上的**间隔最大的线性分类器**。它的优化目标是找到**几何间隔最大的分离超平面**。SVM分为三种：**线性可分支持向量机**、**线性支持向量机**和**非线性支持向量机**。它们的区别如下：

* 当训练数据**线性可分时**，通过硬间隔最大化，学习一个线性分类器，即**线性可分支持向量机**。
* 当训练数据**近似线性可分时**，通过软间隔最大化，学习一个线性分类器，即**线性支持向量机**。
* 当训练数据**线性不可分时**，通过使用核技巧及软间隔最大化，学习一个线性分类器，**非线性支持向量机**。

## 2. SVM中的核方法是什么？
&#8195;  当输入空间为欧式空间或离散集合、特征空间为希尔伯特空间时，核函数表示**将输入从输入空间映射到特征空间得到的特征向量之间的内积**。通过核方法可以学习非线性支持向量机，等价于在高维的特征空间中学习线性支持向量机。
核方法是比SVM中更为一般的机器学习方法，可以用到PCA、K-means等多种模型中。

## 3. SVM中的函数间隔和几何间隔是什么？
&#8195;  对于训练样本$x_i$，超平面$(\omega,b)$，点距离超平面越远表示预测的置信度越高。另外，真实标签是$y_i$，对于二分类问题，取值为1或-1。函数间隔可以反应分类的正确性和置信度，其公式如下：
$$y_{i}(\omega x_i +b)$$

&#8195;  对于一个训练集来说，函数距离越小，超平面越好。但是函数距离有一个问题，仅仅增加w和b的值就可以放大距离，这并非我们想要的结果。 因此对上式进行归一化，得到**几何间隔**如下：
$$y_i ( \frac{\omega}{|| \omega||} x_{i} + \frac{b}{|| \omega||})$$

## 4. SVM中松弛变量$\varepsilon$和惩罚因子$C$
&#8195;  松弛变量和惩罚因子是为了把**线性可分SVM拓展为线性不可分SVM**的。只有被决策面分类错误的点（线性不可分点）才会有松弛变量，然后惩罚因子是对线性不可分点的惩罚。 **增大惩罚因子，模型泛化性能变弱，惩罚因子无穷大时，退化为线性可分SVM（硬间隔）； 减少惩罚因子，模型泛化性能变好**。

* 并非所有的样本点都有一个松弛变量与其对应。实际上只有“离群点”才有，或者说，所有没离群的点松弛变量都等于0。
* 松弛变量的值实际上标示出了对应的点到底离群有多远，值越大，点就越远。
* 惩罚因子C决定了你有多重视离群点带来的损失，显然当所有离群点的松弛变量的和一定时，你定的C越大，对目标函数的损失也越大，此时就暗示着你非常不愿意放弃这些离群点， 最极端的情况是你把C定为无限大，这样只要稍有一个点离群，目标函数的值马上变成无限大，马上让问题变成无解，这就退化成了硬间隔问题。当C无穷大时，为了最小化损失函数，只能使松弛变量 无穷小（趋近于0），等价于线性可分SVM。

## 5. 为什么要将求解 SVM 的原始问题转换为其对偶问题?
* 对偶问题更易求解，当我们寻找带约束的最优化问题时，为了使问题变得易于处理，可以把目标函数和约束全部融入拉格朗日函数，再求解其对偶问题来寻找最优解。
* 可以自然引入核函数，进而推广到非线性分类问题。

## 6. SVM中系数的求解
&#8195;  SMO（Sequential Minimal Optimization）算法。有多个拉拉格朗日乘子，**每次只选择其中两个乘子做优化，其他因子被认为是常数**。将N个变量的求解问题，转换成两个变量的求解问题，并且目标函数是凸的。

## 7. 为什么SVM对缺失数据敏感
&#8195;  这里说的缺失数据是指缺失某些特征数据，向量数据不完整。SVM 没有处理缺失值的策略。而 SVM 希望样本在特征空间中线性可分，所以特征空间的好坏对SVM的性能很重要。缺失特征数据将影响训练结果的好坏。

## 8. SVM的损失函数
&#8195;  SVM的损失函数如下，第一项称为经验风险(Hinge loss), 度量了模型对训练数据的拟合程度; 第二项称为结构风险(正则项), 度量了模型自身的复杂度。正则化项削减了假设空间, 从而降低过拟合风险。λ 是个可调节的超参数, 用于调整经验风险和结构风险的相对权重。
$$\underbrace{min}_{\omega,b} \frac{1}{m} \sum_{i=1}^m
max(0,1-y_{i}(\omega^{T}x_i+b)) +\frac{\lambda}{2} ||\omega||^2$$

## 9. SVM中的核函数的优缺点及如何选择
### 1. 常用的三种核函数的优缺点如下：
* 线性核
形式：$x_{i}^T x_j$
优点：有高效实现，不易过拟合。
缺点：无法解决非线性可分问题。

* 多项式核
形式：$(\beta x_{i}^T x_j + \theta)^n$
优点：比线性核更一般，n直接描述了被映射空间的复杂度。
缺点：参数都，当n很大时会导致计算不稳定。

* RBF核
形式：$exp \left( -\frac{||x_i - x_j||^2}{2 \sigma^2} \right)$
优点：只有一个参数，没有计算不稳定问题。
缺点：计算慢，过拟合风险大。

### 2. 如何选择核函数？
* 当特征维数 d 超过样本数 m 时 (文本分类问题通常是这种情况), 使用线性核;
* 当特征维数 d 比较小，样本数 m 中等时, 使用RBF核;
* 当特征维数 d 比较小，样本数 m 特别大时, 支持向量机性能通常不如深度神经网络。

## 10. 讲一下SVR(支持向量回归)
&#8195;  SVR回归，就是找到一个回归平面，让一个集合的所有数据到该平面的距离最近。传统回归模型的损失是计算模型输出f(x)和真实值y之间的差别，当且仅当f(x)=y时，损失才为零；但是SVR假设我们能容忍f(x)和y之间有一定的偏差，仅当f(x)和y之间的偏差大于该值时才计算损失。

## 11. 支持向量机的优缺点
### 优点
* 由于SVM是一个凸优化问题，所以求得的解一定是全局最优而不是局部最优。
* 不仅适用于线性线性问题还适用于非线性问题(用核技巧)。
* 拥有高维样本空间的数据也能用SVM，这是因为数据集的复杂度只取决于支持向量而不是数据集的维度，这在某种意义上避免了“维数灾难”。
* 理论基础比较完善。

### 缺点
*  二次规划问题求解将涉及m阶矩阵的计算(m为样本的个数), 因此SVM不适用于超大数据集(SMO算法可以缓解这个问题)。
* 当样本数量比较大时，效果通常不如神经网络。
