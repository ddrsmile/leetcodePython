# -*- coding: utf-8 -*-
from ..utils.ListNodes import ListNodes
from ..utils.InputHandler import InputHandler
from ..objs.ListNode import ListNode
from ..sols.sol import Solution

class Main(object):
    def __init__(self, path):
        self.ih = InputHandler(path)
        self.list_util = ListNodes()
        self.sol = Solution()

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
