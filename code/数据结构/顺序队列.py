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
            if not self.__head:  # 如果不是队头
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


if __name__ == '__main__':
    ql = QueueList()
    q = QueueLinks()
