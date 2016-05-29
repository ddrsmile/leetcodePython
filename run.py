#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from project._config import SetFile 

try:
    prob_num = sys.argv[1]
except IndexError:
    msg = "Please input problem number!\n"
    msg += "Or input 'test' to test the utils"
    print(msg)
    sys.exit(1)

set_file = SetFile(prob_num)
input_file = set_file.get_input_path()
from project.main import main

m = main.Main(input_file)
m.main()
