#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     """[summary]
    #     递归法：最终变成了左右子树是否是镜像
    #     1. left.val == right.val
    #     2. 继续递归，left.left 与 right.right;left.right 与right.left
    #     3. left.left.val == right.right.val
    #     4. left.right.val == right.left.val

    #     时间：O(N)，需要遍历整个链表
    #     空间：O(N)，递归空间，
    #     """
    #     if not root:
    #         return True
    #     return self._isSymmetric(root.left, root.right)

    # def _isSymmetric(self, left: TreeNode, right: TreeNode) -> bool:
    #     if not left and not right:
    #         return True
    #     if not left or not right:
    #         return False
    #     return left.val == right.val and self._isSymmetric(left.left, right.right) and self._isSymmetric(left.right, right.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        """[summary]
        迭代法
        1. 遍历层次：左子树、右子树
        2. 将遍历到的元素val放入队列，每次取出两个：
        如果两个都为空，则继续取出两个；
        两个中一个为空，则返回False；
        两个val不一致，则返回False
        两个val一致，则继续遍历，入队列
        3. 遍历层次：左子树左树、右子树右树
        3. 遍历层次：左子树右树、右子树左树
        4. 遍历层次相当于深度优先
        5. 循环出队列
        """
        if not root:
            return True
        queue = []
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            p = queue.pop()
            q = queue.pop()
            if not p and not q:
                continue
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            queue.append(p.left)
            queue.append(q.right)
            queue.append(p.right)
            queue.append(q.left)
        return True


s = Solution()
root = TreeNode(2)
n1 = TreeNode(3)
n2 = TreeNode(3)
n3 = TreeNode(4)
n4 = TreeNode(5)
n5 = TreeNode(4)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.right = n5
print(s.isSymmetric(root))

# @lc code=end
