#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, end = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[end] = nums2[j]
                j -= 1
            else:
                nums1[end] = nums1[i]
                i -= 1
            end -= 1
            print(nums1)
        nums1[:j+1] = nums2[:j+1]
        print('nums1', nums1)


s = Solution()
nums1 = [2, 4, 7, 0, 0, 0]
m = 0
nums2 = [0, 1, 3, 5, 6]
n = 5
s.merge(nums1, m, nums2, n)
# @lc code=end

