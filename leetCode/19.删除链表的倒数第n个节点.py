#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        while p:
            q = p.next
            i = n
            while i > 0 and q:
                q = q.next
                i -= 1
                print('q----')
                printListNode(q)
            if q is None and i > 0:
                return p.next
            if q is None and i == 0:
                print('None')
                break
            p = p.next
            print('p----')
            printListNode(p)
        # printListNode(p)
        p.next = p.next.next
        return head


def printListNode(node):
    print('hello-------------')
    h = node
    node_list = []
    while h:
        node_list.append(str(h.val))
        h = h.next
    print('->'.join(node_list))


head = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)
head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
s = Solution()
# printListNode(s.removeNthFromEnd(head, 2))
# printListNode(s.removeNthFromEnd(head, 1))
# printListNode(s.removeNthFromEnd(head, 7))
printListNode(s.removeNthFromEnd(n7, 1))
# printListNode(s.removeNthFromEnd(n6, 2))


# @lc code=end
