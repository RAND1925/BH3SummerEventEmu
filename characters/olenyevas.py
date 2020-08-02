from character import Character, Damage
from util import roll,log
from dataclasses import dataclass


@dataclass
class Olenyevas(Character):
    name: str = "阿琳姐妹"
    attack: int = 18
    defence: int = 10
    speed: int = 10
    is_multiple: bool = True
    extra_attack_turn: int = 0

    九十六度生命之水used: bool = False
    变成星星吧used: bool = False

    def 九十六度生命之水(self):
        skill_name = "九十六度生命之水"
        if not self.九十六度生命之水used:
            self.九十六度生命之水used = True
            self.log_skill(skill_name)
            self.health = 20
            log(f"【{self.name}】的当前生命值为 {self.health}")

    def 变成星星吧(self):
        skill_name = "变成星星吧"
        if self.九十六度生命之水used:
            if not self.变成星星吧used:
                self.变成星星吧used = True
                self.log_skill(skill_name)
                if roll(50):
                    damageBase = 233
                else:
                    damageBase = 50
                damage = Damage(damageBase - self.enemy.defence, False, True)
                self.cause_damage(damage)
                return True

        return False

    def turn(self, turn):
        if self.九十六度生命之水used and not self.变成星星吧used:
            self.变成星星吧()
        else:
            Character.turn(self, turn)

    def is_dead(self):
        if not self.九十六度生命之水used:
            if Character.is_dead(self):
                self.九十六度生命之水()
            return False
        else:
            return Character.is_dead(self)
