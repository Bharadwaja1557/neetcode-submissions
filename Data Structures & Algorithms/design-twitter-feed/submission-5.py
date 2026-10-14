class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.timestamp, tweetId])
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # ordered starting from recent
        minHeap = []
        self.followMap[userId].add(userId) # add him to his following set

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                timestamp, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([timestamp, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            timestamp, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                timestamp, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [timestamp, tweetId, followeeId, index - 1])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
