#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
from typing import List


class Solution:
    # def removeElement(self, nums: List[int], val: int) -> int:
    #     """[summary]
    #     1. 遍历nums元素，当前元素与移除元素相等，则移除元素个数+1
    #     2. 遍历nums元素，当前元素与移除元素不相等，移除元素个数大于0，当前元素与移除元素交换位置
    #     3. 移除元素个数count，新数组个数n-count，返回移除后的nums[:n-count]
    #     4. nums 最后保证顺序
    #     时间：O(N)
    #     空间：O(1)
    #     """
    #     count = 0
    #     n = len(nums)
    #     for i, e in enumerate(nums):
        #     if e == val:
        #         count += 1
        #         continue
        #     if count:
        #         nums[i - count], nums[i] = nums[i], nums[i - count]
        # return n - count
    def removeElement(self, nums: List[int], val: int) -> int:
        """[summary]
        1. 遍历nums元素，当前元素与移除元素不相等，遍历index+1
        2. 遍历nums元素，当前元素与移除元素相等，则当前元素赋值为第n-1个元素，nums长度减去1。
        3. 基于3，如果最后一个元素还是要移除的元素，由于index没有自增，后一个操作将会继续与n-1后的最后一个元素交换位置
        4. 返回移除后的nums[:n]
        5. nums最后不保证顺序
        时间：O(N)
        空间：O(1)
        """
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
        return n
        

s = Solution()
nums = [3, 2, 2, 3]
assert s.removeElement(nums, 3) == 2
assert 3 not in nums[:2]
nums = [3, 3, 2, 3, 4, 5, 3]
assert s.removeElement(nums, 3) == 3
assert 3 not in nums[:3]
nums = [3, 3, 3]
assert s.removeElement(nums, 3) == 0
assert nums[:0] == []
# @lc code=end
