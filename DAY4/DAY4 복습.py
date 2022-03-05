# 4-2 슬라이싱: 필요 정보만 짤라서 가져오는 것

# jumin = "980316-1111111"
# print(jumin[0:3])
# print(jumin[-7:]) # 뒤에서 7번째부터 끝까지 슬라이싱



# 4-3 문자열 처리 함수

# John = "John is very strong"
# print(John.upper()) # 대문자로 변경
# print(John.lower()) # 소문자로 변경
# print(John[0].isupper())  # 슬라이싱 한 문자가 대문자인지 확인해줌
# print(len(John)) # Jonn 문자열의 길이 알려줌
# print(John.replace("strong", "aaaaaaaaaar")) # 다른 단어로 교체

# index = John.index("s") # s가 몇번째에 있는지 찾아줌 => 
# print(index)
# # 위의 replace 함수에도 변하지 않은 이유는 John함수에 넣은 것이 아닌 그저 
# # 프린트만 했기 때문
# index = John.index("s", index + 1)
# print(index) # 첫번째 s 다음번의 s의 위치를 찾아줌 -> 못찾으면 에러
# print(John.find("e")) # e 위치 찾아줌 -> 못찾으면 -1 출력
# print(John.count("e")) # e의 개수 출력

# 4-4 문자열 포맷

# print("나는 {}살 입니다.".format(20))

# age = 20
# print(f"나는 {age}살 입니다.")


# 4-5 탈출문자

# print("나는\n김동헌\n입니다.") # 줄바꿈

# print("나는 \"김동헌\" 입니다.")

# print("red apple\rpine") # 앞의 4칸을 pine으로 대체

# print("Redd\bapple") # \b앞의 한칸 지움

# print("I am \t apple") # \t = tab

# 4-6 퀴즈 사이트별로 비밀번호를 만들어 주는 프로그램 작성하기

#예) http://naver.com
#규칙1: http:// 부분 제외 -> naver.com
#규칙2: 처음만나는 점 이후 부분은 제외 => naver
#규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#예) 생성된 비밀번호: nav51!

site = "http://daum.net"
my_site = site[7:]
my_site = my_site[:my_site.index(".")] # 처음부터 .까지 인덱싱해서 자르기
# print(site)
password = "{0}{1}{2}!".format(my_site[0:3], len(my_site), my_site.count("e"))
print("{}에서 생성된 비밀번호 : {}".format(site, password))
