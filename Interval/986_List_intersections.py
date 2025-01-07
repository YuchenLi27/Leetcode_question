"""
Question: given various intervals in a sorted order, return the overlap part
for start: it needs the max val of two start times
for ends: it needs the min val of two end times

"""
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            low = max(firstList[i][0], secondList[j][0])
            high = min(firstList[i][1], secondList[j][1])
            if low <= high:
                ans.append([low, high])
            # always update the earlier end-time pointer,
            # --> Shift the pointer which ends earlier -> b/c its consecutive-next
            if firstList[i][1] <= secondList[j][1]:
                i += 1
            else:
                j += 1
        return ans

