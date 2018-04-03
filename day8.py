# Day 8 coding challenge - Dictionaries and Maps

# Given n names and phone numbers, assemble a phone book that maps friends' names to their
# respective phone numbers. You will then be given an unknown number of names to query your
# phone book for. For each name queried, print the associated entry from your phone book on
# a new line in the form name=phoneNumber; if an entry for name is not found, print Not
# found instead.
# Note: Your phone book should be a Dictionary/Map/HashMap data structure.

phoneBook = {}
ip = []
q = []
n = int(input())

for i in range (n):
  ip = input().split(' ')
  phoneBook[ip[0]] = ip[1]

for j in range (n):
  a = input()
  q.append(a)

for k in range (n):
  if q[k] in phoneBook:
    a = phoneBook.get(q[k])
    print(q[k] + '=' + a)
  else:
    print('Not found')