# 예외처리

# try:
#     4/0
#     #print(4/0)
# #except 발생오류 :
# #except 발생오류 as 오류 메시지 변수 :
# except ZeroDivisionError as a:
#     print(a)

# #다중 오류
# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except ZeroDivisionError:
#     print("0으로 나눌 수 없음")
# except IndexError:
#     print("인덱싱 할 수 없습니다")

# #오류 회피
# try:
#     f = open("나는야 안준비된 파일.txt",'r')
# except FileNotFoundError:
#     pass

# #오류 일부러 발생시키기
# class bird:
#     def fly(self):
#         raise NotImplementedError

# class Eagle (bird):
#     def fly(self):
#         print("very fast")
# eagle = Eagle()
# eagle.fly()

# #예외 만들기
# class MyError(Exception):
#     def __str__(self):
#         return ("1".join("병신새끼"))
# def say_nick(nick):
#     if nick == '바보':
#         raise MyError()
#     print(nick)

# try:
#     say_nick("천사")
#     say_nick("바보")
# except MyError as k:
#     print(k)
#     print("허용되지 않는 별명입니다")


