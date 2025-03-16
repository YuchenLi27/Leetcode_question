"""
Given an array of integers representing boxes weight.
You can perform 1 of the following 2 operations each time:
choose 2 boxes with the same weight, or choose 3 boxes with the same weight.
 Determnine the minimum number of traffics to deliver all boxes.
"""

from collections import Counter


def min_traffics(boxes):
    freq = Counter(boxes)
    total_ops = 0

    for weight, count in freq.items():
        if count == 1:
            return -1

        groups_of_3 = count // 3
        remainder = count % 3

        if remainder == 0:
            ops = groups_of_3
        elif remainder == 1:
            ops = groups_of_3 + 1
        elif remainder == 2:
            ops = groups_of_3 + 1

        total_ops += ops

    return total_ops

if __name__ == '__main__':
    print(min_traffics([2,2,3,3,3,6,6,6]))