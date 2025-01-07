"""
Question: subarray sum equals K
answer blow shows how to print all arrays.
example of prefix_sum: {xx:xx}
"""

from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> List[List[int]]:
        prefix_sum = defaultdict(list)  # 使用列表存储每个前缀和对应的索引
        prefix_sum[0].append(-1)  # 初始前缀和为0，索引为-1代表空子数组
        current_sum = 0
        result = []

        for i in range(len(nums)):
            current_sum += nums[i]

            # 检查 current_sum - k 是否在字典中
            if (current_sum - k) in prefix_sum:
                # 对于每个符合条件的前缀和，找到所有子数组
                for j in prefix_sum[current_sum - k]:
                    result.append(nums[j + 1:i + 1])

            # 更新前缀和及其对应的索引
            prefix_sum[current_sum].append(i)

        return result

# 示例使用
# if __name__ == "__main__":
#     solution = Solution()
#     result = solution.subarraySum([1, 2, 3], 3)
#     print(result)  # 输出符合条件的所有子数组
