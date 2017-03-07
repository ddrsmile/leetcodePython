# -*- coding: utf-8 -*-
from project.utils.InputHandler import InputHandler
from project.sols.sol import Solution

class Base(object):
    def __init__(self, path):
        self.ih = InputHandler(path)
        self.sol = Solution()
