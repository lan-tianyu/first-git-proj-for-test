#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#


# @lc code=start
class Solution:
    # def isPowerOfThree(self, n: int) -> bool:
    #     if n <= 0:
    #         return False
    #     while n % 3 == 0:
    #         n = n // 3
    #     return n == 1

    def isPowerOfThree(self, n: int) -> bool:
        max_power = 3**19
        return n > 0 and max_power % n == 0


s = Solution()
assert s.isPowerOfThree(45) is False
assert s.isPowerOfThree(27) is True
assert s.isPowerOfThree(-3) is False
# @lc code=end
