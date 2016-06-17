# -*- coding: utf-8 -*-
import os


def get_cases():
    for f in os.listdir('./project/main'):
        if f.endswith('.py') and f != 'base.py' and f != 'main.py':
            yield(f.split('.')[0])

cases = get_cases()
run_stat = 'python run.py %s'

print('START RUN TEST')
for case in cases:
    case = str(case)
    print('RUN TEST ' + case)
    print(run_stat % case)
    os.system(run_stat % case)
    print('DONE')
    print()
