#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#


# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        """[summary]
        1. 每个字符有一个对应值的map，加上特殊场景IV、IX、XL、XC、CD、CM
        2. 特殊场景值计算，往前一个元素+当前元素 匹配到key，则使用特殊场景值
        3. 特殊场景值计算，往前一个元素+当前元素 匹配到key，则使用当前元素的值，往后迭代加和
        3. 2和3结合，特殊场景值设置是实际值间前一个元素对应的值
        """
        map_nums = dict(I=1,
                        IV=3,
                        V=5,
                        IX=8,
                        X=10,
                        XL=30,
                        L=50,
                        XC=80,
                        C=100,
                        CD=300,
                        D=500,
                        CM=800,
                        M=1000)
        nums = sum([
            map_nums.get(s[i - 1:i + 1], 0)
            if map_nums.get(s[i - 1:i + 1], 0) else map_nums.get(s[i])
            for i in range(len(s))
        ])
        print(nums)
        return nums


s = Solution()
assert s.romanToInt('I') == 1
assert s.romanToInt('IVV') == 9
assert s.romanToInt('VIV') == 9
assert s.romanToInt('VVI') == 11
# @lc code=end
