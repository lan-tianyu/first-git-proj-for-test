#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """[summary]
        递归法
        1. ans 初始化为['']，每次递归的结果更新ans
        2. 遍历每一个digit，遍历每一个当前digit的对应的每一个字符， 遍历上次结果ans， 两者相加，存放在中间结果tmp
        3. 中间结果赋值给ans
        特殊场景， digits为空，直接返回空
        """
        KEY = {
            '0': '',
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        # if not digits:
        #     return []
        # ans = ['']
        # for num in digits:
        #     tmp = []
        #     for char in KEY[num]:
        #         for pre in ans:
        #             tmp.append(pre+char)
        #     ans = tmp
        # return ans

        if not digits:
            return []
        ans = ['']
        for num in digits:
            ans = [pre + char for pre in ans for char in KEY[num]]
        return ans


s = Solution()
print(s.letterCombinations('239'))
# @lc code=end
