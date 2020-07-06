# 反向传播算法
1. 前向传播 `forward propagation` 过程： 当前馈神经网络接收输入$\vec x$并产生输出$y$时，信息前向流动。</br>
输入$\vec x$提供初始信息，然后信息传播到每一层的隐单元，最终产生输出$y$。

2. 反向传播算法 `back propagation` 允许来自代价函数的信息通过网络反向流动以便计算梯度。
    * 反向传播并不是用于学习整个神经网络的算法，而是仅用于计算梯度的算法。</br>
神经网络的学习算法是随机梯度下降这类基于梯度的算法。

    * 反向传播不仅仅适用于神经网络，原则上它适用于计算任何函数的导数。

3. 计算图`computational graph`：
    * 图中的每个节点代表一个变量（可以是标量、向量、矩阵或者张量）。

    * 操作：`operation`为一个或者多个变量的简单函数。
        * 多个操作组合在一起可以描述一个更复杂的函数。
        * 一个操作仅返回单个输出变量（可以是标量、向量、矩阵或者张量）。
    
    * 如果变量$y$是变量$x$通过一个操作计算得到，则在图中绘制一条从$x$到$y$的有向边。</br>
    如：$\hat y=\sigma(\vec x^T\vec w+b)$的计算图：

![](https://upload-images.jianshu.io/upload_images/16911112-a068efe7507dd1fa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
    
# 一、链式法则
1. 反向传播算法是一种利用链式法则计算微分的算法。

2. 在一维的情况下，链式法则为：$\frac{\mathrm{d}z}{\mathrm{d}x}=\frac{\mathrm{d}z}{\mathrm{d}y}\times\frac{\mathrm{d}y}{\mathrm{d}x}$。

3. 在多维情况下，设：$\vec x\in R^m,\vec y\in R^n$，$g为R^m到R^n$的映射且满足$\vec y=g(\vec x)$，$f$为$R^n到R$的映射且满足$z=f(\vec y)$。则有：
$$\frac{\partial z}{\partial x_i}=\sum_{j=1}^{n}\frac{\partial z}{\partial y_j}\frac{\partial y_i}{\partial x_i},\quad i=1,2,...,m$$
使用向量记法，可以等价地写作：
$$\nabla_{\vec x}z=\left( \frac{\partial {\vec y}}{\partial {\vec x}} \right)^T\nabla_{\vec y}z$$
其中：$\frac{\partial {\vec y}}{\partial {\vec x}}为g的n\times m$阶雅可比矩阵，$\nabla_{\vec x}z为z对\vec x的梯度，\nabla_{\vec y}z为z对\vec y的梯度$：
$$\nabla_{\vec x}z=\begin{bmatrix} \frac{\partial z}{\partial x_1} \\[2ex]
 \frac{\partial z}{\partial x_2} \\[2ex]
 \vdots \\[2ex]\frac{\partial z}{\partial x_m}\\[2ex] \end{bmatrix}\quad
\nabla_{\vec y}z=\begin{bmatrix} \frac{\partial z}{\partial y_1} \\[2ex]
 \frac{\partial z}{\partial y_2} \\[2ex]
 \vdots \\[2ex]\frac{\partial z}{\partial y_m}\\[2ex] \end{bmatrix}\quad
\frac{\partial {\vec y}}{\partial {\vec x}}= \begin{bmatrix}
\frac{\partial y_1}{\partial x_1} & \frac{\partial y_1}{\partial x_2} & \cdots & \frac{\partial y_1}{\partial x_m}\\[2ex]
\frac{\partial y_2}{\partial x_1} & \frac{\partial y_2}{\partial x_2} & \cdots & \frac{\partial y_2}{\partial x_m} \\[2ex]
\vdots & \vdots & \ddots & \vdots\\[2ex]
\frac{\partial y_n}{\partial x_1} & \frac{\partial y_n}{\partial x_2} & \cdots & \frac{\partial y_n}{\partial x_m} \\[2ex] \end{bmatrix}$$
反向传播算法由很多这样的雅可比矩阵与梯度的乘积操作组成。

## 1. 张量链式法则
1. 链式法则不仅可以作用于向量，也可以应用于张量：
    * 首先将张量展平为一维向量。
    * 然后计算该向量的梯度。
    * 然后将该梯度重新构造为张量。

2. 记$\nabla_xz$为$z$对张量$X$的梯度。$X$现在有多个索引（如：二维张量有两个索引），可以使用单个变量$i$来表示$X$的索引元组（如$i=1\sim 9$表示：一个二维张量的索引，每个维度三个元素）。</br>
这就与向量中的索引方式完全一致：$(\nabla_xz)_i=\frac{\partial z}{\partial x_i}$。</br>
如：
$$X=\begin{bmatrix} x_1 & x_2 & x_3 \\
 x_4 & x_5 & x_6 \\
 x_7 & x_8 & x_9 \end{bmatrix}$$
则有：
$$\nabla_{\vec x}z=\begin{bmatrix} \frac{\partial z}{\partial x_1} & \frac{\partial z}{\partial x_2} & \frac{\partial z}{\partial x_3}\\[2ex]
\frac{\partial z}{\partial x_4} & \frac{\partial z}{\partial x_5} & \frac{\partial z}{\partial x_6}\\[2ex]
\frac{\partial z}{\partial x_7} & \frac{\partial z}{\partial x_8} & \frac{\partial z}{\partial x_9}\end{bmatrix}$$
 
3. 设$Y=g(X),z=f(Y)$，用单个变量$j$来表示$Y$的索引元组。则张量的链式法则为：
$$\frac{\partial z}{\partial x_i}=\sum_{j}\frac{\partial z}{\partial y_j}\frac{\partial y_i}{\partial x_i}\Rightarrow
\nabla_xz=\sum_{j}(\nabla_xy_j)\frac{\partial z}{\partial y_j}$$
如：
$$X=\begin{bmatrix} x_1 & x_2 & x_3 \\
 x_4 & x_5 & x_6 \\
 x_7 & x_8 & x_9 \end{bmatrix}$$
则有：
$$\nabla_{\vec x}z=\begin{bmatrix}\sum_{j}\frac{\partial z}{\partial y_j}\frac{\partial y_i}{\partial x_1}
&\sum_{j}\frac{\partial z}{\partial y_j}\frac{\partial y_i}{\partial x_2}
&\sum_{j}\frac{\partial z}{\partial y_j}\frac{\partial y_i}{\partial x_3}\\[3ex]
\sum_{j}\frac{\partial z}{\partial y_j}\frac{\partial y_i}{\partial x_4}
&\sum_{j}\frac{\partial z}{\partial y_j}\frac{\partial y_i}{\partial x_5}
&\sum_{j}\frac{\partial z}{\partial y_j}\frac{\partial y_i}{\partial x_6}\\[3ex]
\sum_{j}\frac{\partial z}{\partial y_j}\frac{\partial y_i}{\partial x_7}
&\sum_{j}\frac{\partial z}{\partial y_j}\frac{\partial y_i}{\partial x_8}
&\sum_{j}\frac{\partial z}{\partial y_j}\frac{\partial y_i}{\partial x_9}\end{bmatrix}$$
 

## 2. 重复子表达式
1.给定计算图以及计算图中的某个标量$z$，根据链式法则可以很容易地写出$z$对于产生$z$的任意节点的梯度的数学表达式。</br>
但是在计算该表达式的时候，许多子表达式可能在计算整个梯度表达式的过程中重复很多次。
![](https://upload-images.jianshu.io/upload_images/16911112-c4fc856b2293105b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)        
如图中：
$$x=f(x),\quad y=f(y),\quad z=f(z)\\[2ex]
\Rightarrow \frac{dz}{dw}\;=\;\frac{dz}{dy}\frac{dy}{dx}\frac{dx}{dw}\;=\;f'(y)f'(x)f'(w)=f'(f(f(w)))f'(f(w))f'(w)$$
可以看到$f(w)$被计算多次。
* 在复杂的计算图中，可能存在指数量级的重复子表达式，这使得原始的链式法则几乎不可实现。

* 一个解决方案是：计算$f(w)$一次并将它存储在$x$中，然后采用$f'(y)f'(x)f'(w)$来计算梯度。</br>
这也是反向传播算法采用的方案：在前向传播时，将节点的中间计算结果全部存储在当前节点上。其代价是更高的内存开销。

2. 有时候必须重复计算子表达式。这是以较高的运行时间为代价，来换取较少的内存开销。

---

# 二、反向传播
## 1. 前向传播
1. 考虑计算单个标量$u_n$的计算图：
    * 假设有$n_i$个输入节点：$u_1,u_2,...,u_{n_i}$。它们对应的是模型的参数和输入。
    * 假设$u_{n_i+1}$为中间节点。
    * 假设$u_n$为输出节点，它对应的是模型的代价函数。
    * 对于每个非输入节点$u_i$，定义其双亲节点的集合为 。 
    * 假设每个非输入节点$u_i$，操作$f_i$与其关联，并且通过对该函数求值得到：$u_i=f_i(A_i)$。</br>
通过仔细排序（有向无环图的拓扑排序算法），使得可以依次计算$u_{n_i+1},...,u_n$。

![](https://upload-images.jianshu.io/upload_images/16911112-53ad0b43887ff948.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

2. 前向传播算法：
    * 输入：
        * 计算图$g$
        * 初始化向量$\vec u^*$
    * 输出：$u_n$的值
    
    * 算法步骤：
        * 初始化输入节点：$u_i=u_i^*,i=1,2,...,n_i$。
        
        * 根据计算图，从前到后计算$u_{n_i+1},...,u_n$。对于$u_j,j=n_i+1,...,n$计算过程为：
            * 计算$u_j$的双亲节点集合$A_j$。 
            * 计算$u_j$：$u_j=f_i(A_j)$。
        输出$u_n$。

## 2. 反向传播
1. 计算$\frac{\partial u_n}{\partial u_j},j=1,2,...,n_i$时需要构造另一张计算图$B$：它的节点与$g$中完全相同，但是计算顺序完全相反。
计算图$B$如下图所示：

![](https://upload-images.jianshu.io/upload_images/16911112-da5f6ae31d447f09.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

2. 对于图中的任意一非输出节点$u_j（非u_n）$，根据链式法则：
$$\frac{\partial u_n}{\partial u_j}=\sum_{({\partial u_n},{\partial u_j})\in B}\frac{\partial u_n}{\partial u_i}\frac{\partial u_i}{\partial u_j}$$
其中$(\partial u_i,\partial u_j)\in B$表示图$B$中的边$\partial u_i \rightarrow \partial u_j$。
    * 若图$B$中存在边$\partial u_i \rightarrow \partial u_j$，则在图$g$中存在边$u_j\rightarrow u_i$，则$u_i$为$u_j$的子节点。
    * 设图$g$中$u_j$的子节点的集合为$C_j$，则上式改写作：
$$\frac{\partial u_n}{\partial u_j}=\sum_{u_i\in C_j}\frac{\partial u_n}{\partial u_i}\frac{\partial u_i}{\partial u_j}$$

3. 反向传播算法：
    * 输入：
        * 计算图$g$
        * 初始化参数向量$\vec u^*$
    * 输出：$\frac{\partial u_n}{\partial u_j},j=1,2,...,n_i$
    
    * 算法步骤：
        * 运行计算$u_n$的前向算法，获取每个节点的值。
        * 给出一个`grad_table`表，它存储的是已经计算出来的偏导数。
        
         $u_i$对应的表项存储的是偏导数$\frac{\partial u_n}{\partial u_j}$。
        * 初始化$grad_table[u_n]=1$。
        * 沿着计算图$B$计算偏导数。遍历$j$从$n-1$到1：
            * 计算$\frac{\partial u_n}{\partial u_j}=\sum_{u_i\in C_j}\frac{\partial u_n}{\partial u_i}\frac{\partial u_i}{\partial u_j}$。
            
            * 其中：$\frac{\partial u_n}{\partial u_j}$是已经存储的$grad_table[u_i]$，$\frac{\partial u_n}{\partial u_j}$为实时计算的。
            * 图$g$中的边$u_j\rightarrow u_i$定义了一个操作，而该操作的偏导只依赖于这两个变量，因此可以实时求解$\frac{\partial u_i}{\partial u_j}$。
            * 存储$grad\_tabel[u_j]$。
        * 返回$grad\_tabel[u_j],j=1,2,...,n_i$。
        
4. 反向传播算法计算所有的偏导数，计算量与$g$中的边的数量成正比。其中每条边的计算包括计算偏导数，以及执行一次向量点积。

5. 上述反向传播算法为了减少公共子表达式的计算量 ，并没有考虑存储的开销。这避免了重复子表达式的指数级的增长。
    * 某些算法可以通过对计算图进行简化从而避免更多的子表达式。
    * 有些算法会重新计算这些子表达式而不是存储它们，从而节省内存。

## 3. 反向传播示例
1. 对于$f(x,y,z)=(x+y)z$，将公式拆分成$q=x+y和f=qz$，则有：
$$\frac{\partial q}{\partial x}=1,\quad \frac{\partial q}{\partial y}=1,\quad \frac{\partial f}{\partial q}=z,\quad \frac{\partial f}{\partial z}=q,\quad$$
根据链式法则，有$\frac{\partial f}{\partial x}=\frac{\partial f}{\partial q}*\frac{\partial q}{\partial x}$。</br>
假设$x=-2,y=5,z=-4$，则计算图如下。其中：绿色为前向传播的值，红色为反向传播的结果。
![](https://upload-images.jianshu.io/upload_images/16911112-0147e88385bb6614.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)</br>
    * 前向传播，计算从输入到输出（绿色）；反向传播，计算从尾部开始到输入（红色）。
    * 在整个计算图中，每个单元的操作类型，以及输入是已知的。通过这两个条件可以计算出两个结果：
        * 这个单元的输出值。
        * 这个单元的输出值关于输入值的局部梯度比如$\frac{\partial q}{\partial x}和\frac{\partial q}{\partial y}$。</br>
        每个单元计算这两个结果是独立完成的，它不需要计算图中其他单元的任何细节。</br>
        但是在反向传播过程中，单元将获取整个网络的最终输出值（这里是$f$）在单元的输出值上的梯度，即回传的梯度。</br>
        链式法则指出：**单元应该将回传的梯度乘以它对其输入的局部梯度，从而得到整个网络的输出对于该单元每个输入值的梯度**。如：$\frac{\partial f}{\partial x}=\frac{\partial f}{\partial q}*\frac{\partial q}{\partial x}$。

2. 在多数情况下，反向传播中的梯度可以被直观地解释。如：加法单元、乘法单元、最大值单元。</br>
假设：$f=2*(x*y+max(z,w))$，前向传播的计算从输入到输出（绿色），反向传播的计算从尾部开始到输入（红色）。</br>
![](https://upload-images.jianshu.io/upload_images/16911112-4bf41fc6b43574ea.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)</br>
    * 加法单元$q=x+y，则\frac{\partial q}{\partial x}=1。如果\frac{\partial f}{\partial q}=m$，则有：
$$\frac{\partial f}{\partial x}=m,\quad \frac{\partial f}{\partial y}=m$$
这表明：加法单元将回传的梯度相等的分发给它的输入。
    
    * 乘法单元$q=x*y，则\frac{\partial q}{\partial x}=y,\frac{\partial q}{\partial y}=x。如果\frac{\partial f}{\partial q}=m$，则有：
$$\frac{\partial f}{\partial x}=my,\quad \frac{\partial f}{\partial y}=mx$$
这表明：乘法单元交换了输入数据，然后乘以回传的梯度作为每个输入的梯度。
    * 取最大值单元$q=max(x,y)$，则：
$$\frac{\partial q}{\partial x}=\begin{cases} 1, & x\geq y \ \\ 0, & x<y \end{cases},\quad
\frac{\partial q}{\partial y}=\begin{cases} 1, & y\geq x \ \\ 0, & y<x \end{cases}$$
如果$\frac{\partial f}{\partial q}=m$，则有：
$$\frac{\partial f}{\partial x}=\begin{cases} m, & x\geq y \ \\ 0, & x<y \end{cases},\quad
\frac{\partial f}{\partial y}=\begin{cases} m, & y\geq x \ \\ 0, & y<x \end{cases}$$
这表明：取最大值单元将回传的梯度分发给最大的输入。

3. 通常如果函数$f(x,y)$的表达式非常复杂，则当对$x,y$进行微分运算，运算结束后会得到一个巨大而复杂的表达式。
    * 实际上并不需要一个明确的函数来计算梯度，只需要如何使用反向传播算法计算梯度即可。
    * 可以把复杂的表达式拆解成很多个简单的表达式（这些表达式的局部梯度是简单的、已知的），然后利用链式法则来求取梯度。
    * 在计算反向传播时，前向传播过程中得到的一些中间变量非常有用。实际操作中，最好对这些中间变量缓存。

## 4. 深度前馈神经网络应用
1. 给定一个样本，其定义代价函数为$L(\hat y,y)$，其中$\hat y$为神经网络的预测值。</br>
考虑到正则化项，定义损失函数为：$J(\vec\theta)=L(\hat y,y)+\Omega(\vec\theta)$。其中$\hat y$为正则化项，而$\hat\theta$包含了所有的参数（包括每一层的权重$W$和每一层的偏置$\vec b_i$）。
这里给出的是单个样本的损失函数，而不是训练集的损失函数。</br>

2. 计算$\hat y$的计算图为：

![](https://upload-images.jianshu.io/upload_images/16911112-bb9a2d39730e61e0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

3. 前向传播用于计算深度前馈神经网络的损失函数。算法为：
    * 输入：
        * 网络层数$l$
        * 每一层的权重矩阵$W_i,i=1,2,...,l$
        * 每一层的偏置向量$b_i,i=1,2,...,l$
        * 每一层的激活函数$f_i(\cdot),i=1,2,...,l$ </br>
        注：也可以对所有的层使用同一个激活函数
        * 输入$\vec x$和对应的标记$y$。
        * 隐层到输出的函数$func(\cdot)$。
        
    * 输出：损失函数$J(\vec\theta)$
    * 算法步骤：
        * 初始化$\vec h_0=\vec x$
        
        * 迭代：$k=1,2,...,l$，计算：
            * $\vec a_k=\vec b_k+W_k\vec h_{k-1}$
            
            * $\vec h_k=f_k(\vec b_k)$
        * 计算$\hat y=func(\vec h_l)，J(\vec\theta)=L(\hat y,y)+\Omega(\vec\theta)$





---

# 三、算法实现
## 1. 符号-数值 / 符号-符号方法

![](https://upload-images.jianshu.io/upload_images/16911112-b5b7bfa9b82a7003.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 2. 算法框架
### 2.1 三个子过程
### 2.2 反向传播过程
## 3. 算法复杂度
## 4. 应用


![](https://upload-images.jianshu.io/upload_images/16911112-cea6272723f1db83.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



---

# 四、自动微分










