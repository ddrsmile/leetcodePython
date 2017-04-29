# -*- coding: utf-8 -*-
from project.utils.inputparser.parserfactory import ParserFactory
from project.sols.sol import Solution

class Base(object):
    def __init__(self, path):
        self.path = path
        self.factory = ParserFactory()
        self.sol = Solution()
