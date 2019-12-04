import math


class Solution:
    # def isPowerOfThree(self, n: int) -> bool:
    #     if n <= 0:
    #         return False
    #     while n > 1:
    #         print(n)
    #         if n % 3 != 0:
    #             return False
    #         n = int(n / 3)
    #     return n == 1

    # def isPowerOfThree(self, n: int) -> bool:
    #     if n <= 0:
    #         return False
    #     n = math.log10(n) / math.log10(3)
    #     return int(n) == n

    def isPowerOfThree(self, n: int) -> bool:
        if n > 0 and (3 ** 19) % n == 0:
            return True
        return False
