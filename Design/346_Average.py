"""
total_sums, size
replace the first ele in array to the last one
store in a queue
一定要注意更新total的值
"""
import queue

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.total = 0
        self.queue = queue
        # count means the number of ele we have seen so far
        self.count = 0


    def next(self, val: int) -> float:
        self.count += 1
        self.queue.append(val)
        if self.count > self.size:
            tail = self.queue.popleft()
            self.total = self.total - tail
        self.total += val
        return self.total / min(self.size, self.count)

#time/space: o(1), o(n)


