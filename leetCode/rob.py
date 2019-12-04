from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_max = 0
        cur_max = 0
        for e in nums:
            ans = max(prev_max + e, cur_max)
            prev_max, cur_max = cur_max, ans
        return cur_max


if __name__ == '__main__':
    s = Solution()
    assert s.rob([2]) == 2
    assert s.rob([2, 1]) == 2
    assert s.rob([2, 3, 1]) == 3
    assert s.rob([2, 1, 1, 2]) == 4