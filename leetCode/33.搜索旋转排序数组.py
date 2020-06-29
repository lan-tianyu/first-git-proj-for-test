#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """[summary]
        二分法
        1. left right 分别为nums的最左最右索引，mid为中间索引
        2. mid元素等于target，返回mid
        3. 当nums[mid] > target，满足nums[left] < target < nums[mid]，说明nums[left:mid+1]为连续排序序列且，则可以在这个区间继续查找
        3. 当nums[mid] > target，满足nums[left] > target, 则说明 target不在右边
        4. 当nums[mid] < target，满足nums[mid] < target < nums[right]， 即nums[mid:right+1]为连续排序序列，则可以在这个区间继续查找
        4. 当nums[mid] < target，满足nums[right] < tagert，则说明target不在左边
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                if nums[left] < nums[mid] and nums[left] > target:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] < target:
                if nums[mid] < nums[right] and nums[right] < target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


s = Solution()
nums = [4, 5, 6, 7, 8, 0, 1, 2]
assert s.search(nums, 0) == 5
assert s.search(nums, 8) == 4
assert s.search(nums, 4) == 0
# @lc code=end
