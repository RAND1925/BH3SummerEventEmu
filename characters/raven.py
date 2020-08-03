from character import Character, LowerBoundedInteger, Damage
from util import roll,log
from dataclasses import dataclass
@dataclass
class Raven(Character):
    name: str = "渡鸦"
    attack: LowerBoundedInteger = LowerBoundedInteger(23)
    defence: LowerBoundedInteger = LowerBoundedInteger(14)
    speed: int = 14
    extra_attack_turn: int = 3

    针对你: bool = False

    def 不是针对你(self):
        skill_name = "不是针对你"
        if self.enemy.name == "琪亚娜" or roll(25):
            log(f"【{self.name}】的技能【{skill_name}】发动！！！")
            self.针对你 = True
            log(f"【{self.name}】获得了攻击力上升buff")

    def 别墅小岛(self):
        skill_name = "别墅小岛"
        log(f"【{self.name}】的必杀技【{skill_name}】发动！！！")
        for i in range(7):
            damage_base = LowerBoundedInteger(16)
            damage = Damage(self.get_damage_value(damage_base), False, True)
            self.cause_damage(damage)

    def set_enemy(self, enemy):
        Character.set_enemy(self, enemy)
        self.不是针对你()

    def cause_damage(self, damage: Damage):
        if self.skills_enabled:
            if self.针对你:
                damage.value = damage.value.add_percent(25)
        Character.cause_damage(self, damage)

    def extra_attack(self):
        self.别墅小岛()

