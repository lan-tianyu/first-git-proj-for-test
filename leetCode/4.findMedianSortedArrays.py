#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
from typing import List


class Solution:
    # def findMedianSortedArrays(self, nums1: List[int],
    #                            nums2: List[int]) -> float:
    #     """[summary]
    #     1. 中位数即列表中排在中间位置的平均值；如果列表长度为偶数，则中间位置为(LEN+1)//2、LEN//2 + 1；如果列表长度为奇数，则中间位置为(LEN+1)//2
    #     2. 计算两个列表的总长度，计算中位数位置
    #     3. 遍历规则，同时遍历两个列表，如果nums1元素小于nums2，则nums1继续遍历；否则nums2继续遍历
    #     4. 遍历规则，遍历总个数小于等于LEN//2+1
    #     5. 遍历规则，记录最新的两个数值，a<b
    #     6. 中位数位置一个，则返回最新值b；中位数位置为两个，则返回(a+b)/2
    #     """
    #     m, n = len(nums1), len(nums2)
    #     left, right = (m + n + 1) // 2, (m + n) // 2 + 1
    #     i, j, count = 0, 0, 0
    #     a, b = 0, 0
    #     while (i < m or j < n) and count < right:
    #         count += 1
    #         if i < m and j < n:
    #             if nums1[i] < nums2[j]:
    #                 a, b = b, nums1[i]
    #                 i += 1
    #             else:
    #                 a, b = b, nums2[j]
    #                 j += 1

    #         elif i < m:
    #             a, b = b, nums1[i]
    #             i += 1
    #         else:
    #             a, b = b, nums2[j]
    #             j += 1
    #     if left == right:
    #         return b
    #     else:
    #         return (a + b) / 2

    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        """[summary]
        1. 中位数即列表中排在中间位置的平均值；如果列表长度为偶数，则中间位置为(LEN+1)//2、LEN//2 + 1；如果列表长度为奇数，则中间位置为(LEN+1)//2
        2. 计算两个列表的总长度，计算中位数位置
        3. 遍历规则，同时遍历两个列表，如果nums1元素小于nums2，则nums1继续遍历；否则nums2继续遍历
        4. 遍历规则，将遍历数据记录到中间list中
        5. 返回中位数
        """
        m, n = len(nums1), len(nums2)
        left, right = (m + n + 1) // 2, (m + n) // 2 + 1
        i, j, count = 0, 0, 0
        a, b = 0, 0
        while i < m and j < n and count < right:
            count += 1
            if nums1[i] < nums2[j]:
                a, b = b, nums1[i]
                i += 1
            else:
                a, b = b, nums2[j]
                j += 1
        while i < m and count < right:
            count += 1
            a, b = b, nums1[i]
            i += 1
        while j < n and count < right:
            count += 1
            a, b = b, nums2[j]
            j += 1
        if left == right:
            return b
        else:
            return (a + b) / 2


s = Solution()
assert s.findMedianSortedArrays([1, 3], [2]) == 2
assert s.findMedianSortedArrays([1, 3], [2, 4]) == 2.5
assert s.findMedianSortedArrays([1, 2], [3]) == 2
assert s.findMedianSortedArrays([1], [2, 3]) == 2
assert s.findMedianSortedArrays([], [2, 3]) == 2.5
assert s.findMedianSortedArrays([1, 2], []) == 1.5
# @lc code=end
