#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
from typing import List


class Solution:
    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     """[summary]
    #     1. 先排序
    #     2. 双指针法
    #     如果nums1的元素小于nums2元素，则nums1向右遍历，
    #     如果nums1的元素大于nums2元素，则nums2向右遍历，
    #     如果相等，则记录当前元素，两个list一起向右遍历

    #     时间：O(ml)
    #     空间：O(1)
    #     """
    #     nums = []
    #     nums1.sort()
    #     nums2.sort()
    #     i, j = 0, 0
    #     while i < len(nums1) and j < len(nums2):
    #         if nums1[i] < nums2[j]:
    #             i += 1
    #         elif nums1[i] == nums2[j]:
    #             nums.append(nums1[i])
    #             i += 1
    #             j += 1
    #         else:
    #             j += 1
    #     return nums


    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """[summary]
        哈希映射
        1. 遍历nums1，map_nums存放元素出现的次数
        2. 遍历nums2，如果元素在map_nums能够找到且value!=0，则nums中增加改元素，同时map_nums对应元素个数减1
        时间： O(m+n)
        空间： O(min(m, n))
        """
        map_nums = {}
        nums = []
        for x in nums1:
            map_nums[x] = map_nums.get(x, 0) + 1
        for y in nums2:
            count = map_nums.get(y)
            if count:
                nums.append(y)
                map_nums[y] = count - 1
        return nums


s = Solution()
# assert s.intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
# assert s.intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]
# assert s.intersect([-2147483648, 1, 2, 3],
#                    [1, -2147483648, -2147483648]) == [-2147483648, 1]
# @lc code=end
