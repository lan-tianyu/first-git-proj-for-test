from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_d = {}
        for i, e in enumerate(nums):
            for key, val in map_d.items():
                if e + key == target:
                    return [val, i]
            map_d[e] = i
        return None


class TestSolution:
    def test_twoSum(self):
        target = 22
        nums = [2, 7, 11, 15]
        print(Solution().twoSum(nums, target))


if __name__ == '__main__':
    test = TestSolution()
    test.test_twoSum()