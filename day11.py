# Day 11 coding challenge - 2D Arrays

# Given a 6 x 6 Array, A:
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0

# We define an hourglass in A to be a subset of values with indices falling in this pattern in A's
# graphical representation:
# a b c
#   d
# e f g
# There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.
# Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

print(arr)
for i in range (len(arr)):
    for j in range (len(arr[i])):
        print (arr[i][j])