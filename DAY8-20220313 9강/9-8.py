# 9-8 pass

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed


# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 아무것도 안하고 일단 넘어간다는 뜻(완성된 것 처럼 보여짐)

# 서플라이 디폿: 건물, 1개 건물 = 8 인구 수 추가
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


# 게임 알림
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()


#pass를 쓰면 적어야 할 것을 안적어도 에러가 안뜸. -> 근데 왜 씀??

