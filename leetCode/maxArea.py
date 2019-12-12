from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """[双指针法]
        时间复杂度：O(n)
        空间复杂度：O(1)
        两个指针，从两侧开始，依次移动两边较小的那一个。
        为什么移动较小的哪一个？
        总面积受限于较小的高度，向内移动时，宽度减少，高度必须增加才能达到更大的面积。如果移动较大的那一边，则面积只可能更小。
        遇到小的那一边，向内移动，为的找到一个更大的高，弥补宽度的减少。
        """
        area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            if height[i] <= height[j]:
                area = max(area, height[i] * (j - i))
                i += 1
            else:
                area = max(area, height[j] * (j - i))
                j -= 1
        return area

    # def maxArea(self, height: List[int]) -> int:
    #     """[两次遍历]
    #     时间复杂度：O(n*n)
    #     空间复杂度：O(1)
    #     """
    #     area = 0
    #     for i in range(len(height)):
    #         for j in range(i, len(height)):
    #             area = max(area, (j - i) * min(height[i], height[j]))
    #     return area


solution = Solution()
assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert solution.maxArea([1, 8]) == 1
assert solution.maxArea([1]) == 0
assert solution.maxArea([1, 9, 6]) == 6
