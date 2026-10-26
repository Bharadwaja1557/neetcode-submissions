class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        res = 0
        lastEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= lastEnd:
                lastEnd = end
            else:
                res += 1
                lastEnd = min(lastEnd, end) 
                # keep the shotest end, delete longest end 
                # because the shorter end one will be less probable 
                # to overlap with future ones
        
        return res
        