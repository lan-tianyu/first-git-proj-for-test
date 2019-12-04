from typing import List


class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     i = 0
    #     n = len(nums)
    #     pre = nums[0]
    #     for j in range(1, n):
    #         if pre == nums[j]:
    #             i += 1
    #         else:
    #             pre = nums[j]
    #             nums[j-i], nums[j] = nums[j], nums[j-i]
    #     return n-i

    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        n = len(nums)
        for j in range(1, n):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1




if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 1, 2, 3, 4, 4]
    assert s.removeDuplicates(nums) == 4
    assert nums[0:4] == [1, 2, 3, 4]
    nums = [1, 2, 3, 4, 5]
    assert s.removeDuplicates(nums) == 5
    assert nums[0:5] == [1, 2, 3, 4, 5]
