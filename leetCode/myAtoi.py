import re


class Solution:
    def myAtoi(self, str: str) -> int:
        pattern = r'^[\-\+]?\d+'
        str = str.strip(' ')
        m = re.match(pattern, str)
        if not str or not m:
            return 0
        sub_str = m.group(0)
        ans = 0
        max_int = 2**31
        limit = max_int // 10  # 使用整除，使用/有小数点
        is_negative = sub_str[0] == '-'
        prefix = -1 if is_negative else 1
        limit_last = 8 if is_negative else 7
        limit_ans = -max_int if is_negative else max_int - 1
        if sub_str[0] in '-+':
            for e in sub_str[1:]:
                p = int(e)
                if ans > limit or ans == limit and p > limit_last:
                    return limit_ans
                ans = ans * 10 + int(e)
        else:
            for e in sub_str:
                p = int(e)
                if ans > limit or ans == limit and p > limit_last:
                    return max_int - 1
                ans = ans * 10 + int(e)
        return ans * prefix


solution = Solution()
assert solution.myAtoi('   +1 ') == 1
assert solution.myAtoi('   -a42 ') == 0
assert solution.myAtoi('   - 42 ') == 0
assert solution.myAtoi('   + 42 ') == 0
assert solution.myAtoi('   -42 ') == -42
assert solution.myAtoi('   -42 ') == -42
assert solution.myAtoi('  42 ') == 42
assert solution.myAtoi('  -2147483648 ') == -2147483648
assert solution.myAtoi('  2147483648 ') == 2147483647
assert solution.myAtoi('  +11191657170 ') == 2147483647
