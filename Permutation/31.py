"""
to get next permutation is to find the next larger number then current val.
so we can find from the end to start, then we compare the ele with the previous one
if the later one is larger than the previous, then we switch these two

"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i > 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            # we need to reverse the part that we have amend/switch
        nums[i + 1:] = nums[i + 1:][::-1]
