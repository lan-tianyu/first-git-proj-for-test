class Solution:
    # def countPrimes(self, n: int) -> int:
    #     if n <= 1:
    #         return 0
    #     p = [1] * n
    #     for i in range(2, n):
    #         if p[i]:
    #             j = 2 * i
    #             while j < n:
    #                 p[j] = 0
    #                 j += i
    #     return sum(p) - 2

    def countPrimes(self, n: int) -> int:
        return sum([self._isPrime(i) for i in range(2, n)])

    def _isPrime(self, n: int) -> bool:
        j = 2
        while j * j <= n:
            if n % j == 0:
                return 0
            j += 1
        return 1


solution = Solution()
assert solution.countPrimes(0) == 0
assert solution.countPrimes(1) == 0
assert solution.countPrimes(10) == 4
