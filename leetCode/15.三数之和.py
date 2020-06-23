#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """[summary]
        排序+双指针法
        1. first标识第一个元素，second标识第二个元素，third标识第三个元素
        2. first从第一个元素开始遍历，second从first下一个元素开始遍历，third与second对应的从右往左遍历
        3. 当前third元素+first元素+second元素>0，则third-1
        4. 当前third元素+first元素+second元素<0，则second+1，进入下一个循环
        5. 当前third元素+first元素+second元素==0，则添加到结果，second+1，third-1，进入下一个循环

        关键点在于，怎么过滤相同元素
        1. first为非第一个元素，判断first与first-1是否一致，一致就first+1，进入下一个循环
        2. second为非first+1的元素，判断second与second-1是否一致，一致则second+1，进入下一个循环
        为什么third不需要判断？是不是可以理解，如果前两个都不一致了，那么third必然不会取到相同的
        """
        nums.sort()
        ans = []
        n = len(nums)
        for first in range(n-2):
            if first > 0 and nums[first] == nums[first-1]:
                first += 1
                continue
            second, third = first + 1, n - 1
            while second < n-1 and second < third:
                if second > first + 1 and nums[second] == nums[second-1]:
                    second += 1
                    continue
                if nums[first] + nums[second] + nums[third] > 0:
                    third -= 1
                    continue
                if nums[first] + nums[second] + nums[third] < 0:
                    second += 1
                    continue
                if nums[first] + nums[second] + nums[third] == 0:
                    ans.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
                    continue
        return ans


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([-1, 0, 1, 0]))
print(s.threeSum([0, 0]))
print(s.threeSum([0, 0, 0, 0]))
# @lc code=end
