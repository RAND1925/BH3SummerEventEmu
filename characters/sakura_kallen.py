from character import Character, Damage
from util import roll,log
from dataclasses import dataclass


@dataclass
class SakuraKallen(Character):
    name: str = "樱莲组"
    attack: int = 20
    defence: int = 9
    speed: int = 18
    is_multiple: bool = True
    extra_attack_turn: int = 2

    def 八重樱的饭团(self):
        skill_name = "八重樱的饭团"
        if roll(30):
            self.log_skill(skill_name)
            health_restored = 25
            log(f"【{self.name}】的生命值提高 {min(100 - self.health, health_restored)} 点")
            self.health = min(100, self.health + health_restored)
            log(f"【{self.name}】的当前生命值为 {self.health}")


    def 卡莲的饭团(self):
        skill_name = "卡莲的饭团"
        self.log_skill(skill_name)
        damage = Damage(25, True, True)
        self.cause_damage(damage)

    def move(self, turn):
        self.八重樱的饭团()
        Character.move(self, turn)

    def extra_attack(self):
        self.卡莲的饭团()

