# 9-12 퀴즈
# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# (출력 예제)
# 총 3대의 매물이 잇습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스템 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    def show_detail(self):
        print
        print("매물 정보 : {0} {1} {2} {3} {4} 입니다.".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

class Gangnam(House):
    def __init__(self):
        House.__init__(self, "강남", "아파트", "매매", "10억", "2010년")

class Mapo(House):
    def __init__(self):
        House.__init__(self, "마포", "오피스텔", "전세", "5억", "2007년")

class Songpa(House):
    def __init__(self):
        House.__init__(self, "송파", "빌라", "월세", "500/50", "2000년")

house = []
house.append(Songpa())
house.append(Gangnam())
house.append(Mapo())

print("총 {0}대의 매물이 있습니다.".format(len(house)))
for houses in house:
    houses.show_detail()



# 답
# [코드]
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    def show_detail(self):
        print("매물 정보 : {0} {1} {2} {3} {4} 입니다.".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

house = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")
house.append(house1)
house.append(house2)
house.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(house)))
for houses in house:
    houses.show_detail()