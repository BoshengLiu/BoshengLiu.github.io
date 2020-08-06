class Node(object):
    '''定义一个节点'''

    def __init__(self, item):
        self.item = item  # 数据
        self.next = None  # 下一个数据的指针
        self.prev = None  # 上一个数据的指针


class Double_Links_list(object):
    '''定义一个双向链表'''

    def __init__(self, node=None):
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
        print("链表的长度为 %d" % count)
        return count

    def travel(self):
        '''遍历链表'''
        cur = self.__head
        while cur != None:
            print(cur.item, end=' ')
            cur = cur.next
        print(' ')

    def add(self, item):
        '''头部添加元素'''
        node = Node(item)
        node.next = self.__head
        # self.__head.prev = node
        self.__head = node
        node.next.prev = node

    def append(self, item):
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

    def insert(self, pos, item):
        '''任意位置添加元素'''
        if pos <= 0:
            '''当pos在链表的左边'''
            self.add(item)
        elif pos > (self.length() - 1):
            '''当pos在链表的右边'''
            self.add(item)
        else:
            cur = self.__head
            count = 0
            while count < pos:  # 当移动a节点之前的节点时，移动的量加1，节点往后移动1位
                count += 1
                cur = cur.next
            node = Node(item)  # 插入元素
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        '''删除节点'''
        cur = self.__head
        while cur != None:
            if cur.item == item:  # 判断是否为节点
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

    def search(self, item):
        '''查找节点'''
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    double_links = Double_Links_list()
