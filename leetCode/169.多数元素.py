#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
from typing import List


class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     map_nums = {}
    #     for x in nums:
    #         count = map_nums.get(x, 0) + 1
    #         map_nums[x] = count
    #     m = len(nums)
    #     for k, v in map_nums.items():
    #         if v > m // 2:
    #             return k
    #     return None

    def majorityElement(self, nums: List[int]) -> int:
        """[summary]
        投票法
        1. count标识相同元素的个数
        2. ans 标识众数
        3. 如果 ans与当前元素一致，则count+1，如果不一致，则count-1
        4. 当couunt==0时，重新选一个候选人
        """        
        if not nums:
            return None
        ans, count = None, 0
        for num in nums:
            if count == 0:
                ans = num
            count += 1 if num == ans else -1
            print(ans, count, num)
        return ans

            
s = Solution()
assert s.majorityElement([3, 2, 3]) == 3
assert s.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
# @lc code=end
