class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k = len(nums)//3
        count = {}
        res = []
        
        for n in nums:
            if n in res:
                continue
            count[n] = count.get(n, 0) + 1
            if count[n] > k:
                res.append(n)
        
        return res
        