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
                        while cur.next != self.__head:
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


def LinksListTest(links):
    """链表测试模块"""
    print("初始化...")
    print('-' * 30)

    # 判空、查看链表长度、遍历
    result = links.is_empty()
    if result == True:
        print("链表为空")
    print("链表长度为: %d" % links.length())
    links.travel()
    print('-' * 30)

    # 头部添加元素
    print("向头部添加元素...")
    for i in reversed(range(1, 5)):
        links.add(i)
        links.travel()
    print("链表长度为: %d" % links.length())
    print('-' * 30)

    # 尾部添加元素
    print("向尾部添加元素...")
    for i in range(5, 9):
        links.append(i)
        links.travel()
    print("链表长度为: %d" % links.length())
    print('-' * 30)

    # 中间位置插入元素
    for i, j in zip([4, 9], ['a', 'b']):
        links.insert(i, j)
        print("在链表为 %d 的位置插入元素 %s。" % (i, j))
        links.travel()
    print("链表长度为: %d" % links.length())
    print('-' * 30)

    # 查询指定元素是否存在
    for i in [1, 'c', 'a', 'b']:
        if links.search_from_elem(i) is True:
            print("元素 %s 存在链表中" % i)
        else:
            print("元素 %s 不存在链表中" % i)
    print('-' * 30)

    # 查询指定位置的元素
    for i in [-1, 0, 1, 9, 10]:
        result = links.search_from_pos(i)
        if result is False:
            print("链表 %d 位置的元素不存在" % i)
        else:
            print("链表 %d 位置的元素为 %s" % (i, result))
    print('-' * 30)

    # 删除指定元素
    links.travel()
    for i in [1, 'a', 'b', 8, 100]:
        links.remove_from_elem(i)
        print("删除链表中的元素 %s" % i)
        links.travel()
    print("链表长度为: %d" % links.length())
    print('-' * 30)

    # 删除指定位置的元素
    links.travel()
    for i in [0, 3, 7, 6, 10, -10]:
        links.remove_from_pos(i)
        print("删除链表位置为 %d 的元素" % i)
        links.travel()
    print("链表长度为: %d" % links.length())


if __name__ == '__main__':
    # 单向循环链表
    single_circle_links = SingleCircleLinks()
    LinksListTest(single_circle_links)
