#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys


def get_cases():
    for f in os.listdir('./project/main'):
        if f.endswith('.py') and f != 'base.py' and f != 'main.py':
            yield(f.split('.')[0])


cases = [x for x in get_cases()]

run_stat = 'python run.py {}'

print('STRAT RUN TEST')
for case in cases:
    print('RUN TEST ' + case)
    os.system(run_stat.format(case))
    print('DONE')
    print()
