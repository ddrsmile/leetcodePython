# -*- coding: utf-8 -*-

class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ''

        max_str = ''
        for i in range(len(s)):
            tmp = self.__helper(s, i, i)
            max_str = tmp if len(tmp) > len(max_str) else max_str
            tmp = self.__helper(s, i, i + 1)
            max_str = tmp if len(tmp) > len(max_str) else max_str

        return max_str

    def __helper(self, s, low, high):
        while low >= 0 and high < len(s) and s[low] == s[high]:
            low -= 1
            high += 1

        return s[low + 1: high]
