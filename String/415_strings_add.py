"""
meta interview question 1
ie. str1 = "123", str2 = "2" res = "125"
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # get every ele of string from the end
        # be careful with the carry, if after add, the result is two digits
        # mind the idx, control it within the len of num1 and num2
        # 8 + 9
        n1 = len(num1) - 1
        n2 = len(num2) - 1
        carry = 0
        res = []
        while n1 >= 0 and n2 >= 0:
            x1 = ord(num1[n1]) - ord("0") if n1 >= 0 else 0
            x2 = ord(num2[n2]) - ord("0") if n2 >= 0 else 0
            value = (x1 + x2 + carry)
            # mind which one is first to get, value or carry? why?
            value = value % 10  # 7
            carry = value // 10 # 1
            res.append(value)
            n1 -= 1
            n2 -= 1
        if carry:
            res.append(carry)
        return res[::-1]
        # if the format of ans is not string, it should be written as
        # return ''.join(str(x) for x in res[::-1])