#명령 인수 받기
import sys
print(sys.argv)
#강제로 스크립트 종료하기
while True:
    break
    #sys.exit()

#자신이 만든 모듈 불러와 사용하기
import sys
print(sys.path)

#객체의 형태를 그대로 유지하면서 파일에 저장하고 불러오기
import pickle
t = open("tyt.txt",'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data,t)
t.close()

t = open("tyt.txt",'rb')
data = pickle.load(t)
t.close()
print(data)

#os자원 제어용
#시스템 정보
import os
print(os.environ)

#디렉토리 위치 변경
os.chdir("C:\\Users\\Kenonix\\programming\\python\\005\\game")

#디렉토리 위치 받기
print(os.getcwd())
#시스템 명령어 호출
os.system('dir')

#여러 유용한 관련 함수
# os.mkdir(디렉터리) / 디렉터리 만들기
# os.rmdir(디렉터리) / 디렉터리 지우기(비워져있을때만)
# os.unlink(파일이름) / 파일 지우기
# os.rename(src, dst) / src파일 이름을 dst로 바꿈

#실행한 시스템 명령어의 결과값 돌려받기
lp = os.popen("dir")
print(lp)

#파일 복사
    # import shutil
    # shutil.copy("pp.txt","pk.txt")

    # pass

#특정 디렉토리에 있는 파일이름 모두 찾아서 읽기
import glob
print(glob.glob("C:\\Users\\Kenonix\\programming\\python\\005\\game"))

#파일을 임시로 만들어서 사용
import tempfile
filename = tempfile.mkdtemp()
print(filename)

#시간
import time
print(time.time())

#달력
import calendar
print(calendar.calendar(2015))

#랜덤
import random
print(random.random())

#웹 열기
import webbrowser
webbrowser.open("https://google.com")

