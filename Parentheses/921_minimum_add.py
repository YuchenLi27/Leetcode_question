"""
question: minimum add to valid Parentheses
return the minimum number that add to get the valid Parentheses
"""
from collections import deque


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # initiate a deque to check
        queue = deque()
        count = 0
        for i in s:
            if i == "(":
                queue.append(i)
            elif i == ")":
                if len(queue) > 0:
                    queue.popleft()
                else:
                    count += 1
        return count + len(queue)
# time/space: o(n), o(n)

# improve
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        min_adds_required = 0

        for c in s:
            if c == "(":
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    min_adds_required += 1

        # Add the remaining open brackets as closing brackets would be required.
        return min_adds_required + open_brackets
# time remains o(n), but space is o(1)
# s = ")("
