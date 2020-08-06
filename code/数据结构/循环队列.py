class CircleQueueArray:
    """循环队列-数组实现"""

    def __init__(self):
        self.__list = []

    def enqueue_font(self, item):
        self.__list.insert(0, item)

    def enqueue_rear(self, item):
        self.__list.append(item)

    def dequeue_font(self):
        self.__list.pop(0)

    def dequeue_rear(self):
        self.__list.pop()


class Node:
    def __init__(self, node=None):
        self.item = node
        self.next = None
        self.prev = None


class CircleQueueLinks:
    """循环队列-双向链表实现"""

    def __init__(self):
        self.__head = None
        self.__tail = None


if __name__ == '__main__':
    cqa = CircleQueueArray()
    cql = CircleQueueLinks()
