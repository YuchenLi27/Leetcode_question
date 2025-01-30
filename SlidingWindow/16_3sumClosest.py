"""
this question is follow up of 3sum, but difference is this requires us to find the closest number to the 3sum
two pointers
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float("inf")
        nums.sorted()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if abs(target - total) < diff:
                    diff = target - total
                if total < target:
                    j += 1
                else:
                    k -= 1
            if diff == 0:
                break
        return target - diff

"""
this question may have follow up to get Ksum,
we can reduce the number to 2, then do twoSum with two pointers,
by using kSum to do so (make it become 2sum questions).
"""
