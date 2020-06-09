#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#


# @lc code=start
class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     """[summary]
    #     双指针
    #     """        
    #     m = len(s)
    #     i, j = 0, m - 1
    #     while i <= j:
    #         if not s[i].isalnum():
    #             i += 1
    #             continue
    #         if not s[j].isalnum():
    #             j -= 1
    #             continue
    #         if s[i].lower() == s[j].lower():
    #             i += 1
    #             j -= 1
    #         else:
    #             return False
    #     return True

    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s.lower()))
        return s == s[::-1]


s = Solution()
assert (s.isPalindrome('A man, a plan, a canal: Panama')) is True
assert (s.isPalindrome("race a car")) is False
assert (s.isPalindrome(" , ")) is True
# @lc code=end
