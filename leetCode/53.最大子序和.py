#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """[summary]
        1. ans 记录当前最大的连续和，初始值为第一个元素，cur为最大连续子数组和
        2. cur大于0，则最新cur为cur+nums，cur<0，则cur重置为当前元素值
        """
        # if not nums:
        #     return 0
        cur = ans = -2 ** 31
        for i in range(0, len(nums)):
            cur = max(cur, 0) + nums[i]
            ans = max(ans, cur)
        return ans


s = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
assert s.maxSubArray(nums) == 6
nums = [-2, 1, -3, 4]
assert s.maxSubArray(nums) == 4
nums = [-2, 1]
assert s.maxSubArray(nums) == 1
# @lc code=end
