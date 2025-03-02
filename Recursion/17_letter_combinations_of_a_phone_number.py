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



"""
this question also have two more ways to solve
1. the first way below shows we get the answer based on the index of the input.

"""
# def letterCombinations(self, digits):
#     dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
#     res = []
#     self.helper(digits, 0, dic, res)
#     return res
#
# def helper(self, digits, curr, dic, res):
#     for ele in dic[digits[curr]]:
#         res.append(ele)
#         if curr == len(digits) - 1:
#             tmp_res = self.add_together()
#             res.append(tmp_res)
#         else:
#             self.helper(digits, curr + 1, dic)
#         res.pop()
# def add_together(self, res):
#     ans = ""
#     for i in res:
#         ans += res
#     return ans

if __name__ == "__main__":
    print(Solution().letterCombinations("253"))

"""
solution 2:

def letterCombinations(self, digits):
    res = []
    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    for digit in digits:
        curr = dic[digit]
        res = self.helper(res, curr)
    return res
        
def helper(self,res,curr):
    path = []
    for char in curr:
        if len(res) == 0:
            path.append(char)
        else:
            for com in res:
                new = com + char
                path.append(new)
    return path
    
"""


# def letterCombinations(self, digits: str) -> List[str]:
# dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
#     if len(digits) == 0:
#         return []
#     so_far_list = []
#     result = []
#     self.xuan(so_far_list, digits, 0, dic, result)
#     return result

#     res = []
#     if len(digits) == 0:
#         return res
#     self.helper(digits, 0, dic, [], res)
#     return res

# def helper(self, nums, curr, dic, path, res):
#     if len(path) == len(nums):
#         res.append("".join(path))
#         return

#     for ele in dic[nums[curr]]:
#         path.append(ele)
#         self.helper(nums, curr + 1, dic, path, res)
#         path.pop()


# def xuan(self, so_far_list, input_digit, cur_index, num_dic, result):
#     cur_letter = num_dic[input_digit[cur_index]]
#     for cur_char in cur_letter:
#         so_far_list.append(cur_char)
#         if cur_index == len(input_digit) - 1:
#             temp_res = self.cal_so_far_list(so_far_list)
#             result.append(temp_res)
#         else:
#             self.xuan(so_far_list, input_digit, cur_index+1, num_dic, result)
#         so_far_list.pop()

# def cal_so_far_list(self, so_far_list):
#     result = ""
#     for ele in so_far_list:
#        result = result + ele
#     return result