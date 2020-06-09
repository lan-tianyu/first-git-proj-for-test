#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
from typing import List


class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    #     """[summary]
    #     使用额外空间
    #     时间：O(N) + O(N)
    #     空间：O(N)
    #     """
    #     map = {}
    #     for e in nums:
    #         count = map.get(e, 0) + 1
    #         map[e] = count
    #     for k, v in map.items():
    #         if v == 1:
    #             return k

    def singleNumber(self, nums: List[int]) -> int:
        """[summary]
        不使用额外空间
        """
        ans = 0
        for e in nums:
            ans ^= e
        return ans


s = Solution()
assert (s.singleNumber([2, 2, 1])) == 1
assert (s.singleNumber([4, 1, 2, 1, 2])) == 4
# @lc code=end
