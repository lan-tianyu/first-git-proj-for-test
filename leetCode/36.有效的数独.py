#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """[summary]
        数独有9列，数字是1-9，列index和数值-1对应起来
        如果数字存在，则对应的index值标记为1，初始值是0，后续遍历过程中，出现相同的元素，则对应index值不为1
        """
        row = [[0 for _ in range(9)] for _ in range(9)]
        col = [[0 for _ in range(9)] for _ in range(9)]
        box = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                val = int(board[i][j]) - 1
                box_index = i // 3 * 3 + j // 3
                if row[i][val] == 0 and col[j][val] == 0 and box[box_index][
                        val] == 0:
                    row[i][val] = 1
                    col[j][val] = 1
                    box[box_index][val] = 1
                else:
                    return False
        return True


nums = [["1", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

s = Solution()
print(s.isValidSudoku(nums))

# @lc code=end
