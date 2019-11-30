from typing import List


class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     """[连续增值法]
    #     """
    #     profit = 0
    #     for i in range(1, len(prices)):
    #         profit += max(0, prices[i] - prices[i-1])
    #     return profit

    def maxProfit(self, prices: List[int]) -> int:
        """[连续增值法-一行代码法]
        """
        return sum(
            max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))

    # def maxProfit(self, prices: List[int]) -> int:
    #     """[峰谷法]
    #     """
    #     if not prices:
    #         return 0
    #     valley = prices[0]
    #     profit = 0
    #     for i in range(1, len(prices)-1):
    #         if prices[i-1] <= prices[i] and prices[i] > prices[i+1]:
    #             profit += prices[i] - valley
    #             valley = prices[i]
    #         if prices[i-1] > prices[i] and prices[i] <= prices[i+1]:
    #             valley = prices[i]
    #     profit += max(0, prices[-1]-valley)
    #     return profit


class TestSolution:
    def test_maxProfit(self):
        solution = Solution()
        prices = [1, 2, 3, 4, 3, 6]
        assert (solution.maxProfit(prices)) == 6
        prices = [6, 5, 4, 3, 1, 2]
        assert (solution.maxProfit(prices)) == 1
        prices = [6, 5, 4, 3, 2]
        assert (solution.maxProfit(prices)) == 0


if __name__ == '__main__':
    test = TestSolution()
    test.test_maxProfit()
