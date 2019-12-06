import sys


class Solution:
    # def reverse(self, x: int) -> int:
    #     x = str(x)
    #     if x[0] == '-':
    #         ans = -1 * int(x[1:][::-1])
    #     else:
    #         ans = int(x[::-1])
    #     if ans > sys.maxsize or ans < -sys.maxsize - 1:
    #         return 0
    #     return ans

    def reverse(self, x: int) -> int:
        ans = 0
        is_negative = True if x < 0 else False
        x = -x if x < 0 else x
        while x != 0:
            pop = x % 10
            x = x // 10
            if ans > sys.maxsize // 10 or (ans == sys.maxsize // 10 and pop > (8 if is_negative else 7)):
                return 0
            ans = ans * 10 + pop
        print(is_negative, ans)
        return ans * (-1 if is_negative else 1)


solution = Solution()
assert solution.reverse(-1) == -1
assert solution.reverse(1) == 1
assert solution.reverse(20) == 2
assert solution.reverse(123) == 321
assert solution.reverse(-123) == -321
assert solution.reverse(120) == 21
assert solution.reverse(120) == 21
assert solution.reverse(7463847412) == 2147483647
assert solution.reverse(8463847412) == 0
assert solution.reverse(-8463847412) == -2147483648
assert solution.reverse(-9463847412) == 0
