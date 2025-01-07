"""
88. Merge Sort (inplace), IBM, BBC
注意点： divide and conquer
follow up: optimization could be space: o(1), time is o(n + m)
as nums1's length is n + m, end with m * 0
"""

# time/space: o(n + m), o(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return
        len1 = len(nums1)
        end_idx = len1 - 1

        while n > 0 and m > 0:
            if nums2[n - 1] >= nums1[m - 1]:
                nums1[end_idx] = nums2[n - 1]
                n -= 1
            else:
                nums1[end_idx] = nums1[m - 1]
                m -= 1
            end_idx -= 1
        while n > 0:
            nums1[end_idx] = nums2[n - 1]
            n -= 1
            end_idx -= 1
