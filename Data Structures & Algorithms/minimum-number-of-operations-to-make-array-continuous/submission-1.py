class Solution:
    def minOperations(self, nums: List[int]) -> int:
        actual_length = len(nums)
        new_nums = sorted(set(nums))    # unique and sorted nums

        res = actual_length
        r = 0

        for l in range(len(new_nums)):
            while r < len(new_nums) and new_nums[r] < new_nums[l] + actual_length:
                r += 1
            
            window = r - l
            res = min(res, actual_length - window)
        
        return res