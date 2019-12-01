from typing import List


class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     """[哈希表法]
    #     空间：最坏 O(n)
    #     时间：最坏 O(n)
    #     """
    #     map_d = {}
    #     for e in nums:
    #         if e in map_d:
    #             return True
    #         map_d[e] = 1
    #     return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        """[set方法]
        空间：O(n)
        时间：O(1)
        """
        return len(set(nums)) != len(nums)


if __name__ == '__main__':
    s = Solution()
    assert s.containsDuplicate([1, 3, 2, 4, 5]) is False
    assert s.containsDuplicate([1, 3, 2, 4, 3]) is True
