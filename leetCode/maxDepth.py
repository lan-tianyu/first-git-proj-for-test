# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def maxDepth(self, root: TreeNode) -> int:
    #     """递归方式
        
    #     Arguments:
    #         root {TreeNode} -- [description]
        
    #     Returns:
    #         int -- [description]
    #     """
    #     if not root:
    #         return 0
    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # def maxDepth(self, root: TreeNode):
    #     """[迭代方式，深度优先，DFS]
        
    #     Arguments:
    #         root {TreeNode} -- [description]
    #     """
    #     stack = []
    #     p = root
    #     depth = 0
    #     max_depth = 0
    #     while p or stack:
    #         while p:
    #             depth += 1
    #             stack.append(dict(node=p, dep=depth))
    #             p = p.left
    #         pop = stack.pop()
    #         p = pop.get('node')
    #         depth = pop.get('dep')
    #         p = p.right
    #         max_depth = max(depth, max_depth)

    #     return max_depth

    def maxDepth(self, root: TreeNode):
        """[迭代方式，广度优先，BFS]
        
        Arguments:
            root {TreeNode} -- [description]
        """
        if root is None:
            return 0
        stack = []
        p = root
        depth = 1
        max_depth = 1
        stack.append(dict(node=p, dep=depth))
        while stack:
            depth += 1
            if p.right:
                stack.append(dict(node=p.right, dep=depth))
            if p.left:
                stack.append(dict(node=p.left, dep=depth))
            pop = stack.pop()
            p = pop.get('node')
            depth = pop.get('dep')
            max_depth = max(depth, max_depth)
        return max_depth


class TestSolution:
    def test_maxDepth(self):
        root = TreeNode(3)
        n1 = TreeNode(9)
        n2 = TreeNode(20)
        n3 = TreeNode(15)
        n4 = TreeNode(7)
        root.left = n1
        root.right = n2
        n1.left = n3
        n3.right = n4
        s = Solution()
        assert s.maxDepth(root) == 4

        root1 = TreeNode(0)
        n2 = TreeNode(2)
        n3 = TreeNode(4)
        root1.left = n2
        root1.right = n3
        n4 = TreeNode(1)
        n2.left = n4
        n2.right = None
        n5 = TreeNode(3)
        n6 = TreeNode(-1)
        n3.left = n5
        n3.right = n6
        n7 = TreeNode(6)
        n8 = TreeNode(8)
        n5.right = n7
        n6.right = n8
        n9 = TreeNode(5)
        n10 = TreeNode(1)
        n4.left = n9
        n4.right = n10
        n11 = TreeNode(1)
        n10.right = n11
        assert s.maxDepth(root1) == 5


if __name__ == '__main__':
    test = TestSolution()
    test.test_maxDepth()
