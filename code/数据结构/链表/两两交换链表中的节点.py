"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
"""


def node_list():
    """建立链表"""
    node = ListNode
    node.val = 1
    cur = node
    head = cur
    for i in range(2, 6):
        cur.next = node(i)
        cur = cur.next
    return head


def travel_links(head):
    """遍历链表"""
    while head != None:
        print(head.val, end=" ")
        head = head.next
    print(' ')


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def swapPairs(self, head):  # 迭代法
    #     pre, pre.next = self, head  # 在 head 添加一个空头 pre , 其中 self 指的是空头
    #     pre, pre.next = ListNode(-1), head  # 等同上一行
    #
    #     while pre.next and pre.next.next:  # 终止条件，当前节点和下一个节点不为空
    #         # 利用指针 a,b 和 pre.next 交换节点位置，交换两个元素的位置
    #         a = pre.next
    #         b = a.next
    #         pre.next, b.next, a.next = b, a, b.next
    #         pre = a  # 交换完指针后将 pre 向后移动两位，继续下两个节点位置的交换，直至终止循环
    #     return self.next  # 返回 self.next, 也就是 head

    def swapPairs(self, head):  # 递归方法
        if head is None or head.next is None:  # 终止条件，当前节点和下一个节点不为空
            return head
        a, b = head, head.next  # 用 a,b 指向前两个节点

        # 迭代过程:
        # 1 -> 2 -> 下一次迭代   ==>     2 -> 1 -> 下一次迭代
        # 2 -> 1 -> 3 -> 4 -> 下一次迭代   ==>     2 -> 1 -> 3 -> 4 -> 下一次迭代
        # 迭代直到终止条件

        # 开始迭代，a = 1, b = 2
        # 第一次迭代:
        # 1. b.next = a, 即 b 指向 a;
        # 2. a.next = 下一次迭代 b.next
        # 2——>1——>下一次迭代
        a.next = self.swapPairs(b.next)
        b.next = a
        return b


if __name__ == '__main__':
    node = node_list()
    travel_links(node)

    solute = Solution()
    swap_result = solute.swapPairs(node)
    travel_links(swap_result)
