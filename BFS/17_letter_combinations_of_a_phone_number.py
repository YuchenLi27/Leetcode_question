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

        self.dfs(digits, 0, dic, '', res)
        return res

    def dfs(self, nums, index, dic, path, res):
        if index >= len(nums):
            res.append(path)
            return
        string1 = dic[nums[index]]
        for ele in string1:
            self.dfs(nums, index + 1, dic, path + ele, res)

if __name__ == "__main__":
    print(Solution().letterCombinations("23"))


