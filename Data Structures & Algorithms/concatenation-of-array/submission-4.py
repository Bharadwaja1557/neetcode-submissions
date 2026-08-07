class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        k = 2
        ans = []
        for i in range(k):
            for num in nums:
                ans.append(num)
        
        return ans
        