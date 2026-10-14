class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones) # Max Heap

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first < second:
                diff = first - second  # we need -ve weight remember
                heapq.heappush(stones, diff)
            
        stones.append(0)
        return abs(stones[0])
        