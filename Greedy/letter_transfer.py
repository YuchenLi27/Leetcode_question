"""
give you an array, it contains only letter, then the array will be moved,
every move means the letter will become the next letter, like a becomes to b, b becomes c,
but z will become ab, after certain times move, ask the length of the result.
example array = ["abz"] move = 1, res = ["bcab"], the answer will be 4
"""
from collections import defaultdict


def get_final_length(arrs, moves):
    # res = []
    # total_length = 0
    # if moves // 26 == 0:
    #     for i in range(len(arr)):
    #         change_lim = ord('z') - ord(arr[i])
    #         if change_lim <= moves:
    #             total_length += 1
    # else:

    while moves > 0:
        new_arr = []
        moves -= 1
        for ele in arrs:
            if ele == "z":
                new_arr.append("a")
                new_arr.append("b")
            else:
                move_ele = ord(ele) + 1
                after_mv_ele = chr(move_ele)
                new_arr.append(after_mv_ele)
        arrs = new_arr
    return arrs

# Example usage
if __name__ == '__main__':
    arr = ["a", "b", "z"]
    print(get_final_length(arr, 1))


