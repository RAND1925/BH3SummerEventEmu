from dataclasses import dataclass
from util import roll,log
from character import Character, Damage


# undone


@dataclass
class Aponia(Character):
    name = "阿波尼亚"
    attack = 21
    defence = 10
    speed = 30
    has_extra_attack = True
    extra_attack_turn = 4


    def 深蓝之槛(self):
        

    def 形之笔墨(self):
        skill_name = "形之笔墨"
        log(f"【{self.name} 】的必杀技【{skill_name}】发动！！！")
        damage = Damage(18, False, True)
        self.cause_damage(damage)


    def set_enemy(self, enemy: Character):
        Character.set_enemy(enemy)


    def extra_attack(self):
        self.形之笔墨()

class 深蓝之槛()