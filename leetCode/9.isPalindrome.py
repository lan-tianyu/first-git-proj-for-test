#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#


# @lc code=start
class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     """[summary]
    #     1. 字符串倒序
    #     2. 倒序后与元数据一致则是回文
    #     """
    #     if x < 0:
    #         return False
    #     str_x = str(x)
    #     str_x = str_x[::-1]
    #     print(str_x, int(str_x))
    #     if x == int(str_x):
    #         return True
    #     return False

    # def isPalindrome(self, x: int) -> bool:
    #     """[summary]
    #     1. 中位为中轴线，左右完全对称
    #     2. 长度为奇数，则中位索引是N-1//2，向左向右开始比较
    #     3. 长度为偶数，则中位是N-1//2， N//2,中位开始向左向右比较
    #     """
    #     str_x = str(x)
    #     n = len(str(x))
    #     if n % 2:
    #         i, j = (n - 1) // 2 - 1, (n - 1) // 2 + 1
    #     else:
    #         i, j = (n - 1) // 2, n // 2
    #     while i > -1 and j < n:
    #         if str_x[i] == str_x[j]:
    #             i -= 1
    #             j += 1
    #         else:
    #             return False
    #     return True

    def isPalindrome(self, x: int) -> bool:
        
        


s = Solution()
assert s.isPalindrome(-123) is False
assert s.isPalindrome(121) is True
assert s.isPalindrome(1221) is True
assert s.isPalindrome(1) is True
assert s.isPalindrome(10) is False
# @lc code=end
