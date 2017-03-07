# -*- coding: utf-8 -*-
from project.main.base import Base

class Main(Base):
    def __init__(self, path):
        Base.__init__(self, path)

    def main(self):
        ins = self.ih.get_data_as_int_list()
        
        for i in range(len(ins)//2):
            nums = ins[2*i]
            target = ins[2*i + 1][0]
            print(self.sol.twoSum(nums, target))
