import math


def maxSubArray(nums):
    def binary_helper(left, right, nums):
        if left > right:
            return -math.inf
        cur_sum = 0
        l_total = 0
        r_total = 0
        mid =  (left + right) // 2
        for i in range(0, mid - 1):
            cur_sum += nums[i]
            l_total = max(l_total, cur_sum)

        r_total = 0
        for i in range(mid + 1, right + 1):
            cur_sum += nums[i]
            r_total = max(r_total, cur_sum)
        good_ans = nums[mid] + l_total + r_total

        left_ans = binary_helper(0, mid - 1, nums)
        right_ans = binary_helper(mid + 1, right, nums)
        return max(good_ans, left_ans, right_ans)
    return binary_helper(0, len(nums) -1, nums)


if __name__ == '__main__':
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
