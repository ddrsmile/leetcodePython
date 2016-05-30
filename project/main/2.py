# -*- coding: utf-8 -*-
from .base import Base
from ..objs.ListNode import ListNode
from ..utils.ListNodes import ListNodes

class Main(Base):
    def __init__(self, path):
        Base.__init__(self, path)
        self.list_util = ListNodes()

    def main(self):
        in_int_list = self.ih.get_data_as_int_list()

        for i in range(len(in_int_list)//2):
            l1 = self.list_util.get_list(in_int_list[2*i])
            l2 = self.list_util.get_list(in_int_list[2*i + 1])
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
