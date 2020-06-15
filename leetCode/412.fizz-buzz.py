#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
from typing import List


class Solution:
    # def fizzBuzz(self, n: int) -> List[str]:
    #     s_list = []
    #     for x in range(1, n + 1):
    #         if x % 15 == 0:
    #             s_list.append("FizzBuzz")
    #         elif x % 3 == 0:
    #             s_list.append("Fizz")
    #         elif x % 5 == 0:
    #             s_list.append("Buzz")
    #         else:
    #             s_list.append(str(x))
    #     return s_list

    def fizzBuzz(self, n: int) -> List[str]:
        return [
            'Fizz' * (x % 3 == 0) + 'Buzz' * (x % 5 == 0) or str(x)
            for x in range(1, n + 1)
        ]


s = Solution()
print(s.fizzBuzz(15))
# @lc code=end
