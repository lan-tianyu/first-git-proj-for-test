#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#


# @lc code=start
class Solution:
    # def myAtoi(self, str: str) -> int:
    #     """[summary]
    #     1. 初始值ans=0，去除左边空格
    #     2. 如果字符串为空，返回ans
    #     3. 第一个字符不为-+，且也不是数字，返回ans
    #     4. 初始index，如果第一个字符是+-，则inex=1，否则index=0
    #     5. 标志为sign，如果第一个字符是-，则为-1，否则为1
    #     6. 从初始位置开始遍历每一个字符，如果是非数字，返回sign * ans
    #     7. 是数字，判断当前ans是否大于最大2**31//10，如果大于，返回最大整数或者最小整数
    #     8. 是数字，判断当前ans是否等于2**31//10且满足当前值大于7 或者 8，满足条件，返回最大整数或者最小整数
    #     9. 上述异常路径不满足，计算当前ans=ans * 10 + int(str[i])
    #     10. 最后返回sign * ans

    #     注意
    #     1. 为什么ans每次计算不乘以sign，如果ans是负数，sign是负数，下一步就变成了正数
    #     2. 注意每次都要判断是否是数字
    #     3. 注意每次计算ans，字符要转化成int
    #     """
    #     ans = 0
    #     str = str.strip()
    #     if not str:
    #         return ans
    #     if str[0] not in ['+', '-'] and not str[0].isdigit():
    #         return ans
    #     MAX_INT = 2**31 - 1
    #     MIN_INT = -2**31
    #     MAX_NUM = 2**31 // 10
    #     sign = -1 if str[0] == '-' else 1
    #     index = 1 if str[0] in ['+', '-'] else 0
    #     for i in range(index, len(str)):
    #         if not str[i].isdigit():
    #             return sign * ans
    #         print(ans, int(str[i]))
    #         if ans > MAX_NUM or (ans == MAX_NUM and
    #                              int(str[i]) > (7 if sign == 1 else 8)):
    #             return MAX_INT if sign == 1 else MIN_INT
    #         ans = ans * 10 + int(str[i])
    #     return sign * ans

    def myAtoi(self, str: str) -> int:
        """[summary]
        状态机法
        1. 空格 ''
        2. 符号+-：sign
        3. 数字：number
        4. 非空格或者非+-或者非数字，标记为other
        5. 开始状态start， 结束状态 end
        状态流转
        1. 从start开始，遇到空格、符号、数字、非空格或者非+-或者非数字，依次变成下一状态
        2. 再从上述状态，遇到空格、符号、数字、非空格或者非+-或者非数字，依次变成下一状态
        """
        state_map = {
            'start': ['start', 'sign', 'number', 'end'],
            'sign': ['end', 'end', 'number', 'end'],
            'number': ['end', 'end', 'number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        MAX_NUM = 2 ** 31 // 10
        state = 'start'
        sign = 1
        ans = 0
        for e in str:
            if e == ' ':
                state = state_map[state][0]
            elif e == '-':
                state = state_map[state][1]
            elif e == '+':
                state = state_map[state][1]
            elif e.isdigit():
                state = state_map[state][2]
            else:
                state = state_map[state][3]
            if state == 'sign':
                sign = -1 if e == '-' else 1
            if state == 'number':
                if ans > MAX_NUM or (ans == MAX_NUM and int(e) > (7 if int(e) else 8)):
                    return MAX_INT if sign == 1 else MIN_INT
                else:
                    ans = ans * 10 + int(e)
            print(ans, sign, state, e)
        return ans * sign


s = Solution()
assert s.myAtoi('words and 987') == 0
assert s.myAtoi('4193 with words') == 4193
assert s.myAtoi('   -42') == -42
assert s.myAtoi('-91283472332') == -2147483648
assert s.myAtoi('91283472332') == 2147483647
assert s.myAtoi('-2147483647') == -2147483647
assert s.myAtoi('-2147483648') == -2147483648
assert s.myAtoi('2147483647') == 2147483647
assert s.myAtoi('2147483646') == 2147483646
assert s.myAtoi("-   234") == 0
assert s.myAtoi("-13+8") == -13
