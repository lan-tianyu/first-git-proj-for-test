#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            b, a = a + b, b
        return b


s = Solution()
assert s.climbStairs(3) == 3
assert s.climbStairs(4) == 5

# @lc code=end

