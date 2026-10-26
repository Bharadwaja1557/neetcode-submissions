class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                l = min(newInterval[0], intervals[i][0])
                r = max(newInterval[1], intervals[i][1])
                newInterval = [l, r]
                
        res.append(newInterval)
        return res