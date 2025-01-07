"""
given a array of nums, to return all the results that make the sum of 3 nums is 0
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we need to return all the ans
        res = []
        # sorting can help us avoid duplicate elements
        nums.sort()

        for i in range(len(nums)):
            # if they are same ele
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # setting up two pointers, one from start, one from end
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # we need to check after we move j, if there is any duplication
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return res

