#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """[summary]
        python 的 min方法，然后比较第一个和最后一个的公共前缀
        """
        if not strs:
            return ''
        min_str = min(strs)
        max_str = max(strs)
        i = 0
        pre_fix_list = []
        while i < len(min_str) and i < len(max_str):
            if min_str[i] != max_str[i]:
                break
            pre_fix_list.append(min_str[i])
            i += 1
        return ''.join(pre_fix_list)

    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     """[summary]
    #     python的zip方法，相当于把strs看成一个二维数组，每个元素是一行，zip操作相当于把每一列转成一行。
    #     1. zip之后，如果是公共前缀元素，set去重之后只有元素
    #     2. 公共前缀的另一个条件就是连续。
    #     """
    #     if not strs:
    #         return ''
    #     pre_fix_list = []
    #     zip_strs = list(map(set, zip(*strs)))
    #     for e in zip_strs:
    #         if len(e) > 1:
    #             break
    #         pre_fix_list.append(list(e)[0])
    #     return ''.join(pre_fix_list)

    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     """[summary]
    #     水平扫描法，从第一个字符串第一个元素开始，依次对比strs中的其他元素
    #     时间：最坏场景是O(S)，S是strs所有字符串长度
    #     空间：O(1)，常数级别存储数据
    #     """
    #     if not strs:
    #         return ''
    #     for i, e in enumerate(strs[0]):
    #         for j in range(1, len(strs)):
    #             if i == len(strs[j]) or e != strs[j][i]:
    #                 return strs[0][:i]
    #     return strs[0]

    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     """[summary]
    #     分治法
    #     1. strs的最长前缀 LCP(strs, 0, mid),LCP(strs, mid+1, n)的最长前缀
    #     2. 分治法最小集合，左边

    #     """
    #     if not strs:
    #         return ''
    #     return self._longestCommonPrefix(strs, 0, len(strs) - 1)

    # def _longestCommonPrefix(self, strs, left, right):
    #     if left == right:
    #         return strs[left]
    #     mid = (left + right) // 2
    #     left_lcp = self._longestCommonPrefix(strs, 0, mid)
    #     right_lcp = self._longestCommonPrefix(strs, mid + 1, right)
    #     return self._common_str(left_lcp, right_lcp)

    # def _common_str(self, str1, str2):
    #     m = min(len(str1), len(str2))
    #     for i in range(m):
    #         if str1[i] != str2[i]:
    #             return str1[:i]
    #     return str1[:m]


s = Solution()
assert s.longestCommonPrefix(["flower", "flow", "flight"]) == 'fl'
assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ''
assert s.longestCommonPrefix(["abc", "abcd", "ab"]) == 'ab'
assert s.longestCommonPrefix(["abc", "abcd", "abcde"]) == 'abc'
assert s.longestCommonPrefix(["aa", "aa", "aa"]) == 'aa'
# @lc code=end
