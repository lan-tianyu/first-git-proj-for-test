import re


class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     """[]
    #     1. 忽略大小写
    #     2. 只有数字和字符
    #     """
    #     def _isalnum(s):
    #         return re.match(r'\w', s) is not None

    #     tmp_str = ''.join(filter(_isalnum, str(s))).lower()
    #     n = len(tmp_str)
    #     for i in range(n // 2):
    #         if tmp_str[i] != tmp_str[n - 1 - i]:
    #             return False
    #     return True

    def isPalindrome(self, s: str) -> bool:
        """[]
        1. 忽略大小写
        2. 只有数字和字符
        """
        tmp_str = ''.join(filter(str.isalnum, str(s))).lower()
        # n = len(tmp_str)
        # for i in range(n // 2):
        #     if tmp_str[i] != tmp_str[n - 1 - i]:
        #         return False
        # return True
        return tmp_str[:] == tmp_str[::-1]


if __name__ == '__main__':
    solution = Solution()
    assert solution.isPalindrome("") is True
    assert solution.isPalindrome("A man, a plan, a canal: Panama") is True
    assert solution.isPalindrome("race a car") is False
    assert solution.isPalindrome("11<2 2 ,11") is True
