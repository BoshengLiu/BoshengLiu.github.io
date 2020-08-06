# 链表
# 一、简介
## 1. 定义
&#8195; **链表（Linked List**）是一系列**存储数据的单元通过指针按照特定顺序排列而成的线性表**，链表的各个数据项在计算机内存中的位置是**不连续且随机**存放的。

* 每个单元至少有两个域，一个域用于数据元素的存储，另一个或两个域是指向其他单元的指针。这里具有一个数据域和多个指针域的存储单元通常称为节点（node）。

* 链表的第一个节点和最后一个节点，分别称为链表的头节点和尾节点。链表中每个节点的 next 引用都相当于一个指针，指向另一个节点，借助这些 next 引用，我们可以从链表的头节点移动到尾节点。

* 链表数据结构中主要包含单向链表、双向链表及循环链表。

## 2. 优点
&#8195; 数据的插入或删除都相当方便，有新的数据加入时就向系统申请一块内存空间，而数据被删除后，就可以把这块内存空间还给系统，加入和删除都不需要移动大量的数据。

## 3. 缺点
&#8195; 设计数据结构时比较麻烦，并且在查找数据时，必须按顺序查找到该数据为止。

## 4. 和顺序表的对比
* 对比顺序表，改善了插入与删除操作，适合频繁的写操作。
* 当事先难以确定有多少个元素时，适合链表。

|操作|链表-时间复杂度|顺序表-时间复杂度|
|:---:|:---:|:---:|
|访问元素|O(n)|O(1)|
|在头部插入/删除|O(1)|O(n)|
|在尾部插入/删除|O(n)|O(1)|
|在中间插入/删除|O(n)|O(n)|

## 5. 时间复杂度
* 查询：O(n)
* 插入数据：O(1)
* 删除数据：O(1)

## 6. 链表的应用
由于链表的特性，常用于组织检索较少，而删除、添加、遍历较多的数据。

1. 通讯录的使用
    * 这个大家应该比较熟悉吧，先说为什么要用链表吧，因为通讯录中的信息是不确定的，可增加，也可减少。

