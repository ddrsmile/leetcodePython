# -*- coding: utf-8 -*-
from project.main.base import Base
from project.utils.inputparser.parser import IntegerParser

class Main(Base):
    def __init__(self, path):
        super(Main, self).__init__(path)

    def main(self):
        self.factory.set_type(IntegerParser)
        int_parser = self.factory.create(self.path)
        input_list = int_parser.parse_data_as_list()

        for list in input_list:
            height = list
            print(self.sol.maxArea(height))
