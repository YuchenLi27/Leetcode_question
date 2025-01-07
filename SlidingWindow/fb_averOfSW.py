"""
Find average of each Sliding window. Given an input array of n elements and a sliding window fo size k, find the average of each sliding window.
input = [1,2,3,4,5]
k = 3
output = [2.0, 3.0, 4.0]
(1+2+3)/ 3 = 2.0
(2+3+4)/3 = 3.0
(3+4+5)/3 = 4.0

Expectation was to solve it in O(n) time and O(1) space

https://leetcode.com/discuss/interview-experience/1700810/facebookmeta-ec5-phone-screen-jan22
"""
def findAverage(arr, k):
    ans = []
    i = 0
    j = 0
    n = len(arr)
    total = 0

    while j < n:
        total += arr[j]
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            avg = total / k
            ans.append(avg)
            total -= arr[i]
            i += 1
            j += 1
    return ans

if __name__ == '__main__':
    print(findAverage([1,2,3,4,5], 3))

