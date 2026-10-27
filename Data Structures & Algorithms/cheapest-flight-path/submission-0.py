class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            copy = prices.copy()

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < copy[d]:
                    copy[d] = prices[s] + p
                
            prices = copy
        
        if prices[dst] == float("inf"):
            return -1
        else:
            return prices[dst]