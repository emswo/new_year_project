#변수
a = 1
b = "python"
c = [1,2,3]
#변수의 메모리주소
print(id(a),id(b),id(c))

#리스트 복사
#동일한 객체를 지시
d = c
print(d is c)
c[1] = 'G'
print(d)

#복사 1
e = c[:]
c[1] = 2
print(e)

#복사 2
from copy import copy
a = [1,2,3]
b = copy(a)
a[1] = 'G'
print(b)

#변수를 만드는 방법들
a , b = ('python' , 'life')
(a,b) = 'python' , 'life'
[a,b] = ['python' , 'life']
a=b='python'
#값 바꾸기
a = 3
b = 5
a,b=b,a
print(a,b)
