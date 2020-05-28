#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#


# @lc code=start
class Solution:
    # def reverse(self, x: int) -> int:
    #     """[summary]
    #     1. 假设第一位是数字，则反转之后是正整数。往后一位，多*10，同时判断当前值是否大于2 ** 31 - 1
    #     2. 假设第一位是-，则反转后是负数。往后一位，多*10，同时判断当前值是否大于2 ** 31
    #     """
    #     s = 0
    #     str_x = str(x)
    #     n = len(str_x)
    #     if str_x[0] == '-':
    #         for i in range(1, n):
    #             t = int(str_x[i]) * (10**(i - 1))
    #             if s > 2**31 - t:
    #                 return 0
    #             s += t
    #         return -int(s)
    #     else:
    #         for i in range(n):
    #             t = int(str_x[i]) * (10**i)
    #             if s > 2**31 - 1 - t:
    #                 return 0
    #             s += t
    #         return int(s)

    def reverse(self, x: int) -> int:
        """[summary]
        python 的 负数取模不是取余数
        1. x的最后一位放到最前面，则是x%10的结果放到第一位，下一循环数值是x/10
        2. 每次循环加和，之前取模的数据要 * 10
        3. 循环结束条件：x != 0
        4. 异常返回0条件，当前是正整数，则最后一个是7，则历史数据不能大于 214748364 或者，历史数据等于 214748364且 x % 10 大于7
        5. 异常返回0条件，当前是负整数，则最后一个是8，则历史数据不能小于-214748364 或者，历史数据等于 -214748364且 x % 10 小于-8
        """
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        s = 0
        while x != 0:
            if x > 0:
                t = x % 10
                x = x // 10
                if s > MAX_INT // 10 or (s == MAX_INT // 10
                                         and t > MAX_INT % 10):
                    return 0
            else:
                t = x % -10
                x = -(x//-10)
                print(s, x, t)
                if s < -(MIN_INT // -10) or (s == -(MIN_INT // -10)
                                         and t < MIN_INT % -10):
                    return 0
            s = s * 10 + t
        return s


s = Solution()
assert s.reverse(8463847412) == 0
assert s.reverse(7463847412) == 2147483647
assert s.reverse(-9463847412) == 0
assert s.reverse(-8463847412) == -2147483648
assert s.reverse(-1563847412) == 0

# @lc code=end
