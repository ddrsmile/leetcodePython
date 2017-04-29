#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
from project import SetFile

unload_modules = [
    'project.main.main',
    'project.main',
    'project.main.base',
    'project.sols.sol',
    'project.sols',
    'project.utils.inputparser',
    'project.utils.inputparser.parserfactory',
    'project.utils.inputparser.parser'
]

def get_cases():
    for f in os.listdir('./project/main'):
        if f.endswith('.py') and f != 'base.py' and f != 'main.py' and f != '__init__.py':
            yield(f.split('.')[0])

def run(input_path):
    from project.main import main
    m = main.Main(input_path)
    m.main()

def unload():
    for module in unload_modules:
        try:
            del sys.modules[module]
        except KeyError:
            pass
        

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="run test cases, please assign either all or case...")
    parser.add_argument("cases", nargs="*", type=int, help="assign the numbers of test cases...")
    parser.add_argument("-a", "--all", dest='all', action='store_true', help="assign all to run all test cases...")
    parser.set_defaults(all=False)
    args = parser.parse_args()

    if not (args.all or args.cases) or (args.all and args.cases):
        parser.error("please assign either all or case")
    
    run_stat = "python run.py {case_num}"
    set_file = SetFile()

    cases = get_cases() if args.all else args.cases

    for case in cases:
        print('RUN TEST {case}'.format(case=case))
        set_file.update(case)
        input_path = set_file.get_input_path()
        print('========== RESULT ==========')
        run(input_path)
        print('=========== DONE ===========')
        print()
        unload()
    
    print("Completed running test...")