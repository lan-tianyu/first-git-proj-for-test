class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        first = -1
        last = 0
        map_d = {}
        for i, e in enumerate(s):
            if e in map_d:
                # 考虑 abba， abccba这种场景
                first = max(map_d.get(e), first)
                map_d[e] = i
                last = i
            else:
                map_d[e] = i
                last = i
            count = max(count, last-first)
        return count


class TestSolution():
    def test_lengthOfLongestSubstring(self):
        s = Solution()
        ss1 = 'dddd'
        print(s.lengthOfLongestSubstring(ss1))
        ss1 = 'abcdabc'
        print(s.lengthOfLongestSubstring(ss1))
        ss1 = 'abcabcdaef'
        print(s.lengthOfLongestSubstring(ss1))
        ss1 = 'pwwkew'
        print(s.lengthOfLongestSubstring(ss1))
        ss1 = 'abba'
        print(s.lengthOfLongestSubstring(ss1))
        

if __name__ == '__main__':
    test = TestSolution()
    test.test_lengthOfLongestSubstring()

