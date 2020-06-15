#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def reverseList(self, head: ListNode) -> ListNode:
    #     """[summary]
    #     迭代法
    #     时间：O(n)，遍历了整个链表
    #     空间：O(1)
    #     """        
    #     p, q = head, None
    #     while p:
    #         cur, p = p, p.next
    #         cur.next = q
    #         q = cur
    #     return q
    
    def reverseList(self, head: ListNode) -> ListNode:
        """[summary]
        递归法
        时间：O(n)，遍历了整个链表
        空间：O(N)
        """
        if head is None or head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


head = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
head.next = n2 
n2.next = n3
s = Solution()
s.reverseList(head)

# @lc code=end

