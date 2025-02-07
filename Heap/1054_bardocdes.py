"""
construct a new array that selected elements from one of each barcodes
 heap
"""
import heapq
from collections import Counter, defaultdict


class Bardocdes:
    # def solution(self, nums):

    #     cnt = Counter(nums)
    #     heap = []
    #     res = []
    #     for i in cnt:
    #         heapq.heappush(heap, (-cnt[i], i))
    #
    #     while heap:
    #         n = len(heap)
    #         if n >= 2:
    #             t1, c1 = heapq.heappop(heap)
    #             res.append(c1)
    #             t2, c2 = heapq.heappop(heap)
    #             res.append(c2)
    #             if t1 + 1 < 0:
    #                 heapq.heappush(heap,(t1 + 1, c1))
    #             if t2 + 1 < 0:
    #                 heapq.heappush(heap, (t2 + 1, c2))
    #         else:
    #             t, c = heapq.heappop(heap)
    #             res.append(c)
    #     return res
    def solution(self, barcodes):

        # first to get the frequency

        cnt = defaultdict(list)
        for nums in barcodes:
            if nums in cnt:
                cnt[nums] += 1
            else:
                cnt[nums] = 1
        # then construct a heap
        heap = []
        heap.heapify(heap)
        # put all frq into heap in the format of tuple (frq, input_num)
        for key in cnt:
            value = cnt[1]
            frq = value * -1
            heap_tuple = (frq, key)
            heapq.heappush(heap, heap_tuple)

        res = []
        while len(heap) > 0:
