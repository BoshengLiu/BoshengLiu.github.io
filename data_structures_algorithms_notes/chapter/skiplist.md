# 跳表
## 1. 简介
&#8195; 跳表是在链表的基础上，添加了一些索引，在链表每两个结点添加一个索引到上一级，我们把抽出来的索引称为索引层。在此基础上，我们再对第一层索引层添加索引，得到了第二次索引层，以此类推，如下图所示。

![](https://upload-images.jianshu.io/upload_images/16911112-fdb46abc5912cefd.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

&#8195; 这种链表加多级索引的结构，就是**跳表**。按照上图，两个结点会抽出一个结点作为上一级索引的结点，那第一级索引的结点个数大约就是 n/2，第二级索引的结点个数大约就是 n/4，第三级索引的结点个数大约就是 n/8，依次类推，也就是说，**第 k 级索引的结点个数是第 k-1 级索引的结点个数的 1/2，那第 k级索引结点的个数就是 n/(2k)**。

&#8195; 假设有 k 级索引，最高级索引有2个节点，那么通过上面的公式，我们可以得到 n/(2h)=2，从而求得 h=log2n-1。如果包含原始链表这一层，整个跳表的高度就是 log2n。我们在跳表中查询某个数据的时候，如果每一层都要遍历 m 个结点，那在跳表中查询一个数据的时间复杂度就是 O(mlogn)。

&#8195; 按照前面这种索引结构，我们每一级索引都最多只需要遍历 3 个结点，也就是说 m=3。假设我们要查找的数据是 x，在第 k 级索引中，我们遍历到 y 结点之后，发现 x 大于 y，小于后面的结点 z，所以我们通过 y 的 down 指针，从第 k 级索引下降到第 k-1 级索引。在第 k-1 级索引中，y 和 z 之间只有 3 个结点（包含 y 和 z），所以，我们在 K-1 级索引中最多只需要遍历 3 个结点，依次类推，每一级索引都最多只需要遍历 3 个结点。流程如下图所示：

![](https://upload-images.jianshu.io/upload_images/16911112-e59897630fabf0bf.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

&#8195; 比起单纯的单链表，跳表需要存储多级索引，肯定要消耗更多的存储空间。假设原始链表大小为 n，那第一级索引大约有 n/2 个结点，第二级索引大约有 n/4 个结点，以此类推，每上升一级就减少一半，直到剩下 2 个结点。如果我们把每层索引的结点数写出来，就是一个等比数列。这几级索引的结点总和就是 n/2+n/4+n/8…+8+4+2=n-2。所以，跳表的空间复杂度是 O(n)。也就是说，如果将包含 n 个结点的单链表构造成跳表，我们需要额外再用接近 n 个结点的存储空间。

## 2. 优化及操作
### 2.1 优化
&#8195; 前面都是每两个结点抽一个结点到上级索引，如果我们每三个结点或五个结点，抽一个结点到上级索引，索引所需要的节点数就少了，如下图所示。

![](https://upload-images.jianshu.io/upload_images/16911112-6a04851b560c9f58.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

&#8195; 从图中可以看出，第一级索引需要大约 n/3 个结点，第二级索引需要大约 n/9 个结点。每往上一级，索引结点个数都除以 3。为了方便计算，我们假设最高一级的索引结点个数是 1。我们把每级索引的结点个数都写下来，也是一个等比数列。通过等比数列求和公式，总的索引结点大约就是 n/3+n/9+n/27+…+9+3+1=n/2。尽管空间复杂度还是 O(n)，但比上面的每两个结点抽一个结点的索引构建方法，要减少了一半的索引结点存储空间。

### 2.2 插入和删除
* 对于纯粹的单链表，需要遍历每个结点，来找到插入的位置。但是，对于跳表来说，我查找某个结点的时间复杂度是 O(logn)，所以这里查找某个数据应该插入的位置，方法也是类似的，时间复杂度也是 O(logn)。插入操作流程如下图所示。

![](https://upload-images.jianshu.io/upload_images/16911112-8140dc26dc36f10a.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

* 如果这个结点在索引中也有出现，我们除了要删除原始链表中的结点，还要删除索引中的。因为单链表中的删除操作需要拿到要删除结点的前驱结点，然后通过指针操作完成删除。所以在查找要删除的结点的时候，一定要获取前驱结点。当然，如果我们用的是双向链表，就不需要考虑这个问题了。

### 2.3 索引更新
&#8195; 当我们不停地往跳表中插入数据时，如果我们不更新索引，就有可能出现某 2 个索引结点之间数据非常多的情况。极端情况下，跳表还会退化成单链表，如下图所示。

![](https://upload-images.jianshu.io/upload_images/16911112-312d59458d031e42.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

&#8195; 作为一种动态数据结构，我们需要某种手段来维护索引与原始链表大小之间的平衡，也就是说，如果链表中结点多了，索引结点就相应地增加一些，避免复杂度退化，以及查找、插入、删除操作性能下降。

&#8195; 当我们往跳表中插入数据的时候，我们可以选择同时将这个数据插入到部分索引层中。我们通过一个随机函数，来决定将这个结点插入到哪几级索引中，比如随机函数生成了值 K，那我们就将这个结点添加到第一级到第 K 级这 K 级索引中，如下图所示。

![](https://upload-images.jianshu.io/upload_images/16911112-08dfa86a0419fd2d.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

&#8195; 随机函数的选择很有讲究，从概率上来讲，能够保证跳表的索引大小和数据大小平衡性，不至于性能过度退化。

## 3. 代码实现

```python
import random


class SkipListNode(object):
    def __init__(self, val, high=1):
        # 节点存储的值
        self.data = val
        # 节点对应索引层的深度
        self.deeps = [None] * high


class SkipList(object):
    """
        跳表的一种实现方法。
        跳表中储存的是正整数，并且储存的是不重复的。
    """

    def __init__(self):
        # 索引层的最大深度
        self.__MAX_LEVEL = 16
        # 跳表的高度
        self._high = 1
        # 每一索引层的首节点, 默认值为None
        self._head = SkipListNode(None, self.__MAX_LEVEL)

    def find(self, val):
        cur = self._head
        # 从索引的顶层, 逐层定位要查找的值
        # 索引层上下是对应的, 下层的起点是上一个索引层中小于插入值的最大值对应的节点
        for i in range(self._high - 1, -1, -1):
            # 同一索引层内, 查找小于插入值的最大值对应的节点
            while cur.deeps[i] and cur.deeps[i].data < val:
                cur = cur.deeps[i]

        if cur.deeps[0] and cur.deeps[0].data == val:
            return cur.deeps[0]
        return None

    def insert(self, val):
        '''
        新增时, 通过随机函数获取要更新的索引层数,
        要对低于给定高度的索引层添加新结点的指针
        '''
        high = self.randomLevel()
        if self._high < high:
            self._high = high
        # 申请新结点
        newNode = SkipListNode(val, high)
        # cache用来缓存对应索引层中小于插入值的最大节点
        cache = [self._head] * high
        cur = self._head

        # 在低于随机高度的每一个索引层寻找小于插入值的节点
        for i in range(high - 1, -1, -1):
            # 每个索引层内寻找小于带插入值的节点
            # ! 索引层上下是对应的, 下层的起点是上一个索引层中小于插入值的最大值对应的节点
            while cur.deeps[i] and cur.deeps[i].data < val:
                cur = cur.deeps[i]
            cache[i] = cur

        # 在小于高度的每个索引层中插入新结点
        for i in range(high):
            # new.next = prev.next \ prev.next = new.next
            newNode.deeps[i] = cache[i].deeps[i]
            cache[i].deeps[i] = newNode

    def delete(self, val):
        '''
        删除时, 要将每个索引层中对应的节点都删掉
        '''
        # cache用来缓存对应索引层中小于插入值的最大节点
        cache = [None] * self._high
        cur = self._head
        # 缓存每一个索引层定位小于插入值的节点
        for i in range(self._high - 1, -1, -1):
            while cur.deeps[i] and cur.deeps[i].data < val:
                cur = cur.deeps[i]
            cache[i] = cur
        # 如果给定的值存在, 更新索引层中对应的节点
        if cur.deeps[0] and cur.deeps[0].data == val:
            for i in range(self._high):
                if cache[i].deeps[i] and cache[i].deeps[i].data == val:
                    cache[i].deeps[i] = cache[i].deeps[i].deeps[i]

    def randomLevel(self, p=0.25):
        '''
        #define ZSKIPLIST_P 0.25      /* Skiplist P = 1/4 */
        https://github.com/antirez/redis/blob/unstable/src/t_zset.c
        '''
        high = 1
        for _ in range(self.__MAX_LEVEL - 1):
            if random.random() < p:
                high += 1
        return high

    def __repr__(self):
        vals = []
        p = self._head
        while p.deeps[0]:
            vals.append(str(p.deeps[0].data))
            p = p.deeps[0]
        return '->'.join(vals)

```
