# 集成学习
# 一、简介

&#8195;  集成学习归属于机器学习，他是一种训练思路，并不是某种具体的方法或者算法。现实生活中，大家都知道人多力量大，3 个臭皮匠顶个诸葛亮。而集成学习的核心思路就是人多力量大，它并没有创造出新的算法，而是把已有的算法进行结合，从而得到更好的效果。

![](https://upload-images.jianshu.io/upload_images/16911112-a6e0fabd753a1c23.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

&#8195;  集成学习会挑选一些简单的基础模型进行组装，组装这些基础模型的思路主要有2种方法：bagging和boosting。

---

# 二、bagging算法

&#8195;  **bootstrap aggregating**的缩写，也称作“套袋法”。Bagging的核心思路是——民主。Bagging的思路是所有基础模型都一致对待，每个基础模型手里都只有一票。然后使用民主投票的方式得到最终的结果。大部分情况下，经过bagging得到的结果**方差（variance）更小**。

![](https://upload-images.jianshu.io/upload_images/16911112-33026fff2e09c21c.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### bagging算法具体过程：
* 1.从原始样本集中抽取训练集。每轮从原始样本集中使用Bootstraping的方法抽取n个训练样本（在训练集中，有些样本可能被多次抽取到，而有些样本可能一次都没有被抽中）。共进行k轮抽取，得到k个训练集。（k个训练集之间是相互独立的）     
* 2.每次使用一个训练集得到一个模型，k个训练集共得到k个模型。（注：这里并没有具体的分类算法或回归方法，我们可以根据具体问题采用不同的分类或回归方法，如决策树、感知器等）     
* 3.对分类问题：将上步得到的k个模型采用投票的方式得到分类结果；      
* 4.对回归问题，计算上述模型的均值作为最后的结果。（所有模型的重要性相同）

在bagging的方法中，最广为熟知的就是随机森林了：bagging + 决策树 = 随机森林

---

# 三、boosting算法

&#8195;  Boosting的核心思路是——挑选精英。Boosting和bagging最本质的差别在于他对基础模型不是一致对待的，而是经过不停的考验和筛选来挑选出「精英」，然后给精英更多的投票权，表现不好的基础模型则给较少的投票权，然后综合所有人的投票得到最终结果。大部分情况下，经过 boosting 得到的结果偏差（bias）更小。

![](https://upload-images.jianshu.io/upload_images/16911112-6b5f75dd906af979.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### boosting算法具体过程：
* 1.通过加法模型将基础模型进行线性的组合。     
* 2.每一轮训练都提升那些错误率小的基础模型权重，同时减小错误率高的模型权重。    
* 3.在每一轮改变训练数据的权值或概率分布，通过提高那些在前一轮被弱分类器分错样例的权值，减小前一轮分对样例的权值，来使得分类器对误分的数据有较好的效果。

在boosting的方法中，比较主流的有**Adaboost**和**Gradient boosting**。

---

# 四、集成学习之结合策略
## 1. 平均法
&#8195;  对于数值类的回归预测问题，通常使用的结合策略是平均法，也就是说，对于若干个弱学习器的输出进行平均得到最终的预测输出。
* 最简单的平均是算术平均，也就是说最终预测是：
$$H(x) = \frac{1}{T}\sum\limits_{1}^{T}h_i(x)$$

* 如果每个个体学习器有一个权重$w$，则最终预测是：
$$H(x) = \sum\limits_{i=1}^{T}w_ih_i(x)$$

* 其中$w_i$是个体学习器$h_i$的权重，通常有：
$$w_i \geq 0 ,\;\;\; \sum\limits_{i=1}^{T}w_i = 1$$

## 2. 投票法
&#8195;  对于分类问题的预测，我们通常使用的是投票法。假设我们的预测类别是{$c_1,c_2,...c_K$},对于任意一个预测样本x，我们的T个弱学习器的预测结果分别是$(h_1(x),h_2(x)...h_T(x))$。

&#8195;  最简单的投票法是相对多数投票法，也就是我们常说的少数服从多数，也就是T个弱学习器的对样本x的预测结果中，数量最多的类别$c_i$为最终的分类类别。如果不止一个类别获得最高票，则随机选择一个做最终类别。

&#8195;  稍微复杂的投票法是绝对多数投票法，也就是我们常说的要票过半数。在相对多数投票法的基础上，不光要求获得最高票，还要求票过半数。否则会拒绝预测。

&#8195;  更加复杂的是加权投票法，和加权平均法一样，每个弱学习器的分类票数要乘以一个权重，最终将各个类别的加权票数求和，最大的值对应的类别为最终类别。

## 3. 学习法
&#8195;  上两节的方法都是对弱学习器的结果做平均或者投票，相对比较简单，但是可能学习误差较大，于是就有了学习法这种方法，对于学习法，代表方法是stacking，当使用stacking的结合策略时， 我们不是对弱学习器的结果做简单的逻辑处理，而是再加上一层学习器，也就是说，我们将训练集弱学习器的学习结果作为输入，将训练集的输出作为输出，重新训练一个学习器来得到最终结果。

&#8195;  在这种情况下，我们将弱学习器称为初级学习器，将用于结合的学习器称为次级学习器。对于测试集，我们首先用初级学习器预测一次，得到次级学习器的输入样本，再用次级学习器预测一次，得到最终的预测结果。

---

# 五、Bagging和Boosting
## 1. 样本选择上
* Bagging：训练集是在原始集中有放回选取的，从原始集中选出的各轮训练集之间是独立的。  
* Boosting：每一轮的训练集不变，只是训练集中每个样例在分类器中的权重发生变化。而权值是根据上一轮的分类结果进行调整。

## 2. 样例权重
* Bagging：使用均匀取样，每个样例的权重相等。     
* Boosting：根据错误率不断调整样例的权值，错误率越大则权重越大。

## 3. 预测函数
* Bagging：所有预测函数的权重相等。  
* Boosting：每个弱分类器都有相应的权重，对于分类误差小的分类器会有更大的权重。

## 4. 并行计算
* Bagging：各个预测函数可以并行生成          
* Boosting：各个预测函数只能顺序生成，因为后一个模型参数需要前一轮模型的结果。
