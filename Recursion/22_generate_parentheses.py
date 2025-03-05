"""
generate parentheses. given n pairs of parenthesese, get all combination of well-formed results
"""
class Solution:
    def generateParenthesis(self, n):
        res_set = self.helper(n)
        res_list = list(res_set)
        return res_list

    def helper(self,n):
        res = set()
        if n == 0:
            return set()
        if n == 1:
            return set(["()"])

        smallar_part = self.helper(n - 1)
        for i in smallar_part:
            outter = "(" + i + ")"
            right = i + "()"
            left = "()" + i

            res.add(outter)
            res.add(right)
            res.add(left)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))
