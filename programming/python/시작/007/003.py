import re

p = re.compile('Crow|servo') # Crow 또는 servo
m = p.match('Crowhello')
n = p.match('servohello')
print (m,n)

print(re.search('^life','life id too short')) #각 줄의 처음과 매치
print(re.search('^life','my life'))

print(re.search('short$','life id too short'))

#\A는 문자열의 처음과 매치된다. 이 옵션은 re.MULTILINE을 사용했을때 ^는 각 줄의 첫번째지만 얘는 걍 문자열 첫번째임
#\Z는 문자열의 끝과 매치됨을 의미한다. re.MULTILINE 을 사용했을때 $와는 달리 전체 문자열의 끝과 매치된다
#\b는 단어 구분자이다. 보통 단어는 whitespace에 의해 구분된다.
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
#\B메타 문자는 \b 메타문자와 반대의 경우

#그루핑
p = re.compile('(ABC)+')
print(p.search('ABCABCABC OK?'))

#그루핑된 문자열에 이름 붙이기
p = re.compile(r'(?P<name>\w+)\s+((\d+)[-]\d+)')
m = p.search("park 010-1234-5678")
print(m.group('name'))

#전방탐색
#긍정형 (?=...) ...에 해당하는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않음
#부정형 (?!...) ...에 해당하는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않음

#문자열 바꾸기
p = re.compile('(blue|white|red)')
print(p.sub('colour', 'blue socks and red shoos'))
print(p.sub('colour', 'blue socks and red shoos',count=1))
p = re.compile(r'(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)')
m = p.sub("\g<phone>\g<name>","park 010-1234-5678")
print(m)

p = re.compile(r'(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)')
m = p.sub("\g<2>\g<1>","park 010-1234-5678")
print(m)

#탐욕스러운
#<.*> 을 사용하면 <html><head>...등등 다 들고가서
#<.*?> 로 <html>까지 들고간다