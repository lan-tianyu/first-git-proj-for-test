from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1


class TestSolution:
    def test_moveZeroes(self):
        solution = Solution()
        nums = [0, 1, 2, 0, 3, 0]
        solution.moveZeroes(nums)
        print(nums)
        nums = [2, 1, 2, 0, 0, 0]
        solution.moveZeroes(nums)
        print(nums)
        nums = [2, 1, 0, 0, 3, 4, 5, 0, 0, 6]
        solution.moveZeroes(nums)
        print(nums)


if __name__ == '__main__':
    test = TestSolution()
    test.test_moveZeroes()