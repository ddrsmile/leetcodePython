# -*- coding: utf-8 -*-
from .base import Base

class Main(object):
    def __init__(self, path):
        Base.__init__(self, path)

    def main(self):
        in_int_list = self.ih.get_data_as_int_list()

        for i in range(len(in_int_list)//2):
            arr1 = in_int_list[2*i]
            arr2 = in_int_list[2*i + 1]
            print(self.sol.findMedianSortedArrays(arr1, arr2))
