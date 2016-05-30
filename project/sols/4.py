# -*- coding: utf-8 -*-

class Solution(object):
    def findMedianSortedArrays(self, arr1, arr2):
        m = len(arr1)
        n = len(arr2)
        total = m + n

        if total%2 != 0:
            return float(self.helper(arr1, 0, m - 1, arr2, 0, n - 1, total//2))
        else:
            x = float(self.helper(arr1, 0, m - 1, arr2, 0, n - 1, total//2))
            y = float(self.helper(arr1, 0, m - 1, arr2, 0, n - 1, total//2 + 1))
            return (x + y)/2

    def helper(self, a, aS, aE, b, bS, bE, k):
        m = aE - aS + 1
        n = bE - bS + 1

        if m > n:
            return self.helper(b, bS, bE, a, aS, aE, k)

        if m == 0:
            return b[k - 1]

        if k == 1:
            return a[aS] if a[aS] < b[bS] else b[bS]

        part_a = k//2 if k//2 < m else m
        part_b = k - part_a

        if a[aS + part_a - 1] < b[bS + part_b - 1]:
            return self.helper(a, aS + part_a, aE, b, bS, bE, k - part_a)
        elif a[aS + part_a - 1] > b[bS + part_b - 1]:
            return self.helper(a, aS, aE, b, bS + part_b, bE, k - part_b)
        else:
            return a[aS + part_a - 1]
