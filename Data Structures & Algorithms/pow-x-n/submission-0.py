class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            res = helper(x, abs(n) // 2)
            res = res * res
            if n % 2 == 0:
                return res
            else:
                return x * res
        
        ans = helper(x, n)
        if n >= 0:
            return ans
        else:
            return 1 / ans