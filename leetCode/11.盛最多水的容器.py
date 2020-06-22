#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """[summary]
        双指针法
        1. max_area标识最大容水量
        2. 左右两端的乘积为初始值，短的一边向另外一边靠近
        3. 判断当前的短边，并计算当前的容积，取大值
        """
        max_area = 0
        i, j = 0, len(height) - 1
        while i < j:
            if height[i] < height[j]:
                max_area = max(max_area, height[i] * (j - i))
                i += 1
            else:
                max_area = max(max_area, height[j] * (j - i))
                j -= 1
            print(i, j, max_area)
        return max_area


s = Solution()
assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
# @lc code=end
