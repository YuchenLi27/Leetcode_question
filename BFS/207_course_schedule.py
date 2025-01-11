"""
207 course schedule
topological, bfs
time space: o(m) + o(n)
space: o(m) + o(n)
"""
from collections import deque


class Solution:
    def canFinish(self, numCourses, prerequisites):
        #  build a adj list
        alist = [[] for _ in range(numCourses)]
        # maintain the indegree
        indegree = [0] * numCourses
        #  remember the count of the course to check the ans
        seen_cnt = 0

        for course in prerequisites:
            alist[course[1]].append(course[0])
            indegree[course[0]] += 1

        queue = deque()
        for course_indegree in range(numCourses):
            if indegree[course_indegree] == 0:
                queue.append(course_indegree)

                while queue:
                    ele = queue.popleft()
                    seen_cnt += 1
                    for nei in alist[ele]:
                        indegree[nei] -= 1
                        if indegree[nei] == 0:
                            queue.append(nei)
                return seen_cnt == numCourses


