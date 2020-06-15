#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def isPalindrome(self, head: ListNode) -> bool:
    #     p, val_list = head, []
    #     while p:
    #         val_list.append(p.val)
    #         p = p.next
    #     i, j = 0, len(val_list) - 1
    #     while i < j:
    #         if val_list[i] != val_list[j]:
    #             return False
    #         i += 1
    #         j -= 1
    #     return True

    def isPalindrome(self, head: ListNode) -> bool:
        """
        1. 快慢指针找到链表中点，中点的位置很重要
        2. 反转后半部分，起点选中点位置还是中点后一个位置？？做题要谨慎
        3. 从头和中点开始遍历，依次比较值相等
        """
        if not head:
            return True
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        h, p, q = head, None, slow.next
        while q:
            cur, q = q, q.next
            cur.next = p
            p = cur
        while p:
            if h.val != p.val:
                return False
            p = p.next
            h = h.next
        return True


head = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(2)
n4 = ListNode(1)
head.next = n2
n2.next = n3
n3.next = n4
s = Solution()
assert s.isPalindrome(head) is True
n5 = ListNode(2)
n6 = ListNode(2)
n7 = ListNode(3)
n4.next = n5
n5.next = n6
n6.next = n7
assert s.isPalindrome(head) is False

# @lc code=end
