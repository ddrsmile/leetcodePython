# -*- coding: utf-8 -*-
class Solution(object):
    def maxArea(self, height):
        if not height:
            return 0

        max_val = -(1<<31)
        low = 0
        high = len(height) - 1

        while low < high:
            area = (high - low) * min(height[low], height[high])
            max_val = max(max_val, area)
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return max_val