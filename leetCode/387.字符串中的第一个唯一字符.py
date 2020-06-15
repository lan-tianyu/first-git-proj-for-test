#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
import collections


class Solution:
    # def firstUniqChar(self, s: str) -> int:
    #     """[summary]
    #     哈希表+两次遍历
    #     时间： O(2*N)
    #     空间： O(N)
    #     """
    #     map_s = {}
    #     for e in s:
    #         print(map)
    #         map_s[e] = map_s.get(e, 0) + 1
    #     for i, e in enumerate(s):
    #         if map_s.get(e) == 1:
    #             return i
    #     return -1

    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(s)
        for i, e in enumerate(s):
            if counter.get(e, 0) == 1:
                return i
        return -1


s = Solution()
assert s.firstUniqChar('loveleetcode') == 2
assert s.firstUniqChar('leetcode') == 0
assert s.firstUniqChar('') == -1
# @lc code=end
