# -*- coding: utf-8 -*-
from project.main.base import Base

class Main(Base):
    def __init__(self, path):
        Base.__init__(self, path)

    def main(self):
        in_str = self.ih.get_data_as_str()
        
        for i in range(len(in_str)):
            s = in_str[i]
            print(self.sol.myAtoi(s))
