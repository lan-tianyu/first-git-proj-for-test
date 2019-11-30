# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev  # 断链
            prev = cur  # 指向已经倒序的头
            cur = next  # 往后遍历
        return prev


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

    def test_reverseList(self):
        s = Solution()
        l1 = self.initListNode(1234557890)
        result = s.reverseList(l1)
        self.printListNode(result)
        l1 = self.initListNode(0)
        l2 = self.initListNode(12)
        result = s.reverseList(l1)
        self.printListNode(result)
        result = s.reverseList(l2)
        self.printListNode(result)
        l2 = self.initListNode("")
        result = s.reverseList(l2)
        self.printListNode(result)


if __name__ == '__main__':
    test = TestSolution()
    test.test_reverseList()