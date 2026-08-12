class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverseString(arr: List[int], l: int, r: int) -> List[int]:
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l, r = l + 1, r - 1
            return arr

        k = k % len(nums)
        reverseString(nums, 0, len(nums)-1)
        reverseString(nums, 0, k-1)
        reverseString(nums, k, len(nums)-1)
