#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#


# @lc code=start
class Solution:
    # def isHappy(self, n: int) -> bool:
    #     loop_list = [2, 4, 16, 37, 58, 89, 145, 42, 20]
    #     s = n
    #     while s != 1:
    #         n, s = s, 0
    #         while n:
    #             n, x = divmod(n, 10)
    #             s += x ** 2
    #         if s in loop_list:
    #             return False
    #     return True

    # def isHappy(self, n: int) -> bool:
    #     loop_set = set()
    #     while n != 1:
    #         s = 0
    #         while n:
    #             n, x = divmod(n, 10)
    #             s += x ** 2
    #         n = s
    #         if n not in loop_set:
    #             loop_set.add(n)
    #         else:
    #             return False
    #     return True


s = Solution()
assert s.isHappy(19) is True
assert s.isHappy(2) is False
# @lc code=end
