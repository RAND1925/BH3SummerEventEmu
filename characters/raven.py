from character import Character, Damage
from util import roll,log
from dataclasses import dataclass

@dataclass
class Raven(Character):
    has_extra_attack = True
    extra_attack_turn = 3

    def 不是针对你(self):
        skill_name = "不是针对你"
        log(f"【{self.name}】的技能【{skill_name}】发动！！！")
        if self.enemy.name == "琪亚娜":
            self.attack = int(self.attack * 1.25)
        else:
            if roll(25):
                self.attack = int(self.attack * 1.25)
        log(f"【{self.name}】的攻击力为：{self.attack}")

    def 别墅小岛(self):
        skill_name = "别墅小岛"
        log(f"【{self.name}】的必杀技【{skill_name}】发动！！！")
        for i in range(7):
            damage = Damage(16, False, True)
            self.cause_damage(damage)

    def set_enemy(self, enemy):
        Character.set_enemy(self, enemy)
        self.不是针对你()

    def extra_attack(self):
        self.别墅小岛()

