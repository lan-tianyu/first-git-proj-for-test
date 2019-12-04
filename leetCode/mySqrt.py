class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x // 2 + 1
        while high > low:
            mid = (low + high + 1) >> 1
            print(low, high, mid)
            square = mid * mid
            if square == x:
                return mid
            elif square > x:
                high = mid - 1
                print('>---', low, high, mid)
            else:
                low = mid
            # mid = mid + 1
                print('<---', low, high, mid)
        mid = (low + high + 1) >> 1
        print('end-', low, high, mid)
        print('*' * 10)
        return mid


solution = Solution()
assert solution.mySqrt(1) == 1
assert solution.mySqrt(4) == 2
assert solution.mySqrt(5) == 2
assert solution.mySqrt(8) == 2
assert solution.mySqrt(9) == 3
assert solution.mySqrt(17) == 4
