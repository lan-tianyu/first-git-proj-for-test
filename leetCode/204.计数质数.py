#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <=2 :
            return 0
        primes_list = [1] * n
        for i in range(2, int(n ** 0.5) + 1):
            if primes_list[i]:
                for j in range(i ** 2, n, i):
                    primes_list[j] = 0
        return sum(primes_list) - 2


s = Solution()
assert s.countPrimes(10) == 4

# @lc code=end

