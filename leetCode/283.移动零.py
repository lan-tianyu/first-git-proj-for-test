#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#


# @lc code=start
class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     双指针
    #     1. j为基础位置，i为遍历指针
    #     2. 当i指向的元素等于0，则i指针向前继续遍历
    #     3. 当i指向的元素不等于0，则需要将j位置的元素赋值为当前i位置元素，j指针向前，i指针向前继续遍历
    #     4. 当i指针遍历完，j指针后的元素都要赋值为0、比如0基本都在前面，前面步骤只是将后面的元素赋值到了前面的位置，后面位置的元素值没有变化
    #     """
    #     j = 0
    #     for i in range(len(nums)):
    #         if nums[i]:
    #             nums[j] = nums[i]
    #             j += 1
    #     nums[j:] = [0] * (len(nums)-j)
    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1. 优化上述方法，i指针遍历完，j后的元素都已经是0了
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1

# @lc code=end
