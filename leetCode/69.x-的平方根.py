#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 1:
            return 0
        ans = 2
        while ans*ans <= x:
            ans += 1
            print(x, ans)
        return ans-1
    

s = Solution()
assert s.mySqrt(4) == 2
assert s.mySqrt(1) == 1
assert s.mySqrt(8) == 2
assert s.mySqrt(100) == 10

# @lc code=end

