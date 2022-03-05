# 7-1 함수
# 함수는 박스라고 생각하면 된다. 

# def open_account(): # 함수 정의하기
#     print("새로운 계좌가 생성되었습니다.") # 호출하기 전까지 실행되지 않음

# open_account() # 출력됨



# 7-2 전환 값과 반환 값

# 은행에서 돈을 입금, 출금, 야간 할증 출금하기

# def deposit(balance, money): # 잔액과 입금 금액
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money # 반환하기

# def withdraw(balance, money):
#     if balance >= money: # 잔액이 출금할 금액보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else: # 잔액이 출금할 금액보다 적으면
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money): # 저녁에 출금
#     commission = 100 # 수수료
#     print("수수료는 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance) )
#     return commission, balance - money - commission # 수수료와 잔액에서 출금금액과 수수료를 뺀 금액을 반환


# balance = 0 # 잔액
# balance = deposit(balance, 1000) # 잔액 0원에서 1000원을 입금하고, balance에 1000원을 반환함
# balance = withdraw(balance, 1000) # 잔액 1000원에서 1000원을 출금하고 balance에 0원을 반환함
# commission, balance = withdraw_night(balance, 500) # 애초에 함수에서 두개의 값을 반환하므로 두 개의 값을 한번에 나타냄



# 7-3 기본값 설정하기

# 기본값 설정 전

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
#         .format(name, age, main_lang)) # 글이 길때 \하고 엔터치면 문장이 이어짐

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업 -> 나이와 언어는 같음

# def profile(name, age=17, main_lang="파이썬"): # 나이와 언어를 기본값으로 설정
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
#         .format(name, age, main_lang))

# profile("유재석") # 나이와 언어가 기본값으로 출력됨
# profile("김태호")



# 7-4 키워드 값을 이용한 함수 호출

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile("유재석", 20, "파이썬") # 키워드 설정 X

# profile(name="유재석", main_lang="파이썬", age=20) 
# profile(main_lang="자바", age=25, name="김태호")
# 키워드 설정 시 순서가 달라도 정의된 함수의 순서대로 입력됨



# 7-5 가변인자를 이용한 함수 호출

# 할 줄 아는 언어가 많은 경우

# 가변인자 적용X -> 언어가 늘어날 때마다 함수 변경 or 언어가 적은 경우 빈칸
# def profile(name, age, lang1, lang2, lang3, lang4):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") 
#     # end를 한칸 띄어서 만들어 놓으면 줄바꿈되지 않고 한 칸 띄고 그대로 진행됨
#     print(lang1 , lang2, lang3, lang4)

# 가변인자 적용시 -> 서로 다른 값을 입력하는 경우 사용
# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") 
#     # end를 한칸 띄어서 만들어 놓으면 줄바꿈되지 않고 한 칸 띄고 그대로 진행됨
#     for lang in language:
#         print(lang, end=" ") # 줄바꿈 하지 않고 언어 입력하기 위해 end사용
#     print() # 다 입력 후 다음 사람을 입력 전 줄바꿈을 위해 print 사용
# profile("유재석", 25, "C+", "C++", "Python")
# profile("김태호", 20, "java")
# 언어가 늘어나거나 줄어들어도 변경할 필요가 없음



# 7-5 지역변수와 전역변수
# 지역변수: 함수 내에서만 사용 가능
# 전역변수: 프로그램 모든 공간에서 사용 가능

# gun = 10

# def checkpoint(soldiers): #경계근무
#     global gun # 전역 공간에 있는 위에 있는 gun이라는 함수를 사용하겠다.
#     gun = gun - soldiers 
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2) # 두명이 경계 근무 나감
# print("남은 총 : {0}".format(gun))

# 일반적으로는 전역 변수를 많이 사용하면 코드 관리가 어려워짐 권장x


# 함수의 파라미터로 계산 + 반환값으로 사용하는 것을 권장
# gun = 10

# def checkpoint(gun, soldiers): # 위와 달리 gun과 soldiers 둘 다 적용
#     gun = gun - soldiers 
#     return gun # 값을 리턴해줌 -> 리턴해줘야 gun 값이 밑에 적용됨
# print("전체 총 : {0}".format(gun)) # 전역변수 gun의 값 10 출력
# gun = checkpoint(gun, 2) # 전역변수의 gun 값을 사용해 계산 후 gun 값을 적용
# print("남은 총 : {0}".format(gun))



# 7-7 퀴즈 
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

# 내가 푼 방법
# def std_weight(height, gender): # 키는 m 단위(실수), 성별은 "남자" or "여자"
#     if gender == "남자":
#         std_weight = height / 100 * height / 100 * 22
#         print("키 {0}cm {1}의 표준 체중은 {2:.2f}kg 입니다.".format(height, gender, std_weight))    
#     elif gender == "여자":
#         std_weight = height / 100 * height / 100 * 21
#         print("키 {0}cm {1}의 표준 체중은 {2:.2f}kg 입니다.".format(height, gender, std_weight))    
#     else: 
#         print("잘못 입력했습니다. 다시 입력해주세요.")

# std_weight(195, "남자")

# 답
# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     if gender == "여자":
#         return height * height * 21

# height = 175
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))    
        

while True:
    value = input("홀수를 입력하면 제곱을 계산해줍니다. [그만하고 싶다면 n을 입력하세요]: ")
    if value == "n":
        break
    number = int(value)
    if number % 2 == 0:
        continue
    print("입력한 값은 ", number,"이고, 제곱은 ",number**2,"입니다.")


