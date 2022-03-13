# 9-1 클래스
# 스타크래프트로 클래스 설명

# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
name = "마린" # 유닛의 이름
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력은 {0}, 공격력은 {1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반 모드 / 시즈 모드 존재
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력은 {0}, 공격력은 {1}\n".format(tank_hp, tank_damage))

# 탱크 2 생성
tank_name2 = "탱크"
tank_hp2 = 150
tank_damage2 = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name2))
print("체력은 {0}, 공격력은 {1}\n".format(tank_hp2, tank_damage2))


def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [ 공격력 : {2}]".format(\
        name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank_name2, "1시", tank_damage2)

# 이런 식으로 만들 수는 있지만, 유닛이 매우 많기 때문에 만들기 힘듦 => 클래스로 해결 가능
# 붕어빵 틀: 클래스(변수와 함수의 집합)


# 클래스로 해결하기

class Unit: 
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp, self.damage))

marine1= Unit("마린", 40, 5)
marine2= Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

