money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#조건
a=1
b=2
print(a<b,a>b,a==b,a>=b,a<=b)

#and or not
x=1
y=3
x or y
x and y
not x

#x in s , x not in s
# x in 리스트   x not in 리스트
# x in 튜플   x not in 튜플
# x in 문자열   x not in 문자열

print(1 in [1,2,3])
print(1 not in [1,2,3])

pocket = ['paper','cellphone', 'money']
if 'money' in pocket:
    print("택시 ㄱㄱ")
else :
    print("걸어 가라")

if 'money' in pocket:
    pass
else :
    print("카드를 꺼내라")

pocket = ['paper','cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어 가라")

pocket = ['paper','cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

score = 50
message = "success" if score >= 60 else "failure"
print(message)