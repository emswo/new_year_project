#일반적인 함수
# def add(a , b):
#     return a+b
# print(add(3,4))

# #입력값이 없는 함수
# def say ():
#     return 'HI'
# a = say()
# print(a)

# #결과값이 없는 함수
# def add (a,b) :
#     print(f"{a},{b}의 합은 {a+b}입니다")
# add(3,4) 

# #입력값도 결과값도 없는 함수
# def say():
#     print("hi")
# say()

# #매개변수를 지정하여 호출하기
# def add(a,b):
#     return a+b
# print(add(a=3,b=7))
# print(add(b=7,a=3))

# #입력값이 몇개가 될지 모르는 함수
# def add_many(*args):
#     result = 0
#     for i in args:
#         result = i+result
#     return result
# print(add_many(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))

#함수의 결과값
# def add_more_add (a,b):
#     return a+b , a*b
# print(add_more_add(3,4))
# def add_more_add1 (a,b):
#     return a+b
#     return a*b
# print(add_more_add1(3,4))

# #매개변수의 초기값 (초기화 할 거는 항상 뒤쪽에 놔야함)
# def say_myself(name,old,man=True):
#     print (f"나의 이름은 {name}입니다")
#     print (f"나이는 {old}살입니다")
#     if man:
#         print("남자입니다")
#     else :
#         print("여자입니다")
# say_myself("박현빈",19)

#함수안에서 선언한 변수의 효력 범위
# a=13
# def inadd (a):
#     a=a+1
# inadd(a)
# print(a) #그런거 없다

#함수안에서 함수 밖의 변수를 변경하는 방법
#1. return 사용 
# a=1
# def poop (a):
#     a=a+1
#     return a
# a = poop(a)
# print(a)

#2. global 명령 사용
# a=1
# def ddd():
#     global a
#     a = a + 1
# ddd()
# print(a)

# #lambda 함수
# gg = lambda a,b:a+b
# f = gg(3,4)
# print(f)


