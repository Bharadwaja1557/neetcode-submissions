class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [0] * len(set(nums))
        arr = list(set(nums))
        ans = []

        for i in range(len(nums)):
            freq[arr.index(nums[i])] += 1

        while(k>0):
            ans.append(arr[freq.index(max(freq))])
            freq[freq.index(max(freq))] = -1
            k -= 1

        return ans