# -*- coding: utf-8 -*-
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        map = [-1]*256
        x = -1
        res = 0
        for i, c in enumerate(s):
            x = max(map[ord(c)] + 1, x)
            map[ord(c)] = i
            res = max(res, i - x + 1)
        return res
