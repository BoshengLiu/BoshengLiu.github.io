"""
给定一个有环链表，实现一个算法返回环路的开头节点。
有环链表的定义：在链表中某个节点的next元素指向在它前面出现过的节点，则表明该链表存在环路。

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。

进阶：
你是否可以不用额外空间解决此题？

三种方法：
1. 一直遍历节点，查找到 null 为止，给个截止时间 0.5s，超出时间范围则表明链表没有环。
2. 遍历节点，用 set 存放每个节点，判断节点是否在 set 内。时间复杂度 O(n)
3. 龟兔赛跑：从头开始，快指针走两步，慢指针走一步，判断两个指针是否相遇。时间复杂度 O(n)
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head):
        pass

    # 龟兔赛跑的方法
    def hasCycle(self, head):
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


if __name__ == '__main__':
    pass
