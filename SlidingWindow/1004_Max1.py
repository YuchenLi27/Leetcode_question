"""
max consecutive 1 with the k assigned 0, which can turn to 1
 why we do not need to compare the length of ans, and we can assure the length of ans is max?
as we use sliding window, it never shrinks, so we can get the ans by right - left + 1
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        # then we iterate the input, we amend k when the ele is 0,
        # until the k < 0, means we run out of the 0 so far, we need to move left side to next ele
        # but also update the k, when the ele is not 0, increase k
        # then keep move the left pointer till i reach to the last ele
        for i in range(len(nums)):
            ele = 1 - nums[i]
            k -= ele

            if k < 0:
                ele1 = 1 - nums[left]
                k += ele1
                left += 1
        return i - left + 1
# time/space: o(n), o(1)

