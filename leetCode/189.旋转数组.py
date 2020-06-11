#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
from typing import List


class Solution:
    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     临时数组存放移动后的数据
    #     然后再从临时数组中取出元素，赋值给nums，不能直接将nums直接赋值temp，参考
    #     https://stackoverflow.com/questions/57152755/difference-between-nums-nums-1-and-nums-nums-1/57152830
        
    #     时间: O(N)，遍历了所有的元素一遍
    #     空间：O(N) 额外一个数组存放旋转后的元素
    #     """
    #     m = len(nums)
    #     temp = [0] * m
    #     for i in range(m):
    #         temp[(i+k) % m] = nums[i]
    #     nums[:] = temp[:]

    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     环形移动法
    #     1. 首先想到的是k = k%(len(nums)), 如果k为0，则不需要旋转
    #     2. 从第一个元素开始，往后移动k步。cur为移动后的位置，prev标记移动前cur位置的元素，cur元素赋值为cur-k位置的值
    #     3. 为了避免溢出，每次的位置都要跟len(nums)取余数
    #     4. 循环结束条件是，所有的元素都遍历完
    #     5. 特殊场景，假设k是len(nums)的约数，则遍历len(nums)//k次后，会重复循环，此时，遍历还未完，需要重置元素位置
    #     比如从一个元素开始，回到第一个元素位置（已经交换完数据），考虑从下一个位置开始循环

    #     时间：O(N)
    #     空间：O(1)
    #     """
    #     m = len(nums)
    #     k = k % m
    #     start, count = 0, 0
    #     cur, prev = (start + k) % m, nums[start]
    #     while count < m and k:
    #         nums[cur], prev = prev, nums[cur] 
    #         cur = (cur + k) % m
    #         count += 1
    #         if cur == start:
    #             nums[cur], prev = prev, nums[cur] 
    #             start += 1
    #             cur, prev = (start + k) % m, nums[start]
    #             count += 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        多次反转

        """
        m = len(nums)
        k = k % m
        # nums[:] = (nums[:m-k][::-1] + nums[m-k:][::-1])[::-1]
        # nums[:] = (nums[m-k-1::-1] + nums[:m-k-1:-1])[::-1]
        print(nums)
        # nums[:] = nums[-k:] + nums[:m-k]


s = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
s.rotate(nums, 3)
assert nums == [5, 6, 7, 1, 2, 3, 4]
nums = [1, 2, 3, 4, 5, 6, 7]
s.rotate(nums, 7)
assert nums == [1, 2, 3, 4, 5, 6, 7]
nums = [1, 2, 3, 4, 5, 6, 7]
s.rotate(nums, 8)
assert nums == [7, 1, 2, 3, 4, 5, 6]
nums = [-1, -100, 3, 99]
s.rotate(nums, 2)
assert nums == [3, 99, -1, -100]
# @lc code=end
