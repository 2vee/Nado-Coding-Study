# 9-4 메소드

# 일반 유닛
class Unit: 
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp, self.damage))

# 공격 유닛 생성
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location): # 공격하는 함수
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]".format(self.name, location, self.damage)) 
        # location은 self가 없으므로 멤버 변수의 값을 사용하지 않고 "입력한 값"을 사용

    def damaged(self, damage): # 공격 받은 함수
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0: 
            print("{0} : 사망했습니다.".format(self.name))


# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)

# 파이어뱃이 5시로 공격
firebat1.attack("5시")

# 파이어뱃이 25의 데미지를 두 번 받음
firebat1.damaged(25)
firebat1.damaged(25)


# 혼자 해보기

# 저글링 : 근접 유닛, 숨기 

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향으로 공격했습니다.".format(self.name, location))
    
    def damaged(self, damage):
        print("{0}: {1}의 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage 
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("사망했습니다.")
    
zerg = Unit("저글링", 10, 5)
zerg.attack("5시")
zerg.damaged(10)

