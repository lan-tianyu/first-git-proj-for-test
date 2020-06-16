#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """[summary]
        1. carry 标识进位，两个链表的val相加之后，再加carry，最后计算val、新的carry给下一轮计算
        2. 注意两个链表都遍历完，最后carry不为0，最后一个要进位
        3. 注意两个链表的长度不一定一样长
        4. head是接过链表的头，cur标识当前计算的节点
        """   
        carry = 0     
        head = cur = ListNode(0)
        p, q = l1, l2
        while p or q:
            if p:
                carry += p.val
                p = p.next
            if q:
                carry += q.val
                q = q.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
        if carry:
            cur.next = ListNode(carry % 10)
            cur = cur.next
        return head.next

        
# @lc code=end

