# 正则化
# 一、参数范数正则化
## 1. L2 正则化
### 1.1 整体影响
### 1.2 物理意义
### 1.3 示例

## 2. L1 正则化
### 2.1 整体效果
### 2.2 物理意义

## 3. L1/L2正则化与最大后验估计







---

# 二、显式约束正则化




---

# 三、数据集增强
1. 提高模型泛化能力的一个最直接的方法是采用更多的数据来训练。但是通常在现实任务中，我们拥有的数据量有限。</br>
解决该问题的一种方法是：创建一些虚拟的数据用于训练。

2. 数据集增强仅仅用于模型的训练，而不是用于模型的预测。即：不能对测试集、验证集执行数据集增强。

3. 当比较机器学习算法基准测试的结果时，必须考虑是否采用了数据集增强。</br>
通常情况下，人工设计的数据集增强方案可以大大减少模型的泛化误差。当两个模型的泛化性能比较时，应该确保这两个模型使用同一套人工设计的数据集增强方案。

4. 注意数据集增强和预处理的区别：数据集增强会产生更多的输入数据，而数据预处理产生的输入数据数量不变。

## 1. 线性变换


## 2. 输入噪声注入



---

# 四、噪声鲁棒性
## 1. 输入噪声注入
## 2. 权重噪声注入
## 3. 输出噪声注入



---

# 五、早停
## 1. 早停算法
## 2. 二次训练
## 3. 早停与 L2 正则化






---

# 六、参数相对约束






---

# 七、dropout
## 1. dropout 与 bagging
## 2. 模型推断
## 3. 示例
## 4. 性质
## 5. dropout 与正则化



---

# 八、对抗训练









---

# 九、正切传播算法








---

# 十、其它相关
## 1. 稀疏表达
## 2. 半监督学习
## 3. 多任务学习

![](https://upload-images.jianshu.io/upload_images/16911112-0d50d8946fcfc60e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 4. 正则化和欠定问题



---










![1.png](https://upload-images.jianshu.io/upload_images/16911112-fb2aca4688e5345e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![2.jpg](https://upload-images.jianshu.io/upload_images/16911112-422654905829274e.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![3.png](https://upload-images.jianshu.io/upload_images/16911112-ef5ebe2293c8d86a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![4.png](https://upload-images.jianshu.io/upload_images/16911112-2ad458ef7fead9a4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![5.png](https://upload-images.jianshu.io/upload_images/16911112-8f2a4922f2c7e48b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![6.png](https://upload-images.jianshu.io/upload_images/16911112-eecec9bc27e5ff94.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![7.png](https://upload-images.jianshu.io/upload_images/16911112-2c269e8469809c74.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

