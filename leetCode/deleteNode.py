# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        print(node, node.val)
        node.val = node.next.val
        node.next = node.next.next
        print(node, node.val)


class TestSoluntion:
    # def initListNode(self, node_list) -> ListNode:
    #     head = ListNode(0)
    #     p = head
    #     for e in node_list:
    #         p.next = ListNode(e)
    #         p = p.next
    #     return head.next

    def printListNode(self, head: ListNode):
        p = head
        list_val = []
        while p:
            list_val.append(str(p.val))
            p = p.next
        print('->'.join(list_val))

    def test_deleteNode(self):
        head = ListNode(1)
        n2 = ListNode(2)
        n3 = ListNode(3)
        n4 = ListNode(4)
        n5 = ListNode(5)
        n6 = ListNode(6)
        head.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5
        n5.next = n6
        self.printListNode(head)
        s = Solution()
        s.deleteNode(n3)
        self.printListNode(head)


if __name__ == '__main__':
    test = TestSoluntion()
    test.test_deleteNode()