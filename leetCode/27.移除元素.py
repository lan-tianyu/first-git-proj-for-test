#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """[summary]
        1. 双指针法，从左往右，i为遍历元素的index
        2. 双指针法，从右往左，n标识当前 nums的长度，当i位置为val，则n自减1，i位置赋值n位置的数值
        """
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1
        return n


s = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
assert s.removeElement(nums, 2) == 5
assert 2 not in nums[:5]
# @lc code=end
