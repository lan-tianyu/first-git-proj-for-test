# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     """[递归方式]
    #     """
    #     if not root:
    #         return False
    #     return self._isSymmetric(root.left, root.right)

    # def _isSymmetric(self, t1: TreeNode, t2: TreeNode) -> bool:
    #     # if t1 is None and t2 is None:
    #     #     return True
    #     # if t1 is None or t2 is None:
    #     #     return False
    #     if t1 is None or t2 is None:
    #         return t1 == t2
    #     return (t1.val == t2.val) and (self._isSymmetric(
    #         t1.left, t2.right)) and (self._isSymmetric(t1.right, t2.left))

    def isSymmetric(self, root: TreeNode) -> bool:
        """[迭代方式]
        """
        if root is None:
            return True
        stack = [root.right, root.left]
        while stack:
            t1 = stack.pop()
            t2 = stack.pop()
            print(t1, t2)
            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            stack.append(t2.left)
            stack.append(t1.right)
            stack.append(t2.right)
            stack.append(t1.left)
        return True


class TestSolution:
    def test_isSymmetric(self):
        s = Solution()
        root = TreeNode(1)
        n1 = TreeNode(2)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n4 = TreeNode(4)
        n5 = TreeNode(4)
        n6 = TreeNode(3)
        root.left = n1
        root.right = n2
        n1.left = n3
        n1.right = n4
        n2.left = n5
        n2.right = n6
        assert s.isSymmetric(root) is True
        n1.left = None
        n2.right = None 
        assert s.isSymmetric(root) is True
        n4.val = 5
        assert s.isSymmetric(root) is False
        n1.left = n3
        n1.right = None
        assert s.isSymmetric(root) is False


if __name__ == '__main__':
    test = TestSolution()
    test.test_isSymmetric()

