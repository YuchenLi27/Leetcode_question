class Solution:
    def oa_sum(self, nums):
        left_idx = 0
        right_idx = len(nums)-1
        left_total = 0
        right_total = 0
        while left_idx <= right_idx:
            print(left_total, right_total)
            print(left_idx, right_idx)
            print()
            if left_total < right_total:
                left_total += nums[left_idx]
                left_idx += 1
            elif left_total > right_total:
                right_total += nums[right_idx]
                right_idx -= 1
            else:
                if left_idx == right_idx:
                    return left_idx
                else:
                    left_total += nums[left_idx]
                    left_idx += 1
                    right_total += nums[right_idx]
                    right_idx -= 1

if __name__ == '__main__':
    s = Solution()
    # print(s.oa_sum([1,2,3,4,6]))
    # print(s.oa_sum([3, 4, 5, 4, 3]))
    print(s.oa_sum([4, 3, 5, 4, 3]))
