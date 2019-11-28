from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self._sortedArrayToBST(nums, 0, len(nums)-1)

    def _sortedArrayToBST(self, nums, low, high) -> TreeNode:
        if low > high:
            return None
        mid = (low + high)//2
        root = TreeNode(nums[mid])
        root.left = self._sortedArrayToBST(nums, low, mid-1)
        root.right = self._sortedArrayToBST(nums, mid+1, high)
        return root
