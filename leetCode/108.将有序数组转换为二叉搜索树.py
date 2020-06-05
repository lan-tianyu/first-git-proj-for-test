#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """[summary]
        递归法，每次root的val取中间位置的元素
        下面两种方式都是可以的
        1. mid向左取整
        2. mid向右取整
        """
        def _buildBST(left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            # mid = left + (right - left + 1) // 2
            node = TreeNode(nums[mid])
            node.left = _buildBST(left, mid - 1)
            node.right = _buildBST(mid + 1, right)
            return node

        return _buildBST(0, len(nums) - 1)


s = Solution()
nums = [-10, -3, 0, 5, 9]
s.sortedArrayToBST(nums)
# @lc code=end
