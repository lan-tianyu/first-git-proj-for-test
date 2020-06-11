#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#


# @lc code=start
class Solution:
    # def trailingZeroes(self, n: int) -> int:
    #     """[summary]
    #     计算0-n中，5的倍数中包含多少个5，比如5包含一个，25包含两个，30包含1个
    #     时间：
    #     """
    #     count = 0
    #     for i in range(5, n+1, 5):
    #         x = i
    #         while x > 0 and x % 5 == 0:
    #             count += 1
    #             x //= 5
    #         print(i, count)
    #     return count

    def trailingZeroes(self, n: int) -> int:
        """[summary]
        计算0-n中，5的倍数中包含多少个5，比如5包含一个，25包含两个，30包含1个
        时间：
        """
        count = 0
        while n >= 5:
            n = n // 5
            count += n
        return count


s = Solution()
assert s.trailingZeroes(10) == 2
assert s.trailingZeroes(25) == 6
assert s.trailingZeroes(30) == 7
print(s.trailingZeroes(1808548329))
# @lc code=end
