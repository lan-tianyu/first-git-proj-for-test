#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#


# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        s = str.strip()
        if not s:
            return 0
        if not s[0] in ['-', '+'] and not s[0].isdigit():
            return 0
        ans = 0
        sign = -1 if s[0] == '-' else 1
        i = 1 if s[0] in ['-', '+'] else 0
        while i < len(s):
            print(ans)
            if not s[i].isdigit():
                return ans
            ans = sign * (10 * ans + int(s[i]))
            ans = min(MAX_INT, ans) if sign == 1 else max(MIN_INT, ans)
            i += 1
        return ans


s = Solution()
assert s.myAtoi('words and 987') == 0
assert s.myAtoi('4193 with words') == 4193
assert s.myAtoi('   -42') == -42
assert s.myAtoi('-91283472332') == -2147483648
assert s.myAtoi('91283472332') == 2147483647
# @lc code=end
