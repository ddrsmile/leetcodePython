#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .base import Base

class Main(Base):
    def __init__(self, path):
        Base.__init__(self, path)

    def main(self):
        in_str = self.ih.get_data_as_str()
        
        for i in range(len(in_str)//2):
            s = in_str[2*i]
            n_row = int(in_str[2*i + 1])

            print(self.sol.convert(s, n_row))
        
