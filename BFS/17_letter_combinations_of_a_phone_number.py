"""
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.
Return the answer in any order.
"""


class Solution(object):
    def letterCombinations(self, digits):

        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        res = []
        if len(digits) == 0:
            return res
        self.helper(digits, 0, dic, [], res)
        return res

    def helper(self, nums, curr, dic, path, res):
        if len(path) == len(nums):
            res.append("".join(path))
            return

        for ele in dic[nums[curr]]:
            path.append(ele)
            self.helper(nums, curr + 1, dic, path, res)
            path.pop()



if __name__ == "__main__":
    print(Solution().letterCombinations("23"))


