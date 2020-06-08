#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
from typing import List


class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     """[summary]
    #     1. base标识当前元素与之前元素比较的基础，如果当前元素不等于base，则base赋值为当前元素
    #     2. count计算当前重复的元素个数，用于后续元素的向前移动的位置
    #     """
    #     base, count, n = 0, 0, len(nums)
    #     for i in range(1, n):
    #         if nums[i] == nums[base]:
    #             count += 1
    #         else:
    #             base = i
    #             nums[i - count] = nums[i]
    #     return n - count

    def removeDuplicates(self, nums: List[int]) -> int:
        """[summary]
        1. i标识当前元素需要比较的元素index，如果当前元素与index处不相等，则i自增1，i处赋值为当前元素值；
        2. j标识当前遍历的元素位置
        """
        i = 0
        for j in range(0, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1


s = Solution()
nums = [1, 1, 2]
assert s.removeDuplicates(nums) == 2
assert nums[:2] == [1, 2]
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
assert s.removeDuplicates(nums) == 5
assert nums[:5] == [0, 1, 2, 3, 4]
# @lc code=end
