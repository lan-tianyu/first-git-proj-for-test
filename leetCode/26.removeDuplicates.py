#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """[summary]
        1. 双指针法遍历nums，最后nums中元素不保证与之前的一致；
        2. 当前元素与前一个元素比较，相等，则与最后一个位置元素交换位置，nums长度-1，进入下一个循环
        3. 当前元素与前一个元素比较，不相等，则继续遍历
        """
        n = len(nums)
        i = 1
        while i < n:
            base = nums[i - 1]
            if base == nums[i]:
                nums[i], nums[n - 1] = nums[n - 1], nums[i]
                n -= 1
            else:
                
                i += 1
            print(nums, base, i, n)
        return n


s = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
assert s.removeDuplicates(nums) == 5
assert nums[:5] == [0, 4, 1, 3, 2]
# @lc code=end
