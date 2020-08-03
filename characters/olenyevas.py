from character import Character, Damage, Buff
from util import roll,log, LowerBoundedInteger
from dataclasses import dataclass


@dataclass
class Olenyevas(Character):
    name: str = "阿琳姐妹"
    attack: LowerBoundedInteger = LowerBoundedInteger(18)
    defence: LowerBoundedInteger = LowerBoundedInteger(10)
    speed: int = 10
    is_multiple: bool = True
    extra_attack_turn: int = 0

    use_extra_attack: bool = False

    class 超级头槌(Buff):
        name = "超级头槌"
        def on_turn_start(self):
            self.target.use_extra_attack = True
            self.lasting -= 1

        def on_turn_end(self):
            if self.lasting == 0:
                self.target.use_extra_attack = False
                log(f"【{self.target.name}】的【{self.name}】消失了")

    九十六度生命之水used: bool = False

    def 九十六度生命之水(self):
        skill_name = "九十六度生命之水"
        if not self.九十六度生命之水used:
            self.九十六度生命之水used = True
            self.log_skill(skill_name)
            self.health = 20
            log(f"【{self.name}】的当前生命值为 {self.health}")
            self.status.append(self.超级头槌(self))

    def 变成星星吧(self):
        skill_name = "变成星星吧"
        self.log_skill(skill_name)
        if roll(50):
            damageBase = LowerBoundedInteger(233)
        else:
            damageBase = LowerBoundedInteger(50)
        damage = Damage(self.get_damage_value(damageBase), False, True)
        self.cause_damage(damage)

    def extra_attack_available(self, turn):
        return self.skills_enabled and self.use_extra_attack

    def extra_attack(self):
        self.变成星星吧()

    def is_dead(self):
        if self.skills_enabled:
            if not self.九十六度生命之水used:
                if Character.is_dead(self):
                    self.九十六度生命之水()
                return False
        return Character.is_dead(self)
