class Solution:
    def hammingWeight(self, n: int) -> int:
        # O(number of 1's in number) , more efficient
        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res
        
        # O(32) solution
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res
        