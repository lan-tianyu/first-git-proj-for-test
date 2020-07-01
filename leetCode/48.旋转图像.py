#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
from copy import deepcopy
from typing import List


class Solution:
    # def rotate(self, matrix: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     转换公式
    #     (i, j) --> (j, n-1-i)
    #     深拷贝matrix，时间O(N^2)，空间O(N^2)
    #     """
    #     n = len(matrix)
    #     tmp = deepcopy(matrix)
    #     for i in range(n):
    #         for j in range(n):
    #             matrix[j][n - 1 - i] = tmp[i][j]

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        转换公式
        (i, j) --> (j, n-1-i)，即matrix[j][n-1-i] = matrix[i][j]
        以n=3的matrix举例
        以第一行为基准开始顺时针旋转，从第一个元素开始旋转
        (0,0)-->(0,n-1)-->(n-1,n-1)-->(n-1,0)-->(0,0)
        相当于每一条边都旋转了一次
        然后旋转第一行第二个元素，由于最后一个元素是第一个元素旋转过来的，所以不需要旋转
        -----
        继续以n=5的matrix举例
        最外层旋转完，进入row=1的层，col初始值为1。旋转四条边后是对称的，所以col末尾减-1，row截止条件是n//2
        
        时间O(N^2)，空间O(1)
        """
        n = len(matrix)
        for row in range(n // 2):
            for col in range(row, n - 1 - row):
                # i, j = row, col
                # pre = matrix[i][j]
                # for _ in range(4):
                #     next_i, next_j = j, n-1-i
                #     next = matrix[next_i][next_j]
                #     matrix[next_i][next_j] = pre
                #     i, j = next_i, next_j
                #     pre = next
                # 不用循环，一行代码实现四个数据交换
                # matrix[col][n - 1 - row], matrix[n - 1 - row][n - 1 - col], matrix[n - 1 - col][row], matrix[row][col] = matrix[row][col], matrix[col][n - 1 - row], matrix[n - 1 - row][n - 1 - col], matrix[n - 1 - col][row]
                # 换成容易看的，matrix[j][n-1-i] = matrix[i][j]
                temp = matrix[n - 1 - col][row]
                matrix[n - 1 - col][row] = matrix[n - 1 - row][n - 1 - col]
                matrix[n - 1 - row][n - 1 - col] = matrix[col][n - 1 - row]
                matrix[col][n - 1 - row] = matrix[row][col]
                matrix[row][col] = temp


s = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s.rotate(matrix)
print(matrix)

# @lc code=end
