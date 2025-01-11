"""
use ALL the characters in s to construct k palindrome
"""
from collections import defaultdict


class Solution:
    def longestPalindrome(self, s, k):
        #  check if the character in s could be mod by 2
        if len(s) < k:
            return False
        if len(s) == k:
            return True

        res = 0
        frq = defaultdict()
        for letter in s:
            if letter in frq:
                frq[letter] += 1
            else:
                frq[letter] = 1
        for key, cnt in list(frq.items()):
            if cnt % 2 == 1:
                res += 1
        return res <= k