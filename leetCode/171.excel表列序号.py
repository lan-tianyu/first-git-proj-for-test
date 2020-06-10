#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#


# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for c in s:
            ans = ans * 26 + ord(c) - ord('A') + 1
        return ans

s = Solution()
assert s.titleToNumber('A') == 1
assert s.titleToNumber('AB') == 28

# @lc code=end
