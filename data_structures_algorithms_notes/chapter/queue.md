# 队列
# 一、简介
## 1. 定义
&#8195; 队列是一种“**先进先出”（FIFO**）的数据结构，和堆栈一样都是一种**有序线性表**的**抽象数据类型（ADT**）。与栈结构不同的是，队列的两端都"开口"，要求数据只能从一端进，从另一端出。

&#8195; 通常，称进数据的一端为 "队尾"，出数据的一端为 "队头"，数据元素进队列的过程称为 "入队"，出队列的过程称为 "出队"。不仅如此，队列中数据的进出要遵循 "先进先出" 的原则，即最先进队列的数据元素，同样要最先出队列。如下图所示：

![](https://upload-images.jianshu.io/upload_images/16911112-a1918df8c238cb2b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 2. 特性
* 1. 具有“先进先出”（FIFO）的特性。
* 2. 拥有加入与删除两种基本操作，而且使用 front 和 rear 两个指针来分别指向队列的前端与末尾。

## 3. 基本操作
* **create**：创建空队列。
* **add**：将新数据加入队列的末尾，返回新队列。
* **delete**：删除队列前端的数据，返回新队列。
* **front**：返回队列前端的值。
* **empty**：若队列为空，返回 true，否则返回 false。
* **size**：返回队列的长度。

## 4. 实现方式
队列存储结构的实现有以下两种方式：
* 顺序队列：在顺序表的基础上实现的队列结构；
* 链队列：在链表的基础上实现的队列结构；

两者的区别仅是顺序表和链表的区别，即在实际的物理空间中，数据集中存储的队列是顺序队列，分散存储的队列是链队列。

## 5. 实际应用
&#8195; 实际生活中，队列的应用随处可见，比如排队买 XXX、医院的挂号系统等，采用的都是队列的结构。

---

# 二、顺序队列
## 1. 简介
&#8195; 由于顺序队列的底层使用的是数组，因此需预先申请一块足够大的内存空间初始化顺序队列。除此之外，为了满足顺序队列中数据从队尾进，队头出且先进先出的要求，我们还需要定义两个指针（top 和 rear）分别用于指向顺序队列中的队头元素和队尾元素。

&#8195; 由于顺序队列初始状态没有存储任何元素，因此 top 指针和 rear 指针重合，且由于顺序队列底层实现靠的是数组，因此 top 和 rear 实际上是两个变量，它的值分别是队头元素和队尾元素所在数组位置的下标。

&#8195; 当有数据元素进队列时，对应的实现操作是将其存储在指针 rear 指向的数组位置，然后 rear+1；当需要队头元素出队时，仅需做 top+1 操作。

## 2. 参考程序

* 数组实现

```python
class QueueList:
    """顺序队列-数组实现"""

    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """往队列中添加元素"""
        print("从队列尾部添加元素 %s" % item)
        self.__list.append(item)  # 队列尾部添加元素

    def dequeue(self):
        """从队列中删除元素"""
        print("从队列头部删除元素 %s" % (self.__list.pop(0)))
        # self.__list.pop(0)  # 删除队列头部元素

    def isEmpty(self):
        """判空"""
        if self.__list == []:
            print("队列为空")
        else:
            print("队列不为空")

    def front(self):
        """返回队列前端元素"""
        if self.__list:
            print("队列头部元素为: %s" % self.__list[0])
            return self.__list[0]
        else:
            print("队列为空")
            return None

    def rear(self):
        """返回队列尾部元素"""
        if self.__list:
            print("队列尾部元素为: %s" % self.__list[-1])
            return self.__list[-1]
        else:
            print("队列为空")
            return None

    def size(self):
        """返回队列长度"""
        print("队列的元素个数为: %d" % len(self.__list))
        return len(self.__list)

```

* 链表实现

```python
class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None


class QueueLinks:
    """顺序队列-链表实现"""

    def __init__(self, node=None):
        self.__head = node
        self.__tail = None

    def enqueue(self, item):
        """往队列中添加元素"""
        node = Node(item)
        if self.__tail:
            self.__tail.next = node
        else:
            self.__head = node
        self.__tail = node

    def dequeue(self):
        """从队列中删除元素"""
        if self.__head:  # 判断是否为队头
            item = self.__head.item  # 获取队头数据
            self.__head = self.__head.next  # 将第二位数据设为队头
            if not self.__head: # 如果不是队头
                self.__tail = None
            return item

    def travel(self):
        """遍历元素"""
        items = []
        cur = self.__head
        while cur:
            items.append(cur.item)
            cur = cur.next
        return items

```

## 3. 存在的问题
整个顺序队列在数据不断地进队出队过程中，在顺序表中的位置不断后移。顺序队列整体后移造成的影响是：
1. 顺序队列之前的数组存储空间将无法再被使用，造成了空间浪费；
2. 如果顺序表申请的空间不足够大，则直接造成程序中数组 a 溢出，产生溢出错误。

---

# 三、双端队列
双端队列（deque）是指允许两端都可以进行入队和出队操作的队列，deque 是 “double ended queue” 的简称。那就说明元素可以从队头出队和入队，也可以从队尾出队和入队。

* 参考程序

```python
class DequeArray:
    """双端队列"""

    def __init__(self):
        self.__list = []

    def add_font(self, item):
        """队头添加元素"""
        print("队头添加元素 %s" % item)
        self.__list.insert(0, item)

    def add_rear(self, item):
        """队尾添加元素"""
        print("队尾添加元素 %s" % item)
        self.__list.append(item)

    def remove_font(self):
        """队头删除元素"""
        print("从队列头部删除元素 %s" % (self.__list.pop(0)))

    def remove_rear(self):
        """队尾删除元素"""
        print("从队列尾部删除元素 %s" % (self.__list.pop()))

    def is_empty(self):
        if self.__list == []:
            print("队列为空")
        else:
            print("队列不为空")

    def size(self):
        print("队列长度为 %d" % len(self.__list))

```


---

# 四、循环队列
&#8195; 循环队列，顾名思义，它长得像一个环。原本数组是有头有尾的，是一条直线。现在我们把首尾相连，扳成了一个环，如下图所示。

![2.jpg](https://upload-images.jianshu.io/upload_images/16911112-07b49649f28624b1.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

&#8195; 我们可以看到，图中这个队列的大小为 8，当前 head=4，tail=7。当有一个新的元素 a 入队时，我们放入下标为 7 的位置。但这个时候，我们并不把 tail 更新为 8，而是将其在环中后移一位，到下标为 0 的位置。当再有一个元素 b 入队时，我们将 b 放入下标为 0 的位置，然后 tail 加 1 更新为 1。所以，在 a，b 依次入队之后，循环队列中的元素就变成了下面的样子：

![3.jpg](https://upload-images.jianshu.io/upload_images/16911112-d7c75abb41b1aacf.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

通过这样的方法，我们成功避免了数据搬移操作。看起来不难理解，但是循环队列的代码实现难度要比前面讲的非循环队列难多了。要想写出没有 bug 的循环队列的实现代码，最关键的是要确定好队空和队满的判定条件。


## 1. 数组实现

* 参考程序：

```python

```


## 2. 链表实现：

* 参考程序：

```python

```

---

# 四、阻塞队列和并发队列
## 1. 阻塞队列
阻塞队列其实就是在队列基础上增加了阻塞操作。简单来说，就是在队列为空的时候，从队头取数据会被阻塞。因为此时还没有数据可取，直到队列中有了数据才能返回；如果队列已经满了，那么插入数据的操作就会被阻塞，直到队列中有空闲位置后再插入数据，然后再返回。



## 2. 并发队列
线程安全的队列我们叫作并发队列。最简单直接的实现方式是直接在 enqueue()、dequeue() 方法上加锁，但是锁粒度大并发度会比较低，同一时刻仅允许一个存或者取操作。实际上，基于数组的循环队列，利用 CAS 原子操作，可以实现非常高效的并发队列。这也是循环队列比链式队列应用更加广泛的原因。

---


# 五、题目



