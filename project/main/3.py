# -*- coding utf-8 -*-
from ..utils.InputHandler import InputHandler
from ..sols.sol import Solution

class Main(object):
    def __init__(self, path):
        self.ih = InputHandler(path)
        self.sol = Solution()

    def main(self):
        in_str = self.ih.get_data_as_str()

        for str in in_str:
            print(self.sol.lengthOfLongestSubstring(str))
