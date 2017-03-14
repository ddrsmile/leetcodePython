# -*- coding: utf-8 -*-
import os, sys
from shutil import copy

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MAIN_DIR = os.path.join(BASE_DIR, 'main')
SOLS_DIR = os.path.join(BASE_DIR, 'sols')
INPUT_DIR = os.path.join(BASE_DIR, 'input')

class SetFile(object):
    def __init__(self):
        self.case_num = None
    
    def update(self, case_num):
        self.case_num = case_num

        main_src = os.path.join(MAIN_DIR, '{case_num}.py'.format(case_num=case_num))
        main_dist = os.path.join(MAIN_DIR, 'main.py')
        print(main_src)
        copy(main_src, main_dist)

        sol_scr = os.path.join(SOLS_DIR, '{case_num}.py'.format(case_num=case_num))
        sol_dist = os.path.join(SOLS_DIR, 'sol.py')
        copy(sol_scr, sol_dist)

    def get_input_path(self):
        if self.case_num:
            return os.path.join(INPUT_DIR, '{case_num}.txt'.format(case_num=self.case_num))
        raise Exception("please update case number before get input path...")
