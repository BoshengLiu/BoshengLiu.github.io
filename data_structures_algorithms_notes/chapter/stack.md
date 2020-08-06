# 堆栈
# 一、简介
## 1. 定义
&#8195; **栈（Stack**）是一组相同数据类型的组合，具有“**后进先出”（LIFO**）的特性，所有的操作均在栈顶结构的顶端进行。因此，我们可以给栈下一个定义，即栈**是一种只能从表的一端存取数据且遵循 "先进后出" 原则的线性存储结构**。

## 2. 特性
* 1. 栈只能从表的一端存取数据，另一端是封闭的，只能从栈顶的顶端存取数据。

* 2. 数据的存取符合“后进先出”（LIFO）的原则。在栈中，无论是存数据还是取数据，都必须遵循"先进后出"的原则，即最先进栈的元素最后出栈。

* 通常，栈的开口端被称为栈顶；相应地，封口端被称为栈底。

如下图所示：

![](https://upload-images.jianshu.io/upload_images/16911112-3a72decf1e117ac9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 3. 基本运算
* **create**：创建一个空栈堆。
* **push**：把数据压入堆栈顶端，并返回新栈堆。
* **pop**：从堆栈顶端弹出数据，并返回新栈堆。
* *peek*：返回栈顶元素。
* **isEmpty**：判断堆栈是否为空堆栈，是则返回true，不是则返回false。
* **size**：返回栈的元素个数。

## 4. 进栈和出栈
基于栈结构的特点，在实际应用中，通常只会对栈执行以下两种操作：
1. 向栈中添加元素，此过程被称为"**进栈**"（**入栈**或**压栈**）；

2. 从栈中提取出指定元素，此过程被称为"**出栈**"（或**弹栈**）；

## 5. 栈的具体实现
栈是一种 "特殊" 的线性存储结构，因此栈的具体实现有以下两种方式：

1. 顺序栈：采用顺序存储结构可以模拟栈存储数据的特点，从而实现栈存储结构；

2. 链栈：采用链式存储结构实现栈结构；
    * 两种实现方式的区别，仅限于数据元素在实际物理空间上存放的相对位置，顺序栈底层采用的是数组，链栈底层采用的是链表。

## 6. 栈的应用
基于栈结构对数据存取采用 "先进后出" 原则的特点，它可以用于实现很多功能。

1. 例如，我们经常使用浏览器在各种网站上查找信息。
    * 假设先浏览的页面 A，然后关闭了页面 A 跳转到页面 B，随后又关闭页面 B 跳转到了页面 C。而此时，我们如果想重新回到页面 A，有两个选择：

        * 重新搜索找到页面 A；

        * 使用浏览器的"回退"功能。浏览器会先回退到页面 B，而后再回退到页面 A。<br>
 
    * 浏览器 "回退" 功能的实现，底层使用的就是栈存储结构。当你关闭页面 A 时，浏览器会将页面 A 入栈；同样，当你关闭页面 B 时，浏览器也会将 B入栈。因此，当你执行回退操作时，才会首先看到的是页面 B，然后是页面 A，这是栈中数据依次出栈的效果。

2. 不仅如此，栈存储结构还可以帮我们检测代码中的括号匹配问题。
    * 多数编程语言都会用到括号（小括号、中括号和大括号），括号的错误使用（通常是丢右括号）会导致程序编译错误，而很多开发工具中都有检测代码是否有编辑错误的功能，其中就包含检测代码中的括号匹配问题，此功能的底层实现使用的就是栈结构。

3. 同时，栈结构还可以实现数值的进制转换功能。
    * 例如，编写程序实现从十进制数自动转换成二进制数，就可以使用栈存储结构来实现。

---

# 二、栈的实现
## 1. 顺序栈

* 参考程序如下：

```python
class Stack:
    """栈"""

    def __init__(self):
        """建立容器"""
        self.__list = []

    def isEmpty(self):
        """判断是否为空"""
        if self.__list == []:
            print("栈为空")
        else:
            print("栈不为空")

    def push(self, item):
        """压入元素"""
        print("压入元素 %s" % item)
        self.__list.append(item)

    def pop(self):
        """弹出元素"""
        print("弹出元素 %s" % self.__list.pop())
        # return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            print("栈顶元素为: %s" % self.__list[-1])
            return self.__list[-1]
        else:
            print("栈为空")
            return None

    def size(self):
        """返回栈的元素"""
        print("栈的元素个数为: %d" % len(self.__list))
        return len(self.__list)

```

## 2. 链表栈
* 参考程序如下：

```python
class Node:
    def __init__(self, node=None):
        self.item = node
        self.next = None


class LinksStack:
    """栈-链表实现"""

    def __init__(self, node=None):
        self.__top = node

    def push(self, item):
        """压栈"""
        self.__top = Node(item)
        self.__top.next = None

    def pop(self):
        """出栈"""
        if self.__top:
            item = self.__top.item  # 栈顶元素
            self.__top = self.__top.next
            return item

    def traverse(self):
        """遍历"""
        cur = self.__top
        links = []
        while cur:
            links.append(cur.item)
            cur = cur.next
        return links

```

---

# 三、题目
## 1. 

