"""
Question is ask the sum of the product of two elements of two arrays
for sparse vect: it has more zero values, so we just need to find the non-zero value and to multiply

"""
class SparseVector:
    def __init__(self, nums: List[int]):
        # store the non-zero value in a dict, can save us time/space
        self.vals = dict()
        # we need a count to remember the index, so we can find if two arrays has non-zero val, when share same index
        self.count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                self.vals[i] = nums[i]
                self.count += 1

    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        # we need to see if there is any value with the same index
        for k in self.vals.keys():
            if k in vec.vals:
                res += self.vals[k] * vec.vals[k]

        return res

# follow up: What if only one of the vectors is sparse?
# use the vec with more 0 to do for loop, so if the number of 0 is larger,
# so we use it to multiply the vec with more 0
# 谁sparce谁就放在for loop 里
        # if self.count < vec.count:
        #     for i in vec.vals:
        #         if i in self.vals.keys():
        #             res += self.vals[i] * vec.vals[i]
        # else:
        #     for i in self.vals.keys():
        #         if i in vec.vals:
        #             res += self.vals[i] * vec.vals[i]
        # return res

# time complexity from o(m or n) to o(min(m, n))
