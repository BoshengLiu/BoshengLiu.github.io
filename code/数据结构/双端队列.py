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


def deque_test(d):
    d.is_empty()
    print('-' * 30)

    for i in range(5):
        d.add_font(i)
        d.size()
        print('-' * 30)

        d.add_rear(i)
        d.size()
        print('-' * 30)

        if i >= 3:
            d.remove_font()
            d.size()
            print('-' * 30)

            d.remove_rear()
            d.size()
            print('-' * 30)


if __name__ == '__main__':
    d = DequeArray()
