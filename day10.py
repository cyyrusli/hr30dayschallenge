# Day 10 coding challenge - Binary Numbers

# Given a base-10 integer, , convert it to binary (base-2). Then find and print the base-10
# integer denoting the maximum number of consecutive 1's in n's binary representation.

import sys

count = 0
current = 0
n = int(input().strip())

binary = list("{0:b}".format(n))

for i in range (len(binary)):
  if binary[i] == '1':
    count += 1
  else:
    if current < count:
      current = count
    count = 0

if current < count:
  current = count
  print(current)
else:
  print(current)