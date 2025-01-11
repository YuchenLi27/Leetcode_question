"""
course schedule 2, the main difference is this question is looking for the result, instead of boolean value
"""
from collections import deque


class Solution:
    def canFinish(self, nums, pres):
        alist = [[] for _ in range(nums)]
        indegree = [0] * nums
        res = []

        for course in pres:
            alist[course[1]].append(course[0])
            indegree[course[0]] += 1

        queue = deque()
        for course_indegree in range(nums):
            if indegree[course_indegree] == 0:
                queue.append(course_indegree)
                res.append(course_indegree)

        while len(queue) != 0:
            ele = queue.popleft()
            for nei in alist[ele]:
                # be careful with the below step, when we check it, we reduce the indegree
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
                    res.append(nei)

            if len(res) != nums:
                return []