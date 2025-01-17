"""
216. Combination III,
"""


class Solution:
    def combinationSum3(self, k: int, n: int):
        return self.helper_func(k, n, [], 1)

    def helper_func(self, nums, goal, comb, current):
        res = []
        if len(comb) == nums:
            if goal == 0:
                res.append(list(comb))
                return res

        for ele in range(current, 10):
            remain = goal - ele
            if remain < 0:
                continue
            comb.append(ele)
            res.extend(self.helper_func(nums, remain, comb, ele + 1))
            comb.pop()

        # for result in res:
        #     if len(result) == nums:
        #         ans.append(result)

        return res

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum3(3,7))


