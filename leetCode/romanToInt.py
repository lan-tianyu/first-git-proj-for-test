class Solution:
    # def romanToInt(self, s: str) -> int:
    #     map_d = {
    #         'I': 1,
    #         'IV': 4,
    #         'V': 5,
    #         'IX': 9,
    #         'X': 10,
    #         'XL': 40,
    #         'L': 50,
    #         'XC': 90,
    #         'C': 100,
    #         'CD': 400,
    #         'D': 500,
    #         'CM': 900,
    #         'M': 1000
    #     }
    #     i = 0
    #     sum_s = 0
    #     len_s = len(s)
    #     while i < len_s-1:
    #         k = s[i:i+2]
    #         v = map_d.get(k)
    #         if v:
    #             sum_s += v
    #             i += 2
    #         else:
    #             sum_s += map_d.get(s[i])
    #             i += 1
    #     if i == len_s-1:
    #         sum_s += map_d.get(s[i])
    #     return sum_s

    # def romanToInt(self, s: str) -> int:
    #     map_d = {
    #         'I': 1,
    #         'IV': 3,
    #         'V': 5,
    #         'IX': 8,
    #         'X': 10,
    #         'XL': 30,
    #         'L': 50,
    #         'XC': 80,
    #         'C': 100,
    #         'CD': 300,
    #         'D': 500,
    #         'CM': 800,
    #         'M': 1000
    #     }
    #     sum_s = 0
    #     for i, e in enumerate(s):
    #         k = s[max(i-1, 0):i+1]
    #         v = map_d.get(k)
    #         if v:
    #             sum_s += v
    #         else:
    #             sum_s += map_d.get(e)
    #     return sum_s

    def romanToInt(self, s: str) -> int:
        map_d = {
            'I': 1,
            'IV': 3,
            'V': 5,
            'IX': 8,
            'X': 10,
            'XL': 30,
            'L': 50,
            'XC': 80,
            'C': 100,
            'CD': 300,
            'D': 500,
            'CM': 800,
            'M': 1000
        }
        return sum(
            map_d.get(s[max(i - 1, 0):i + 1], map_d.get(e))
            for i, e in enumerate(s))


class TestSolution:
    def test_romanToInt(self):
        solution = Solution()
        print(solution.romanToInt('II'))
        print(solution.romanToInt('IV'))
        print(solution.romanToInt('IX'))
        print(solution.romanToInt('IXX'))
        print(solution.romanToInt('LVIII'))
        print(solution.romanToInt('MCMXCIV'))


if __name__ == '__main__':
    test = TestSolution()
    test.test_romanToInt()