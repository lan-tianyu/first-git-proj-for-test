#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """[summary]
        1. map_s存放当前遍历过元素的最新索引；count存放当前最长的子串长度；
        2. base标记当前无重复子串的开始前一个位置；当前无重复子串长度为：当前索引index-base
        3. 遍历规则，当前元素在map中，则需要重置base值，base值为历史base值与当前元素在map中的索引的最大值---- 很重要
        4. 遍历规则，每次需要更新map中当前元素最新索引
        5. 遍历规则，count为历史count中与当前无重复子串的长度中最大值
        """
        map_s = {}
        base, count = -1, 0
        for i, e in enumerate(s):
            if e in map_s:
                base = max(base, map_s.get(e))
            map_s[e] = i
            count = max(count, i-base)
        return count


s = Solution()
assert s.lengthOfLongestSubstring('aaa') == 1
assert s.lengthOfLongestSubstring('abcdedcba') == 5
assert s.lengthOfLongestSubstring('abcdedcbaef') == 6
assert s.lengthOfLongestSubstring('pwwkew') == 3


# @lc code=end

