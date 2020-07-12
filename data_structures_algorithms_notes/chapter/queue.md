# 队列
# 一、简介
## 1. 定义
&#8195; 队列是一种“**先进先出”（FIFO**）的数据结构，和堆栈一样都是一种**有序线性表**的**抽象数据类型（ADT**）。

## 2. 特性
* 1. 具有“先进先出”（FIFO）的特性。
* 2. 拥有加入与删除两种基本操作，而且使用 front 和 rear 两个指针来分别指向队列的前端与末尾。

## 3. 基本操作
* 1. **create**：创建空队列。
* 2. **add**：将新数据加入队列的末尾，返回新队列。
* 3. **delete**：删除队列前端的数据，返回新队列。
* 4. **front**：返回队列前端的值。
* 5. **empty**：若队列为空，返回 true，否则返回 false。

![1.png](https://upload-images.jianshu.io/upload_images/16911112-a1918df8c238cb2b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)





