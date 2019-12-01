# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def func(self):
        pass


class TestSoluntion:
    def initListNode(self, node_list) -> ListNode:
        head = ListNode(0) 
        p = head
        for e in node_list:
            p.next = ListNode(e)
            p = p.next
        return head.next

    # def init_TreeNode(self, node_list) -> TreeNode:
    #     if not node_list:
    #         return None
    #     head = TreeNode(node_list[0])
    #     left = head.left
    #     right = head.right
    #     count_l = 0
    #     count_r = 0
    #     len_node_list = len(node_list)
    #     for i in range(1, len_node_list-1):
            
    def printListNode(self, head: ListNode):
        p = head
        list_val = []
        while p:
            list_val.append(str(p.val))
            p = p.next
        print('->'.join(list_val))

    def test_initListNode(self):
        head = self.initListNode('1234567')
        self.printListNode(head)

    def test_func(self):
        s = Solution()
        s.func()


if __name__ == '__main__':
    test = TestSoluntion()
    test.test_initListNode()