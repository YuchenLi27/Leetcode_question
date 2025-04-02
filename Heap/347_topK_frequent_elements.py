"""
this question is that given the list of array and an integer k, return the k most frequent
"""
import heapq


class Solution:
    def topKFrequent(self, nums, k):
        frq = dict()
        for num in nums:
            if num not in frq:
                frq[num] = 1
            else:
                frq[num] += 1

        heap = []
        for num, cnt in frq.items():
            heapq.heappush(heap, (cnt, num))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        for cnt, num in heap:
            ans.append(num)
        return ans

if __name__ == "__main__":
    print(Solution().topKFrequent([1,1,1,2,2,3], 2))