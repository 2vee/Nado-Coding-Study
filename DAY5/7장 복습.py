# 함수는 박스

# 계좌 개설
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()

# # 입금 시 
# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
#     return balance + money # 반환하지 않으면 balance에 값이 저장되지 않음
#     # 즉, 반환 값이 없으면 실행은 되지만 deposit 함수에 값이 반환되지 않고 None으로 반환되어 balance 값이 저장이 안되므로 다음 함수에 적용이 되지 않음
# # deposit(500, 1000)

# # 출금 시 
# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("잔액이 부족합니다. 잔액은 {0}원 입니다.".format(balance))
#         return balance
# # withdraw(1500, 1000)

# # 야간 출금 시
# def withdraw_night(balance, money):
#     commission = 100
#     if balance >= money + commission:
#         print("수수료는 {0}원 입니다. 잔액은 {1}입니다.".format(commission, balance - money - commission))
#         return commission, balance - money - commission
#     else:
#         print("수수료는 {0}원 입니다. 잔액이 부족합니다. 잔액은 {1}입니다.".format(commission, balance))
#         return commission, balance

# balance = 0
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 400) # 반환 값을 balance에 저장해 줌으로써 다음 잔액에 반영이 됨.
# print(commission, balance)


# 가변인자 복습
# 가변인자 적용 x
# def profile(name, age, lang1, lang2, lang3, lang4):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4)

# # profile("유재석", 20, "java", "Python", "d", "4") # 하나씩 다 적어줘야함 
# # 다른 사람이 언어가 3개일 경우 따로 ""를 입력해야 함.

# # 가변인자 적용 o
# def profile(name, age, *language): # *를 활용해 가변인자 사용
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end = " ")
#     print()
# profile("유재석", 30, "파이썬")
# profile("유재석", 30, "공부", "ㅇ")


# 지역변수와 전역변수 복습
# gun = 10
# def checkpoint(gun, soldiers):
#     gun = gun - soldiers
#     return gun

# print("전체 총: {0}".format(gun))
# gun = checkpoint(gun, 2)
# print("남은 총 : {0}".format(gun))



# 퀴즈 복습
# 표준 체중을 구하는 프로그램을 작성하시오.

# 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자: 키(m) x 키(m) x 22
# 여자: 키(m) x 키(m) x 21

# 조건 1: 표준 체중은 별도의 함수 내에서 계산
#             * 함수명: std_weight
#             * 전달값: 키(height), 성별(gender)
# 조건 2: 표준 체중은 소수점 둘째자리까지 표시

# (출력예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if gender == "남자":
        std_weight = height/100 * height/100 * 22
        print("키 {0}cm {1}의 표준 체중은 {2:.2f}kg 입니다.".format(height, gender, std_weight))
        # return height * height * 22
    if gender == "여자":
        std_weight = height/100 * height/100 * 22
        print("키 {0}cm {1}의 표준 체중은 {2:.2f}kg 입니다.".format(height, gender, std_weight))
        # return height * height * 21
std_weight(175, "남자")

# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     if gender == "여자":
#         return height * height * 21

# height = 175
# gender = "남자"
# weight = std_weight(height / 100, gender)
# print("키 {0}cm {1}의 표준 체중은 {2:.2f}kg 입니다.".format(height, gender, weight))
