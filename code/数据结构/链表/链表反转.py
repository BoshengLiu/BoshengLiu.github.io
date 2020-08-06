"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

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
    def reverseIterate(self, head):
        """链表反转-迭代"""
        # 代码最简洁-单指针
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev

        # 变量赋值写法-双指针
        # prev, cur = None, head
        # while cur:
        #     temp = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = temp
        # return prev

    # def reverseRecursive(self, head):
    #     """链表反转-递归"""
    #     if head is None or head.next is None:  # 递归结束条件 - 当前节点为空或者下一个节点为空
    #         return head
    #     cur = self.reverseRecursive(head.next)  # 递归 - 处理以 head.next 为头的链表
    #
    #     """
    #     处理当前节点 head - 每一步迭代过程
    #                                             1 ——> 2 ——> 3 ——> 4 ——> 5 ——> null
    #     5.next = 4, 4.next = None,  :return 5   1 ——> 2 ——> 3 ——> 4 <——5
    #     4.next = 3, 3.next = None,  :return 5   1 ——> 2 ——> 3 <—— 4 <——5
    #     3.next = 2, 2.next = None,  :return 5   1 ——> 2 <—— 3 <—— 4 <—— 5
    #     2.next = 1, 1.next = None,  :return 5   null <—— 1 <—— 2 <—— 3 <—— 4 <—— 5
    #     """
    #     head.next.next = head
    #     head.next = None
    #     return cur



if __name__ == '__main__':
    node = node_list()
    travel_links(node)

    solute = Solution()
    reverse_rec = solute.reverseIterate(node)  # 迭代法
    # reverse_rec = solute.reverseRecursive(node)  # 递归
    travel_links(reverse_rec)
