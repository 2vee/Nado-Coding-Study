# 9-5 상속
# 일반 유닛에 있는 name, hp를 공격 유닛에서 사용할 수 있도록 "상속"하는 것 

# 일반 유닛 (메딕처럼 공격력이 없는 유닛)
class Unit: 
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit): # ()안에 상속받을 클래스 입력
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 상속받은 클래스 입력
        self.damage = damage # 데미지만 추가
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp, self.damage))

zerg = AttackUnit("저글링", 10, 5)



# 9-6 다중 상속
# 부모가 둘 이상; 여러 곳에서 상속을 받는 것

# 드랍쉽 : 공중 유닛, 수송기(공격 기능x) 마린, 파이어뱃, 탱크 등 수송 
# 날 수 있는 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

dropship = Flyable(10)
dropship.fly("드랍쉽", "3시")

# 공중 공격 유닛 클래스
class Fly_attack(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)
    
    def attack(self, location):
        print("{0} : {1} 방향으로 공격했습니다. [공격력 {2}]".format(self.name, location, self.damage))

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
varkyrie = Fly_attack("발키리", 200, 6, 5)
varkyrie.fly(varkyrie.name, "3시")
varkyrie.attack("5시")