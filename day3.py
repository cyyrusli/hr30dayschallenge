# Day 3 coding challenge - Intro to Conditional Statements

# Given an integer,N , perform the following conditional actions:
# If N  is odd, print Weird
# If N is even and in the inclusive range of  to , print Not Weird
# If N is even and in the inclusive range of  to , print Weird
# If N is even and greater than , print Not Weird

import sys

N = int(input().strip())

if N % 2 != 0:
    print('Weird')
elif N % 2 == 0:
    if 2 <= N <= 5:
        print('Not Weird')
    elif 6 <= N <= 20:
        print('Weird')
    elif N > 20:
        print('Not Weird')

