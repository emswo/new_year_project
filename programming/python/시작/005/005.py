#내장 함수들

#절댓값
print(abs(-3))

#반복 가능한 자료형에서 모두 참이면 true 하나라도 거짓이면 false 출력
print(all([11,2,3,4,5]))
print(all([11,0,3,4,5]))

#하나라도 참이면 참 모두 거짓일때만 false를 출력
print(any([0,0,3,0,0]))
print(any([0,0,0,0,0]))

#아스키코드 입력 받아서 문자로 출력한다
print(chr(65))

#객체가 자체적으로 가지고 있는 변수나 함수를 보여준다.
print(dir ([1,2,3]))
print(dir ({'1':'a'}))

#2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플로 돌려줌
print(divmod(7,3)) #2는 몫 1은 나머지

#이 함수는 순서가 있는 자료형을 입력받아 인덱스값을 포함하는 enumerate 객체를 돌려준다
for i , name in enumerate(['body','foo','bar']):
    print(i, name)

#실행 가능한 문자열 (1+2나 'hi'+'a' 같은것) 을 입력으로 받아 문자열을 실행한 결과값을 돌려주는 함수이다
a = eval('1+2')
print(a)    
a = eval("'hi'+'a'")
print(a)
a = eval('divmod(4,3)')
print(a)


#함수에 넣은 반환값이 참인것만 묶어서 돌려줌
def pos(ok):
    result = []
    for i in ok:
        if i > 0:
            result.append(i)
    return result
print(pos([1,-3,2,0,-5,6]))

def pos1(x):
    return x>0
print(list(filter(pos1,[1,-3,2,0,-5,6])))

#정수를 16진수로 반환
print(hex(15))

#객체의 레퍼런스 (고유 주소값)을 반환
b = 3
print(id(b))
print(id(3))
c = b
print(id(c))

#입력
#print(input("나는야 준비된 :"))

#정수 (10진수)
print(int(3.14))

class p : pass
k = p()
print(isinstance(k,p))

#요소의 전체 개수를 돌려줌
print(len("dop is pop"))

#리스트로 변환
print(list((1,2,3)))

#받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 반환
def two(x): return x*2
print(list(map(two,[1,2,3,4])))

#최대치
print(max([1,2,3]))

#최소치
print(min([1,2,3]))

#8진수
print(oct(34))

#파일 입출력
# w 쓰기모드
# r 읽기모드
# a 추가모드
# b 바이너리모드 (rwa와 같이 사용)
lo = open("pp.txt",'bw')
#lo.write(345)
lo.close()

#아스키 코드 반환
print(ord('0'))

#제곱
print(pow(2,4))

#범위값
print(range(5))
print(range(5,10))
print(range(5,10,2))

#반올림
print(round(3.537,2))

#입력값 정렬 후 리스트로 반환
print(sorted([1,6,9,3,5,2,7,8,3,4,0]))

#문자열로 변환 및 출력
print(str(65))

#모든 요소들의 합
print(sum([1,2,3,4,5,6,7,8,9,10]))
print(sum((1,2,3,4,5,6,7,8,9,10)))

#튜플로 변환
print(tuple([1,2,3,4,5,6,7,8,9]))

#자료형 출력
print(type("aa"))
print(type([]))
print(type(open("d",'w')))

#자료형 묶기
print(list(zip([1,2,3],[4,5,6])))
print(list(zip([1,2,3],[4,5,6],[7,8,9])))
print(list(zip("abc","def")))



