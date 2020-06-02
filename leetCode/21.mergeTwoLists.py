#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        h = cur = ListNode(0)
        while p and q:
            if p.val < q.val:
                cur.next = ListNode(p.val)
                p = p.next
            else:
                cur.next = ListNode(q.val)
                q = q.next
            cur = cur.next
        if p:
            cur.next = p
        if q:
            cur.next = q
        return h.next


# @lc code=end
