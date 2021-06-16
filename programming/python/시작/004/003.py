f = open("newfile.txt",'w')
f.close()

f = open("newfile.txt",'w')
for i in range(1,10):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()

#프로그램 외부에 저장된 파일을 읽는 여러가지 방법
#1. readline 사용
# f = open("newfile.txt",'r')
# while True :
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

#2. readlines 사용
# f = open("newfile.txt",'r')
# lines = f.readlines()
# print(lines)
# for line in lines:
#     print(line)
# f.close()

#3. read 함수 사용
# f = open("newfile.txt",'r')
# lines = f.read()
# print(lines)
# f.close()

#with문과 함께 사용
# with open("foo.txt",'w') as k:
#     k.write("Life is too short, you need python")

