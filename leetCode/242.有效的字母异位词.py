#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
import collections


class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return len(s) == len(t) and sorted(s) == sorted(t)

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = collections.defaultdict(int)
        for i in range(len(s)):
            d[s[i]] = d[s[i]] + 1
            d[t[i]] = d[t[i]] - 1
        for k, v in d.items():
            if v != 0:
                return False
        return True


s = Solution()
assert s.isAnagram("anagram", "anagram") is True
assert s.isAnagram("rat", "car") is False
assert s.isAnagram("rat", "rate") is False
# @lc code=end
