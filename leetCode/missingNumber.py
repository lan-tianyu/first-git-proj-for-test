from typing import List


class Solution:
    # def missingNumber(self, nums: List[int]) -> int:
    #     """[数学法]
    #     """
    #     n = len(nums)
    #     sum_all = int(n / 2 * (n + 1))
    #     sum_nums = sum(e for e in nums)
    #     return sum_all - sum_nums

    def missingNumber(self, nums: List[int]) -> int:
        """[异或法]
        """
        n = len(nums)
        for i, e in enumerate(nums):
            n = n ^ i ^ e
            print(n)
        return n ^ n

    # def missingNumber(self, nums: List[int]) -> int:
    #     """[哈希表法]
    #     """
    #     map_d = {}
    #     n = len(nums)
    #     for e in nums:
    #         map_d[e] = 1
    #     for i in range(n+1):
    #         if map_d.get(i) is None:
    #             return i

    # def missingNumber(self, nums: List[int]) -> int:
    #     """[哈希表法-衍生]
    #     """
    #     n = len(nums)
    #     p = [0] * (n + 1)
    #     for e in nums:
    #         p[e] = 1
    #     for i, e in enumerate(p):
    #         if e == 0:
    #             return i


class TestSolution:
    def test_missingNumber(self):
        s = Solution()
        assert s.missingNumber([0, 3, 1]) == 2
        assert s.missingNumber([2, 3, 1]) == 0
        assert s.missingNumber([0, 2, 1]) == 3


if __name__ == '__main__':
    test = TestSolution()
    test.test_missingNumber()
