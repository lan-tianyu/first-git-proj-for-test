#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
from typing import List
import collections


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int],
                     D: List[int]) -> int:
        # map = {}
        # res = 0
        # for i in range(len(A)):
        #     for j in range(len(B)):
        #         sum_ab = A[i] + B[j]
        #         map[sum_ab] = map.get(sum_ab, 0) + 1
        # for i in range(len(C)):
        #     for j in range(len(D)):
        #         sum_cd = -(C[i] + D[j])
        #         res += map.get(sum_cd, 0)
        # return res
        dic = collections.Counter(a + b for a in A for b in B)
        return sum(dic.get(-(c + d), 0) for c in C for d in D)


# @lc code=end
