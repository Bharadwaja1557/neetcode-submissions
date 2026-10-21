class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin, currMax = 1, 1
        res = max(nums)

        for n in nums:
            if n == 0:
                currMin, currMax = 1, 1
                continue
            
            # we need temp, because to update currMin we need actual currMax,
            # which is currMax before we do "step1", not the updated currMax
            temp = currMax * n
            currMax = max(temp, currMin * n, n) # step1
            currMin = min(temp, currMin * n, n)
            res = max(res, currMax)
        
        return res
        