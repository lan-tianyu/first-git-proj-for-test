from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """[python处理方式zip]
        1. 将每个字符串作为一个可遍历的对象
        2. zip所有字符串，结果纵向长度为所有子串最短的，横向长度为子串的个数
        3. zip后的结果，每一行的元素为每一个子串的同一个位置的元素
        """
        s_list = []
        for s in zip(*strs):
            if len(set(s)) == 1:
                s_list.append(s[0])
        return ''.join(s_list)

    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     """[python ascii码排序]
    #     根据字符串的字符ascii码比较大小，最终比较的肯定是最长与最小之间的公共头
    #     """
    #     if not strs:
    #         return ''
    #     str1 = min(strs)
    #     str2 = max(strs)
    #     for i, e in enumerate(str1):
    #         if str2[i] != e:
    #             return str1[:i]
    #     return str1

    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     """[python 水平扫描法]
    #     """
    #     if not strs:
    #         return ''
    #     str1 = strs[0]
    #     n = len(strs)
    #     for i, e in enumerate(str1):
    #         for j in range(1, n):
    #             ss = strs[j]
    #             if i >= len(ss) or ss[i] != e:
    #                 return str1[:i]
    #     return str1


solution = Solution()
strs = ['fliwht', 'fliw', 'fliwer']
assert solution.longestCommonPrefix(strs) == 'fliw'
strs = ['flight', 'flow', 'flower']
assert solution.longestCommonPrefix(strs) == 'fl'
strs = ['dog', 'racecar', 'car']
assert solution.longestCommonPrefix(strs) == ''