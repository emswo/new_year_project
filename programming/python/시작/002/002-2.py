#문자열 정리
#문자열 만드는법
#1. 큰따옴표
"현빈 is pig"
#2. 작은따옴표 
'no! 현빈 is godgod'
#3. 큰따옴표 3개 연속
"""현빈이는 매우 짧기에 당신은 파이썬이 필요합니다"""
#4. 작은 따옴표 3개 연속
'''이건 좀 에반데'''

#문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을때
#1. 문자열에 작은 따옴표 포함시키기
pig1 = "hunbin's look like pig"
#2. 문자열에 큰 따옴표 포함시키기
pig2 = 'hunbin look like "pig"'
#3. 백슬래시 사용해서 넣기
pig3 = "hunbin look like \"pig\""

#여러줄인 문자열을 변수에 대입
multiline = """
나는야
준비된
취준생
"""
multiline2 = '''
나는야
준비된
취준생
'''
multiline3 = "나는야\n준비된\n취준생"

#문자열 연산
#문자열의 덧셈
a1 = "현빈 is "
a2 = "pig"
print (a1+a2)
#문자열의 곱
b1 = "pig"
print (b1*2)
#문자열 길이 구하기
c1 = "line is loooong"
print (len(c1))

#문자열의 인덱싱
d1 = "test indexing"
print (d1[12], len(d1))
print (d1[-3], len(d1)) #뒤에서부터 읽음
print (d1[7], len(d1))

#문자열 슬라이싱
print (d1[0:4], len(d1))#에서부터 4밑에까지
print (d1[5:13], len(d1))#5에서부터 13밑에까지
print (d1[4:5], len(d1))
print (d1[4:], len(d1))
print (d1[:], len(d1))
print (d1[:5], len(d1))
print (d1[4:-5], len(d1))
#문장 나누기
pa = "20010331rainy"
date = pa[:8]
water = pa[8:]
print (date, water)

#문장 수정하기
p = "pithon"
#p[1]='y' 오류남
po = p[:1]+'y'+p[2:]
print (po)

#문자열 포메팅
print("i eat %d apples" %3)
print("do %s x" %"it")

op=3
print("op is %d"%op)
print("op is %d and do %s x" %(op,"it"))
print("%-10sq1" %"ss")
print("%10sq2" %"ss")
fox=4.3456789
print("%04.4f"%fox)
print("%0.4f"%fox)
print("%4.4f"%fox)
print("%10.4f"%fox)

print("i eat {0} apples" .format(3))
print("i eat {0} apples" .format("many"))
print("i eat {0} apples" .format(op))

number = 10
day = "three"
print("i ate {0} apples. so i was sick for {1} days.".format(number, day))
print("i ate {number} apples. so i was sick for {day} days.".format(number=7, day=9))

print("[{0:<10}]" .format("hi"))
print("[{0:>10}]" .format("hi"))
print("[{0:^10}]" .format("hi"))

print("[{0:=<10}]" .format("hi"))
print("[{0:=>10}]" .format("hi"))
print("[{0:=^10}]" .format("hi"))
pi=3.14159265358979
print("[{0:0.4f}]" .format(pi))

print("[{{and}}]" .format())

name = "고길동"
age = 1976
print(f"my name is {name} my age is {age}" .format("anything"))

#문자열 관련 함수
#문자개수 세기
apa= "apple"
print(apa.count('p'))
#위치 알려주기1
print(apa.find('p')) #문자열에 없으면 -1을 반환, 처음으로 나온 위치 반환
#위치 알려주기2
print(apa.index('p')) #문자열에 없으면 오류가 발생, 처음으로 나온 위치 반환

#문자열 삽입
print("1".join("시발개같은파이썬존나안하고싶네"))
#소문자 -> 대문자
ako1="hi"
print(ako1.upper())
#대문자 -> 소문자
ako2="HI"
print(ako2.lower())
#왼쪽 공백 지우기
ako3=" Hi "
print(ako3.lstrip())
#오른쪽 공백 지우기
print(ako3.rstrip())
#양쪽 공백 지우기
print(ako3.strip())
#문자열 바꾸기
lagdis= "Life is too short"
print(lagdis.replace("Life","Your lag"))
#문자열 나누기 
print(lagdis.split()) #공백을 기준으로
apl="folfolfol"
print(apl.split("fol")) #문자를 기준으로
print(apl.split("l")) #문자를 기준으로