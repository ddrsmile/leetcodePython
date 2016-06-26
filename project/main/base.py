# -*- coding: utf-8 -*-
from ..utils.InputHandler import InputHandler
from ..sols.sol import Solution

class Base(object):
    def __init__(self, path):
        self.ih = InputHandler(path)
        self.sol = Solution()
