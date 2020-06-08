#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
from typing import List


class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     """[summary]
    #     1. beg 标识买入点，end标识卖出点
    #     2. 当beg点大于当前值，则end重置为当前点
    #     3. end为当前最高值
    #     """
    #     beg, end, profit = 0, 0, 0
    #     for i in range(1, len(prices)):
    #         if prices[beg] > prices[i]:
    #             beg = i
    #             end = i
    #         elif prices[i] > prices[end]:
    #             end = i
    #         profit = max(profit, prices[end] - prices[beg])
    #     return profit

    def maxProfit(self, prices: List[int]) -> int:
        """[summary]
        1. min_price 最小股票价格，max_price 最高利润
        2. min_price 永远是最小的
        3. max_price 
        """
        min_price, max_price = 2 ** 31 - 1, 0
        for price in prices:
            min_price = min(price, min_price)
            max_price = max(max_price, price-min_price) 
        return max_price


s = Solution()
assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert s.maxProfit([2, 8, 1, 5, 3, 6, 4]) == 6
assert s.maxProfit([4, 10, 1, 5, 1, 9, 4]) == 8
# @lc code=end
