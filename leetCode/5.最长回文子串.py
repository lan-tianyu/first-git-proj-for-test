#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#


# @lc code=start
class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     """[summary]
    #     动态规划法
    #     假设s[i:j] 是回文子串，则是s[i+1:j-1]必然是回文子串，且s[i]==s[j]
    #     这里假定i>=j, i<j 已经覆盖了的，相当于i,j交换值。
    #     动态规划状态方程：
    #     dp[i][j] = dp[i+1][j-1] and s[i] == s[j]

    #     1. 初始化dp为长度各为n的二位数组，当i==j场景下，只有一个字符，默认都是回文字符串
    #     2. 初始化ans最长回文子串，为s[0]
    #     3. dp动态生成，每次遍历，步长固定增加1
    #     4. 当dp[i][j] 为True，则说明s[i:j+1]是回文字符串，需要对比之前ans，取长的
    #     """
    #     if not s:
    #         return ''
    #     n = len(s)
    #     ans = s[0]
    #     dp = [[False if x != y else True for x in range(n)] for y in range(n)]
    #     for k in range(1, n):
    #         for i in range(0, n - k):
    #             j = i + k
    #             if k == 1:
    #                 dp[i][j] = (s[i] == s[j])
    #             else:
    #                 dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
    #             if dp[i][j] and k + 1 > len(ans):
    #                 ans = s[i:j + 1]
    #     return ans

    def longestPalindrome(self, s: str) -> str:
        """[summary]
        中心扩展法
        上面的动态规划解法中，我们得到了两个中心，一个奇数点，一个对称点
        1. s[i:i+1]必然是回文字符串，通过这个中心向外扩散，是s[i-1:i+2]是否是回文，取决于是s[i-1] == s[i+1]
        2. s[i:i+2]是否是回文字符串，取决于是s[i]==s[i+1]，通过这个中心向外扩展，则s[i-1:i+3]，取决于s[i-1] == s[i+2]
        3. s中每一个元素都可能是是一个中心点，但因为奇数点不需要判断，我决定从第二个元素开始
        """
        def _expandAroundCenter(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left+1, right-1
        
        start, end = 0, 0
        for i in range(len(s)):
            print('=' * 70)
            left, right = _expandAroundCenter(s, i, i)
            if end - start < right-left:
                start, end = left, right
            print(start, end, left, right, '--1')
            left, right = _expandAroundCenter(s, i, i+1)
            if end - start < right-left:
                start, end = left, right
            print(start, end, left, right, '--2')
        return s[start:end+1]


s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
# @lc code=end
