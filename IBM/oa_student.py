from collections import Counter


def student(self, height):
    sort_height = height.sort()
    cnt = 0
    for ele in range(height):
        for ele2 in range(sort_height):
            if height[ele] == sort_height[ele2]:
                continue
            else:
                cnt += 1
    return cnt






