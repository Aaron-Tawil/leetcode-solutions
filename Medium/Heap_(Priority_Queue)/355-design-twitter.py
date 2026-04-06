from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.user_tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.time = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.time,tweetId))
        self.time+=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        q = []
        users = self.follows[userId] | {userId}
        for user in users:
            idx = len(self.user_tweets[user])-1
            if idx >=0:
                time , tweet = self.user_tweets[user][idx]
                q.append((-time, tweet, user, idx)) # minus for max heap

        heapq.heapify(q)

        while q and len(res)<10:
            _ ,tweet, user, idx = heapq.heappop(q)
            res.append(tweet)

            if idx-1 >=0:
                time, tweet = self.user_tweets[user][idx-1]
                heapq.heappush(q, (-time, tweet, user, idx-1)) # minus for max heap
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)