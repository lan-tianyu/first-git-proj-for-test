#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
# class MinStack:
#     """[summary]
#     最小栈与栈数据不一致
#     """    
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.min_stack = []        

#     def push(self, x: int) -> None:
#         self.stack.append(x)
#         if not self.min_stack or x <= self.min_stack[-1]:
#             self.min_stack.append(x)
        
#     def pop(self) -> None:
#         num = self.stack.pop()
#         if num == self.min_stack[-1]:
#             self.min_stack.pop()
#         return num

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.min_stack[-1]


# class MinStack:
#     """[summary]
#     最小栈与栈数据一致
#     """    
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.min_stack = []        

#     def push(self, x: int) -> None:
#         self.stack.append(x)
#         if not self.min_stack or x <= self.min_stack[-1]:
#             self.min_stack.append(x)
#         else:
#             num = self.min_stack[-1]
#             self.min_stack.append(num)
        
#     def pop(self) -> None:
#         self.min_stack.pop()
#         return self.stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.min_stack[-1]

# class MinStack:
#     """[summary]
#     最小值存储在一个变量里，当前最小值小于上一个最小值，则将上一个最小值放入栈中
#     """    
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.min_num = 2 ** 31 - 1

#     def push(self, x: int) -> None:
#         if not self.stack:
#             self.stack.append(x)
#             self.min_num = x
#         elif x <= self.min_num:
#             self.stack.append(self.min_num)
#             self.min_num = x
#         self.stack.append(x)

#     def pop(self) -> None:
#         num = self.stack.pop()
#         if num == self.min_num:
#             self.min_num = self.stack[-1]
#             self.stack.pop()
#         return num

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.min_num

class ListNode:
    def __init__(self, x, min_num):
        self.val = x
        self.min_num = min_num
        self.next = None


class MinStack:
    """[summary]
    最小值存储在一个变量里，当前最小值小于上一个最小值，则将上一个最小值放入栈中
    """    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None

    def push(self, x: int) -> None:
        if self.head:
            min_num = min(x, self.head.min_num)
            node = ListNode(x, min_num)
            node.next = self.head
            self.head = node
        else:
            self.head = ListNode(x, x)

    def pop(self) -> None:
        node = self.head
        self.head = self.head.next
        return node.val

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min_num


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.push(-3)
assert minStack.getMin() == -3
assert minStack.pop() == -3
assert minStack.top() == -3
assert minStack.getMin() == -3
assert minStack.pop() == -3
assert minStack.top() == 0
assert minStack.getMin() == -2


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

