# -*- coding: utf-8 -*-
class Solution(object):
    def myAtoi(self, s):

        s = s.strip()
        if not s:
            return 0

        res = 0
        i = 0
        is_neg = False

        if s[0] == '-' or s[0] == '+':
            is_neg = (s[0] == '-')
            i += 1

        while len(s) > i and s[i] >= '0' and s[i] <= '9':
            res = res * 10 + int(s[i])
            i += 1

        res = -res if is_neg else res

        if res > (1<<31) - 1:
            return (1<<31) - 1
        elif res < -(1<<31):
            return -(1<<31)
        else:
            return res