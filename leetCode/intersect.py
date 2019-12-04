from typing import List


class Solution:
    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     """[先排序+双指针方法]
    #     时间: max(O(nlogn), O(mlogm), n, m)
    #     空间：O(1)
    #     """
    #     nums1.sort()
    #     nums2.sort()
    #     i, j = 0, 0
    #     ans = []
    #     while i < len(nums1) and j < len(nums2):
    #         if nums1[i] < nums2[j]:
    #             i += 1
    #         elif nums1[i] > nums2[j]:
    #             j += 1
    #         else:
    #             ans.append(nums1[i])
    #             i += 1
    #             j += 1
    #     return ans

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """[哈希表法]
        map存放短的数组
        遍历长的数组，检查是否在map中
        """
        m, n = len(nums1), len(nums2)
        map_d = {}
        ans = []
        for e in nums1 if m < n else nums2:
            map_d[e] = map_d.get(e, 0) + 1
        for x in nums2 if m < n else nums1:
            if map_d.get(x, 0):
                ans.append(x)
                map_d[x] -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    # assert s.intersect([1, 2, 3, 2, 4], [2, 5, 3, 2]) == [2, 2, 3]
    print(s.intersect([1, 2, 3, 2, 4], [2, 5, 3, 2]))
    assert s.intersect([1, 2, 3, 2, 4], []) == []
    assert s.intersect([], [1, 2, 3, 2, 4]) == []
    assert s.intersect([4], [1, 2, 3, 2, 4]) == [4]
