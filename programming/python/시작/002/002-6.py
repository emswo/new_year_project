#집합 자료형
s1 = set([1,2,3])
s2 = set("hello")
print(s1,s2)
#중복을 허용하지 않는다
#순서가 없다

#리스트로 바꾸기
l1= list(s1)
#튜플로 바꾸기
t1= tuple(s2)
print(l1,t1)

#교집합,합집합,차집합 구하기
s1= set([1,2,3,4,5,6])
s2= set([4,5,6,7,8,9])
print(s1 & s2)
print(s1 | s2)
print(s1 - s2)

#값 1개 추가하기
s1.add(12)
print(s1)
s1.update([7,8,9])
print(s1)
s1.remove(12)
print(s1)