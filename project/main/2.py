# -*- coding: utf-8 -*-
from project.main.base import Base
from project.utils.inputparser.parser import IntegerParser
from project.utils.ListNodes import ListNodes

class Main(Base):
    def __init__(self, path):
        super(Main, self).__init__(path)
        self.list_util = ListNodes()

    def main(self):
        self.factory.set_type(IntegerParser)
        int_parser = self.factory.create(self.path)
        input_list = int_parser.parse_data_as_list()


        for i in range(len(input_list)//2):
            l1 = self.list_util.get_list(input_list[2*i])
            l2 = self.list_util.get_list(input_list[2*i + 1])
            head = self.sol.addTwoNumbers(l1, l2)

            if not head:
                print("NO INPUT")
                continue
            
            res = ''
            while head.next:
                res += str(head.val) + ','
                head = head.next
            res += str(head.val)
            print(res)
