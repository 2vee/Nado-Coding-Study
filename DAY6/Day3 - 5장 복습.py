# print(abs(-5)) # 절대값
# print(pow(4, 2)) # 4의 2승
# print(max(2, 10)) # 최대값
# print(min(2, 10)) # 최소값
# print(round(3.14)) # 반올림
# print(round(3.14, 1)) # 소수점 2의 자리에서 반올림 

# from math import * # math 라이브러리 활용
# print(floor(3.14))
# print(ceil(3.45))
# print(sqrt(4))

# from random import *
# print(randint(4, 16))
# print(random())

# 잘못함 (3장임)



# 5장 복습
# subway = [1, 2, 3]
# print(subway.index(2))
# subway.append(10) # 리스트 마지막에 10 추가
# print(subway)
# subway.insert(2, 5) # 인덱스 2의 자리에 5 추가
# print(subway)
# subway.pop() # 뒤에 하나 제거
# print(subway)
# print(subway.count(5)) # 5가 몇개 있는지 계산

# 리스트 복습
# list = [5, 2, 3, 1, 5]
# list.sort() # 크기가 작은 순으로 정렬
# print(list)
# list.reverse() # 크기가 큰 순으로 정렬
# print(list)
# list.clear() # 리스트 전부 제거
# print(list)
# s_list = ["김동헌", 10]
# list.extend(s_list) # 리스트에 리스트를 추가
# print(list)

# 사전 복습
# dic = {"김동헌": 25, "김시형": 23}

# print(dic["김동헌"])
# print(dic.get("김동헌")) 
# 두개 차이점: get을 사용 -> 없을 경우 None 출력 BUT get사용x -> 에러 출력
# print(dic.get("김동", "없습니다.")) # None 대신 다른 말도 출력 가능

# print("김동헌" in dic) # 딕셔너리에 키인 "김동헌"이 있는지 확인

# del(dic["김동헌"]) # 김동헌 키 삭제
# print(dic)

# print(dic.keys()) # 키만 출력
# print(dic.values()) # 값만 출력
# print(dic.items()) # 키와 값 모두 출력

# dic.clear() # 모두 삭제
# print(dic) 

# 튜플 복습 - 추가 변경 불가능 BUT 속도가 리스트보다 빠름

# 세트 복습 - 중복 안됨, 순서 없음
# set = {1, 2, 3, 4, 4}
# print(set) # 중복이 안되므로 4가 하나만 출력
# set.add(5)
# print(set)
# set.remove(5)
# print(set)



# 5-6 퀴즈 복습
# 파이썬 코딩 대회
# 1명 치킨, 3명 커피쿠폰

# 조건1 : 댓글은 20명 작성, 아이디는 1~20
# 조건2 : 무작위 추첨, 중복 불가
# 조건3 : random 모듈 shuffle과 sample 활용

# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# from random import *
# event = range(1, 21) # 타입이 range이기 때문에 list 함수를 사용할 수 없음
# event = list(event) # 리스트로 변경해줌
# # print(event)
# shuffle(event)
# sel = sample(event, 4)
# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {}".format(sel[0]))
# print("커피 당첨자 : {}".format(sel[1:]))
# print("-- 축하합니다 --")
