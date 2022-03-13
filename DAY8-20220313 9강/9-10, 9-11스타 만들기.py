# 9-10 스타크래프트 프로젝트 전반전
# 텍스트로 게임하는 것처럼 만들어 보기

from random import * # 난수 생성 함수

# 일반 유닛
from ssl import ALERT_DESCRIPTION_CERTIFICATE_UNKNOWN


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
    
    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0}: {1}의 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage 
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("사망했습니다.")

# 공격 유닛
class AttackUnit(Unit): # ()안에 상속받을 클래스 입력
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed) # 상속받은 클래스 입력
        self.damage = damage # 데미지만 추가

    def attack(self, location):
        print("{0} : {1} 방향으로 공격했습니다. [공격력 : {2}]".format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0}: {1}의 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage 
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("사망했습니다.")    

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 5, 1)

    # 스팀팩 : 일정 시간동안 이동 및 공격 속도 증가, 자기 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용할 수 없습니다.".format(self.name))

# 탱크
class Tank(AttackUnit):
    # 시즈 모드: 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동 불가
    seize_developed = False # 시즈모드 개발 여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 35, 1)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        # 현재 시즈모드가 아닐 때
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True

        # 현재 시즈모드가 일 때
        else:
            print("{0} : 시즈모드가 해제됩니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

# 날 수 있는 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 
class Fly_attack(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0) # 공중 유닛의 지상 스피드는 0
        Flyable.__init__(self, flying_speed)
    
    def attack(self, location):
        print("{0} : {1} 방향으로 공격했습니다. [공격력 {2}]".format(self.name, location, self.damage))

    def move(self, location): # 메소드 오버라이딩 한 위치
        self.fly(self.name, location)

# 레이스
class Wraith(Fly_attack):
    clocking_developed = False
    def __init__(self):
        Fly_attack.__init__(self, "레이스", 80, 20, 5)
        self.clocking = False

    def set_clocking(self):
        if Wraith.clocking_developed == False:
            return
        
        if self.set_clocking == True:
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name)) # 클로킹 모드 ON -> OFF
            self.set_clocking = False
        else: 
            print("{0} : 클로킹 ON".format(self.name)) # 클로킹 모드 OFF-> ON
            self.set_clocking = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")



# 게임 시작
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")
    
# 탱크 시즈모드 개방
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 레이스 클로킹 개발
Wraith.clocking_developed = True
print("[알림] 레이스 클로킹 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine): # "isinstance" : 지금 만들어진 객체가 어떤 클래스인지 확인
        unit.stimpack()           # 유닛이 마린이라면 스팀팩 
    if isinstance(unit, Tank):
        unit.set_seize_mode()
    if isinstance(unit, Wraith):
        unit.set_clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21)) # 공격은 5~20 사이의 데미지 받음

# 게임 종료
game_over()