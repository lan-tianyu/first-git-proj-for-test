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
    #     1. 双指针法，p指针从头到尾，q指针从尾到头，依次比较位置上的元素是否一致，不一致，返回False
    #     2. 循环结束条件，p<=q
    #     时间：O(N) 数字的位数大小
    #     空间：O(N) 数字的位数大小
    #     """
    #     str_x = str(x)
    #     p, q = 0, len(str(x)) - 1
    #     while p < q:
    #         if str_x[p] != str_x[q]:
    #             return False
    #         p += 1
    #         q -= 1
    #     return True

    def isPalindrome(self, x: int) -> bool:
        """[summary]
        数学法，数字x后半部分与前一半值一致，则是回文数字
        1. 怎么判断已经反转一半了？前半部分的数值小于后半部分的数值
        2. 异常条件：负数直接返回False
        3. 异常条件：末尾是0的数字直接返回False，0除外
        4. 数字个数为奇数，怎么判断是否一致？

        时间：O(log10(x))   数字每次都除以10
        空间：
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        reversion = 0
        while x > reversion:
            t = x % 10
            reversion = reversion * 10 + t
            x = x // 10
        return x == reversion or x == reversion // 10


s = Solution()
assert s.isPalindrome(-123) is False
assert s.isPalindrome(121) is True
assert s.isPalindrome(1221) is True
assert s.isPalindrome(1) is True
assert s.isPalindrome(10) is False
# @lc code=end
