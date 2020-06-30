#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
from typing import List


class Solution:
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     """[summary]
    #     暴力法：
    #     1. 从左往右找到左边界，直到找到nums[index]==target，则start=index
    #     2. 从start开始找end，当nums[index]>target，则end=index-1
    #     边界值
    #     1. 找左边界，当index=len(nums)，则说明没有找到target，直接返回[-1, -1]
    #     """
    #     start, end = -1, -1
    #     i, n = 0, len(nums)
    #     while i < n and nums[i] != target:
    #         i += 1
    #     if i == n:
    #         return [start, end]
    #     start = i
    #     while i < n and nums[i] == target:
    #         i += 1
    #     end = i - 1
    #     return [start, end]

    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     """[summary]
    #     二分法，注意细节，注意边界
    #     1. 先找到nums[mid]==target，退出循环查找。后续[left, mid]区间内找start，[mid, right]区间内找end
    #     2. 步骤1边界场景，当left<right，说明没有找到target，直接返回[-1,-1]
    #     3. 二分法[left, mid]区间内找start，当nums[mid]==target，继续在左边查找，right=mid-1
    #     4. 二分法[mid, right]区间内找end，当nums[mid]==target，继续在右边查找，left=mid+1
    #     """
    #     left, right = 0, len(nums) - 1
    #     mid = (left + right) >> 1
    #     while left <= right:
    #         mid = (left + right) >> 1
    #         if nums[mid] == target:
    #             break
    #         if nums[mid] < target:
    #             left = mid + 1
    #         elif nums[mid] > target:
    #             right = mid - 1
    #     if left > right:
    #         return [-1, -1]

    #     def search(low, high, target, flag=0):
    #         # flag标识找左右边界，0标识找左边界，1标识找右边界
    #         ans = -1
    #         while low <= high:
    #             m = (low + high) >> 1
    #             if nums[m] == target:
    #                 ans = m
    #                 if flag == 1:
    #                     low = m + 1
    #                 else:
    #                     high = m - 1
    #             elif nums[m] < target:
    #                 low = m + 1
    #             elif nums[m] > target:
    #                 high = m - 1
    #         return ans

    #     start = search(left, mid, target)
    #     end = search(mid, right, target, 1)
    #     return [start, end]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """[summary]
        二分法，注意细节，注意边界
        1. 先找到nums[mid]==target，退出循环查找。后续[left, mid]区间内找start，[mid, right]区间内找end
        2. 步骤1边界场景，当left<right，说明没有找到target，直接返回[-1,-1]
        3. 二分法[left, mid]区间内找start，当nums[mid]==target，继续在左边查找，right=mid-1，循环中断是nums[left]>target
           返回值是
        4. 二分法[mid, right]区间内找end，当nums[mid]==target，继续在右边查找，left=mid+1，循环中断是nums[right]<target
        """
        left, right = 0, len(nums) - 1
        mid = (left + right) >> 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                break
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if left > right:
            return [-1, -1]

        def search_left(low, high, target):
            while low <= high and nums[low] <= target:
                m = (low + high) >> 1
                if nums[m] == target:
                    high = m - 1
                elif nums[m] < target:
                    low = m + 1
                elif nums[m] > target:
                    high = m - 1
            return low

        def search_right(low, high, target):
            while low <= high and nums[high] >= target:
                m = (low + high) >> 1
                if nums[m] == target:
                    low = m + 1
                elif nums[m] < target:
                    low = m + 1
                elif nums[m] > target:
                    high = m - 1
            return high

        start = search_left(left, mid, target)
        end = search_right(mid, right, target)
        return [start, end]


s = Solution()
nums = [5, 7, 7, 8, 8, 10]
assert s.searchRange(nums, 8) == [3, 4]
assert s.searchRange(nums, 6) == [-1, -1]
assert s.searchRange(nums, 7) == [1, 2]
assert s.searchRange(nums, 10) == [5, 5]
assert s.searchRange([], 0) == [-1, -1]
assert s.searchRange([2, 2], 2) == [0, 1]
assert s.searchRange([0, 0, 0, 1, 2, 3], 0) == [0, 2]
# @lc code=end
