class Solution(object):
    def search(self, nums, target):
        #  this function helps us find the pivot point
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
            return mid # mid here is index of the point

    # def helper(self, arr, mid, goal):
    #     left = 0
    #     right = arr[mid]
    #     while left <= right:
    #         middle = (left + right) // 2
    #         if middle <= goal:
    #             left = middle + 1
    #         if middle > goal:
    #             right = middle - 1
    #     ret

if __name__ == '__main__':
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], 3))
