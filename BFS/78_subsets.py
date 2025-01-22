"""
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""

class Solution:
    def subsets(self, nums):
        res = []
        self.helper(nums, 0, [], res)
        return res

    def helper(self, nums, curr, res, path):
        res.append(list(path))

        for ele in range(curr, len(nums)):
            path.append(nums[ele])
            self.helper(nums, ele + 1, path, res)
            path.pop()

"""
takeaway:
this question focus on the breaking condition, when we need to stop append answer into res, 
however, there is no certain condition, like others, (certain length etc). so we just append all the ans to res.
 
"""