#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#


# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        """[summary]
        1. result初始字符串为'1'，tmp记录当前外观字符串的数组形式，初始值为['1', result[0]]
        2. 遍历result，当前j元素与初始j元素一致，则count+=1，tmp更新倒数第二个元素count
        3. 遍历result，当前j元素与初始j元素不一致，tmp插入最新元素和['1', result[j]]，i变更为就， count初始化1
        4. result为tmp转化成字符串形式，进入下一个循环
        """
        result = '1'
        for _ in range(2, n+1):
            i, count, tmp = 0, 1, ['1', result[0]]
            for j in range(1, len(result)):
                if result[i] == result[j]:
                    count += 1
                    tmp[-2] = str(count)
                else:
                    i, count = j, 1
                    tmp.append(str(count))
                    tmp.append(result[j])
            result = ''.join(tmp)
        return result if n > 0 else ''


s = Solution()
assert s.countAndSay(4) == '1211'
assert s.countAndSay(5) == '111221'
assert s.countAndSay(6) == '312211'
# print(s.countAndSay(30))

# @lc code=end
