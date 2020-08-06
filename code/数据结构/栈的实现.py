class ListStack:
    """栈-数组实现"""

    def __init__(self):
        self.__list = []

    def isEmpty(self):
        """判空"""
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


class Node:
    def __init__(self, item=None):
        self.item = item
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


def stackTest(s):
    s.isEmpty()  # 判空
    print('-' * 30)

    for i in range(10):
        s.push(i)  # 入栈
        s.peek()  # 返回栈顶元素
        s.size()  # 返回栈的元素个数
        print('-' * 30)

    s.isEmpty()  # 判空

    for _ in range(5):
        s.pop()  # 压栈
        s.peek()  # 返回栈顶元素
        s.size()  # 返回栈的元素个数
        print('-' * 30)


if __name__ == '__main__':
    ls = ListStack()
    stackTest(ls)
