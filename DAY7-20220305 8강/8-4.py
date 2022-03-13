# 8-4 pickle
# 프로그램에서 사용하는 데이터를 파일로 저장 -> 다른 사람이 pickle을 사용해 데이터 가져와 사용 가능


import pickle 
profile_file = open("profile.pickle", "wb") # b는 바이너리. pickle은 인코딩 설정 필요x
profile = {"이름": "박명수", "나이": 30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 파일에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile) # 파일에 있는 데이터를 변수에 저장해 
profile_file.close()
