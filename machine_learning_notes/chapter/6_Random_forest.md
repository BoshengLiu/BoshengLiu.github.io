# 随机森林
# 一、随机森林原理
&#8195; 随机森林(Random Forest,以下简称RF)是Bagging算法的进化版，也就是说，它的思想仍然是bagging,但是进行了独有的改进。我们现在就来看看RF算法改进了什么。　　　

&#8195; 首先，RF使用了CART决策树作为弱学习器，这让我们想到了梯度提示树GBDT。第二，在使用决策树的基础上，RF对决策树的建立做了改进，对于普通的决策树，我们会在节点上所有的n个样本特征中选择一个最优的特征来做决策树的左右子树划分，但是RF通过随机选择节点上的一部分样本特征，这个数字小于n，假设为$n_{sub}$，然后在这些随机选择的$n_{sub}$个样本特征中，选择一个最优的特征来做决策树的左右子树划分。这样进一步增强了模型的泛化能力。

&#8195; 如果$n_{sub}=n$，则此时RF的CART决策树和普通的CART决策树没有区别。$n_{sub}$越小，则模型约健壮，当然此时对于训练集的拟合程度会变差。也就是说$n_{sub}$越小，模型的方差会减小，但是偏倚会增大。在实际案例中，一般会通过交叉验证调参获取一个合适的$n_{sub}$的值。

&#8195; 除了上面两点，RF和普通的bagging算法没有什么不同， 下面简单总结下RF的算法。输入为样本集$D= \lbrace (x_1,y_1),(x_2,y_2),...(x_m,y_m)\rbrace $，弱分类器迭代次数T。输出为最终的强分类器f(x)。
* 1. 对于t=1,2...,T：
  * a. 对训练集进行第t次随机采样，共采集m次，得到包含m个样本的采样集$D_t$
  * b. 用采样集$D_t$训练第t个决策树模型$G_t(x)$，在训练决策树模型的节点的时候， 在节点上所有的样本特征中选择一部分样本特征， 在这些随机选择的部分样本特征中选择一个最优的特征来做决策树的左右子树划分
* 2. 如果是分类算法预测，则T个弱学习器投出最多票数的类别或者类别之一为最终类别。如果是回归算法，T个弱学习器得到的回归结果进行算术平均得到的值为最终的模型输出。

随机森林如下图所示：

