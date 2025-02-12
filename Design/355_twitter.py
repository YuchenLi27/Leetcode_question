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

# optimiaziton 1: use heap to compare the post's time
import heapq

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
        all_posts = []
        fans_post = []
        # get userId self's all post
        #list of list
        if userId in self.posts:
            all_users_posts.append(self.posts[userId])
        if userId in self.followers:
            for fan in self.followers[userId]:
                if fan in self.posts:
                    fans_post.append(self.posts[fan])

        for i in fans_post:
            #  [[(1, 1)]]
            # all_users_posts.append(i)
            all_users_posts.append(i)

        for list_of_post in all_users_posts:
            for tuple_of_list in list_of_post:
                all_posts.append(tuple_of_list)

        # while len(all_posts) > 10 and len(newst_heap) < 10:
        #     heap = []
        #     for ele in all_posts:
        #         for tup in ele:
        #             max_timestamp = tup[1] * -1
        #     max_heap_tup = (tup[0], max_timestamp)
        #     update_heap = heapq.heappush((heap,max_heap_tup))
        #     newst_ten = heapq.heappop(update_heap)
        #     all_users_posts.append(news_ten)

        print(all_posts)
        minheap = []
        heapq.heapify(minheap)
        for post in all_posts:
            switched_tuple = (post[1], post[0])
            if len(minheap) < 10:
                heapq.heappush(minheap, switched_tuple)
            else:
                oldest_in_ten = minheap[0]
                if post[1] > oldest_in_ten[0]:
                    heapq.heappop(minheap)
                    heapq.heappush(minheap, switched_tuple)
        res = []
        while len(minheap) > 0:
            post = heapq.heappop(minheap)
            res.append(post[1])
        reverse_res = []
        for index in range(len(res)):
            reverse_res.append(res[len(res)-1-index])
        return reverse_res

        # sorted_post = sorted(all_posts, key=lambda x:-x[1])
        # ten_eles = []
        # res = []
        # if len(sorted_post) >= 10:
        #     ten_eles = sorted_post[:10]
        # else:
        #     ten_eles = sorted_post
        # for first_ele in ten_eles:
        #     res.append(first_ele[0])
        # return res



    def follow(self, followerId: int, followeeId: int) -> None:
        # poster: follower
        if followerId not in self.followers.keys():
            self.followers[followerId] = set() # fans = set()
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers.keys():
            if followeeId in self.followers[followerId]:
                self.followers[followerId].remove(followeeId)

# we also can do improve by use heap directly to compare the post's time


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)