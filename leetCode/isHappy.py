class Solution:
    # def isHappy(self, n: int) -> bool:
    #     """[基础实现，假设最后的和会进入循环]
    #     """
    #     tmp_arr = [n]
    #     while n != 1:
    #         n = sum(int(e)**2 for e in str(n))
    #         if n in tmp_arr:
    #             print('arr', tmp_arr)
    #             return False
    #         tmp_arr.append(n)
    #     print('arr', tmp_arr)
    #     return True

    def isHappy(self, n: int) -> bool:
        """[进阶实现，最后的和会进入循环]
        [4, 16, 37, 58, 89, 145, 42, 20]
        """
        arr = [4, 16, 37, 58, 89, 145, 42, 20]
        while n != 1:
            n = sum(int(e)**2 for e in str(n))
            if n in arr:
                return False
        return True


class TestSolution:
    def test_isHappy(self):
        s = Solution()
        assert s.isHappy(99) is False
        for i in range(1, 20):
            print(s.isHappy(i))


if __name__ == '__main__':
    test = TestSolution()
    test.test_isHappy()
