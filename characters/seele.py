from dataclasses import dataclass
from util import log, LowerBoundedInteger
from character import Character, Damage
from random import randint

@dataclass
class Seele(Character):
    name: str = "希儿"
    attack: LowerBoundedInteger = LowerBoundedInteger(23)
    defence: LowerBoundedInteger = LowerBoundedInteger(13)
    speed: int = 26
    extra_attack_turn: int = 0

    is_white :bool = True
    def 我换我自己(self):
        skill_name = "我换我自己"
        self.log_skill(skill_name)
        self.is_white = not self.is_white
        log(f"【{self.name}】的当前状态为{'纯白' if self.is_white else '漆黑'}")
        if self.skills_enabled:
            self.拜托了另一个我()

    def 拜托了另一个我(self):
        skill_name = "拜托了另一个我"

        self.log_skill(skill_name)
        if self.is_white:
            self.restore_health(randint(1, 15))
            self.attack -= 10
            self.defence += 5
        else:
            self.attack += 10
            self.defence -= 5

    def move(self, turn):
        if self.skills_enabled:
            self.我换我自己()
        Character.move(self, turn)
