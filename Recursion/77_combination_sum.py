"""
n: from the range of [1:n] to get the k digits of combination
ie. n = 4, k = 2, outcome: [1,2], [1,3], [1, 4], [2, 3], [2, 4], [3, 4]
"""
class Solution:
    def combinationSum(self, end, k):
        res = []
        path = []
        self.helper(1, end, k, path, res)
        return res

    def helper(self, start, end,k, path, res):
        if len(path) == k:
            res.append(list(path))
            return

        for ele in range(start, end + 1):
            path.append(ele)
            self.helper(ele + 1, end, k, path, res)
            # print(start)
            # print(end + 1)
            path.pop()
        return


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum(4, 2))