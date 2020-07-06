# 定义双向链表，对单链表进行判断，查看链表长度，遍历整个链表，在链表头部添加元素，
# 在链表尾部添加元素，在指定位置添加元素，删除节点，查找节点等操作
class Node(object):     #定义一个节点
    def __init__(self,item):
        self.item = item
        self.next = None
        self.prev = None

class Double_Links_list(object):    #定义一个双向链表
    def __init__(self,node = None):
        self.__head = node

    def is_empty(self): #判断是否为空
        return self.__head == None

    def length(self):   #链表长度
        cur = self.__head   #用来移动遍历节点
        count = 0   #节点数
        while cur != None:  #判断条件
            count += 1
            cur = cur.next
        return count

    def travel(self):   #遍历链表
        cur = self.__head  # 用来移动遍历节点
        while cur != None:  # 判断条件
            print(cur.item,end=' ')
            cur = cur.next
        print(' ')

    def add(self,item): #头部添加元素
        node = Node(item)
        node.next = self.__head
        #self.__head.prev = node
        self.__head = node
        node.next.prev = node

    def append(self,item):  #尾部添加元素,item指具体的数据
        node = Node(item)   #先创建一个节点
        if self.is_empty(): #判断是否为空
            self.__head = node
        else:
            cur = self.__head   #遍历节点
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self,pos,item):  #任意位置添加元素，pos的起始位置为0，若插在a、b之间
        if pos <= 0:    #当pos在链表的左边
            self.add(item)
        elif pos > (self.length()-1):   #当pos在链表的右边
            self.add(item)
        else:
            cur = self.__head
            count = 0   #定义移动的量
            while count < pos:     #当移动a节点之前的节点时，移动的量加1，节点往后移动1位
                count += 1
                cur = cur.next
            node = Node(item)  # 插入元素
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self,item):  #删除节点
        cur = self.__head   #后一个节点
        while cur != None:
            if cur.item == item: #判断是否为节点
                if cur == self.__head:  #判断是否为头结点
                    self.__head = cur.next
                    cur.next.prev = None
                else:
                    cur.prev.next = cur.next  #让a节点next指向c节点prev
                    cur.next.prev = cur.prev  #让c节点prev指向a节点next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next  #后一个节点往后移

    def search(self,item):   #查找节点
        cur = self.__head
        while cur != None: #在链表没遍历之前，执行下面的程序
            if cur.item == item:  #判断节点中是否有item存在
                return True
            else:
                cur = cur.next
        return False

if __name__ == '__main__':
    links = Double_Links_list()
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
    links.insert(2, 9)  # 6 8 9 1 2 3 4 5
    links.travel()

    links.remove(8)  # 6 9 1 2 3 4 5
    links.travel()
    links.remove(9)  # 6 1 2 3 4 5
    links.travel()
    links.remove(6)  # 1 2 3 4 5
    links.travel()
