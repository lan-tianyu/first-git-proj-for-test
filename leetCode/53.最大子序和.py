#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """[summary]
        1. max_s 记录当前最大的连续和，初始值为第一个元素
        2. 当前元素为负数，则不计入加和
        时间 O9）
        """        
# @lc code=end

