#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """[summary]
        1. count标识最长的无重复子串长度
        2. i标识无重复子串最开始的位置, j标识无重复子串末尾的位置
        3. d为保存元素出现的位置
        4. 出现重复元素，则取d中元素上一次出现的位置与当前i的位置，取大。后面出现的重复元素可能在最开始出现了，不能直接赋值为重复元素上一个位置 
        5. 更新d中元素的位置
        6. 最长子串长度为max(count, j-i+1)
        """
        i, count = -1, 0
        d = {}
        for j, e in enumerate(s):
            if d.get(e) is not None:
                i = max(i, d[e])
            count = max(count, j - i)
            d[e] = j
        return count


s = Solution()
assert s.lengthOfLongestSubstring("abcabcbb") == 3
assert s.lengthOfLongestSubstring("bbb") == 1
assert s.lengthOfLongestSubstring("pwwkew") == 3
# @lc code=end
