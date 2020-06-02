#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        """[summary]
        1. 栈存放左括号，每次遇到右括号，出栈，匹配是否有效一对
        2. map存放左右括号键值对
        """
        map_s = {')': '(', '}': '{', ']': '['}
        stack = []
        for e in s:
            if e in map_s.keys():
                if not stack or stack.pop() != map_s.get(e):
                    return False
            else:
                stack.append(e)
        if stack:
            return False
        return True

    # def isValid(self, s: str) -> bool:
    #     while '{}' in s or '[]' in s or '()' in s:
    #         s = s.replace('()', '')
    #         s = s.replace('{}', '')
    #         s = s.replace('[]', '')
    #     return s == ''


s = Solution()
assert s.isValid(']') is False
assert s.isValid('}{') is False
assert s.isValid('((') is False
assert s.isValid('([)]') is False
assert s.isValid('([]{})') is True
assert s.isValid('([{}]{()})') is True

# @lc code=end
