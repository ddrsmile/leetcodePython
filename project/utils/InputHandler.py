#!/usr/bin/env python
# -*- coding: utf-8 -*-

class InputHandler(object):
    def __init__(self, path = ''):
        self.path = path
    
        # container for integer
        self.in_int = None
        self.in_int_list = None
        self.in_int_lists = None
        self.in_int_matrix = None
    
        # container for double
        self.in_float = None
        self.in_float_list = None
        self.in_float_lists = None
        self.in_float_matrix = None

        # container for str
        self.in_str = None
        self.in_str_list = None
        self.in_str_lsits = None
        self.in_str_matrix = None

    def __get_int(self, chars):
        return int(chars)

    def __get_float(self, chars):
        return float(chars)

    def __get_int_list(self, chars):
        if not '[' in chars and not ']' in chars:
            return [int(chars)]

        chars = chars[1:-1]
        if not chars:
            return []
        ints = chars.split(',')
        outs = []
        for n in ints:
            outs.append(int(n))

        return outs

    def __get_float_list(self, chars):
        if not '[' in chars and not ']' in chars:
            return [float(chars)]

        chars = chars[1:-1]
        if not chars:
            return []
        floats = chars.split(',')
        outs = []
        for n in floats:
            outs.append(float(n))

        return outs

    def __get_int_lists(self, chars):
        if not '[' in chars and not ']' in chars:
            return [[int(chars)]]

        chars = chars[1:-1]
        if not chars:
            return [[]]

        chars = chars.replace('],[', '], [')
        ints = chars.split(', ')
        out_lists = []
        for item in ints:
            out_lists.append(self.__get_int_list(item))

        return out_lists

    def __get_float_lists(self, chars):
        if not '[' in chars and not ']' in chars:
            return [[float(chars)]]

        chars = chars[1:-1]
        if not chars:
            return [[]]

        chars = chars.replace('],[', '], [')
        floats = chars.split(', ')
        out_lists = []
        for item in floats:
            out_lists.append(self.__get_float_list(item))

        return out_lists

    def __get_str(self, chars):
        chars = chars.replace('"', '')
        return chars

    def __get_str_list(self, chars):
        chars = chars.strip()[1:-1]
        strs = chars.split(',')
        out_list = []
        for c in strs:
            out_list.append(c.strip().replace('"', ''))

        return out_list

    def get_data_as_int(self):
        if not self.path:
            return self.in_int

        self.in_int = []

        with open(self.path, 'r') as in_file:
            for line in in_file:
                self.in_int.append(self.__get_int(line.strip()))

        return self.in_int

    def get_data_as_int_list(self):
        if not self.path:
            return self.in_int_list

        self.in_int_list = []

        with open(self.path, 'r') as in_file:
            for line in in_file:
                self.in_int_list.append(self.__get_int_list(line.strip()))

        return self.in_int_list
    
    def get_data_as_int_lists(self):
        if not self.path:
            return self.in_int_lists

        self.in_int_lists = []

        with open(self.path, 'r') as in_file:
            for line in in_file:
                self.in_int_lists.append(self.__get_int_lists(line.strip()))

        return self.in_int_lists

    def get_data_as_float(self):
        if not self.path:
            return self.in_float

        self.in_float = []

        with open(self.path, 'r') as in_file:
            for line in in_file:
                self.in_float.append(self.__get_int(line.strip()))

        return self.in_float

    def get_data_as_float_list(self):
        if not self.path:
            return self.in_float_list

        self.in_float_list = []

        with open(self.path, 'r') as in_file:
            for line in in_file:
                self.in_float_list.append(self.__get_float_list(line.strip()))

        return self.in_float_list

    def get_data_as_float_lists(self):
        if not self.path:
            return self.in_float_lists

        self.in_float_lists = []

        with open(self.path, 'r') as in_file:
            for line in in_file:
                self.in_float_lists.append(self.__get_float_lists(line.strip()))

        return self.in_float_lists

    def get_data_as_str(self):
        if not self.path:
            return self.in_str

        self.in_str = []

        with open(self.path, 'r') as in_file:
            for line in in_file:
                self.in_str.append(self.__get_str(line.strip()))

        return self.in_str

    def get_data_as_str_list(self):
        if not self.path:
            return self.in_str_list

        self.in_str_list = []

        with open(self.path, 'r') as in_file:
            for line in in_file:
                self.in_str_list.append(self.__get_str_list(line.strip()))

        return self.in_str_list
