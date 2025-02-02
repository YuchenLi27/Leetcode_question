class MinHeap(object):
    def __init__(self):
        self.heap = []

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def get_parent_idx(self, cur_idx):
        if cur_idx == 0:
            return 0
        if cur_idx % 2 == 1:
            return (cur_idx - 1) // 2
        else:
            return (cur_idx - 2) // 2

    def append(self, ele):
        self.heap.append(ele)
        if len(self.heap) != 1:
            self.heapify_up_helper(len(self.heap) - 1)

    def heapify_up_helper(self, cur_idx):
        parent_idx = self.get_parent_idx(cur_idx)
        if self.heap[parent_idx] > self.heap[cur_idx]:
            tmp = self.heap[parent_idx]
            self.heap[parent_idx] = self.heap[cur_idx]
            self.heap[cur_idx] = tmp
            self.heapify_up_helper(parent_idx)

    def heappop(self):
        if len(self.heap) == 1:
            return None
        


    def heapify_down_helper(self, idx):
        right_child_idx = idx * 2 + 2
        tmp = right_child_idx
        right_child_idx = idx
        idx = tmp





if __name__ == '__main__':
    test_heap = MinHeap()
    test_heap.heap = [1, 2, 3, 4, 5, 7, 8, 9, 10]
    test_heap.append(1.1)
    print(test_heap.heap)

