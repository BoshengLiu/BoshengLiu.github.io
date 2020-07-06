# 数学基础
# 一、基本知识
1. 文档中所有的向量都是列向量的形式：
$$\vec{x}=(x_1,x_2,...,x_n)^T
=\begin{bmatrix}
x_1 \\ x_2 \\
x_3 \\ x_4 \\ 
\end{bmatrix}$$
所有的矩阵$X\in R_{m \times n}$都表示为：
$$X=\begin{bmatrix}
x_{1,1} & x_{1,2} & \cdots & x_{1,n} \\
x_{2,1} & x_{2,2} & \cdots & x_{2,n} \\
\vdots & \vdots & \ddots & \vdots \\
x_{n,1} & x_{1,2} & \cdots & x_{1,n}
\end{bmatrix}$$
简写为：$(x_{i,j})_{m,n}$或者$[x_{i,j}]_{m,n}$。

2. 矩阵的F范数：设矩阵$A=(a_{i,j})_{m\times n}$，则其F范数为：$||A||_F=\sqrt{\sum_{i,j}a^2_{i,j}}$。它是向量的$L_2$范数的推广。

3. 矩阵的迹：设矩阵$A=(a_{i,j})_{m\times n}$，则A的迹为：$tr(A)=\sqrt{\sum_{i}a_{i,i}}$。迹的性质有：
    * A的F范数等于$AA^T$的迹的平方根：$||A||_F=\sqrt{tr(AA^T)}$。 
    
    * A的迹等于$A^T$的迹：$tr(A)=tr(A^T)$。
    * 交换律：假设$A\in R^{m\times n},B\in R^{n\times m}$，则有：$tr(AB)=tr(BA)$。
    * 结合律：$tr(ABC)=tr(CAB)=tr(BCA)$。

---

# 二、向量操作
1. 一组向量$\vec{v_1},\vec{v_2},...,\vec{v_n}$是线性相关的：指存在一组不全为零的实数$a_1,a_2,...,a_n$，使得：$\sum_{i=1}^n a_i\vec{v_i}=\vec{0}$。

2. 一组向量$\vec{v_1},\vec{v_2},...,\vec{v_n}$是线性无关的，当且仅当$a_i=0,i=1,2,...,n$时，才有：$\sum_{i=1}^n a_i\vec{v_i}=\vec{0}$。

3. 一个向量空间所包含的最大线性无关向量的数目，称作该向量空间的维数。

4. 三维向量的点积：$\vec{u}\cdot\vec{v}=u_xv_x+u_yv_y+u_zv_z=|\vec{u}||\vec{v}|cos(\vec{u},\vec{v})$。

