#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def maxDepth(self, root: TreeNode) -> int:
    #     """[summary]
    #     递归法：
    #     root的深度等于max(left深度, right深度) + 1
    #     递归终止条件：
    #     当前节点的左右节点都为空
    #     """
    #     if not root:
    #         return 0
    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # def maxDepth(self, root: TreeNode) -> int:
    #     """[summary]
    #     迭代法，按照BSF广度优先规则，将每层node放入队列
    #     1. 每次从队列左边取出一层所有node，如果node子节点不为空，则在队列尾部插入新节点
    #     2. 每遍历一层，depth+1
    #     """
    #     if not root:
    #         return 0
    #     depth = 0
    #     queue = collections.deque()
    #     queue.append(root)
    #     while queue:
    #         depth += 1
    #         len_queue = len(queue)
    #         for _ in range(len_queue):
    #             node = queue.popleft()
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.righ:
    #                 queue.append(node.right)
    #     return depth

    def maxDepth(self, root: TreeNode) -> int:
        """[summary]
        迭代法，按照DFS深度优先规则
        1. 遍历一个节点的左节点，直到左节点全部遍历完
        2. 遍历右节点
        3. 最大深度为depth，当前深度为cur_depth
        4. 每次队列增加一个元素，则cur_depth+1，pop一个元素，cur_depth-1
        """
        if not root:
            return 0
        depth = 0
        
        def _dfs(node, level):
            if not node:
                return None
            nonlocal depth
            depth = max(depth, level)
            _dfs(node.left, level + 1) 
            _dfs(node.right, level + 1) 
        
        _dfs(root, 1)
        return depth


s = Solution()
root = TreeNode(3)
n1 = TreeNode(9)
n2 = TreeNode(20)
n3 = TreeNode(15)
n4 = TreeNode(7)
n5 = TreeNode(6)
root.left = n1
root.right = n2
n2.left = n3
n2.right = n4
n4.right = n5
h = root
assert s.maxDepth(root) == 4
# @lc code=end
