# 定义单向循环链表，对单链表进行判断，查看链表长度，遍历整个链表，在链表头部添加元素，在链表尾部添加元素，在指定位置添加元素，删除节点，查找节点等操作
class Node(object):  # 定义节点
    def __init__(self, item):
        self.item = item  # 定义数据区
        self.next = None  # 定义链接区


class SingleCircleLinks(object):
    def __init__(self, node=None):  # 定义链表头部
        self.__head = node

    def is_empty(self):  # 判断是否为空
        return self.__head == None

    def length(self):  # 链表长度
        if self.is_empty():  # 判断链表是否为空
            return 0
        cur = self.__head  # 用来移动遍历节点
        count = 1  # 节点数
        while cur.next != self.__head:  # 判断条件
            count += 1
            cur = cur.next
        return count

    def travel(self):  # 遍历链表
        if self.is_empty():
            return 0
        cur = self.__head  # 用来移动遍历节点
        while cur.next != self.__head:  # 判断条件
            print(cur.item, end=' ')
            cur = cur.next
        # 退出循环，cur指向尾节点，但是尾节点的元素未被打印
        print(cur.item)

    def add(self, item):  # 头部添加元素
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head  # 退出循环，cur指向尾节点
            self.__head = node
            cur.next = node

    def append(self, item):  # 尾部添加元素,item指具体的数据
        node = Node(item)  # 先创建一个节点
        if self.is_empty():  # 判断是否为空
            self.__head = node
            node.next = node
        else:
            cur = self.__head  # 遍历节点
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, pos, item):  # 任意位置添加元素，pos的起始位置为0，若插在a、b之间
        if pos <= 0:  # 当pos在链表的左边
            self.add(item)
        elif pos > (self.length() - 1):  # 当pos在链表的右边
            self.add(item)
        else:
            pre = self.__head  # 定义头
            count = 0  # 定义移动的量
            while count <= (pos - 1):  # 当移动a节点之前的节点时，移动的量加1，节点往后移动1位
                count += 1
                pre = pre.next
            node = Node(item)  # 插入元素
            node.next = pre.next  # 插入的节点指向b节点
            pre.next = node  # a节点的next指向插入的节点

    def remove(self, item):  # 删除节点
        if self.is_empty():  # 链表为空
            return

        cur = self.__head  # 后一个节点
        pre = None  # 前一个节点
        while cur.next != self.__head:
            if cur.item == item:  # 判断是否为节点
                if cur == self.__head:  # 判断是否为头结点
                    rear = self.__head  # 查找尾节点
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:  # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur  # 前一个节点往后移
                cur = cur.next  # 后一个节点往后移
        if cur.item == item:  # cur指向尾节点
            if cur == self.__head:  # 链表只有一个节点
                self.__head = None
            else:
                pre.next = cur.next

    def search(self, item):  # 查找节点
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:  # 在链表没遍历之前，执行下面的程序
            if cur.item == item:  # 判断节点中是否有item存在
                return True
            else:
                cur = cur.next  # 退出循环，cur指向尾节点
        if cur.item == item:
            return True
        return False


if __name__ == '__main__':
    links = single_circle_links()
    print(links.is_empty())
    print(links.length())

    links.append(1)
    links.append(2)
    links.add(8)
    links.append(3)
    links.append(4)
    links.append(5)  # 8 1 2 3 4 5
    links.travel()
    links.insert(-1, 6)  # 6 8 1 2 3 4 5
    links.travel()
    links.insert(2, 9)  # 6 8 1 9 2 3 4 5
    links.travel()

    links.remove(8)  # 6 1 9 2 3 4 5
    links.travel()
    links.remove(9)  # 6 1 2 3 4 5
    links.travel()
    links.remove(6)  # 1 2 3 4 5
    links.travel()
