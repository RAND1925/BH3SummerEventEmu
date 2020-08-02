from dataclasses import dataclass
from character import Character, Damage
from util import roll,log

@dataclass
class Mei(Character):
    name: str = "芽衣"
    attack: int = 22
    defence: int = 12
    speed: int = 30
    extra_attack_turn: int = 2

    def 崩坏世界的歌姬(self):
        skill_name = "崩坏世界的歌姬"
        if roll(30):
            self.log_skill(skill_name)
            log(f"【{self.name}】对【{self.enemy.name}】造成【麻痹】")
            self.enemy.status.append("麻痹")

    def 雷电家的龙女仆(self):
        skill_name = "雷电家的龙女仆"
        self.log_skill(skill_name)
        damage = Damage(3, True, True)
        for i in range(5):
            self.cause_damage(damage)

    def normal_attack(self):
        Character.normal_attack(self)
        self.崩坏世界的歌姬()

    def extra_attack(self):
        self.雷电家的龙女仆()

