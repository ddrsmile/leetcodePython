# -*- coding: utf-8 -*-

class Solution(object):
    def convert(self, s, n_row):
        if not s:
            return ''

        if n_row == 1:
            return s

        size = 2*n_row - 2
        res = []
        for i in range(n_row):
            for j in range(i, len(s), size):
                res.append(s[j])
                if i != 0 and i != n_row - 1:
                    tmp = j + size - 2*i
                    if tmp < len(s):
                        res.append(s[tmp])

        return ''.join(res)
