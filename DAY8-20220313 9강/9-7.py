# 9-7 메소드 오버라이딩
# 자식 클래서에서 정의한 메소드를 쓰고 싶을 때 메소드를 새롭게 정의하는 것

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit): # ()안에 상속받을 클래스 입력
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed) # 상속받은 클래스 입력
        self.damage = damage # 데미지만 추가

# 날 수 있는 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

dropship = Flyable(10)
dropship.fly("드랍쉽", "3시")

# 공중 공격 유닛 
class Fly_attack(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0) # 공중 유닛의 지상 스피드는 0
        Flyable.__init__(self, flying_speed)
    
    def attack(self, location):
        print("{0} : {1} 방향으로 공격했습니다. [공격력 {2}]".format(self.name, location, self.damage))

    def move(self, location): # 메소드 오버라이딩 한 위치
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 벌쳐 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 20, 10 )

# 배틀크루져 : 공중 유닛, 체력 좋음, 공격력 좋음
battlecruiser = Fly_attack("배틀크루저", 500, 25, 3)

# 이 경우 유닛이 지상 유닛인지, 공중 유닛인지를 확인하고 메소드를 적용해야 한다는 단점이 있음
vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시")

# 메소드 오버라이딩을 통해 똑같이 move함수로 지상은 이동, 공중은 날아가도록 처리
vulture.move("11시")
battlecruiser.move("9시") # Fly_attack 클래스에 move를 정의해주고, self.fly를 통해 fly함수를 이용



# 기본적으로 Unit에 move 메소드를 통해 지상유닛이 이동하는 메소드를 정의
# 공중 유닛의 경우 fly라는 메소드가 있지만, 둘을 구분해야 하는 번거로움이 있으므로 fly_attack 클래스에 새로 정의된 move 메소드를 적용
# move 메소드에 self.fly를 사용해 move메소드를 사용하면 자동으로 fly 메소드를 사용하로독 적용 
# 둘 다 move 메소드이지만, 적용되는 클래스에 따라 다르게 출력되는 것