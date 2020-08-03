from dataclasses import dataclass
from util import log, LowerBoundedInteger, roll
from character import Character, Damage, Buff


@dataclass
class Kiana(Character):
    name: str = "琪亚娜"
    attack: LowerBoundedInteger = LowerBoundedInteger(24)
    defence: LowerBoundedInteger = LowerBoundedInteger(11)
    speed: int = 23
    extra_attack_turn: int = 2

    class 眩晕(Buff):
        name = "眩晕"

        def on_add(self):
            super().on_add()

        def on_turn_start(self):
            self.target.movable = False
            self.lasting -= 1

        def on_turn_end(self):
            if self.lasting == 0:
                self.target.movable = True
                log(f"【{self.target.name}】的【{self.name}】消失了")

    def 吃我一矛(self):
        skill_name = "吃我一矛"
        self.log_skill(skill_name)
        damageBase = LowerBoundedInteger(self.attack + 2 * self.enemy.defence)
        damage = Damage(self.get_damage_value(damageBase), False, True)
        self.cause_damage(damage)
        self.音量太强()

    def 音量太强(self):
        skill_name = "音量太强"
        if roll(35):
            self.log_skill(skill_name)
            log(f"【{self.name}】眩晕了！！！")
            self.status.append(self.眩晕(self))

    def extra_attack(self):
        self.吃我一矛()
