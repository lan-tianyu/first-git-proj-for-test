from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        sum_nums = 0
        for index, e in enumerate(nums):
            # sum_nums = e if sum_nums <= 0 else sum_nums + e
            sum_nums = max(sum_nums + e, e)
            ans = max(ans, sum_nums)
        return ans


if __name__ == '__main__':
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray([-2, 1, 2, 4, -1, 2, 1, -5, 6]) == 10
    assert s.maxSubArray([-1, -2]) == -1
    assert s.maxSubArray([-2, 1, -3]) == 1

    
