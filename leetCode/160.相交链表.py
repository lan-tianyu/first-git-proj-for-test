#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> ListNode:
        """[summary]
        1. p指向headA，q指向headB
        2. p q 同時向后遍历，当p遍历完q没有遍历完，则指向headB，q遍历完p没有遍历完指向headA。相当于p/q都遍历了headA+headB
        3. 如果中间相交了，则pq 相等；如果遍历完，还不相等，则说明不想交

        异常情况：
        1. p q 不想交，长度一致，则同时遍历到None
        2. p q 想交，长度一致，则一开始比较就可以返回中间节点
        3. p q 想交，长度不一致，则肯定是q为空时p不为空，p为空时q不为空
        时间O(N)
        空间O(1)
        """        
        p, q = headA, headB
        if not p or not q:
            return None
        while p or q:
            if p == q:
                return p
            # if p and not q:
            #     q = headA
            #     p = p.next
            # elif not p and q:
            #     p = headB
            #     q = q.next
            # else:
            #     p = p.next
            #     q = q.next
            p = p.next if p else headB
            q = q.next if q else headA
        return None


headA = ListNode(4)
headB = ListNode(5)
n1 = ListNode(1)
n2 = ListNode(8)
n3 = ListNode(4)
n4 = ListNode(5)
n5 = ListNode(0)
n6 = ListNode(1)
headA.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
headB.next = n5
n5.next = n1
# n6.next = n2
s = Solution()
assert s.getIntersectionNode(headA, headB) == n1

# @lc code=end
