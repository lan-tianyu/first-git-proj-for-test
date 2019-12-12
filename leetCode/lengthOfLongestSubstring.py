class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map_d = {}
        base = -1
        count = 0
        for i, e in enumerate(s):
            base = max(base, map_d.get(e, -1))
            count = max(count, i - base)
            map_d[e] = i
        return count


solution = Solution()
assert solution.lengthOfLongestSubstring('abcde') == 5
assert solution.lengthOfLongestSubstring('abcdeabc') == 5
assert solution.lengthOfLongestSubstring('abccbad') == 4
assert solution.lengthOfLongestSubstring('abcdcba') == 4
assert solution.lengthOfLongestSubstring('pwwkew') == 3
