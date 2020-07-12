# 图
# 一、简介
## 1. 定义
&#8195; **图（Graph）**是由**顶点**和**连接顶点的边**构成的离散结构。通常用 G = (V, E) 来表示，其中 V 是所有顶点所组成的集合，而 E 代表所有边组成的集合。图的种类有两种：一种是无向图，一种是有向图。无向图用 $(V_1, V_2)$ 表示其边，有向图用 $<V_1, V_2>$表示其边。

## 2. 无向图
&#8195; **无向图（Graph**）是一种边没有方向的图，即通便两个顶点没有次序关系，如下图所示。

![2.jpg](https://upload-images.jianshu.io/upload_images/16911112-0d0652f1cf81366c.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 3. 有向图
&#8195; **有向图（Digraph**）是一种每一条边都可以使用有序对 $<V_1, V_2>$ 来表示的图，并且 $<V_1, V_2>$ 和 $<V_2, V_1>$ 表示两个不同方向的边，如下图所示。

![1.jpg](https://upload-images.jianshu.io/upload_images/16911112-5b04baf10c4144da.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)