##for문

# #전형적인 for문
# test_list = ['one', 'two', 'three']
# for i in test_list:
#     print(i)
# #리스트 마지막까지 반복

#다양한 for문의 사용
# a = [(1,2),(3,4),(5,6)]
# for (fi,la) in a:
#    print(fi+la) 

# marks = [90,25,67,45,80]
# number = 0
# for mark in marks:
#     number = number + 1
#     if mark >= 60:
#         print(f"{number}번 학생은 합격입니다")
#     else:
#         print(f"{number}번 학생은 불합격입니다")

# marks = [90,25,67,45,80]
# number = 0
# for mark in marks:
#     number = number+1
#     if mark < 60: continue
#     print(f"{number}번 학생 축하합니다. 합격입니다")

# a = range(1,10)
# print(a)

# number = 0
# for num in range(1,101):
#     number = num + number
#     print(num)
# print(number)

# for i in range(2,10):
#     for j in range(1,10):
#         print(i*j,end=' ')
#     print(' ')

# a = [1,2,3,4]
# result = [num * 3 for num in a]
# print(result)

# result = [x*y for x in range(2,10)
#           for y in range(1,10)]
# print(result)


