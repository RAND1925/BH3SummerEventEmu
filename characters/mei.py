from dataclasses import dataclass
from character import Character, Damage, Buff
from util import roll,log, LowerBoundedInteger

@dataclass
class Mei(Character):
    name: str = "芽衣"
    attack: LowerBoundedInteger = LowerBoundedInteger(22)
    defence: LowerBoundedInteger = LowerBoundedInteger(12)
    speed: int = 30
    extra_attack_turn: int = 2

    class 麻痹(Buff):
        name = "麻痹"

        def on_add(self):
            super().on_add()

        def on_turn_start(self):
            self.target.movable = False
            self.lasting -= 1

        def on_turn_end(self):
            if self.lasting == 0:
                self.target.movable = True
                log(f"【{self.target.name}】的【{self.name}】消失了")

    def 崩坏世界的歌姬(self):
        skill_name = "崩坏世界的歌姬"
        if roll(30):
            self.log_skill(skill_name)
            log(f"【{self.name}】对【{self.enemy.name}】造成【麻痹】")
            self.enemy.status.append(self.麻痹(self.enemy))

    def 雷电家的龙女仆(self):
        skill_name = "雷电家的龙女仆"
        self.log_skill(skill_name)
        damage = Damage(3, True, True)
        for i in range(5):
            self.cause_damage(damage)

    def normal_attack(self):
        Character.normal_attack(self)
        if self.skills_enabled:
            self.崩坏世界的歌姬()

    def extra_attack(self):
        self.雷电家的龙女仆()

