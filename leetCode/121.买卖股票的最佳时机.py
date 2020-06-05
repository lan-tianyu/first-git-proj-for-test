#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """[summary]
        1. beg 标识买入点，end标识卖出点
        2. 当beg点大于当前值，则end重置为当前点
        3. end为当前最高值
        """     
        


s = Solution()
assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert s.maxProfit([2, 8, 1, 5, 3, 6, 4]) == 6
assert s.maxProfit([4, 10, 1, 5, 3, 9, 4]) == 8
# @lc code=end
