#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#


# @lc code=start
class Solution:
    # def reverseBits(self, n: int) -> int:
    #     """[summary]
    #     1. bit_list存放n的二进制数据，从左到右，对应n的低位到高位，由于n不一定有32位，我们固定bit_list长度为32，高位不足用0补齐
    #     2. 从左到右遍历bit_list，计算二进制对应的ans
    #     """
    #     ans, i, bit_list = 0, 0, [0] * 32
    #     while n:
    #         bit_list[i] = n % 2
    #         n = n >> 1
    #         i += 1
    #     for x in bit_list:
    #         ans = ans * 2 + x
    #     return ans

    # def reverseBits(self, n: int) -> int:
    #     """[summary]
    #     1. 简化上述版本，不用额外空间存放二进制
    #     2. 相当于 上一次结果*2 后与 n每次取余数后 相加。
    #     3. 由于n不一定能左移31次，所以固定每次从低位bit开始*2**31，后面求2的幂次方依次减一
    #     """
    #     ans, power = 0, 31
    #     while n:
    #         x = n & 1
    #         n = n >> 1
    #         ans += x << power
    #         power -= 1
    #     return ans

    def reverseBits(self, n: int) -> int:
        """[summary]
        题目中讲到多次调用，可以将已经计算的数据缓存起来，避免重复计算
        """
        n = n >> 16 | n << 16
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n


s = Solution()
assert s.reverseBits(43261596) == 964176192
# @lc code=end
