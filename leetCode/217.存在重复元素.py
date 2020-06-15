#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
from typing import List


class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     return len(set(nums)) != len(nums)

    def containsDuplicate(self, nums: List[int]) -> bool:
        map_nums = {}
        for e in nums:
            if map_nums.get(e, 0):
                return True
            map_nums[e] = 1
        return False


s = Solution()
assert s.containsDuplicate([1, 2, 3, 1]) is True
assert s.containsDuplicate([1, 2, 3, 4]) is False
# @lc code=end
