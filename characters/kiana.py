from character import Character, Kimewaza
from util import roll,log

def 吃我一矛(self: Character):
    damage_value_this_time = self.attack + self.enemy.defence
    log(f"{self.name} 的必杀技吃我一矛发动！！！")
    self.cause_damage(damage_value_this_time, False)
    音量太强(self)


def 音量太强(self: Character):
    if roll(35):
        log(f"{self.name} 眩晕了！！！")
        self.status.append("眩晕")


kiana = Character("琪亚娜", 24, 11, 23)
kiana.kimewaza = Kimewaza("吃我一矛", 2, 吃我一矛)