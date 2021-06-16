list1= [1,2,3,4]
list2= ["HTK",45,"l","po",958]
list3= [1,2,[3,4,[5,6]]]
print(list1[3])
print(list2[3-4]) #-1값임
#다중 리스트
print(list3[2][2][0])
print(list3[2][2])
#리스트의 슬라이싱
print(list1[2:3])
#리스트 연산
print(list1+list3)
print(str(list1)+"hi")
print(list1*3)
list4= [1,2,3,4,5,6,7,8,9]
list4[3]=7
print(list4)
del list4[3:5]
print(list4)
#리스트 관련 함수
#리스트 추가
list4.append(4)
print(list4)
#리스트 정렬
list4.sort()
print(list4)
#리스트 뒤집기
list4.reverse()
print(list4)
#위치반환
print(list4.index(3))
#리스트 요소 삽입
list4.insert(3,180)
print(list4)
#리스트 요소 제거
list4.remove(9)
print(list4)
#리스트 요소 끄집어내기
print(list4.pop())
print(list4)
#리스트에 포함된 요소 x의 개수 세기
print(list4.count(4))
#리스트 확장
list4.extend([56,48])
print(list4)
#튜플 자료형
t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a','b',("ab","cd"))
#튜플 자료형은 변경 불가
#오류
#del t3[0] #(오류)
#t3[0]='f' #오류

#튜플 다루기
#인덱싱
tu=1,2,3,4,5,6,7,8,9
print(tu[3])
#슬라이싱
print(tu[3:5])
#튜플 더하기
print(tu+t3)
#튜플 곱하기
print(tu*5)
#튜플 길이 구하기
print(len(tu))

#딕셔너리 자료형
dic = {'name':'박현빈','school':'금오공업고등학교','phone number':[123,4567,8910]}
dic2= {'p24':'2'}
dic2['ko']='d'
dic2[2]=[1,2,3]
dic2[3]=90
print(dic2)
#딕셔너리 키 사용해서 값얻기
print(dic2['ko']) #없으면 에러
#딕셔너리 주의사항
# a = {1:'a',1:'b'} #1:'a'가 무시됨
# a = {[1,2]:3} # 형 에러

#딕셔너리 관련 함수
#키만 얻기
print(dic.keys())
#값만 얻기
print(dic.values())
#키 값 쌍으로 얻기
print(dic.items())
#키로 값얻기2
print(dic.get('n1ame')) #없으면 None
print(dic.get('n1ame','돼지')) #없으면 디폴트값
#해당 키가 딕셔너리 안에 있는지 조사
print('name' in dic)
print('1name' in dic)
