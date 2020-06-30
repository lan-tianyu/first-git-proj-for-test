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
    #     递归法，剩余节点递减法
    #     1. left标识左括号剩余个数，right标识右括号剩余个数，初始值均是n，结束值均是0
    #     2. 当left==0 and right==0，说明左括号右括号消耗完了，保存当前结果，然后返回
    #     3. 当left>right，说明上一层多消耗了一个右括号，放弃这个结果，返回
    #     4. 当left>0，进入下一层递归，left-1，当前字符串后面加左括号
    #     5. 当right>0，进入下一层递归，right-1，当前字符串后面加右括号

    #     重点在，进入下一层递归时，左右括号加在什么位置
    #     我们可以画下上述递归方法生成树的过程，n设置为2，就可以得出结论
    #     """
    #     res = []
    #     cur_str = ''

    #     def dfs(cur, left, right):
    #         if left == 0 and right == 0:
    #             res.append(cur)
    #             return
    #         if left > right:
    #             return
    #         if left > 0:
    #             dfs(cur+'(', left-1, right)
    #         if right > 0:
    #             dfs(cur+')', left, right-1)
        
    #     dfs(cur_str, n, n)
    #     return res

    # def generateParenthesis(self, n: int) -> List[str]:
    #     """[summary]
    #     递归法，剩余节点递增法
    #     1. left标识左括号个数，right标识右括号个数，初始值均是0，结束值均是n
    #     2. 当left==n and right==n，说明左括号右括号消耗完了，保存当前结果，然后返回
    #     3. 当left<right，说明上一层多消耗了一个右括号，放弃这个结果，返回
    #     4. 当left<n，进入下一层递归，left+1，当前字符串后面加左括号
    #     5. 当right<n，进入下一层递归，right+1，当前字符串后面加右括号

    #     重点在，进入下一层递归时，左右括号加在什么位置
    #     我们可以画下上述递归方法生成树的过程，n设置为2，就可以得出结论
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
    #             dfs(cur+'(', left+1, right, n)
    #         if right < n:
    #             dfs(cur+')', left, right+1, n)
        
    #     dfs(cur_str, 0, 0, n)
    #     return res

    def generateParenthesis(self, n: int) -> List[str]:
        """[summary]
        动态规划
        状态转移方程
        dp[i] = (dp[j]) + dp[i-1-j]
        """ 
        dp = [None for _ in range(n+1)]
        dp[0] = ['']
        for i in range(1, n+1):
            cur = []
            for j in range(i):
                left = dp[j]
                right = dp[i-1-j]
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
