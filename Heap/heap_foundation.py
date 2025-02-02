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
            self.heap.pop()
            return
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down_helper(0)

    def heapify_down_helper(self, idx):
        # if there is no left child which means, there is no right child
        right_child_idx = idx * 2 + 2
        left_child_idx = idx * 2 + 1
        # there is a left child but no right child
        if left_child_idx == len(self.heap) - 1:
            min_val = min(self.heap[idx], self.heap[left_child_idx])
            if min_val == self.heap[left_child_idx]:
                tmp = self.heap[idx]
                self.heap[idx] = self.heap[left_child_idx]
                self.heap[left_child_idx] = tmp
                self.heapify_down_helper(left_child_idx)
            return
        # this node has no either left or right children
        if left_child_idx > len(self.heap) - 1:
            return

        min_val = min(self.heap[idx], self.heap[right_child_idx], self.heap[left_child_idx])
        if min_val == self.heap[right_child_idx]:
            tmp = self.heap[idx]
            self.heap[idx] = self.heap[right_child_idx]
            self.heap[right_child_idx] = tmp
            self.heapify_down_helper(right_child_idx)

        if min_val == self.heap[left_child_idx]:
            tmp = self.heap[idx]
            self.heap[idx] = self.heap[left_child_idx]
            self.heap[left_child_idx] = tmp
            self.heapify_down_helper(left_child_idx)


def heapsort(input_arr):
    heap = MinHeap()
    for ele in input_arr:
        heap.append(ele)
    res = []
    for i in range(len(input_arr)):
        num = heap.peek()
        res.append(num)
        heap.heappop()
    return res


if __name__ == '__main__':
    # test_heap = MinHeap()
    # test_heap.heap = [1, 2, 3,4,5,6]
    # test_heap.heappop()
    # print(test_heap.heap)

    input_arr = [3, 5,76,34,23,1,409,53,76]
    sorted_arr = heapsort(input_arr)
    print(sorted_arr)
