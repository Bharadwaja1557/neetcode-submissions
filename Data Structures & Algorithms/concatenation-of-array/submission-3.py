class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        k = 2
        ans = []
        n = len(nums)
        for i in range(k * n):
            ans.append(nums[i % n])
        
        return ans
        