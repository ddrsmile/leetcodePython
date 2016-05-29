#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..utils.InputHandler import InputHandler
from ..sols.sol import Solution

class Main(object):

    def __init__(self, path):
        self.ih = InputHandler(path)
        self.sol = Solution()

    def main(self):
        ins = self.ih.get_data_as_int_list()
        
        for i in range(len(ins)//2):
            nums = ins[2*i]
            target = ins[2*i + 1][0]
            print(self.sol.twoSum(nums, target))
