"""
construct a new array that selected elements from one of each barcodes
 heap
"""
import heapq
from collections import Counter


class Bardocdes:
    def solution(self, nums):
        cnt = Counter(nums)
        heap = []
        res = []
        for i in cnt:
            heapq.heappush(heap, (-cnt[i], i))

        while heap:
            n = len(heap)
            if n >= 2:
                t1, c1 = heapq.heappop(heap)
                res.append(c1)
                t2, c2 = heapq.heappop(heap)
                res.append(c2)
                if t1 + 1 < 0:
                    heapq.heappush(heap,(t1 + 1, c1))
                if t2 + 1 < 0:
                    heapq.heappush(heap, (t2 + 1, c2))
            else:
                t, c = heapq.heappop(heap)
                res.append(c)
        return res

