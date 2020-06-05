#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        nums = [[1]]
        for i in range(1, numRows):
            base = nums[-1]
            temp = [1]
            for i in range(1, len(base)):
                e = base[i-1] + base[i]
                temp.append(e)
            temp.append(1)
            nums.append(temp)
        return nums


s = Solution()
print(s.generate(5))
# @lc code=end
