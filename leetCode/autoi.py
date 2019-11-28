import re


class Solution:
    def myAtoi(self, str: str) -> int:
        pattern = r'^[\+\-]?\d+'
        # m = re.match(pattern, str.strip())
        m = re.findall(pattern, str.strip())
        if m:
            #  int_n = int(m.group(0))
            int_n = int(m[0])
            return max(int_n, -2**31) if int_n < 0 else min(int_n, 2**31-1)
        return 
    

if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi('    -'))
    print(s.myAtoi('    +'))
    print(s.myAtoi('    +-  '))
    print(s.myAtoi('    -42'))
    print(s.myAtoi('    -42aa4354a   '))
    print(s.myAtoi('    +42aa4354a   '))
    print(s.myAtoi('    42aa4354a   '))
    print(s.myAtoi("4193 with words"))
    print(s.myAtoi("words and 987"))
    print(s.myAtoi("-91283472332"))
    print(s.myAtoi("91283472332  91283472332"))
