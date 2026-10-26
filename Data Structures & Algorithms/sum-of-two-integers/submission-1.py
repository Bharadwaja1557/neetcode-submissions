class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff # binary number  0b1111111111111111111111111111111

        while b != 0:
            tmp = (a & b) << 1
            a = (a ^ b) & mask
            b = tmp & mask

        if a > mask // 2: # checking if a is -ve
            return ~(a ^ mask) # negating a and then returning
        else:
            return a # a is +ve, so return directly