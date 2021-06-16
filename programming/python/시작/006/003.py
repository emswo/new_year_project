def paging(d,o):
    if d%o == 0:
        return d//o
    else:
        return d//o+1
    
print(paging(50,5))