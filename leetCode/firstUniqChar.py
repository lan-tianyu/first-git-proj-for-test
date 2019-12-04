class Solution:
    # def firstUniqChar(self, s: str) -> int:
    #     map_d = {}
    #     for i, e in enumerate(s):
    #         count = map_d.get(e, {}).get('count', 0) + 1
    #         map_d[e] = dict(count=count, index=i)
    #     arr = []
    #     for k, v in map_d.items():
    #         if v.get('count') == 1:
    #             arr.append(v.get('index'))
    #     if not arr:
    #         return -1
    #     arr.sort()
    #     return arr[0]

    def firstUniqChar(self, s: str) -> int:
        map_d = {}
        for i, e in enumerate(s):
            map_d[e] = map_d.get(e, 0) + 1
        for i, e in enumerate(s):
            if map_d.get(e) == 1:
                return i
        return -1
        

if __name__ == '__main__':
    solution = Solution()
    s = "leetcode"
    assert solution.firstUniqChar(s) == 0
    s = "loveleetcode"
    assert solution.firstUniqChar(s) == 2
    s = "lool"
    assert solution.firstUniqChar(s) == -1