# 8-5 with
# with를 사용하면 파일을 열고 사용하고 닫는 것을 더 편리하게 사용 가능

import pickle 

with open("profile.pickle", "rb") as profile_file: # with문을 사용하면 close를 사용하지 않고 자동으로 닫힘.
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file: # 두줄로 텍스트를 만들고 쓸 수 있음
    study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file: # 두줄로 텍스트를 불러올 수 있음
    print(study_file.read())