from math import *
print(ceil(4.99))
print(floor(4.99))
print(sqrt(16))

from random import *
print(random()) # 0.0 이상 1.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0.0 이상 10.0 미만의 정수 값 생성

print(randint(1, 45)) # 1 이상 45이하의 정수 값 생성
print(randrange(1, 46)) # 1 이상 46 미만의 정수 값 생성

# 복습 퀴즈
# 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하십시오.

# 조건1: 랜덤으로 날짜를 뽑아야 함
# 조건2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3: 매월 1~3일은 스터디 준비를 해야 하므로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
from random import *
offline_meeting = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 {} 일로 선정되었습니다.".format(offline_meeting))