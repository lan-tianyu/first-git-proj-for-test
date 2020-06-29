#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from typing import List


class Node:
    def __init__(self, cur_str, left, right):
        self.res = cur_str
        self.left = left
        self.right = right


class Solution:
    # def generateParenthesis(self, n: int) -> List[str]:
    #     """[summary]
    #     深度优先法，节点个数递减法
    #     1. 当前有n个左括号和n个有括号，当前字符串是''
    #     2. 递归处理
    #     a 当左括号个数大于右括号个数，说明右括号使用了，此时直接返回，不使用该结果
    #     b 当左括号大于0，可以继续递归 cur+'('
    #     c 当右括号大于0，可以继续递归 cur+')'
    #     d 当左括号个数和右括号个数都是0，则已经递归完，添加到结果，返回
    #     """
    #     res = []
    #     cur_str = ''

    #     def dfs(cur, left, right):
    #         if left == 0 and right == 0 :
    #             res.append(cur)
    #             return
    #         if left > right:
    #             return
    #         if left > 0:
    #             dfs(cur + '(', left-1, right)
    #         if right > 0:
    #             dfs(cur + ')', left, right-1)
    #     dfs(cur_str, n, n)
    #     return res

    # def generateParenthesis(self, n: int) -> List[str]:
    #     """[summary]
    #     深度优先法，节点个数递增法
    #     1. 当前有n个左括号和n个有括号，当前字符串是''
    #     2. 递归处理
    #     a 当左括号个数小于右括号个数，说明右括号使用了，此时直接返回，不使用该结果
    #     b 当左括号小于n，可以继续递归 cur+'('
    #     c 当右括号小于n，可以继续递归 cur+')'
    #     d 当左括号个数和右括号个数都是n，则已经递归完，添加到结果，返回
    #     """
    #     res = []
    #     cur_str = ''

    #     def dfs(cur, left, right, n):
    #         if left == n and right == n:
    #             res.append(cur)
    #             return
    #         if left < right:
    #             return
    #         if left < n:
    #             dfs(cur + '(', left + 1, right, n)
    #         if right < n:
    #             dfs(cur + ')', left, right + 1, n)

    #     dfs(cur_str, 0, 0, n)
    #     return res

    def generateParenthesis(self, n: int) -> List[str]:
        dp = [None for _ in range(n + 1)]
        dp[0] = [""]
        for i in range(1, n + 1):
            cur = []
            for j in range(i):
                left = dp[j]
                right = dp[i - 1 - j]
                for s1 in left:
                    for s2 in right:
                        cur.append('(' + s1 + ')' + s2)
            dp[i] = cur
        return dp[n]


s = Solution()
print(s.generateParenthesis(2))
print(s.generateParenthesis(3))
print(s.generateParenthesis(6))

# @lc code=end
