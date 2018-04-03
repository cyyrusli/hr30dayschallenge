# Day 5 coding challenge - Loops
# Given an integer, n, print its first 10 multiples. Each multiple n (where 1<= i <= 10) should
# be printed on a new line in the form: n x i = result.

import sys

n = int(input().strip())

for i in range (1, 11):
    result = n * i
    print(str(n) + ' x ' + str(i) + ' = ' + str(result))