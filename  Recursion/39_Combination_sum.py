"""
given the two arrys, the ans should follow the order, if the ele in order is before the ele1,
then in ans, the ele should be located before the ele1

recursion needs get back to check different element
"""


class Solution:
    def combine(self, candidates: int, target: int):
        candidates.sort()
        if candidates[0] > target:
            return []
        return self.helper_func(candidates, target, [])

    # get the current_val and its remain(target - current_val), then to check if there is any ele can make the remain val.
    # the content of return will be the combination of remain val form candidates list
    # the fomrat of return is list of list,
    # return [[2, 2, 3], [3, 5]]
    # if cannot find any meaningful result, return []


    def helper_func(self, nums, goal, comb):
        res = []
        if goal == 0:
            res.append(list(comb))
            return res

        for ele in range(len(nums)):
            remain = goal - nums[ele]
            if remain < 0:
                continue
            comb.append(nums[ele])
            remain_comb = self.helper_func(nums[ele:], remain, comb)
            res.extend(remain_comb)
            comb.pop()

        return res


if __name__ == '__main__':
    print(Solution().combine([2,3,5], 8))