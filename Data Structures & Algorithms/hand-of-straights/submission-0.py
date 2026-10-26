class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}

        for num in hand:
            count[num] = 1 + count.get(num, 0)
        
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]
            for num in range(first, first + groupSize):
                if num not in count:
                    return False
                count[num] -= 1
                if count[num] == 0:
                    if num != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        
        return True