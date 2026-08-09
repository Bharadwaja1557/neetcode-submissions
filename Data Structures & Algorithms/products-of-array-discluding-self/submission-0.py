class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [1] * n
        pre = 1
        post = 1
        for i in range(n-1):
            pre *= nums[i]
            arr[i+1] = pre
        for i in range(n-1, 0, -1):
            post *= nums[i]
            arr[i-1] *= post

        return arr