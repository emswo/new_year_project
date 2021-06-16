import sys
try:
    option = sys.argv[1]
except:
    print('ERROR CODE [0] : no input content')
    exit()
#print(option,memo)
try:
    memo = sys.argv[2]
except: pass
if option == '-a' :
    f = open('memo.txt','a')
    f.write(memo)
    f.write('\n')
    f.close()
    print(memo)
elif option =='-v':
    f = open('memo.txt','r')
    memo = f.read()
    f.close()
    print(memo)
    