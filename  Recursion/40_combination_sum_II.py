"""
Given a collection of candidate numbers and target, and candidates can be only once
the solution NOT ALLOWED duplicate combinations
"""

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        return self.helper_func(candidates, target, 0, [])

    def helper_func(self, nums, goal, current, comb):
        res = []

        if goal == 0:
            res.append(list(comb))
            return res

        for ele in range(current, len(nums)):
            if ele > current and nums[ele] == nums[ele - 1]:
                continue
            remain = goal - nums[ele]
            if remain < 0:
                break
            comb.append(nums[ele])
            res.extend(self.helper_func(nums, remain, ele + 1, comb))
            comb.pop()

        return res