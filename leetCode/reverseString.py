class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        双指针法
        """
        # n = len(s)
        # for i in range(n//2):
        #     s[i], s[n-1-i] = s[n-1-i], s[i]
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


class TestSoluntion:
    def test_reverseString(self):
        s = Solution()
        list1 = ["h", "e", "l", "l", "o"]
        s.reverseString(list1)
        print(list1)
        list1 = ["H", "a", "n", "n", "a", "h"]
        s.reverseString(list1)
        print(list1)


if __name__ == '__main__':
    test = TestSoluntion()
    test.test_reverseString()