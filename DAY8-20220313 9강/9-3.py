# 9-3 멤버 변수
# Self.name, Self.hp , ... 클래스 내에서 정의된 변수

class Unit: 
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp, self.damage))

# 레이스: 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit ("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # 클래스 외부에서 멤버 변수를 쓸 수 있음

# 다크 아칸의 마인드 컨트롤: 상대방 유닛을 내 것으로 만듦
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:    # clocking이라는 변수는 외부에서 추가 할당. 외부에서 할당할 때는 지정한 변수에만 적용
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# if wraith1.clocking == True:    # 즉 레이스2에만 적용되고 레이스 1에는 적용 안됨
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith1.name))

