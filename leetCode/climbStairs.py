class Solution:
    def climbStairs(self, n: int) -> int:
        prev, cur = 0, 1
        for i in range(1, n+1):
            ans = cur + prev
            cur, prev = ans, cur
        return cur

    # def climbStairs(self, n: int) -> int:
    #     prev, cur = 1, 2
    #     if n == 1:
    #         return prev
    #     if n == 2:
    #         return cur
    #     for i in range(3, n+1):
    #         ans = cur + prev
    #         cur, prev = ans, cur
    #     return cur