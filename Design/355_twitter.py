class Twitter:

    def __init__(self):
        self.posts = dict()
        self.followers = dict()
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None: # [1,5]
        if userId not in self.posts.keys():
            self.posts[userId] = [] # ini_post = []
        self.timestamp += 1
        self.posts[userId].append((tweetId, self.timestamp))

    def getNewsFeed(self, userId: int) -> List[int]:
        all_users_posts = []
        fans_post = []
      # get userId self's all post
         #list of list
        if userId not in self.followers:
            all_users_posts.append(self.posts[userId])
        else:
            all_users_posts.append(self.posts[userId])
            for fan in self.followers[userId]:
                fans_post.append(self.posts[fan])
        for i in fans_post:
            all_users_posts.append(i)
        print(all_users_posts)
        sorted_post = sorted(all_users_posts, key=lambda x:x[1])
        return sorted_post[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        # poster: follower
        if followerId not in self.followers.keys():
            self.followers[followerId] = set() # fans = set()
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers.keys():
            if followeeId in self.followers[followerId]:
                self.followers[follwerId].remove(followeedId)




# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)