# -*- coding: utf-8 -*-
from .base import Base


class Main(Base):
    def __init__(self, path):
        Base.__init__(self, path)

    def main(self):
        in_int = self.ih.get_data_as_int()

        for i in range(len(in_int)):
            s = in_int[i]
            print(self.sol.isPalindrome(s))