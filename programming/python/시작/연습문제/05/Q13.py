import random
maxi = -999
mine = 999
a=0
k=0
while k<6:
    k = k + 1
    a = random.randrange(1,46)
    if maxi < a : maxi = a
    if mine > a : mine = a
    print(a,maxi,mine)