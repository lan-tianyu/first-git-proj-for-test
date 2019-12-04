class Solution:
    # def climbStairs(self, n: int) -> int:
    #     """[递归法]
    #     """
    #     if n == 1:
    #         return 1
    #     if n == 2:
    #         return 2
    #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs(self, n: int) -> int:
        """[迭代法]
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b = 1, 2
        ans = 0
        for i in range(3, n+1):
            ans = a + b
            a, b = b, ans
        return ans


if __name__ == '__main__':
    s = Solution()
    assert s.climbStairs(10) == 89
    assert s.climbStairs(8) == 34