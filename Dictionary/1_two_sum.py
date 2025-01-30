"""
this question will be answered by using dict
"""
class Solution:
    def twoSum(self, nums, target):
        nums_dict = dict()
        res = []
        for i in range(len(nums)):
            if target - nums[i] in nums_dict:
                res.append([i, nums[target - nums[i]]])
            else:
                nums_dict[nums[i]] = i
        return [-1, -1]