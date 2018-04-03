# Day 14 coding challenge - Scope

# The absolute difference between two integers, a and b, is written as |a-b|. The
# maximum absolute difference between two integers in a set of positive integers,
# elements, is the largest absolute difference between any two integers in elements.

# Complete the Difference class by writing the following:
# - A class constructor that takes an array of integers as a parameter and saves it to the
#   elements instance variable.
# - A computeDifference method that finds the maximum absolute difference between
#   any 2 numbers in N and stores it in the maximumDifference instance variable.

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        l = len(a)
        for i in range(l):
            for j in range(i+1, l):
                difference = abs(a[i] - a[j])
                self.maximumDifference = max(difference, self.maximumDifference)


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)