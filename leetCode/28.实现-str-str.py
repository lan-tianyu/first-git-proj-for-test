#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#


# @lc code=start
class Solution:
    # def strStr(self, haystack: str, needle: str) -> int:
    #     """[summary]
    #     1. 双指针法
    #     """
    #     m = len(needle)
    #     n = len(haystack)
    #     i, j = 0, 0
    #     while i < m and j < n and m - i <= n - j:
    #         if needle[i] == haystack[j]:
    #             i += 1
    #             j += 1
    #         elif i:
    #             j = j - i + 1
    #             i = 0
    #         else:
    #             j += 1
    #     return j-i if i == m else -1

    # def strStr(self, haystack: str, needle: str) -> int:
    #     """[summary]
    #     匹配机制
    #     1. 如果haystack[start:start+m] == needle则说明找到了
    #     2. start边界值，最大值满足strt+m==len(haystack)，说明start<len(haystack)-m+1
    #     3. 异常场景：两个一样长
    #     4. 异常场景：haystack长度小于needle
    #     时间：O((N-L)L)
    #     空间：O(1)
    #     """
    #     m = len(needle)
    #     n = len(haystack)
    #     for start in range(0, n-m+1):
    #         if haystack[start:start+m] == needle:
    #             return start
    #     return -1

    def strStr(self, haystack: str, needle: str) -> int:
        """[summary]
        双指针法
        1. i指向needle当前元素，j指向haystack当前元素
        2. 当i元素与j元素值一致，则都自增1
        3. 当i元素与j元素值不一致，如果i==0，j自增1，i不自增
        4. 当i元素与j元素值不一致，如果i!=0，i要从头开始，j也要重置位置。
        由步骤2可推导出，j-i位置一定与i==0值相等时才会都自增1，haystack的j-i个元素已经和needle的i=0元素比较过了，所以needle指针i重置为0时，先haystack指针j重置为j-i+1，后指针i重置为0，
        5. 边界值：两个字符串长度一致；needle 长度大于haystack长度；needle为空；两个字符串为空
        6. 循环跳出条件之一：当i指针及以后元素个数大于j指针及以后元素个数

        时间：最优是O(N)，最差是O((N-L)L)，每次差最后一个元素不匹配，则又得重来
        """
        m = len(needle)
        n = len(haystack)
        i, j = 0, 0
        while i < m and j < n and m - i <= n - j:
            if needle[i] == haystack[j]:
                i += 1
                j += 1
            elif i == 0:
                j += 1
            else:
                j = j - i + 1
                i = 0
        return j - i if i == m else -1


s = Solution()
assert s.strStr('aababcde', '') == 0
assert s.strStr('aababcde', 'abc') == 3
assert s.strStr('aababcde', 'aabc') == -1
assert s.strStr('aababcde', 'b') == 2
assert s.strStr('abab', 'abc') == -1
assert s.strStr('ab', 'abc') == -1
assert s.strStr('ab', 'ab') == 0
assert s.strStr('mississippi', 'issip') == 4
# @lc code=end
