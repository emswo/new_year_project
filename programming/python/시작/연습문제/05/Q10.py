import os
os.chdir("C:\\Users\\Kenonix\\programming\\python\\연습문제\\05")
print(os.getcwd())
lp = os.popen("dir")
print(list(lp))