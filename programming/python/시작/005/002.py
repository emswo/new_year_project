# 모듈 불러오기
import m1
print(m1.add(3,4))
print(m1.sub(4,3))
#모듈 이름 없이 함수만 불러오기
from m1 import add
print(add(8,9))
#모듈 이름 없이 함수만 불러오기 (전부)
from m1 import *
print(sub(4,2))

import m2
k = m2.math()
print(k.solv(3))
