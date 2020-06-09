#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # def hasCycle(self, head: ListNode) -> bool:
    #     """[summary]
    #     快慢指针
    #     1. 注意head为空的场景，如果head为空，则返回False
    #     2. 慢指针每次走一步，快指针每次走两步。
    #     3. 如果是环，则相遇的时间复杂度是O(N) + O(N/2)
    #     4. 如果不是环，则时间复杂度是O(N)
    #     5. 快指针初始化为head 或者 head.next 结果是一样的，差别在于相遇的时间点，少了一步
    #     """
    #     if not head or not head.next:
    #         return False
    #     slow, fast = head, head.next
    #     while fast.next and fast.next.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #         if slow == fast:
    #             return True
    #     return False
    
    def hasCycle(self, head: ListNode) -> bool:
        """[summary]
        map存放每次遍历的node
        时间：O(N)
        空间：O(N)
        """
        map = {}
        p = head
        while p:
            if map.get(p):
                return True
            map[p] = 1
            p = p.next
        return False
        
# @lc code=end
