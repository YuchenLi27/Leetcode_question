class Solution(object):
    def search(self, nums, target):
        #  this function helps us find the pivot point
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid - 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                return mid # mid here is index of the point

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
    print(s.search([4,5,6,7,0,1,2], 3))
# if __name__ == '__main__':
#     s = Solution()
#     print(s.find_target(0, 3, 5, [4, 5, 6, 7, 0, 1, 2]))
# if __name__ == '__main__':
#     s = Solution()
#     print(s.search_which_phase([4, 5, 6, 7, 0, 1, 2], 3, -2))
