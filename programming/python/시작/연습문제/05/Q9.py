import sys, os
a = sys.argv
summ = 0
for i in a:
    if i == a[0] : continue
    summ += int(i)
print(summ)