# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    #     """[双指针法]
    #     p、q分别指向两个指针头部headA、headB，遍历一次
    #     1. 假设p、q长度相等，中间就找到相同的节点，直接返回
    #     2. 假设p、q长度相等，遍历一遍后没找到相同的节点，返回None
    #     3. 假设p、q长度不等，q先到最后，设置q为headA，继续向后遍历，直到p结束，设置p为headB，此时p、q相差的长度补齐了，继续遍历，直到找到相同节点或者到结束返回None
    #     4. 假设p、q长度不等，p先到最后，设置p为headB，继续向后遍历，直到q结束，设置p为headA，此时p、q相差的长度补齐了，继续遍历，直到找到相同节点或者到结束返回None
    #     """
    #     p = headA
    #     q = headB
    #     while p and q:
    #         if p == q:
    #             return p
    #         p = p.next
    #         q = q.next
    #     if p:
    #         q = headA
    #         while p:
    #             p = p.next
    #             q = q.next
    #         p = headB
    #         while p and q:
    #             if p == q:
    #                 return p
    #             p = p.next
    #             q = q.next
    #     if q:
    #         p = headB
    #         while q:
    #             p = p.next
    #             q = q.next
    #         q = headA
    #         while p and q:
    #             if p == q:
    #                 return p
    #             p = p.next
    #             q = q.next
    #     return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """[双指针法--简化]
        """
        p = headA
        q = headB
        if not p or not q:
            return None
        r = 0  # p或者q 指向了下一个循环
        while p != q and r <= 2:
            if p.next:
                p = p.next
            else:
                p = headB
                r += 1
            if q.next:
                q = q.next
            else:
                q = headA
                r += 1
            print(p, q, r)
        return p if p == q else None


class TestSolution:
    def initListNode(self, node_list) -> ListNode:
        head = ListNode(0)
        p = head
        for e in node_list:
            p.next = ListNode(e)
            p = p.next
        self.printListNode(head.next)
        return head.next

    def printListNode(self, head: ListNode):
        p = head
        list_val = []
        while p:
            list_val.append(str(p.val))
            p = p.next
        print('->'.join(list_val))

    def test_getIntersectionNode(self):
        s = Solution()
        headA = self.initListNode([4, 1])
        headB = self.initListNode([5, 0, 1])
        headC = self.initListNode([8, 4, 5])
        headA.next = headC
        headB.next = headC
        a = s.getIntersectionNode(headA, headB)
        self.printListNode(a)
        assert a == headC
        b = s.getIntersectionNode(headB, headC)
        self.printListNode(b)
        assert b == headC
        headA = self.initListNode([4, 1])
        headB = self.initListNode([5, 0, 1])
        headC = self.initListNode([1])
        assert s.getIntersectionNode(headA, headB) is None
        assert s.getIntersectionNode(headC, headC) == headC


if __name__ == '__main__':
    test = TestSolution()
    test.test_getIntersectionNode()