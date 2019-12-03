# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """[快慢指针]
        快指针走两步，慢指针走一步，直到快指针与慢指针相等，则说明是环
        如果快指针为空，则不是环
        """
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


class TestSolution:
    def test_hasCycle(self):
        s = Solution()
        head = ListNode(0)
        n1 = ListNode(1)
        n2 = ListNode(2)
        n3 = ListNode(3)
        n4 = ListNode(4)
        head.next = n1
        n1.next = n2
        n2.next = n3
        n3.next = n4
        assert s.hasCycle(head) is False
        n4.next = n2
        assert s.hasCycle(head) is True
        n1.next = head
        assert s.hasCycle(head) is True
        head.next = None
        assert s.hasCycle(head) is False
        assert s.hasCycle(None) is False


if __name__ == '__main__':
    test = TestSolution()
    test.test_hasCycle()
