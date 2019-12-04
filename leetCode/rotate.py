from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [切片法]
        切片操作的时间复杂度：O(k)，k为切片的大小
        时间复杂度：两次切片操作，时间复杂度O(n)
        空间复杂度： O(1)
        """
        n = len(nums)
        k = k % n
        # nums[0:k], nums[k:n] = nums[n - k:n], nums[0:n - k]
        nums[:] = nums[n - k:n] + nums[0:n - k]
        # print(nums)

    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     [原地插入法]
    #     末尾的元素插入到list头部
    #     """
    #     n = len(nums)
    #     k = k % n
    #     for i in range(k):
    #         nums.insert(0, nums.pop())
    #     print(nums)

    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     [三次反转法]
    #     1. 全部反转
    #     2. 反转k-n，注意python的反转写法
    #     3. 反转0-k，注意python的反转写法
    #     """
    #     n = len(nums)
    #     k = k % n
    #     nums[:] = nums[:][::-1]
    #     nums[k:] = nums[k:][::-1]
    #     nums[:k] = nums[:k][::-1]
    #     print(nums)


solution = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
solution.rotate(nums, 3)  # [5, 6, 7 1, 2, 3, 4]
nums = [1, 2, 3, 4, 5, 6, 7]
solution.rotate(nums, 5)  # [3, 4, 5, 6, 7, 1, 2]
nums = [1, 2, 3, 4, 5, 6, 7]
solution.rotate(nums, 7)  # [1, 2, 3, 4, 5, 6, 7]
nums = [1, 2, 3, 4, 5, 6, 7]
solution.rotate(nums, 8)  # [7, 1, 2, 3, 4, 5, 6]
