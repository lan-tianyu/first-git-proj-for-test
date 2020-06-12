#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """[summary]
        prev标识当前隔一个元素及之前可以获取的最大值
        cur标识当前元素前一个及以前可以获取的最大值
        计算加上当前元素的最大值：
        temp = cur
        cur = max((prev+e), cur)
        prev = cur
        """
        prev = cur = 0
        for x in nums:
            prev, cur = cur, max(cur, prev+x)
        return cur

    # def rob(self, nums: List[int]) -> int:
    #     """[summary]
    #     动态规划方程：dp[n] = max(dp[n-1], dp[n-2] + num)
    #     """
    #     dp = [0, 0]
    #     for num in nums:
    #         dp.append(max(dp[-1], dp[-2] + num))
    #     return dp[-1]


s = Solution()
assert s.rob([1, 2, 3, 1]) == 4
assert s.rob([2, 1, 3, 1]) == 5
assert s.rob([2, 7, 9, 3, 1]) == 12
# @lc code=end
