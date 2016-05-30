#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .base import Base

class Main(Base):
    def __init__(self, path):
        Base.__init__(self, path)

    def main(self):
        in_str = self.ih.get_data_as_str()

        for s in in_str:
            print(self.sol.longestPalindrome(s))
        
