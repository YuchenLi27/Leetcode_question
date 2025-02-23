"""
give you an array, it contains only letter, then the array will be moved,
every move means the letter will become the next letter, like a becomes to b, b becomes c,
but z will become ab, after certain times move, ask the length of the result.
example array = ["abz"] move = 1, res = ["bcab"], the answer will be 4
"""
from collections import defaultdict


def get_final_length(arr, moves):
    res = []
    total_length = 0
    if moves // 26 == 0:
        for i in range(len(arr)):
            change_lim = ord('z') - ord(arr[i])
            if change_lim <= moves:
                total_length += 1
    else:




# Example usage
if __name__ == '__main__':
    arr = ["abz"]
    print(get_final_length(arr, 4))


