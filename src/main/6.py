# -*- coding: utf-8 -*-
from src.main.base import Base
from src.utils.inputparser.parser import StringParser

class Main(Base):
    def __init__(self, path):
        super(Main, self).__init__(path, StringParser)

    def main(self):
        input_values = self.parser.parse_data_as_single_value()
        
        for i in range(len(input_values)//2):
            s = input_values[2*i]
            n_row = int(input_values[2*i + 1])

            print(self.sol.convert(s, n_row))
        
