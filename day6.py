# Day 6 coding challenge - Strings and Loops
#Given a string, S, of length Nthat is indexed from 0 to N-1, print its even-indexed and odd-
# indexed characters as 2 space-separated strings on a single line

t = []
e = []
o = []

n = int(input())

for x in range (n):
    s = input()
    t.append(s)

for p in range (len(t)):
    del e[:]
    del o[:]
    y = list(t[p])

    for i in range (1, len(y), 2):
        a = y[i]
        e.append(a)
    for j in range (0, len(y), 2):
        b = y[j]
        o.append(b)

    print (''.join(o) + ' ' + ''.join(e))
