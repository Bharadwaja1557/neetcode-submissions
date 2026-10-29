class Solution:
    def minCost(self, startPos: list[int], homePos: list[int], rowCosts: list[int], colCosts: list[int]) -> int:

        sr, sc = startPos
        hr, hc = homePos
        cost = 0
        
        # move vertically
        if sr < hr:
            for r in range(sr + 1, hr + 1):
                cost += rowCosts[r]
        else:
            for r in range(hr, sr):
                cost += rowCosts[r]
        
        # move horizontally
        if sc < hc:
            for c in range(sc + 1, hc + 1):
                cost += colCosts[c]
        else:
            for c in range(hc, sc):
                cost += colCosts[c]
        
        return cost
