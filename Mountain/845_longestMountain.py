"""
longest Mountain in array
so we need to find the uphill part and downhill part,
then by marking two pointers, we can use the end pointer subtracts the start pointer
or, if there is no answer, we can return the ans = 0

"""
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        pt1 = 0

        while pt1 < n:
            pt2 = pt1
            # it the ele in array is satisfied the condition, we can continue search until not meet requirement
            if pt2 + 1 < n and arr[pt2] < arr[pt2 + 1]:
                while pt2 + 1 < n and arr[pt2] < arr[pt2 + 1]:
                    pt2 += 1
                if pt2 + 1 < n and arr[pt2] > arr[pt2 + 1]:
                    while pt2 + 1 < n and arr[pt2] > arr[pt2 + 1]:
                        pt2 += 1
                    ans = max(ans, pt2 - pt1 + 1)
            # we also need to move the pt1 to a new position
            # it either could be the pt2, which is the end
            # or it could be the next ele of pt1
            pt1 = max(pt2, pt1 + 1)
        return ans
# time/space: o(n), 0(1)
