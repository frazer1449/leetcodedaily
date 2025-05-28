# Design Twitter

import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.tweetsPerUser = {} # Dict[userId] -> List of (timestamp, tweetId)
        self.follows = {} # Dict[userId] -> Set of followeeIds
        self.timestamp = 0 # allows tracking of time

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetsPerUser:
            self.tweetsPerUser[userId] = []
        self.tweetsPerUser[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        for tweet in self.tweetsPerUser.get(userId, []):
            heapq.heappush(minHeap, tweet)
            if len(minHeap) > 10:
                heapq.heappop(minHeap)

        for followeeId in self.follows.get(userId, set()):
            for tweet in self.tweetsPerUser[followeeId]:
                heapq.heappush(minHeap, tweet)
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)
        
        result = []

        while minHeap:
            result.append(heapq.heappop(minHeap)[1])  # append tweetId

        return result[::-1]



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].remove(followeeId)
        
