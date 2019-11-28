from typing import List


class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     """[排序法]
    #     python 的排序时间复杂度： O(NlogN)
    #     空间复杂度：O(1)，就地排序
    #     """
    #     if not nums:
    #         return None
    #     nums.sort()
    #     return(nums[(len(nums) - 1)//2])

    def majorityElement(self, nums: List[int]) -> int:
        """[哈希表法]
        时间复杂度：O(n+n), O(n)
        空间复杂度：O(n)
        """
        if not nums:
            return None
        map_d = {}
        major_len = (len(nums)) // 2
        for e in nums:
            count = map_d.get(e, 0)
            count += 1
            map_d[e] = count
        for k, v in map_d.items():
            print(k, v)
            if v > major_len:
                return k
        return None


class TestSolution:
    def test_majorityElement(self):
        solution = Solution()
        nums = [2,2,1,1,1,2,2]
        assert solution.majorityElement(nums) == 2
        nums = [2,1,1]
        assert solution.majorityElement(nums) == 1
        nums = [2,1,3,3,3]
        assert solution.majorityElement(nums) == 3
        nums = []
        assert solution.majorityElement(nums) is None
        nums = [1]
        assert solution.majorityElement(nums) == 1
        
        
if __name__ == '__main__':
    test = TestSolution()
    test.test_majorityElement()