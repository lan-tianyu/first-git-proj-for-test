class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for t in range(32):
            result = (result << 1) + (n & 1)
            n = n >> 1
        return result

    
if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(4294967293))
    print(s.reverseBits(43261596))
