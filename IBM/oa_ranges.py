from collections import Counter

class Solution:
    def findOrder(self, arrs):
        mod = 10 ** 9 + 7
        # make the arr sorted
        sort_arr = sorted(arrs,key=lambda x:x[0])
        limit = [] # list of list
        for i in sort_arr:
            if len(limit) == 0:
                limit.append(i)
                continue
            right_side = limit[-1][-1]
            if i[0] <= right_side:
                limit[-1][1] = max(i[1], right_side)
            else:
                limit.append(i)
        ball_number = len(limit)
        res = pow(2, ball_number, mod) - 2
        # res %= mod
        return res

if __name__ == '__main__':
    a = Solution()
    print(a.findOrder([[1,5], [3, 8], [10, 15], [13, 14], [20, 100]]))








