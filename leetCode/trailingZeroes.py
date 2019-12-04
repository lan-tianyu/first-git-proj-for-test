class Solution:
    # def trailingZeroes(self, n: int) -> int:
    #     """[数学规律]
    #     5 * 2 = 10  --- 1个0
    #     5 * 20 = 100 ---- 2个0
    #     5 * 200 = 1000 ---- 3个0
    #     1. 5以内  0个
    #     2. 5-10   1个
    #     3. 10-15  两个
    #     4. 15-20  多了一个10， 3个
    #     5. 20     多了一个 10 ，4个
    #     最终归结到，n之内的数字，有多少个5的倍数
    #     """
    #     print('*' * 40)
    #     count = 0
    #     for N in range(5, n+1):
    #         while N > 0:
    #             if N % 5 == 0:
    #                 count += 1
    #                 print('111', count, N)
    #             N = N / 5
    #     return count

    def trailingZeroes(self, n: int) -> int:
        """[数学规律]
        最终归结到，n之内的数字，有出现了多少次5
        5出现一次
        25出现2次
        125出现3次
        --- 使用递归处理
        """
        if n < 5:
            return 0
        return n // 5 + self.trailingZeroes(n // 5)

    # def trailingZeroes(self, n: int) -> int:
    #     """[数学规律]
    #     最终归结到，n之内的数字，有出现了多少次5
    #     5出现一次
    #     25出现2次
    #     125出现3次
    #     ----  使用迭代处理
    #     """
    #     count = 0
    #     while n > 0:
    #         print(count, n)
    #         count += n // 5
    #         n = n // 5
    #     return count


solution = Solution()
assert solution.trailingZeroes(0) == 0
assert solution.trailingZeroes(5) == 1
assert solution.trailingZeroes(20) == 4
assert solution.trailingZeroes(40) == 9
