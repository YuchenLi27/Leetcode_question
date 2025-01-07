"""
（if you are not allowed to use build in sort
if parameter is key= funcation）
this question intends to merge two arrays, so once:
we need to sort all ele
the b start is smaller a's end, we need to merge
if there is no ans, we append the first, then compare, it also requires to append,
when the condition is not meet. Otherwise, we need to change the end time to a bigger one
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans

# time/space: o(NlogN)
# space could be o(n) if sort is not in place, Otherwise,
# we must allocate linear space to store a copy of intervals and sort that.