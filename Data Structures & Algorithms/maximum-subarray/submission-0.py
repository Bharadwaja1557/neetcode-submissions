class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = nums[0]
        currSum = 0
        
        for n in nums:
            if currSum < 0:
                currSum = 0
            
            currSum += n
            res = max(res, currSum)
        
        return res