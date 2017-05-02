# -*- coding: utf-8 -*-
from src.main.base import Base
from src.utils.inputparser.parser import IntegerParser

class Main(Base):
    def __init__(self, path):
        super(Main, self).__init__(path, IntegerParser)

    def main(self):
        input_list = self.parser.parse_data_as_list()

        for list in input_list:
            height = list
            print(self.sol.maxArea(height))
