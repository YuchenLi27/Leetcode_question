"""
Build 2 functions to meet the demand of put and get
detail: initiate a list with the int as the size, for example, we have 2 lenght size
put the number 1,2 , get 1. put 3. which means 2 had not been used for a while, drop it
so it becomes, 1,3. when we check 2. it returns -1.

with build in functions, and without build in functions.

"""
# import collections
#
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.dic = collections.OrderedDict()
#
#     def get(self, key: int) -> int:
#         if key not in self.dic:
#             return -1
#
#         self.dic.move_to_end(key)
#         return self.dic[key]
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.dic:
#             self.dic.move_to_end(key)
#
#         self.dic[key] = value
#         if len(self.dic) > self.capacity:
#             self.dic.popitem(False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# without build in
"""
we can use double linked list to do. we need add, remove function

"""
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            old_node = self.dic[key]
            # once we have known the node
            self.remove(old_node)

        node = ListNode(key, value)
        self.dic[key] = node
        self.add(node)

        if len(self.dic) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key]

    def add(self, node):
        previous_end = self.tail.prev
        previous_end.next = node
        node.prev = previous_end
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


