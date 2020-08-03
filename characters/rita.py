from dataclasses import dataclass
from util import log, LowerBoundedInteger,roll
from character import Character, Damage, Buff
from random import randint

@dataclass
class Rita(Character):
    name: str = "丽塔"
    attack: LowerBoundedInteger = LowerBoundedInteger(26)
    defence: LowerBoundedInteger = LowerBoundedInteger(11)
    speed: int = 17
    extra_attack_turn: int = 4

    class 魅惑(Buff):
        name = "魅惑"

        def on_turn_start(self):
            self.target.skills_enabled = False
            self.lasting -= 1

        def on_turn_end(self):
            if self.lasting == 0:
                self.target.skills_enabled = True
                log(f"【{self.target.name}】的【{self.name}】消失了")

    # trick 丽塔的减伤效果是加给自己的
    魅惑成功: bool = False

    def 女仆的温柔清理(self, damage):
        skill_name = "女仆的温柔清理"
        if roll(35):
            self.log_skill(skill_name)
            damage.value -= 3
            self.enemy.attack -= 4


    # 丽塔的技能真难写
    def 完美心意(self):
        skill_name = "完美心意"
        self.log_skill(skill_name)
        self.enemy.restore_health(4)
        self.enemy.status.append(self.魅惑(self.enemy, 2))
        self.魅惑成功 = True


    def normal_attack(self):
        damage = self.get_normal_damage()
        if self.skills_enabled:
            self.女仆的温柔清理(damage)
        return self.cause_damage(damage)

    # trick 丽塔的减伤效果是加给自己的
    def receive_damage(self, damage: Damage):
        value = damage.value
        if self.魅惑成功:
            damage.value = damage.value.add_percent(-60)
        Character.receive_damage(self, damage)

    def extra_attack(self):
        self.完美心意()



