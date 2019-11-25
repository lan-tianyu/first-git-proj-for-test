# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        来源：https://leetcode-cn.com/problems/add-two-numbers/
        按照这个题目，假设是顺序
        1. carry表示进位，要进位到一个节点val里边
        2. 存在一个链表，返回为空
        3. 需要考虑位数不对齐的场景，短的链表前面要补齐0
        3. 最后返回数据，如果第一位有进位，则全部返回，第一位没有进位，则返回下一个节点
        '''
        if not (l1 and l2):
            return None
        p1 = l1
        p2 = l2
        carry = 0 
        result = ListNode(0)
        cur = result
        while p1 or p2:
            s_val = 0
            if p1:
                s_val += int(p1.val)
                p1 = p1.next
            if p2:
                s_val += int(p2.val)
                p2 = p2.next
            carry = s_val // 10
            cur.val += carry
            cur.next = ListNode(s_val % 10)
            cur = cur.next
        return result if result.val == 1 else result.next

class TestSolution:
    def initListNode(self, num) -> ListNode :
        list_node = ListNode(0)
        cur = list_node
        for e in str(num):
             cur.next = ListNode(e)
             cur = cur.next
        print('initListNode')
        self.printListNode(list_node)
        print(len(ListNode))
        return list_node.next

    def printListNode(self, list_node):
        p = list_node
        list_num = []
        while p:
            list_num.append(str(p.val))
            p = p.next
        print('->'.join(list_num))
            
    def test_addTwoNumbers(self):
        s = Solution()
        l1 = self.initListNode(243)
        l2 = self.initListNode(564)
        result = s.addTwoNumbers(l1, l2)
        self.printListNode(result)
        l1 = self.initListNode(0)
        l2 = self.initListNode(12)
        result = s.addTwoNumbers(l1, l2)
        self.printListNode(result)
        l1 = self.initListNode(99)
        l2 = self.initListNode(1)
        result = s.addTwoNumbers(l1, l2) 
        self.printListNode(result)
        l1 = None
        l2 = self.initListNode(1)
        result = s.addTwoNumbers(l1, l2) 
        self.printListNode(result)


if __name__ == '__main__':
    test = TestSolution()
    test.test_addTwoNumbers()