![](https://upload-images.jianshu.io/upload_images/16911112-365ff9a8b6065d15.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

5. 三维向量的叉积：
$$\vec{w}=\vec{u}\times\vec{v}=\begin{bmatrix}
\vec{i} & \vec{j} & \vec{k} \\
u_x & u_y & u_z \\
v_x & v_y & v_z
\end{bmatrix}$$
其中$\vec{i},\vec{j},\vec{k}$分别为$x,y,z$轴的单位向量。
$$\vec{u}=u_x\vec{i}+u_y\vec{j}+u_z\vec{k},\quad \vec{v}=v_x\vec{i}+v_x\vec{j}+v_x\vec{k}$$
    * $\vec u$和$\vec v$的叉积垂直于$\vec{u},\vec{v}$构成的平面，其方向符合右手规则。
    * 叉积的模等于$\vec{u},\vec{v}$构成的平行四边形的面积
    * $\vec{u}\times\vec{v}=-\vec{v}\times\vec{u}$
    * $\vec{u}\times(\vec{v}\times\vec{w})=(\vec{u}\cdot\vec{w})\vec{v}-(\vec{u}\cdot\vec{v})\vec{w}$

![](https://upload-images.jianshu.io/upload_images/16911112-df48111bfc135264.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

6. 三维向量的混合积：
$$\begin{aligned}
|\vec{u}\vec{v}\vec{w}|&=(\vec{u}\times\vec{v})\cdot\vec{w}=\vec{u}\cdot(\vec{v}\times\vec{w})\\
&=\begin{vmatrix}
u_x & u_y & u_z \\
v_x & v_y & v_z \\
w_x & w_y & w_z \\
\end{vmatrix}=\begin{vmatrix}
u_x & v_x & w_x \\
u_y & v_y & w_y \\
u_z & v_z & w_z \\
\end{vmatrix}\end{aligned}$$
其物理意义为：以$\vec{u}\vec{v}\vec{w}$为三个棱边所围成的平行六面体的体积。当$\vec{u}\vec{v}\vec{w}$构成右手系时，该平行六面体的体积为正号。

7. 两个向量的并矢：给定两个向量$\vec{x}=(x_1,x_2,...,x_n)^T,\vec{y}=(y_1,y_2,...,y_m)^T$，则向量的并矢记作：
$$\begin{bmatrix}
x_1y_1 & x_1y_2 & \cdots & x_1y_m \\
x_2y_1 & x_2y_2 & \cdots & x_2y_m \\
\vdots & \vdots & \ddots & \vdots \\
x_ny_1 & x_ny_2 & \cdots & x_ny_m \\
\end{bmatrix}$$
也记作$\vec{x}\bigotimes\vec{y}$或者$\vec{x}\vec{y}^T$。

---

# 三、特殊函数

## 1. sigmoid 函数
1. `sigmad`函数的表达式为：
$$\sigma(x) = \frac{1}{1+exp(-x)}$$
    * 该函数可以用于生成二项分布的$\phi$参数。
    * 当$x$很大或者很小时，该函数处于饱和状态。此时函数的曲线非常平坦，并且自变量的一个较大的变化只能带来函数值的一个微小的变化，即：导数很小。
    
![](https://upload-images.jianshu.io/upload_images/16911112-6a3862286e32fdbf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 2. softplus 函数
1. `softplus`函数的表达式为：
$$\zeta(x)=log(1+exp(x))$$
    * 该函数可以生成正态分布的${\sigma}^2$参数。
    * 它之所以称作`softplus`，因为它是下面函数的一个光滑逼近：$x^+ = max(0,x)$。

![](https://upload-images.jianshu.io/upload_images/16911112-7508654579bb92ef.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

2. 如果定义两个函数：
$$x^+ = max(0,x),\quad\quad x^- = max(0,-x)$$
则它们分布获取了$y=x$的正部分和负部分。
根据定义有：$x=x^+-x^-$ 。而$\zeta(x)$逼近的是$x^+$，$\zeta(-x)$逼近的是$x^-$，于是有：
$$\zeta(x)-\zeta(-x)=x$$

3. `sigmoid` 和`softplus`函数的性质：
$$
\sigma(x)=\frac{exp(x)}{exp(x)+exp(0)}\\[2ex]
\frac{d}{dx}\sigma(x) = \sigma(x)(1-\sigma(x))\\[2ex]
1-\sigma(x) = \sigma(-x)\\[2ex]
log\sigma(x)=-\zeta(-x)\\[2ex]
\frac{d\zeta(x)}{dx}=\sigma{x}\\[2ex]
\forall{x}\in(0,1),\sigma^{-1}(x)=log(\frac{x}{1-x})\\[2ex]
\forall{x}>0,\zeta{-1}(x)=log(exp(x)-1)\\[2ex]
\zeta(x)=\int_{-\infty}^x \sigma(y) \,{\rm d}y\\[2ex]
\zeta(x)-\zeta(-x)=x\\[2ex]
$$
其中$f^{-1}(\cdot)$为反函数，$\sigma^{-1}(x)$也称作`logit`函数。

![](https://upload-images.jianshu.io/upload_images/16911112-a62998dc644d7a09.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 3. 伽马函数
1. 伽马函数定义为：
$$\Gamma(x)=\int_{0}^{+\infty}t^{x-1}e^{-t}dt,\quad x\in R\\
or.\quad \Gamma(z)=\int_{0}^{+\infty}t^{z-1}e^{-t}dz,\quad x\in Z$$
![](https://upload-images.jianshu.io/upload_images/16911112-b81ac509229b1220.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

性质为：
* 对于正整数$n$有：$\Gamma(n)=(n-1)!$。    
* $\Gamma(x+1)=x\Gamma(x)$，因此伽马函数是阶乘在实数域上的扩展。
* 与贝塔函数的关系：
$$B(m,n)=\frac{\Gamma(m)\Gamma(n)}{\Gamma(m+n)}$$
* 对于$x\in(0,1)$有：
$$\Gamma(1-x)\Gamma(x)=\frac{\pi}{sin\pi{x}}$$
则可以推导出重要公式：$\Gamma(\frac{1}{2})=\sqrt{\pi}$。
* 对于$x>0$，伽马函数是严格凹函数。

2. 当$x$足够大时，可以用`Stirling`公式来计算`Gamma`函数值：$\Gamma(x)~\sqrt{2\pi}e^{-x}x^{x+1/2}$。

## 4. 贝塔函数
1. 对于任意实数$m,n>0$，定义贝塔函数：
$$B(m,n)=\int_{0}^{1}x^{m-1}(1-x)^{n-1}dx$$
其它形式的定义：
$$B(m,n)=2\int_{0}^{\frac{\pi}{2}}sin^{2m-1}(x)cos^{2n-1}(x)dx
B(m,n)=\int_{0}^{+\infty}\frac{x^{m-1}}{(1+x)^{m+n}}dx
$$B(m,n)=\int_{0}^{1}\frac{x^{m-1}+x^{n-1}}{(1+x)^{m+n}}dx

2. 性质：
    * 连续性：贝塔函数在定义域$m>0,n>0$内连续。
    * 对称性：$B(m,n)=B(n,m)$。

    * 递个公式：
$$B(m,n)=\frac{n-1}{m+n-1}B(m,n-1),\quad m>0,n>1\\[2ex]
B(m,n)=\frac{m-1}{m+n-1}B(m-1,n),\quad m>1,n>0\\[2ex]
B(m,n)=\frac{(m-1)(n-1)}{(m+n-1)(m+n-2)}B(m-1,n-1),\quad m>1,n>1
$$

    * 当$m,n$较大时，有近似公式：
$$B(m,n)=\frac{\sqrt{(2\pi)m^{m-1/2}n^{n-1/2}}}
{(m+n)^{m+n-1/2}}$$

    * 与伽马函数关系：
        * 对于任意正实数$m,n$，有：
$$B(m,n)=\frac{\Gamma(m)\Gamma(n)}{\Gamma(m+n)}$$
        * $B(m,1-m)=\Gamma(m)\Gamma(1-m)$
        
---

# 四、矩阵运算

**更新中...**
