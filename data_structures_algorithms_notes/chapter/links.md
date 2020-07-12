# 链表
# 一、简介
## 1. 定义
&#8195; **链表（Linked List**）是由许多**相同数据类型的数据项按照特定顺序排列而成的线性表**。链表的各个数据项在计算机内存中的位置是**不连续且随机**存放的。链表是由节点组成，每个节点包含 data 以及 next。

## 2. 优点
&#8195; 数据的插入或删除都相当方便，有新的数据加入时就向系统申请一块内存空间，而数据被删除后，就可以把这块内存空间还给系统，加入和删除都不需要移动大量的数据。

## 3. 缺点
&#8195; 设计数据结构时比较麻烦，并且在查找数据时，必须按顺序查找到该数据为止。

## 4. 和数组的对比
* 对比数组，改善了插入与删除操作，适合频繁的写操作。
* 当不知道有多少个元素需要存放时，适合链表。

|操作|链表-时间复杂度|顺序表-时间复杂度|
|:---:|:---:|:---:|
|访问元素|O(n)|O(1)|
|在头部插入/删除|O(1)|O(n)|
|在尾部插入/删除|O(n)|O(1)|
|在中间插入/删除|O(n)|O(n)|

## 5. 时间复杂度
* 查询：O(n)
* 插入数据：平均 O(1)
* 删除数据：平均 O(1)

## 6. 注意
* 1. 链表只有表头有索引，所以查找数据时要从表头开始。
* 2. 链表是一种数据存储的方式。

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
        cur = self.__head
        print("链表元素为：", end="")
        while cur.next != None:
            print(cur.item, end=" ")
            cur = cur.next
        print(cur.item)

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


if __name__ == '__main__':
    single_links = SingleLinksList()

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
    '''定义节点'''
    def __init__(self, item):
        self.item = item  # 定义数据区
        self.next = None  # 定义链接区


class single_circle_links(object):
    def __init__(self, node=None):
        '''定义链表头部'''
        self.__head = node

    def is_empty(self):
        '''判断是否为空'''
        return self.__head == None

    def length(self): 
        '''链表长度'''
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1 
        while cur.next != self.__head: 
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历链表'''
        if self.is_empty():
            return 0
        cur = self.__head
        while cur.next != self.__head:
            print(cur.item, end=' ')
            cur = cur.next
        # 退出循环，cur指向尾节点，但是尾节点的元素未被打印
        print(cur.item)

    def add(self, item):
        '''头部添加元素'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
                # 退出循环，cur指向尾节点
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, item):
        '''尾部添加元素'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, pos, item):
        '''任意位置添加元素'''
        if pos <= 0:
            '''当pos在链表的左边'''
            self.add(item)
        elif pos > (self.length() - 1):
            '''当pos在链表的右边'''
            self.add(item)
        else:
            pre = self.__head  # 定义头
            count = 0  # 定义移动的量
            while count <= (pos - 1): 
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        '''删除节点'''
        if self.is_empty():
            return

        cur = self.__head  # 后一个节点
        pre = None  # 前一个节点
        while cur.next != self.__head:
            # 判断是否为该节点
            if cur.item == item:  
                # 头结点
                if cur == self.__head:  
                    # 查找尾节点
                    rear = self.__head  
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                # 中间节点
                else:  
                    pre.next = cur.next
                return
            else:
                pre = cur  # 前一个节点往后移
                cur = cur.next  # 后一个节点往后移
        # 尾节点
        if cur.item == item:
            # 当链表只有一个节点时
            if cur == self.__head:
                self.__head = None
            else:
                pre.next = cur.next

    def search(self, item):
        '''查找节点'''
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.item == item:
                return True
            else:
                cur = cur.next
                # 退出循环，cur指向尾节点
        if cur.item == item:
            return True
        return False


if __name__ == '__main__':
    links = single_circle_links()

```

---

# 四、双向链表
&#8195; 对比单链表，多了一个尾指针，即每个数据既有上一个数据的节点，也有下一个数据的节点

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

if __name__ == '__main__':
    links = Double_Links_list()

```

# 五、习题
## 1. 反转一个单链表
* input: 1->2->3->4->5->null
* output: 5->4->3->2->1->null

* 代码参考

```python
def reverseList(self,head):
    cur, prev = head, None    # cur为当前节点，prev为上一个节点
    while cur: 
        # 指向上一个的节点和指向下一个的节点交换，当前数据节点为变为下一个数据的及诶单
        cur.next, prev, cur = prev, cur, cur.next
    return prev

```

## 2. 链表交换两个相邻元素
* input: 1->2->3->4->5
* output: 2->1->4->3->5

* 代码参考

```python
def swapPairs(self, head):  # 传入头指针
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next

```

## 3. 判断链表是否有环
给定一个链表，判断链表是否有环
* 三种方法：
    * 一直遍历节点，查找到 null 为止，给个截止时间 0.5s~1s，超出时间范围则表明链表没有环。
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
