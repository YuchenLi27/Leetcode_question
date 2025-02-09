class Twitter:

    def __init__(self):
        self.posts = dict()
        self.followers = dict()
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:  # [1,5]
        if userId not in self.posts.keys():
            self.posts[userId] = []  # ini_post = []
        self.timestamp += 1
        self.posts[userId].append((tweetId, self.timestamp))

    def getNewsFeed(self, userId: int) -> List[int]:
        all_users_posts = []
        all_posts = []
        fans_post = []
        # get userId self's all post
        # list of list
        if userId in self.posts:
            all_users_posts.append(self.posts[userId])
        if userId in self.followers:
            for fan in self.followers[userId]:
                if fan in self.posts:
                    fans_post.append(self.posts[fan])
        for i in fans_post:
            all_users_posts.append(i)
        for list_of_post in all_users_posts:
            for tuple_of_list in list_of_post:
                all_posts.append(tuple_of_list)
        sorted_post = sorted(all_posts, key=lambda x: -x[1])
        ten_eles = []
        res = []
        if len(sorted_post) >= 10:
            ten_eles = sorted_post[:10]
            for first_ele in ten_eles:
                res.append(first_ele[0])
        else:
            ten_eles = sorted_post
            for first_ele in ten_eles:
                res.append(first_ele[0])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # poster: follower
        if followerId not in self.followers.keys():
            self.followers[followerId] = set()  # fans = set()
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers.keys():
            if followeeId in self.followers[followerId]:
                self.followers[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)