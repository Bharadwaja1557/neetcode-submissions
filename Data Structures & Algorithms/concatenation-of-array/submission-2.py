class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        c = 2

        while(c>1):
            for i in range(len(nums)):
                nums.append(nums[i])
            c = c - 1

        return nums

        