![](https://upload-images.jianshu.io/upload_images/16911112-6c709d26752bd2c4.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

---

# 二、构造随机森林的4个步骤
1. 假如有N个样本，则有放回的随机选择N个样本(每次随机选择一个样本，然后返回继续选择)。这选择好了的N个样本用来训练一个决策树，作为决策树根节点处的样本。
2. 当每个样本有M个属性时，在决策树的每个节点需要分裂时，随机从这M个属性中选取出m个属性，满足条件m << M。然后从这m个属性中采用某种策略（比如说信息增益）来选择1个属性作为该节点的分裂属性。
3. 决策树形成过程中每个节点都要按照步骤2来分裂（很容易理解，如果下一次该节点选出来的那一个属性是刚刚其父节点分裂时用过的属性，则该节点已经达到了叶子节点，无须继续分裂了）。一直到不能够再分裂为止。注意整个决策树形成过程中没有进行剪枝。
4. 按照步骤1~3建立大量的决策树，这样就构成了随机森林了。

过程如下图所示：

![](https://upload-images.jianshu.io/upload_images/16911112-ebe405e3378dc61c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

---

# 三、随机森林的推广
&#8195; 由于RF在实际应用中的良好特性，基于RF，有很多变种算法，应用也很广泛，不光可以用于分类回归，还可以用于特征转换，异常点检测等。下面对于这些RF家族的算法中有代表性的做一个总结。

## 3.1 extra trees
&#8195; **extra trees**是RF的一个变种, 原理几乎和RF一模一样，仅有区别有：

1. 对于每个决策树的训练集，RF采用的是随机采样bootstrap来选择采样集作为每个决策树的训练集，而extra trees一般不采用随机采样，即每个决策树采用原始训练集。
2. 在选定了划分特征后，RF的决策树会基于基尼系数，均方差之类的原则，选择一个最优的特征值划分点，这和传统的决策树相同。但是extra trees比较的激进，他会随机的选择一个特征值来划分决策树。

&#8195; 从第二点可以看出，由于随机选择了特征值的划分点位，而不是最优点位，这样会导致生成的决策树的规模一般会大于RF所生成的决策树。也就是说，模型的方差相对于RF进一步减少，但是偏倚相对于RF进一步增大。在某些时候，extra trees的泛化能力比RF更好。

## 3.2 Totally Random Trees Embedding
&#8195; **Totally Random Trees Embedding**(以下简称 TRTE)是一种非监督学习的数据转化方法。它将低维的数据集映射到高维，从而让映射到高维的数据更好的运用于分类回归模型。我们知道，在支持向量机中运用了核方法来将低维的数据集映射到高维，此处TRTE提供了另外一种方法。

&#8195; TRTE在数据转化的过程也使用了类似于RF的方法，建立T个决策树来拟合数据。当决策树建立完毕以后，数据集里的每个数据在T个决策树中叶子节点的位置也定下来了。比如我们有3颗决策树，每个决策树有5个叶子节点，某个数据特征x划分到第一个决策树的第2个叶子节点，第二个决策树的第3个叶子节点，第三个决策树的第5个叶子节点。则x映射后的特征编码为(0,1,0,0,0,     0,0,1,0,0,     0,0,0,0,1), 有15维的高维特征。这里特征维度之间加上空格是为了强调三颗决策树各自的子编码。

&#8195; 映射到高维特征后，可以继续使用监督学习的各种分类回归算法了

## 3.3 Isolation Forest
&#8195; **Isolation Forest**（以下简称IForest）是一种异常点检测的方法。它也使用了类似于RF的方法来检测异常点。

&#8195; 对于在T个决策树的样本集，IForest也会对训练集进行随机采样,但是采样个数不需要和RF一样，对于RF，需要采样到采样集样本个数等于训练集个数。但是IForest不需要采样这么多，一般来说，采样个数要远远小于训练集个数？为什么呢？因为我们的目的是异常点检测，只需要部分的样本我们一般就可以将异常点区别出来了。

&#8195; 对于每一个决策树的建立， IForest采用随机选择一个划分特征，对划分特征随机选择一个划分阈值。这点也和RF不同。

&#8195; 另外，IForest一般会选择一个比较小的最大决策树深度max_depth,原因同样本采集，用少量的异常点检测一般不需要这么大规模的决策树。

&#8195; 对于异常点的判断，则是将测试样本点x拟合到T颗决策树。计算在每颗决策树上该样本的叶子节点的深度$h_t(x)$。从而可以计算出平均高度h(x)。此时我们用下面的公式计算样本点x的异常概率:
$$
s(x,m) = 2^{-\frac{h(x)}{c(m)}}
$$其中，m为样本个数。c(m)的表达式为：
$$c(m) =2\ln(m-1) + \xi - 2\frac{m-1}{m}, \; \xi为欧拉常数$$

s(x,m)的取值范围是[0,1],取值越接近于1，则是异常点的概率也越大。

---

# 四、小结
## 优点：
* 1.它可以出来很高维度（特征很多）的数据，并且不用降维，无需做特征选择；
* 2.它可以判断特征的重要程度；
* 3.可以判断出不同特征之间的相互影响；    
* 4.不容易过拟合；  
* 5.训练速度比较快，容易做成并行方法；    
* 6.实现起来比较简单；
* 7.对于不平衡的数据集来说，它可以平衡误差；
* 8.如果有很大一部分的特征遗失，仍可以维持准确度。

## 缺点：
* 1.随机森林已经被证明在某些噪音较大的分类或回归问题上会过拟合；
* 2.对于有不同取值的属性的数据，取值划分较多的属性会对随机森林产生更大的影响，所以随机森林在这种数据上产出的属性权值是不可信的。

---

# 五、随机森林sklearn的参数
&#8195; 随机森林的分类学习器为*RandomForestClassifier*，回归学习器为*RandomForestRegressor*。

## 1. 分类随机森林
分类随机森林参数如下所示：
```
RandomForestClassifier(
      n_estimators=10, criterion=’gini’,
      max_depth=None,min_samples_split=2,
      min_samples_leaf=1, min_weight_fraction_leaf=0.0,
      max_features=’auto’,max_leaf_nodes=None,
      min_impurity_decrease=0.0, min_impurity_split=None, 
      bootstrap=True, oob_score=False, n_jobs=None, 
      random_state=None, verbose=0, warm_start=False, class_weight=None)
```

### 1.1 控制bagging框架的参数
* estimators：随机森林中树的棵树，即要生成多少个基学习器（决策树）。    
* boostrap：是否采用自助式采样生成采样集。  
* obb_score：是否使用袋外数据来估计模型的有效性。

### 1.2 控制决策树的参数
* criterion：选择最优划分属性的准则，默认是"gini"，可选"entropy"。      
* max_depth：决策树的最大深度    
* max_features：随机抽取的候选划分属性集的最大特征数（属性采样）     
* min_samples_split：内部节点再划分所需最小样本数。默认是2，可设置为整数或浮点型小数。   
* min_samples_leaf：叶子节点最少样本数。默认是1，可设置为整数或浮点型小数。     
* max_leaf_nodes：最大叶子结点数。默认是不限制。    
* min_weight_fraction_leaf：叶子节点最小的样本权重和。默认是0。   
* min_impurity_split：节点划分最小不纯度。

### 1.3 其他参数：
* n_jobs：并行job的个数   
* verbose：是否显示任务进程

### 1.4 可调用方法：
* predict_proba：计算预测的概率值    
* predict(x)：预测     
* predict_log_proba(x)：计算出预测的对数概率值

### 1.5 可调用的属性：
* estimators_：列出决策树参数   
* feature_importances_：列出变量重要性  
* n_features：   
* n_outputs_：   
* obb_score_：袋外数据测试效果   
* obb_prediction_：袋外数据预测结果

## 2. 更多请参考：
1. [*分类随机森林-RandomForestClassifier*](http://lijiancheng0614.github.io/scikit-learn/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier)
2. [*回归森林-RandomForestRegressor*](http://lijiancheng0614.github.io/scikit-learn/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
