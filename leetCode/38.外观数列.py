#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#


# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        """[summary]

        """
        result = '1'
        for i in range(2, n + 1):
            tmp = []
            j = 0
            print('i', i, tmp, '-' * 30)
            count = 1
            while j < len(result):
                if result[j] != result[j - 1:j]:
                    count = 1
                    tmp.append(str(count))
                    tmp.append(result[j])
                else:
                    count += 1
                    tmp[-2] = str(count)             
                j += 1
                print('j', j, count, tmp)
            result = ''.join(tmp)
            print('result', result)
        return result


s = Solution()
# assert s.countAndSay(4) == '1211'
# assert s.countAndSay(5) == '111221'
assert s.countAndSay(6) == '312211'
# print(s.countAndSay(30))

# @lc code=end
