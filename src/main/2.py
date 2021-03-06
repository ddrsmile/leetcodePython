# -*- coding: utf-8 -*-
from src.main.base import Base
from src.utils.inputparser.parser import IntegerParser
from src.utils.ListNodes import ListNodes

class Main(Base):
    def __init__(self, path):
        super(Main, self).__init__(path, IntegerParser)
        self.list_util = ListNodes()

    def main(self):
        input_list = self.parser.parse_data_as_list()

        for i in range(len(input_list)//2):
            l1 = self.list_util.get_list(input_list[2*i])
            l2 = self.list_util.get_list(input_list[2*i + 1])
            head = self.sol.addTwoNumbers(l1, l2)
            self.list_util.show_list(head)