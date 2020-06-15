#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#


# @lc code=start
from typing import List


class Solution:
    # def reverseString(self, s: List[str]) -> None:
    #     """
    #     Do not return anything, modify s in-place instead.
    #     """
    #     i, j = 0, len(s)-1
    #     while i < j:
    #         s[i], s[j] = s[j], s[i]
    #         i += 1
    #         j -= 1

    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        

s = Solution()
# assert s.reverseString(["h", "e", "l", "l", "o"]) == ["o", "l", "l", "e", "h"]
# @lc code=end
