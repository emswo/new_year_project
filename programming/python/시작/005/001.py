#클래스와 객체
#클래스의 예시
# class cookie:
#     pass
# a = cookie()
# b = cookie()

#사칙연산 클래스
# class FourCal:
#     def setdata(self,first,second):
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def mul(self):
#         result = self.first * self.second
#         return result
#     def sub(self):
#         result = self.first - self.second
#         return result
#     def dev(self):
#         result = self.first / self.second
#         return result

# a = FourCal()
# a.setdata(4,2)
# b = FourCal()
# b.setdata(3,7)
# print(a.first,a.second,b.first,b.second,id(a),id(b))
# print(a.add(),b.add())
# print(a.sub(),b.sub())
# print(a.mul(),b.mul())
# print(a.dev(),b.dev())

#생성자
class FourCal:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def dev(self):
        result = self.first / self.second
        return result

a = FourCal(4,2)
#a.setdata(4,2)
b = FourCal(3,7)
#b.setdata(3,7)
print(a.first,a.second,b.first,b.second,id(a),id(b))
print(a.add(),b.add())
print(a.sub(),b.sub())
print(a.mul(),b.mul())
print(a.dev(),b.dev())

#클레스의 상속
class MoreFourCal(FourCal):
    def pow (self):
        result = self.first ** self.second
        return result
c = MoreFourCal(4,2)
print(c.add(),c.sub(),c.mul(),c.dev(),c.pow())

#메서드 오버라이드
class SelfFourCal(FourCal):
    def div (self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
d = SelfFourCal(4,0)
print(d.div())

#클래스 변수
class family:
    lastname = "김"
e = family()
f = family()
print(family.lastname,e.lastname,f.lastname)
class family1:
    lastname = "박"
e = family1()
f = family1()
print(family1.lastname,e.lastname,f.lastname)
print(id(family1.lastname),id(e.lastname),id(f.lastname))