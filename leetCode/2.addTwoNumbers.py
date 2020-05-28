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
        1. 同时遍历两个链表，新链表存放和
        2. 和大于等于10，使用进位s//10，值存储s%10
        3. 当其中一个到了末尾，则需要看是否有进位，如果有进位要继续做加和，不能直接指向未遍历完的链表。
        
        ------------
        这样会写出两个循环，现在简化成一个循环
        1. 新链表存放和，t表示进位，初始进位为0，同时遍历两个链表
        2. 只要链接没有遍历完就可以继续进行加和
        3. 当最后还有进位，注意最后一个进位
        """
        p, q = l1, l2
        result = ListNode(0)
        cur = result
        t = 0
        while p or q:
            if p:
                t += p.val
                p = p.next
            if q:
                t += q.val
                q = q.next
            cur.next = ListNode(t % 10)
            cur = cur.next
            t = t // 10
        if t:
            cur.next = ListNode(t)
        return result.next


def printListNode(node):
    p = node
    s = []
    while p:
        s.append(str(p.val))
        p = p.next
    print('->'.join(s))
    print('-' * 30)


s = Solution()
n1 = ListNode(2)
n2 = ListNode(4)
n3 = ListNode(3)
Node1 = n1
n1.next = n2
n2.next = n3

n11 = ListNode(5)
n21 = ListNode(6)
n31 = ListNode(4)
Node2 = n11
n11.next = n21
n21.next = n31

printListNode(s.addTwoNumbers(Node1, Node2))

n1 = ListNode(2)
n2 = ListNode(4)
n3 = ListNode(3)
Node1 = n1
n1.next = n2
n2.next = n3

n11 = ListNode(5)
n21 = ListNode(6)
n31 = ListNode(7)
Node2 = n11
n11.next = n21
n21.next = n31

printListNode(s.addTwoNumbers(Node1, Node2))

n1 = ListNode(9)
# n2 = ListNode(4)
# n3 = ListNode(3)
Node1 = n1
# n1.next = n2
# n2.next = n3

n11 = ListNode(6)
n21 = ListNode(9)
# n31 = ListNode(7)
Node2 = n11
n11.next = n21
# n21.next = n31

printListNode(s.addTwoNumbers(Node1, Node2))

n1 = ListNode(9)
n2 = ListNode(4)
# n3 = ListNode(3)
Node1 = n1
n1.next = n2
# n2.next = n3

n11 = ListNode(6)
# n21 = ListNode(9)
# n31 = ListNode(7)
Node2 = n11
# n11.next = n21
# n21.next = n31

printListNode(s.addTwoNumbers(Node1, Node2))

# @lc code=end
