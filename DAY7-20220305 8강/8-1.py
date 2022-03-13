# 8-1 표준 입출력


print("Python", "Java", sep=", ", end="ㅋㅋ") # sep는 단어 사이 값, end는 마지막 마무리 추가
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout) # 표준 출력으로 처리
print("Python", "Java", file=sys.stderr) # 표준 에러로 처리 => 나중에 확인해서 수정하도록 설정

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(6), str(score).rjust(4), sep = ":")

# 은행 대기 순번표
# 001, 002, 003 ...
for num in range(1, 21):
    print("대기번호 :" + str(num).zfill(3)) # 3의 공간 중 남는 공간은 0으로 채움

# 표준 입력
answer = input("아무 값이나 입력하세요: ")
print(" 입력하신 값은 " + answer + "입니다.") # str 처리 안해도 숫자가 입력됨.
print(type(answer)) # 사용자 입력 형태로 저장을 하면 항상 "문자열" 형태로 저장



