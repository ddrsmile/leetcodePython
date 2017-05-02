# -*- coding: utf-8 -*-
class Solution(object):
    def romanToInt(self, s):
        if not s:
            return 0

        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = 0

        for symbol, val in zip(symbols, vals):
            if len(symbol)%2 == 1:
                while s[0:1] == symbol:
                    res += val
                    s = s[1:]
                    if len(s) < 1:
                        break
            else:
                if len(s) > 2:
                    while s[0:2] == symbol:
                        res += val
                        s = s[2:]
                        if len(s) < 1:
                            break
        return res