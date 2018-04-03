# Day 7 coding challenge - Arrays
# Given an array, A, of N integers, print A's elements in reverse order as a single
# line of space-separated numbers

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

t = []
for i in reversed(arr):
    t.append(str(i))

print(' '.join(t))