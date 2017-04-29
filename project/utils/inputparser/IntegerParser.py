# -*- coding: utf-8 -*-
from . import Parser

class IntegerParser(Parser):
    def __init__(self):
        super(IntegerParser, self).__init__()

    def _to_value(self, chars):
        chars = self.clean_chars(chars)
        return int(chars.strip())

