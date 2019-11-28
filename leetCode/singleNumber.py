from typing import List


class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    #     """[哈希表法1]
    #     时间复杂度：O(n+n) = O(n)
    #     空间复杂度：O(n)，存储与nums数量相等的元素
    #     """
    #     map_d = {}
    #     for e in nums:
    #         map_d[e] = map_d.get(e, 0) + 1
    #     for k, v in map_d.items():
    #         if v == 1:
    #             return k
    #     return None

    # def singleNumber(self, nums: List[int]) -> int:
    #     """[哈希表法2]
    #     时间复杂度：O(n) = O(n), python 中hash表操作时间为O(1)
    #     空间复杂度：O(n)，存储与nums数量相等的元素
    #     """
    #     map_d = {}
    #     for e in nums:
    #         if e in map_d:
    #             map_d.pop(e)
    #         else:
    #             map_d[e] = 1
    #     if map_d:
    #         return map_d.popitem()[0]
    #     return None

    # def singleNumber(self, nums: List[int]) -> int:
    #     """[数学方式]
    #     关键信息: 除了某个元素只出现一次以外，其余每个元素均出现两次
    #     如果没有上述前提，则下面的处理方式不成立
    #     时间复杂度：
    #     空间复杂度：
    #     """
    #     result = 2*(sum(set(nums))) - sum(nums)
    #     if result != 0:
    #         return result
    #     return None
        
    def singleNumber(self, nums: List[int]) -> int:
        """[位操作运算]
        数学公式
        a ^ 0 = a
        a ^ a = 0
        a ^ b ^ a = (a ^ a) ^ b= 0 ^ b = b

        """
        result = 0
        for e in nums:
            result = result ^ e
        return result


class TestSolution:
    def test_singleNumber(self):
        solution = Solution()
        nums = [2, 2, 3, 3]
        assert solution.singleNumber(nums) == 0
        nums = [2, 1, 3, 2, 3]
        assert solution.singleNumber(nums) == 1
        nums = [2]
        assert solution.singleNumber(nums) == 2
        nums = [1, 2, 3, 2, 1, 0, 3]
        assert solution.singleNumber(nums) == 0


if __name__ == "__main__":
    t = TestSolution()
    t.test_singleNumber()