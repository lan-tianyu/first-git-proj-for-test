#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#


# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        """[summary]
        二分法
        """
        left = 0
        right = x // 2 + 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 < x:
                left = mid + 1
            else:
                right = mid - 1
            print(left, right, mid)
        return right


s = Solution()
assert s.mySqrt(0) == 0
assert s.mySqrt(1) == 1
assert s.mySqrt(4) == 2
assert s.mySqrt(8) == 2
assert s.mySqrt(100) == 10

# @lc code=end
