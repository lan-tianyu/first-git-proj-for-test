#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        二分法找到target所在的行，再用二分法找到目标行中对应的列。找不到返回false。

        1、中间行第一个元素等于target，则返回True
        2、中间行第一个元素大于target，则目标行向低位查询，high=m-1
        3、中间行第一个元素小于target，则目标行向高位查询，low=m+1
        4、退出循环，假设high<low，且high=-1，说明target小于最小元素，返回False；其实可以不判断，matrix[-1]是倒序索引，不会报错
        5、当high<low场景，说明目标行在high行，退出循环后中间行要重新计算；其实等于high也没关系
        6、当high=low场景，这个场景在步骤1就返回True，这里不需要考虑。

        时间：O(log(m) + log(n))
        空间：O(1)
        '''
        print('-' * 80)
        if not matrix:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        if cols == 0:
            return False
        # if target < matrix[0][0] or target > matrix[rows-1][cols-1]:
        #     return False
        low, high = 0, rows - 1 
        while low <= high:
            m = (low + high) // 2
            print('low, high, m', low, high, m)
            if matrix[m][0] == target:
                return True
            if matrix[m][0] > target:
                high = m - 1
            else:
                low = m + 1
        print('low, high, m', low, high, m)
        if high < -1:
            return False
        left, right = 0, cols - 1
        while left <= right:
            n = (left + right) // 2
            print('left, right, n', left, right, n)
            if matrix[high][n] == target:
                return True
            if matrix[high][n] > target:
                right = n - 1
            else:
                left = n + 1
        return False


s = Solution()
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
assert s.searchMatrix(matrix, 3) is True
assert s.searchMatrix(matrix, 0) is False
assert s.searchMatrix(matrix, 9) is False
assert s.searchMatrix(matrix, 20) is True
assert s.searchMatrix(matrix, 23) is True
assert s.searchMatrix(matrix, 51) is False
assert s.searchMatrix([], 3) is False
assert s.searchMatrix([[]], 3) is False
# @lc code=end
