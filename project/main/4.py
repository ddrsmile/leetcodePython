# -*- coding: utf-8 -*-
from project.main.base import Base
from project.utils.inputparser.parser import IntegerParser

class Main(Base):
    def __init__(self, path):
        super(Main, self).__init__(path, IntegerParser)

    def main(self):
        input_list = self.parser.parse_data_as_list()

        for i in range(len(input_list)//2):
            arr1 = input_list[2*i]
            arr2 = input_list[2*i + 1]
            print(self.sol.findMedianSortedArrays(arr1, arr2))
