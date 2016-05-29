import os, sys
from shutil import copy

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MAIN_DIR = os.path.join(BASE_DIR, 'main')
SOLS_DIR = os.path.join(BASE_DIR, 'sols')
INPUT_DIR = os.path.join(BASE_DIR, 'input')

class SetFile(object):
    def __init__(self, prob_num):
        self.prob_num = prob_num
        main_src = os.path.join(MAIN_DIR, prob_num + '.py')
        main_dist = os.path.join(MAIN_DIR, 'main.py')
        copy(main_src, main_dist)

        sol_scr = os.path.join(SOLS_DIR, prob_num + '.py')
        sol_dist = os.path.join(SOLS_DIR, 'sol.py')
        copy(sol_scr, sol_dist)
    
    def get_input_path(self):
        return os.path.join(INPUT_DIR, self.prob_num + '.txt')
