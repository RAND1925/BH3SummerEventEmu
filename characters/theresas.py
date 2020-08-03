from character import Character, Damage
from util import roll,log, LowerBoundedInteger
from dataclasses import dataclass


@dataclass
class Theresas(Character):
    name: str = "德丽莎"
    attack: LowerBoundedInteger = LowerBoundedInteger(19)
    defence: LowerBoundedInteger = LowerBoundedInteger(12)
    speed: int = 22
    extra_attack_turn: int = 3

    def 血犹大第一可爱(self):
        skill_name = "血犹大第一可爱"
        if roll(30):
            self.log_skill(skill_name)
            defence_decreased = 5
            log(f"【{self.enemy.name}】的防御力降低 {defence_decreased} 点")
            self.enemy.defence = max(0, self.enemy.defence - defence_decreased)


    def 在线踢人(self):
        skill_name = "在线踢人"
        self.log_skill(skill_name)
        for i in range(5):
            damageBase = LowerBoundedInteger(16)
            damage = Damage(self.get_damage_value(damageBase), False, True)
            self.cause_damage(damage)


    def move(self, turn):
        Character.move(self, turn)
        if self.skills_enabled:
            self.血犹大第一可爱()

    def extra_attack(self):
        self.在线踢人()

