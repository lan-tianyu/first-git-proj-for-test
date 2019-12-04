class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_d = {')': '(', ']': '[', '}': '{'}
        for x in s:
            y = map_d.get(x)
            if y is None:
                stack.append(x)
            elif not stack or stack.pop() != y:
                return False
        return stack == []


solution = Solution()
assert solution.isValid('(') is False
assert solution.isValid('}') is False
assert solution.isValid('][') is False
assert solution.isValid('()[]{}') is True
assert solution.isValid('{([])}') is True
assert solution.isValid('(]') is False
assert solution.isValid('([)]') is False
assert solution.isValid('()[]]]') is False
assert solution.isValid('()[') is False
