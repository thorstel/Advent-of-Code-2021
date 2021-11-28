# TODO URL

from collections import *
from functools import *
import itertools
import re
import sys

def solve(data):
    for line in data.splitlines():
        print(line)

########################################################################
#                             SETUP STUFF                              #
########################################################################

sample_input = r"""
""".strip()

actual_input = r"""
""".strip()

if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as f:
        file_input = f.read().strip()
    solve(file_input)
else:
    print('=== SAMPLE ===')
    solve(sample_input)
    print('=== ACTUAL ===')
    solve(actual_input)
