class Solution:
    def search(self, nums, target):
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        if nums[0] < nums[-1]:
            return self.find_target(0, len(nums) - 1, target, nums)

        pivot_idx = self.search_pivot(nums)
        return self.search_which_phase(nums, pivot_idx, target)

    def search_pivot(self, nums):
        #  this function helps us find the pivot point
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                return mid

            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid
            else:
                return mid  # mid here is index of the point

    # let us know where does the target locate and then do bs individually
    def search_which_phase(self, nums, pivot_idx, goal):

        if nums[0] <= goal <= nums[pivot_idx]:
            res = self.find_target(0, pivot_idx, goal, nums)
        else:
            res = self.find_target(pivot_idx + 1, len(nums) - 1, goal, nums)
        return res

    #  help use to find the position of the goal, if it does exist
    def find_target(self, left, right, goal, nums):
        while left <= right:
            middle = (left + right) // 2
            val = nums[middle]
            if val < goal:
                left = middle + 1
            if val > goal:
                right = middle - 1
            if val == goal:
                return middle
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search_pivot([5, 1, 3]))
# if __name__ == '__main__':
#     s = Solution()
#     print(s.find_target(0, 3, 5, [4, 5, 6, 7, 0, 1, 2]))
# if __name__ == '__main__':
#     s = Solution()
#     print(s.search_which_phase([4, 5, 6, 7, 0, 1, 2], 3, -2))
