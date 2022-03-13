# 9-9 super

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # 위 문장과 같은 의미. super 뒤에 ()붙혀야 하고, self를 빼야함
        self.location = location

# super 사용시 고려해야 할 점 (다중 상속의 경우 사용하면 안됨)
class Unit1:
    def __init__(self):
        print("Unit1 생성자")

class Flyable1:
    def __init__(self):
        print("Flayble1 생성자")

class FlyableUnit(Unit1, Flyable1):
    def __init__(self):
        super().__init__() # 다중 상속인 경우 super를 사용하면 Unit1, 즉 앞의 생성자만 적용됨
                            # 따라서 다중 상속의 경우 둘 다 개별로 적용해 줘야 함

dropship = FlyableUnit()
