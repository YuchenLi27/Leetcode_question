"""
locked position to make this ele[idx] cannot change
"""
class Solution:
    def isValid(self, s, locked):
        # if the input is odd, which is wrong
        if len(s) % 2 != 0:
            return False
        stack = []
        left = []
        # the first ele is unlocked
        for i in range(len(s)):
            if s[i] == 0:
                stack.append(i)
            elif s[i] == "(":
                left.append(i)
            elif s[i] == ")":
                if len(left) != 0:
                    left.pop()
                elif len(stack) != 0:
                    stack.pop()
                else:
                    return False
        while len(stack) != 0 and len(left) != 0 and left[-1] < stack[-1]:
            left.pop()
            stack.pop()

        if len(left) != 0:
            return False

        return True
# this question also could use greedy to explain, we go through the input from left to right AND right to left,
# if there is a open bracket we add 1, if there is close bracket, we reduce 1, but MUST go both sides.

def can_locked_valide_parentheses(self, s, locked):
    if len(s) % 2 == 1:
        return False

    left = 0
    for i, c in enumerate(s):
        if locked[i] == "0" or c == "(":
            left += 1
        elif left > 0:
            left -= 1
        else:
            return False

    left = 0
    for i in range(len(s) - 1, -1, -1):
        if locked[i] == "0" or s[i] == ")":
            left += 1
        elif left > 0:
            left -= 1
        else:
            return False
    return True




