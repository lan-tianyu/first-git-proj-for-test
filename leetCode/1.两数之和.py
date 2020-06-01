#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """[summary]
        1、用一个map存放nums中已经遍历的元素和索引 -- 避免两个重复元素之和的用例
        2、遍历nums，如果target-当前元素 在 map中可以找到，则返回对应的索引
        3、遍历nums，如果target-当前元素 在 map中找不到，则元素放入map中
        时间：O(N)
        空间：O(N)
        """
        map_nums = {}
        for i, e in enumerate(nums):
            t = target - e
            if t in map_nums:
                return map_nums.get(t), i
            else:
                map_nums[e] = i
        

s = Solution()
assert s.twoSum([], 9) is None
assert s.twoSum([2, 7, 11, 15], 9) == (0, 1)
assert s.twoSum([2, 7, 11, 15], 22) == (1, 3)
assert s.twoSum([2, 7, 11, 15], 13) == (0, 2)
assert s.twoSum([2, 7, 11, 15], 18) == (1, 2)
assert s.twoSum([2, 7, 11, 15], 26) == (2, 3)
assert s.twoSum([2, 7, 11, 15], 25) is None
assert s.twoSum([2, 7, 11, 15], 17) == (0, 3)
assert s.twoSum([2, 7, 11, 15], 15) is None

assert s.twoSum([11, 2, 7, 15], 9) == (1, 2)
assert s.twoSum([11, 2, 7, 15], 22) == (2, 3)
assert s.twoSum([11, 2, 7, 15], 13) == (0, 1)
assert s.twoSum([11, 2, 7, 15], 18) == (0, 2)
assert s.twoSum([11, 2, 7, 15], 26) == (0, 3)
assert s.twoSum([11, 2, 7, 15], 25) is None
assert s.twoSum([11, 2, 7, 15], 17) == (1, 3)
assert s.twoSum([11, 2, 7, 15], 15) is None
        
# @lc code=end

