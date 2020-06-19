#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#


# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        """[summary]
        a ^ b 获得无进位加和
        (a & b) << 1 获得进位
        a+b = (a ^ b) + ((a & b) << 1)
        直到进位为0
        """
        print('-' * 80)
        # 2^32
        MASK = 0x100000000
        # 整型最大值
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b != 0:
            # 计算进位
            carry = (a & b) << 1
            # 取余范围限制在 [0, 2^32-1] 范围内
            a = (a ^ b) % MASK
            b = carry % MASK
            print(a, b)
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)


s = Solution()
assert s.getSum(3, -4) == -1
assert s.getSum(3, -2) == 1
# assert s.getSum(3, 2) == 5
# assert s.getSum(3, 3) == 6
# assert s.getSum(3, -3) == 0
# assert s.getSum(9, 7) == 16
# @lc code=end
