g3 = 0
g5 = 0
for i in range(1,1001):
    if i%3 == 0 : g3 += i
    elif i%5 == 0 : g5 += i
print (g3+g5)