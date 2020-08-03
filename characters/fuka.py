from dataclasses import dataclass
from util import roll,log
from character import Character, Damage


# undone

class Fuka(Character):
    is_elemented: bool = True


@dataclass
class Mei(Character):
    name = "符华"
    attack = 17
    defence = 15
    speed = 16
    has_extra_attack = True
    extra_attack_turn = 3


    def 凭神化剑(self):
        pass

    def 形之笔墨(self):
        skill_name = "形之笔墨"
        log(f"【{self.name} 】的必杀技【{skill_name}】发动！！！")
        damage = Damage(18, False, True)
        self.cause_damage(damage)


    def set_enemy(self, enemy: Character):
        Character.set_enemy(enemy)


    def extra_attack(self):
        self.形之笔墨()
