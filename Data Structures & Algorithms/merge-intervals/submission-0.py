class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda i : i[0])

        res = [intervals[0]]

        for start, end in intervals:
            lastEnd = res[-1][1]
            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end) # [1, 5] [2, 4]
            else:
                res.append([start, end])
        
        return res