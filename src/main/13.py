# -*- coding: utf-8 -*-
from src.main.base import Base
from src.utils.inputparser.parser import StringParser

class Main(Base):
    def __init__(self, path):
        super(Main, self).__init__(path, StringParser)

    def main(self):
        input_values = self.parser.parse_data_as_single_value()

        for val in input_values:
            print(self.sol.romanToInt(val))
