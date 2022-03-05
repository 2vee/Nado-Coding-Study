# 6-1 if문

# 날씨 확인하기

# weather = input("오늘 날씨는 어때요? ") # input은 입력된 문자열에 대해 실행하도록 함.
# if weather == "비" or "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("오늘은 준비물이 필요 없어요")

# 기온 확인하기

# temp = int(input("기온은 어때요? ")) # input은 문자열만 인식하기 때문에 적은 문자열을 숫자로 바꿔주는 int 사용(온도이기 때문)
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요.")
# elif 10 <= temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 < temp <= 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요.")



# 6-2 for문 (반복문)

# 손님 순서대로 부르기

# for waiting_no in range(1, 6): #randrange와 비슷함 range(1,6) = 1, 2, 3, 4, 5
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))



# 6-3 while문 (반복문)

# 손님 5번 호출하고 안오면 폐기하기

# customer = "토르"
# index = 5
# while index >= 1: # 조건을 만족할 때 까지 반복
#     print("{0}, 커피가 준비되었습니다. {1}번 남았습니다.".format(customer, index )) 
#     index -= 1 
#     if index == 0:
#         print("커피는 폐기처분되었습니다. ")


# 손님이 답장할 때 까지 호출

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았습니다.".format(customer, index)) 
#     index += 1
# 무한루프되므로 ctrl + c를 입력하면 강제 종료됨


# 종업원이 이름을 확인하고 확인되면 주고 배달 완료 메세지 생성, 아니면 계속 부름 

# customer = "토르"
# person = "Unknown" # 커피 확인하러 오는 사람

# while person != customer:
#     print("{}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 무엇입니까? ")
# if person == customer:
#     print("커피 배달이 완료되었습니다.")
    


# 6-4 continue 와 break 

# 책을 순서대로 읽도록 해라 (결석 인원 제외, 책을 안가져오면 반복문 종료)

# no_book = [7] # 책을 안 가져옴
# absent = [2, 5] # 결석
# for student in range(1, 11): # 1부터 10까지 출석 번호가 있음
#     if student in absent: # 리스트 안에 absent한 학생이 리스트에 포함되어 있는 경우
#         continue
#     elif student in no_book:
#         print("오늘 수업은 여기까지. {}은 교무실로 따라와.".format(no_book))
#         break
#     print("{}, 책을 읽어봐".format(student))    
# # continue는 밑의 명령문을 모두 무시 -> 다시 반복문 처음으로 돌아감
# # break는 반복문을 아예 종료 



# 6-5 한 줄 for

# 출석번호가 1 2 3 4 앞에 100을 붙이기로 함 -> 101 102 103 104

# students = [1, 2, 3, 4, 5]
# students = [i+100 for i in students] # students 리스트에 100씩 더해라
# print(students)


# 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students] # students에 들어가 있는 i값을 하나씩 조회하며 len로 변환
# print(students)


# 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students] #upper는 대문자로 변환하는 함수
# print(students)



# 6-6 퀴즈
# 택시 기사가 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
# 조건 1: 승객 별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# 출력문 예제
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 45분)
# ...
# [ ] 50번째 손님 (소요시간 : 35분)

# 총 탑승 승객 : 2 분

# 당일 복습
# from random import *
# count = 0
# for customers in range(1, 51):
#     time = randint(5, 50)
#     if 5 <= time <= 15:
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(customers, time))
#         count += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customers, time))
# print("총 탑승 승객 : {0} 분".format(count))



# 내가 푼 방법
# from random import *
# numbers = 0 # 총 탑승 승객 수
# for customers in range(1, 51): # 손님은 50명
#     time = (randint(5, 50)) # 손님의 이동시간은 5~50으로 랜덤
#     if 5 <= time <= 15: # 손님 이동시간이 15분 이하
#         choose = "[O]"
#         numbers += 1 # 손님 이동시간이 15분 이하일 때만 손님 수 추가
#     else:
#         choose = "[ ]"
#     print("{} {}번째 손님 (소요시간 : {}분)".format(choose, customers, time))

# print("총 탑승 승객 : {} 분".format(numbers))
    
# # 답
# from random import *
# numbers = 0 # 총 탑승 승객 수
# for customers in range(1, 51): # 손님은 50명
#     time = (randint(5, 50)) # 손님의 이동시간은 5~50으로 랜덤
#     if 5 <= time <= 15: # 손님 이동시간이 15분 이하
#         print("[O] {}번째 손님 (소요시간 : {}분)".format(customers, time))
#         numbers += 1 # 손님 이동시간이 15분 이하일 때만 손님 수 추가
#     else:
#         print("[ ] {}번째 손님 (소요시간 : {}분)".format(customers, time))
        
# print("총 탑승 승객 : {} 분".format(numbers))


