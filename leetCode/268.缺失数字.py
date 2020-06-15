#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#


# @lc code=start
class Solution:
    # def missingNumber(self, nums: List[int]) -> int:
    #     """[summary]
    #     数学法
    #     预期总和-实际总和
    #     """
    #     n = len(nums)
    #     expect_sum = n * (n + 1) / 2
    #     real_sum = sum(nums)
    #     return int(expect_sum - real_sum)

    def missingNumber(self, nums: List[int]) -> int:
        """[summary]
        位运算
        任何数 ^ 0 = 数字本身
        任何数 ^ 数字本身 = 0
        """
        ans = 0
        for i in range(len(nums)):
            ans = ans ^ (i+1) ^ nums[i]
        return ans

    # def missingNumber(self, nums: List[int]) -> int:
    #     """[summary]
    #     map哈希表
    #     """
    #     for x in range(len(nums) + 1):
    #         if x not in nums:
    #             return x
    



# @lc code=end
