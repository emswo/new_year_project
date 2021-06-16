import os
os.chdir("C:\\Users\\Kenonix\\programming\\python\\연습문제\\05")
print(os.getcwd())
lp = list(os.popen("dir"))
for i in lp:
    if '.py' in i:
        print(i)