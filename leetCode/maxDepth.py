# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def maxDepth(self, root: TreeNode) -> int:
    #     """[递归方式]
        
    #     Arguments:
    #         root {TreeNode} -- [description]
        
    #     Returns:
    #         int -- [description]
    #     """
    #     if root:
    #         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    #     return 0

    # def maxDepth(self, root: TreeNode) -> int:
    #     """[迭代方式，深度优先]
    #     左节点遍历完，遍历右节点
    #     遍历完的节点都放到stack里边了
    #     左节点遍历完，到右节点，不用加深度，进入下一个循环节点有判断depth+1
    #     注意每次depth变化，都要判断max_depth
        
    #     Arguments:
    #         root {TreeNode} -- [description]
        
    #     Returns:
    #         int -- [description]
    #     """
    #     stack = []
    #     p = root
    #     max_depth = 0
    #     depth = 0
    #     while stack or p:
    #         while p:
    #             depth += 1
    #             stack.append(dict(node=p, dep=depth))
    #             max_depth = max(depth, max_depth)
    #             p = p.left
    #         pop = stack.pop()
    #         p = pop.get('node')
    #         depth = pop.get('dep')
    #         p = p.right
    #     return max_depth

    def maxDepth(self, root: TreeNode) -> int:
        """[迭代方式，广度优先]
        遍历所有子节点，再往下遍历；左节点先出栈，先遍历左节点的下一个节点
        遍历完的节点都放到stack里边了
        左节点遍历完，到右节点，不用加深度，进入下一个循环节点有判断depth+1
        注意每次depth变化，都要判断max_depth
        
        Arguments:
            root {TreeNode} -- [description]
        
        Returns:
            int -- [description]
        """
        if not root:
            return 0
        stack = []
        depth = 1
        max_depth = 1
        p = root
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


class TestSoluntion:
    def test_maxDepth(self):
        root = TreeNode(3)
        n2 = TreeNode(9)
        n3 = TreeNode(20)
        root.left = n2
        root.right = n3
        n2.left = None
        n2.right = None
        n4 = TreeNode(15)
        n5 = TreeNode(7)
        n3.left = n4
        n3.right = n5
        n6 = TreeNode(21)
        n7 = TreeNode(19)
        n5.left = n6
        n6.right = n7
        print(Solution().maxDepth(root)) # 5
        print('---'*20)

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
        print(Solution().maxDepth(root1)) # 5


if __name__ == '__main__':
    test = TestSoluntion()
    test.test_maxDepth()