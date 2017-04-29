# -*- coding: utf-8 -*-
from project.main.base import Base
from project.utils.inputparser.parser import IntegerParser


class Main(Base):
    def __init__(self, path):
        super(Main, self).__init__(path)

    def main(self):
        self.factory.set_type(IntegerParser)
        int_parser = self.factory.create(self.path)
        input_values = int_parser.parse_data_as_single_value()

        for value in input_values:
            print(self.sol.isPalindrome(value))
