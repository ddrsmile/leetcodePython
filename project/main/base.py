# -*- coding: utf-8 -*-
from project.utils.inputparser.parserfactory import ParserFactory
from project.sols.sol import Solution

class Base(object):
    def __init__(self, path, parser_type):
        self.path = path
        factory = ParserFactory(parser_type)
        self.parser = factory.create(path)
        self.sol = Solution()
