class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()

        l, r = 0, length - 1
        while l < r:
            m = (l + r) // 2
            if mountain_arr.get(m) < mountain_arr.get(m + 1):
                l = m + 1
            else:
                r = m
        peak = l

        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            val = mountain_arr.get(m)
            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return m
        
        l, r = peak, length - 1
        while l <= r:
            m = (l + r) // 2
            val = mountain_arr.get(m)
            if val > target:
                l = m + 1
            elif val < target:
                r = m - 1
            else:
                return m
        
        return -1