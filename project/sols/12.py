# -*- coding: utf-8 -*-
class Solution(object):
    def intToRoman(self, num):
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = ""

        for i, val in enumerate(vals):
            while num >= val:
                num -= val
                res += symbols[i]
        return res

