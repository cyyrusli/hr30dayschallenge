# Day 16 coding challenge - Exceptions: String to Integer

# Read a string, S, and print its integer value; if S cannot be converted to an integer, print Bad String.

import sys

S = input().strip()

try:
    i = int(S)
    print(i)
except ValueError:
    print('Bad String')