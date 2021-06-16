import sys 
a = sys.argv[1]
b = sys.argv[2]
print(a,b)
af = open(a,'r')
bf = open(b,'w')
ap = af.read()
ko = ap.replace("\t","    ")
print(ap)
print(ko)
bf.write(ko)
af.close()
bf.close()
