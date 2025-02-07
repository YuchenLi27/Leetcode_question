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
        heapq.heapify(heap)
        # put all frq into heap in the format of tuple (frq, input_num)
        for key in cnt:
            value = cnt[1]
            frq = value * -1
            heap_tuple = (frq, key)
            heapq.heappush(heap, heap_tuple)

        res = []

        # only if the heap is not empty we can process the heap first,
        # then we need to see if the res is empty, if so, we can append it directly
        # meanwhile change the content of the heap tuple before push it to heap
        while len(heap) > 0:
            tup_to_process = heapq.heappop(heap)
            input_num = tup_to_process[1]
            if len(res) == 0:
                res.append(input_num)
                frq = tup_to_process[0] + 1
                if frq == 0:
                    continue
                update_tup = (frq, input_num)
                heapq.heappush(heap, update_tup)

                continue
            #  to check if heappop pop two same number
            last_ele = res[-1]
            if last_ele != tup_to_process[1]:
                res.append(input_num)
                frq = tup_to_process[0] + 1
                if frq == 0:
                    continue
                update_tup = (frq, input_num)
                heapq.heappush(heap, update_tup)
            else:
            # if the two tuples are same
                new_tuple_to_precess = heapq.heappop(heap)
                new_val = new_tuple_to_precess[1]
                res.append(new_val)
                new_frq = new_tuple_to_precess[0] + 1
                if new_frq == 0:
                    heapq.heappush(heap,tup_to_process)
                    continue
                new_second_tuple = (new_frq, new_val)
                heapq.heappush(heap, new_second_tuple)
                heapq.heappush(heap, tup_to_process)
        return res
if __name__ == '__main__':
    print(Bardocdes().solution([1,1,1,1,2,2,3,3]))


