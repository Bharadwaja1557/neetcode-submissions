class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = 0
        w = 0
        b = 0
        for num in nums:
            if num==0:
                r += 1
            elif num == 1:
                w += 1
            else:
                b += 1
        
        arr = [0] * r + [1] * w + [2] * b
        print(arr)

        nums[:] = arr[:]


        