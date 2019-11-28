import pytest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map_d = {}
        first = -1
        last = 0
        max_count = 0
        for i, e in enumerate(s):
            if e in map_d:
                first = max(first, map_d.get(e))
                last = i
                map_d[e] = i
            else:
                last = i
                map_d[e] = i
            max_count = max((last - first), max_count)
        return max_count


class TestSolution:
    def test_lengthOfLongestSubstring(self):
        s = Solution()
        print(s.lengthOfLongestSubstring("abcabcbb"))  # 3
        print(s.lengthOfLongestSubstring("abccba"))   # 3
        print(s.lengthOfLongestSubstring("abccbaef"))   # 5
        print(s.lengthOfLongestSubstring("pppp"))   # 1
        print(s.lengthOfLongestSubstring("abcdefcbaffabc"))   # 6




if __name__ == '__main__':
    test = TestSolution()
    test.test_lengthOfLongestSubstring()

