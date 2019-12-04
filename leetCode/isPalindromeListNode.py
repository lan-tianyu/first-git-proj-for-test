# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """[快慢双指针+前半段指针倒序]
        1. slow/fast 快慢双指针，让slow指针遍历到后半段第一个node、
        2. 遍历的同时，设置一个指针，可以倒序遍历前半段指针
        3. 注意奇数链、偶数链 边界处理
        """
        prev = None
        slow, fast = head, head
        while fast and fast.next:
            tmp = prev
            prev = slow
            slow = slow.next
            fast = fast.next.next  # 注意这里的顺序，fast指向head的时候，prev也指向head。所以fast要先走
            prev.next = tmp
        if fast:
            slow = slow.next  # 当fast指向最后一个node，机奇数链
        while slow:
            if slow.val != prev.val:
                return False
            slow = slow.next
            prev = prev.next
        return True


class TestSoluntion:
    def initListNode(self, node_list) -> ListNode:
        head = ListNode(0)
        p = head
        for e in node_list:
            p.next = ListNode(e)
            p = p.next
        return head.next

    def printListNode(self, head: ListNode):
        p = head
        list_val = []
        while p:
            list_val.append(str(p.val))
            p = p.next
        print('->'.join(list_val))

    def test_isPalindrome(self):
        solution = Solution()
        head = self.initListNode('12321')
        assert solution.isPalindrome(head) is True
        head = self.initListNode('123321')
        assert solution.isPalindrome(head) is True
        head = self.initListNode('1234324')
        assert solution.isPalindrome(head) is False


if __name__ == '__main__':
    test = TestSoluntion()
    test.test_isPalindrome()
