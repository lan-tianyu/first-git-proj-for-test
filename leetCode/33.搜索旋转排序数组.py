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
        3. 当nums[mid] > target，一般情况下right=mid-1，继续查找；
           当nums[mid] > target and nums[left]<=nums[mid]场景下，说明是连续递增，如果第一个numds[left]>target，说明要在mid右边查找
           当nums[mid] > target and nums[left]<=nums[mid]场景下，说明是连续递增，如果第一个numds[left]<=target，说明要在mid左边查找
           当nums[mid] > target and nums[left]>nums[mid]场景下，说明是非连续递增，此时在mid左边查找
        4. 当nums[mid] < target，一般情况下left=mid+1，继续查找；
           当nums[mid] < target and nums[mid]<=nums[right]场景下，说明是连续递增，如果第一个numds[right]<target，说明要在mid左边查找
           当nums[mid] < target and nums[mid]<=nums[right]场景下，说明是连续递增，如果第一个numds[right]>=target，说明要在mid右边查找
           当nums[mid] < target and nums[mid]>nums[right]场景下，说明是连续递增，此时在mid右边查找

        上面场景中nums[left]<=nums[mid] 以及 nums[mid]<=nums[right] 边界条件很关键
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                if nums[left] <= nums[mid]:
                    if nums[left] > target:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    right = mid - 1
            elif nums[mid] < target:
                if nums[mid] <= nums[right]:
                    if nums[right] < target:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    left = mid + 1
        return -1


s = Solution()
nums = [4, 5, 6, 7, 8, 0, 1, 2]
assert s.search(nums, 0) == 5
assert s.search(nums, 8) == 4
assert s.search(nums, 4) == 0
assert s.search(nums, 3) == -1
assert s.search([2, 1], 1) == 1
# @lc code=end
