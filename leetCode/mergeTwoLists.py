# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p, q = l1, l2
        head = ListNode(0)
        cur = head
        while p and q:
            if p.val <= q.val:
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
        return head.next


class TestSolution:
    def initListNode(self, num) -> ListNode:
        list_node = ListNode(0)
        cur = list_node
        for e in str(num):
            cur.next = ListNode(e)
            cur = cur.next
        print('initListNode')
        self.printListNode(list_node)
        return list_node.next

    def printListNode(self, list_node):
        p = list_node
        list_num = []
        while p:
            list_num.append(str(p.val))
            p = p.next
        print('->'.join(list_num))

    def test_mergeTwoLists(self):
        solution = Solution()
        l1 = self.initListNode('124')
        l2 = self.initListNode('234')
        ll = solution.mergeTwoLists(l1, l2)
        self.printListNode(ll)
        ll = solution.mergeTwoLists(None, l2)
        self.printListNode(ll)
        ll = solution.mergeTwoLists(l1, None)
        self.printListNode(ll)


if __name__ == '__main__':
    test = TestSolution()
    test.test_mergeTwoLists()
