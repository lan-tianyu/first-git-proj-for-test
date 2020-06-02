#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
from typing import List


class Solution:
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     """[summary]
    #     1. 反转
    #     2. 加1进位，第一位的进位可以认为是1，后续根据十进制进行进位
    #     3. 最后一位有进位，则要加一位
    #     4. 反转
    #     """
    #     if not digits:
    #         return digits
    #     digits = digits[::-1]
    #     n = len(digits)
    #     carry = 1
    #     for i in range(0, n):
    #         e = digits[i] + carry
    #         digits[i] = e % 10
    #         carry = e // 10
    #     if carry:
    #         digits.append(carry)
    #     digits = digits[::-1]
    #     return digits
    def plusOne(self, digits: List[int]) -> List[int]:
        """[summary]
        1. 从最后一位遍历，最后一位加1。
        2. 如果加1后最后一位大于等于10，则后续都要进位1；否则，直接返回
        时间： 最坏O(N)，最好O(1)
        空间： O(1)
        """
        n = len(digits)
        for i in range(n - 1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            digits[i] = digits[i] % 10
        digits.insert(0, 1)
        # digits = [1] + digits
        return digits


s = Solution()
digits = [1, 2, 3]
assert s.plusOne(digits) == [1, 2, 4]
digits = [9]
assert s.plusOne(digits) == [1, 0]
digits = [1, 9, 9]
assert s.plusOne(digits) == [2, 0, 0]
# @lc code=end
