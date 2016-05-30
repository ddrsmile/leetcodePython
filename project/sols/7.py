# -*- coding: utf-8 -*-
class Solution(object):
    def reverse(self, x):
        max_val = ((1<<31) - 1) // 10
        flag = True
        res = 0

        if x < 0:
            x = -x
            flag = False

        while x != 0:
            if res != 0 and res > max_val:
                return 0
            res = res*10 + x%10
            x //= 10

        return res if flag else -res
