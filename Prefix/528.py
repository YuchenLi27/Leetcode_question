# random pick with weight
# this question asks us to get the weight of random select number's idx
# so in __init__, we need to get the prefix_sums, and append them to a list.
# and we also need to get the total_sums of the input
#
# in pickIndex()
# get a random number, and by multiping the total to get the value pairs the random number.
# then we can find the idx by using BST from prefix_sums, the list we have.

import random


def __init__(self, w: list[int]):
    #
    self.prefix_sums = []
    prefix_sum = 0
    for i in range(len(w)):
        prefix_sum += i
        self.prefix_sums.append(prefix_sum)
    self.total_sum = prefix_sum

def pickIndex(self) -> int:
    target = self.total_sum * random.Random()
    for i, prefix_sum in enumerate(self.prefix_sums):
        if target < prefix_sum:
            return i
#improve
def pick(self) -> int:
    target = self.total_sum * random.random()
    l, r = 0, len(self.prefix_sums)
    while l < r:
        mid = (l + r) // 2
        if target > self.prefix_sums[mid]:
            l = mid + 1
        else:
            r = mid
    return l
