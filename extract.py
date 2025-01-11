#!/usr/bin/env python3

"""Extracts the flag from a modified version of highlyoptimized.c"""

import re

stack = []

def handle_mod(a, b):
    n = a % b
    print(chr(n), end='')

with open('highlyoptimized.c', 'r') as f:
    flag = False
    last_line = ''
    for line in f:
        if re.match(r'^_QWORD', line):
            flag = True
        if flag and re.match(r' +[0-9]+LL,$', line):
            # ignore the line with 9LL and duplicates
            if not re.match(r'  9LL,', line) and last_line != line:
                # remove LL, and spaces, convert to int
                num = int(re.sub(r'LL,', '', re.sub(r' +', '', line)))
                stack.append(int(num))
                if len(stack) == 2:
                    handle_mod(stack[0], stack[1])
                    stack = []
            last_line = line
        if re.match(r'}', line):
            flag = False
print()
