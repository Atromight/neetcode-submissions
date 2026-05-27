from collections import deque

import heapq

class Twitter:

    def __init__(self):
        self.time = 1
        self.tweets = {} # tweets = {userId1: deque[(time1, tweetId1), (time2, tweetId2)]}
        self.follows = {} # follows = {userId1: set([userId2, userId3])}


    def postTweet(self, userId: int, tweetId: int) -> None:
        print(f"user: {userId} posted tweet: {tweetId} at time: {self.time}")
        if userId in self.tweets:
            self.tweets[userId].appendleft((self.time, tweetId))
        else:
            self.tweets[userId] = deque([(self.time, tweetId)])

        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()

        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        print(f"")
        userIds = self.follows.get(userId, set())
        userIds.add(userId)
        tweets = deque([])
        for uId in userIds:
            tweets += self.tweets.get(uId, deque([]))
        
        tweets = list(tweets)
        heapq.heapify(tweets)
        top10 = heapq.nlargest(10, tweets)
        res = [tweetId for (time, tweetId) in top10]
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            if followeeId not in self.follows[followerId]:
                self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = set([followeeId])


    def unfollow(self, followerId: int, followeeId: int) -> None:
        # print(f"self.follows: {self.follows}")
        if followerId in self.follows:
            if followeeId in self.follows[followerId]:
                self.follows[followerId].remove(followeeId)


