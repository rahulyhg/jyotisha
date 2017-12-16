#!/usr/bin/python3
#  -*- coding: utf-8 -*-
from jyotisha.names.init_names_auto import init_names_auto
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s {%(filename)s:%(lineno)d}: %(message)s "
)


if __name__ == '__main__':
    NAMES = init_names_auto()

    # TODO: Fix the below.
    for angam in NAMES:
        fname = '%s_names.md' % angam.lower()
        with open(fname, 'w') as f:
            f.write('## ' + angam + '\n')
            f.write('(as initialised from `init_names_auto.py`)\n\n')
            f.write('| # | ' + ' | '.join(sorted(list(NAMES[angam].keys()))) + ' |\n')
            f.write('|---| ' + ' | '.join(['-' * len(scr)
                                           for scr in sorted(list(NAMES[angam].keys()))]) + ' |\n')
            for num in sorted(list(NAMES[angam]['hk'])):
                line = '| %d' % num
                for scr in sorted(list(NAMES[angam].keys())):
                    line += ' | ' + NAMES[angam][scr][num]
                f.write(line + ' |\n')
