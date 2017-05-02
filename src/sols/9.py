# -*- coding: utf-8 -*-
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x < 10:
            return True

        max_val = (1<<31) - 1
        tmp = x
        converted = 0

        while tmp != 0:
            if converted != 0 and max_val/converted < 10:
                return False
            converted = converted*10 + tmp%10
            tmp //= 10


        return converted == x