2. 文件系统
    * [*详情请参考-文件系统*](https://baike.baidu.com/item/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F)

---

# 二、单链表
## 1. 基本概念
&#8195; 一个单链表的节点由**数据字段**和**指针**两个元素所组成的，指针会指向下一个元素在内存中的地址。其中第一个节点为链表头指针。指向最后最后一个节点的指针为None，表示链表尾。

![](https://upload-images.jianshu.io/upload_images/16911112-5d3914e4a189695c.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 2. 参考程序

```python
class Node(object):
    """节点"""

    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinksList(object):
    """单向链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判空"""
        return self.__head is None

    def length(self):
        """查看链表长度"""
        cur = self.__head
        count = 0
        while cur != None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            print("链表为空")
        else:
            cur = self.__head
            print("链表元素为: ", end="")
            while cur != None:
                print(cur.item, end=" ")
                cur = cur.next
            print(' ')

    def add(self, elem):
        """头部添加元素"""
        node = Node(elem)
        node.next = self.__head
        self.__head = node

    def append(self, elem):
        """尾部添加元素"""
        node = Node(elem)
        cur = self.__head
        while cur.next != None:
            cur = cur.next
        cur.next = node
        node.next = None

    def insert(self, pos, elem):
        """从任意位置添加元素"""
        node = Node(elem)
        cur = self.__head
        if pos <= 0:
            self.add(elem)
        elif pos > (self.length() - 1):
            self.append(elem)
        else:
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def search_from_elem(self, elem):
        """查找指定元素是否存在"""
        cur = self.__head
        while cur != None:
            if cur.item != elem:
                cur = cur.next
            else:
                return True
        return False

    def search_from_pos(self, pos):
        """查找指定位置的元素"""
        if pos < 0:
            return False
        elif pos >= self.length():
            return False
        else:
            cur = self.__head
            count = 0
            while count != pos:
                count += 1
                cur = cur.next
            return cur.item

    def remove_from_elem(self, elem):
        """删除元素"""
        cur = self.__head
        pre = None
        while cur != None:  # 当节点是不为空时
            if cur.item == elem:  # 判断是否为查找的数据
                if cur == self.__head:  # 判断是否为头结点
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def remove_from_pos(self, pos):
        """删除指定位置的元素"""
        if pos < 0:
            return
        elif pos > self.length():
            return
        else:
            cur = self.__head
            count = 0
            pre = None
            while cur != None:  # 当节点是不为空时
                if count == pos:
                    if cur == self.__head:  # 判断是否为头结点
                        self.__head = cur.next
                    else:
                        pre.next = cur.next
                    break
                else:
                    count += 1
                    pre = cur
                    cur = cur.next

```
---

# 三、单向循环链表
## 1. 基本概念

&#8195; 在单链表的基础上，人们设计了一种“循环性”单向链表，称之为“单向循环链表”，相比于单向链表，单向循环链表的最大特点是“**尾结点指向头节点**”。

![](https://upload-images.jianshu.io/upload_images/16911112-5c18800d6bd0c999.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 2. 相对于单向链表的优势
&#8195; 对单向链表中任一个节点的访问都需要从头结点开始；而对单向循环链表从任意节点出发都能遍历整个列表，极大的增强了其灵活性。

## 3. 和单向链表的对比
### 3.1 判断是否为空
* 单向链表：如果头结点指向空，那么为空链表
* 单向循环链表：如果头结点指向自身，那么为空链表

### 3.2 判断是否为尾结点
* 单向链表：指向空的节点为尾结点
* 单向循环链表：指向头结点的节点为尾结点

## 4. 参考程序

```python
class Node(object):
    """节点"""

    def __init__(self, item):
        self.item = item
        self.next = None


class SingleCircleLinks(object):
    """单向循环链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判空"""
        return self.__head is None

    def length(self):
        """长度"""
        cur = self.__head
        count = 0
        while cur != None:
            if cur.next != self.__head:
                cur = cur.next
                count += 1
            else:
                count += 1
                break
        return count

    def travel(self):
        """遍历"""
        if self.is_empty():
            print("链表为空")
        else:
            cur = self.__head
            print("链表元素为:", end="")
            while cur.next != self.__head:
                print(cur.item, end=" ")
                cur = cur.next
            print(cur.item)

    def add(self, elem):
        """头部添加元素"""
        node = Node(elem)
        cur = self.__head
        if cur == None:
            self.__head = node
            node.next = self.__head
        else:
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, elem):
        """尾部添加元素"""
        node = Node(elem)
        cur = self.__head
        if cur == None:
            self.__head = node
            node.next = self.__head
        else:
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, pos, elem):
        """从任意位置添加元素"""
        if pos <= 0:
            self.add(elem)
        elif pos > (self.length() - 1):
            self.append(elem)
        else:
            node = Node(elem)
            cur = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def search_from_elem(self, elem):
        """查找元素"""
        cur = self.__head
        while cur != None:
            if cur.item == elem:
                return True
            else:
                cur = cur.next
                if cur == self.__head:
                    return False
        return False

    def search_from_pos(self, pos):
        """查找元素"""
        if pos < 0:
            return False
        elif pos >= self.length():
            return False
        else:
            cur = self.__head
            count = 0
            while count != pos:
                count += 1
                cur = cur.next
            return cur.item

    def remove_from_elem(self, elem):
        """删除指定元素"""
        cur = self.__head
        pre = None
        while cur != None:  # 当节点是不为空时
            if cur.item == elem:  # 判断是否为查找的数据
                if cur == self.__head:  # 判断是否为头结点
                    pre = cur
                    while cur.next != self.__head:  # 遍历节点
                        cur = cur.next
                    self.__head = pre.next
                    cur.next = self.__head
                elif cur.next == self.__head:  # 判断是否为尾结点
                    pre.next = self.__head
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
                if cur == self.__head:  # 遍历一遍后若不存在则退出循环
                    break

    def remove_from_pos(self, pos):
        """删除指定位置的元素"""
        if pos < 0:
            return
        elif pos >= self.length():
            return
        else:
            cur = self.__head
            count = 0
            pre = None
            while cur != None:  # 当节点是不为空时
                if count == pos:  # 判断是否为查找的位置
                    if cur == self.__head:  # 判断是否为头结点
                        pre = cur
                        while cur.next != self.__head:  # 遍历一遍节点
                            cur = cur.next
                        self.__head = pre.next
                        cur.next = pre.next
                    else:
                        pre.next = cur.next
                    break
                else:
                    count += 1
                    pre = cur
                    cur = cur.next

```

---

# 四、双向链表
&#8195; 对比单链表，每一个节点除了有下一个数据的索引外，还有上一个数据的索引，好处是双向链表可以从任意位置遍历前面的节点和后面的节点。

![](https://upload-images.jianshu.io/upload_images/16911112-2a8918aa37871fa6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 参考程序

```python
class Node(object):
    '''定义一个节点'''
    def __init__(self,item):
        self.item = item
        self.next = None
        self.prev = None

class Double_Links_list(object):
    '''定义一个双向链表'''
    def __init__(self,node = None):
        self.__head = node

    def is_empty(self):
        '''判断是否为空'''
        return self.__head == None

    def length(self):
        '''链表长度'''
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历链表'''
        cur = self.__head
        while cur != None:
            print(cur.item,end=' ')
            cur = cur.next
        print(' ')

    def add(self,item):
        '''头部添加元素'''
        node = Node(item)
        node.next = self.__head
        # self.__head.prev = node
        self.__head = node
        node.next.prev = node

    def append(self,item):
        '''尾部添加元素'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self,pos,item):
        '''任意位置添加元素'''
        if pos <= 0:
            '''当pos在链表的左边'''
            self.add(item)
        elif pos > (self.length()-1):
            '''当pos在链表的右边'''
            self.add(item)
        else:
            cur = self.__head
            count = 0
            while count < pos:     # 当移动a节点之前的节点时，移动的量加1，节点往后移动1位
                count += 1
                cur = cur.next
            node = Node(item)  # 插入元素
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self,item):
        '''删除节点'''
        cur = self.__head
        while cur != None:
            if cur.item == item: # 判断是否为节点
                if cur == self.__head:  # 判断链表是否只有一个结点
                    self.__head = cur.next
                    cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self,item):
        '''查找节点'''
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False

```

# 五、习题
## 1. 反转一个单链表
* input: 1->2->3->4->5->null
* output: 5->4->3->2->1->null

* 代码参考-迭代

```python
def reverseList(head):
    cur, prev = head, None
    while cur: 
        cur.next, prev, cur = prev, cur, cur.next
    return prev

```

* 代码参考-递归

```python
def reverseRecursive(self, head):
    """链表反转-递归"""
    if head is None or head.next is None:  # 递归结束条件 - 当前节点为空或者下一个节点为空
        return head
    cur = self.reverseRecursive(head.next)  # 递归 - 处理以 head.next 为头的链表

    """
    处理当前节点 head - 每一步迭代过程
                                            1 ——> 2 ——> 3 ——> 4 ——> 5 ——> null
    5.next = 4, 4.next = None,  :return 5   1 ——> 2 ——> 3 ——> 4 <——5
    4.next = 3, 3.next = None,  :return 5   1 ——> 2 ——> 3 <—— 4 <——5
    3.next = 2, 2.next = None,  :return 5   1 ——> 2 <—— 3 <—— 4 <—— 5
    2.next = 1, 1.next = None,  :return 5   null <—— 1 <—— 2 <—— 3 <—— 4 <—— 5
    """
    head.next.next = head
    head.next = None
    return cur
```

## 2. 链表交换两个相邻元素
* input: 1->2->3->4->5
* output: 2->1->4->3->5

* 代码参考-

```python
def swapPairs(self, head):  # 在 head 添加一个空头 pre , 其中 self 指的是空头
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next    # 返回 self.next, 也就是 head

```

## 3. 判断链表是否有环
给定一个链表，判断链表是否有环
* 三种方法：
    * 一直遍历节点，查找到 null 为止，给个截止时间 0.5s，超出时间范围则表明链表有环。
    * 遍历节点，用 set 存放每个节点，判断节点是否在 set 内。时间复杂度 O(n)
    * 龟兔赛跑：从头开始，快指针走两步，慢指针走一步，判断两个指针是否相遇。时间复杂度 O(n)
    
* 代码参考-龟兔赛跑的方法

```python
def hasCycle(self, head):
    fast = slow = head 
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

```
