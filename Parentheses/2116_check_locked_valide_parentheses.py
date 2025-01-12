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


