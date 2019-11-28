from typing import List


class Solution:
    # def fizzBuzz(self, n: int) -> List[str]:
    #     return [self._fizzBuzz(i) for i in range(1, n+1)] 
    
    # def _fizzBuzz(self, n: int) -> str:
    #     if n % 15 == 0:
    #         return 'FizzBuzz'
    #     if n % 3 == 0:
    #         return 'Fizz'
    #     if n % 5 == 0:
    #         return 'Buzz'
    #     return str(n)

    def fizzBuzz(self, n: int) -> List[str]:
        return ['Fizz' * (not i % 3) + 'Bizz' * (not i % 5) or str(i) for i in range(1, n+1)]


class TestSolution:
    def test_fizzBuzz(self):
        solution = Solution()
        print(solution.fizzBuzz(15))      
        print(solution.fizzBuzz(16)) 


if __name__ == '__main__':
    test = TestSolution()
    test.test_fizzBuzz()