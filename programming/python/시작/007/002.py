import re
#정규 표현식
# 문자클래스 (매치) [a-c] = abc , [0 - 5] 012345
a = ['afg','before','dude']
ao = re.compile('[abc]')
print(ao.sub(' ',a[2]))
# \d 숫자와 매치, [0-9] 와 동일
# \D 숫자가 아닌것과 매치, [^0-9]와 동일
# \s 문자나 공백을 표현하는 문자와 매치 ([' ','\t','\n','\r','\f','\v']), [ \t\n\r\f\v]와 동일한 표현식
# \S 문자나 공백을 표현하는 문자가 아닌것과 매치 ([' ','\t','\n','\r','\f','\v']), [^ \t\n\r\f\v]와 동일한 표현식
# \w 문자+숫자와 매치 [a-zA-Z0-9_]와 동일
# \W 문자+숫자가 아닌것과 매치 [^a-zA-Z0-9_]와 동일

# Dot(.)는 \n 제외한 모든 문자와 매치됨
a = ['aab','a0b','abc']
ao = re.compile('a.b')
print(ao.sub(' ',a[2]))
# a[.]b 는 a.b와 매치되고 a0b와는 매치되지 않는다

# ca*t a가 0번 이상 반복되면 매치
# ct 매치
# cat 매치
# caaaaaaaaaaaaaaaaaaaaaaaaaaaaaaat 매치

# ca+t a가 1번이상 반복되면 매치
# ct 매치되지 않음
# cat 매치
# caaaaaaaaaaaaaaaaaaaaaaaaaaaaaaat 매치

# ({m,n},?)
#1. {m}
# ca{2}t (반드시 a가 2번 반복되어야 매치)
# cat 매치되지않음
# caat 매치

#2. {m,n}
# ca{2,5}t (반드시 a가 2에서 5번 반복되어야 매치)
# cat 매치되지 않음
# caat 매치
# caaaaat 매치

#3. ? 
# ab?c (b는 있어도 되고 없어도 된다)
# ac  매치
# abc 매치

#정규표현식 모듈
import re

#match() 문자열의 처음부터 정규식과 매치되는지 검사
#search() 문자열 전체를 검색하여 정규식과 매치되는지 검사
#findall() 정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다.
#finditer() 정규식과 매치되는 모든 문자열을 반복가능한 객체로 돌려준다

p = re.compile('[a-z]+')
m = p.match("python")
if m:
    print(m)
else:
    print("no match")

m = p.search("3 python") #문자열 전체를 검사하는거기때문에 3과 공백은 매치되지 않는다
if m:
    print(m)
else:
    print("no match")
    
m = p.findall("Life is too short") #단어를 각각 매치해서 리스트로 돌려줌
if m:
    print(m)
else:
    print("no match")
    
m = p.finditer("Life is too short") 
if m:
    for bp in m:
        print(bp)
else:
    print("no match")
    
#match 객체의 메서드
#group() 매치된 문자열 돌려주기
#start() 문자열의 시작위치 반환
#end() 문자열의 끝위치 반환
#span() 매치된 문자열의 (시작,끝에 해당하는 튜플을 돌려줌)

#컴파일 옵션
#DOTALL 약어: S  dot문자(.)가 줄바꿈문자를 포함하여 모든 문자와 매치됨
#IGNORECASE 약어 I  대.소문자에 관계없이 매치
#MULTILINE 약어: M  여러줄과 매치한다
#VERBOSE 약어: X  verbose모드 사용
lp = re.compile('a.b', re.DOTALL)
ma = lp.match('a\nb')
print(ma)

lp = re.compile('[a-z]', re.I)
print(lp.match("python"))
print(lp.match("Python"))
print(lp.match("PYTHON"))

lp = re.compile("^python\s\w+",re.MULTILINE)
data = '''python one
life is too short
python two
you need python
python three'''
print(lp.findall(data))

lp = re.compile("""
                &[#] #나는야 준비된 주석
                (
                    0[0-7]+
                    | [0-9]+
                    | x[0-9a-fA-F]+
                )
                ;
                """.re.VERBOSE)

#lp = re.compile(r'\\section')

