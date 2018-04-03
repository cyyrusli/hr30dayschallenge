# Day 9 coding challenge - Recursion

# Write a factorial function that takes a positive integer, N as a parameter and prints the result
# of N!(N factorial).

import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)