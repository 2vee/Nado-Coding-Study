# 8-3 파일 입출력

# 쓰기
score_file = open("score.txt", "w", encoding='"utf8') # utf8을 적어야 한글이 잘 인식됨, w는 쓰기용도(덮어쓰기)
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

# 추가하기
score_file = open("score.txt", "a", encoding="utf8") # a:append(추가)
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

# 읽기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read()) # 텍스트 불러오기
score_file.close()

# 한줄씩 읽기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 한줄만 읽고 커서를 다음 줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

# 몇줄인지 모를때 한줄씩 읽기
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

# 리스트에 넣어서 처리하기
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 리스트 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()