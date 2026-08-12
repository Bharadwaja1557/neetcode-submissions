class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def helper(arr: List[int], l: int, r: int) -> List[int]:
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l, r = l + 1, r - 1
            return arr

        k = k % len(nums)
        helper(nums, 0, len(nums)-1)
        helper(nums, 0, k-1)
        helper(nums, k, len(nums)-1)
