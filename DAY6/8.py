# 8-2 

# print("{0: >+10,}".format(500000))

# print("{0:.2f}".format(5/3))


# 8-3 파일입출력

# score_file = open("score.txt", "w", encoding="utf8") # w = 덮어쓰기
# print("수학: 0", file=score_file)
# print("영어: 50", file=score_file)
# score_file.close()

# 파일 내용 추가하기
# score_file = open("score.txt", "a", encoding="utf8") # append(a) = 확장용도
# score_file.write("과학 : 80") # .write로 쓸 경우 줄바꿈 x
# score_file.write("\n코딩 : 100") # \n을 통해 줄바꿈해줌
# score_file.close()


# 파일 내용 한번에 읽어오기
# score_file = open("score.txt", "r", encoding="utf8") # r = 파일을 읽어오는 용도로 오픈
# print(score_file.read()) # 파일의 모든 내용을 읽어옴
# score_file.close()

# 파일 내용 한줄씩 읽어오기
# score_file = open("score.txt", "r", encoding="utf8") # r = 파일을 읽어오는 용도로 오픈
# print(score_file.readline()) # 줄별로 이동, 한 줄 읽고 커서는 다음줄로 이동
# print(score_file.readline()) # print에서 알아서 줄바꿈을 한번 더 해줌
# print(score_file.readline()) # 줄바꾸기 싫으면 마지막에 end=""입력
# print(score_file.readline()) 
# score_file.close()

# 파일 내용이 몇 줄인지 모를때 한 줄씩 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line: # 줄이 없는 경우
#         break # while 문 탈출
#     print(line, end="")
# score_file.close()

# 모든 라인을 리스트화 시켜서 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # 모든 줄을 리스트로 만듦
# for line in lines: # 모든 리스트를 순서대로 반복
#     print(line, end="")

# score_file.close()


# 8-4 pickle

# 프로그램 상에서 사용하는 데이터를 파일 형태로 저장해놓은 것
# 가지고 있는 정보를 dump로 저장하고, load를 통해 계속해서 사용하는 라이브러리

# import pickle
# profile_file = open("profile.pickle", "wb") # pickle은 인코딩 x, wb입력
# profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 저장
# profile_file.close()

# pickle 파일에서 데이터 가져오기
# import pickle
# profile_file = open("profile.pickle", "rb") # b = binary
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()


# 8-5 with(파일 작성, 불러오기 간편하게 가능) close 필요 x

# pickle을 사용해 파일 불러오기
# import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file)) # 파일 자동 종료

# pickle을 쓰지 않고 파일 쓰기
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.") # 파일 자동 종료

# pickle을 쓰지 않고 파일 불러오기
# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read()) # 파일 자동 종료


# 8-6 퀴즈 

# 당신의 회사에서 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 - 
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건: 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.

# while문 사용
# i = 1
# week = 1
# while i <= 50:
#     with open("{}주차.txt".format(week), "w", encoding="utf8") as report:
#         report.write("- {} 주차 주간보고 -".format(week))
#         report.write("\n부서 : ")
#         report.write("\n이름 : ")
#         report.write("\n업무 요약 : ")
#         week += 1
#     i += 1

# for문 사용
# for week in range(1, 51):
#     with open("{0}주차.txt".format(week), "w", encoding="utf8") as report:
#         report.write("- {0} 주차 주간보고 -".format(week))
#         report.write("\n부서 : ")
#         report.write("\n이름 : ")
#         report.write("\n업무 요약 : ")






