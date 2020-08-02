from dataclasses import dataclass
from util import log

@dataclass
class Buff:
    name: str

@dataclass
class Damage:
    value: int
    is_elemental: bool = False
    is_extra_skill: bool = False
    attacker = None
    receiver = None


@dataclass(order=True)
class Character:

    @dataclass
    class Skill():
        skill_name: str

        def skill_log(self, name):
            log(f"{self.name}")

    @dataclass
    class ExtraSkill(Skill):
        turn: int

        def __call__(self, *args, **kwargs):
            pass

    name: str
    attack: int
    defence: int
    speed: int
    extra_attack_turn: int
    health: int = 100
    # is_multiple: bool 姬子阿姐。。。
    status = []

    def log_skill(self, skill):
        log(f"{self.name} 的技能【{skill.skill_name}】 发动")


    def set_enemy(self, enemy):
        self.enemy = enemy

    def is_dead(self) -> bool:
        return self.health <= 0

    def turn(self, turn):
        if self.status != []:
            self.status = []
            log(f"【{self.name}】什么都做不到...")
            return

        self.status = []
        if self.extra_attack_turn:
            if turn % self.extra_attack_turn == 0:
                return self.extra_attack()

        return self.normal_attack()

    def normal_attack(self):
        damage = self.get_normal_damage()
        return self.cause_damage(damage)


    def extra_attack(self):
        pass

    def get_normal_damage_value(self, is_elemental = False):
        if is_elemental:
            return self.attack
        else:
            return self.attack - self.enemy.defence

    def get_normal_damage(self) -> Damage:
        return Damage(self.get_normal_damage_value(False), False, False)

    def cause_damage(self, damage: Damage):
        log(f"【{self.name}】对【{self.enemy.name}】造成了 {damage.value} 点伤害")
        self.enemy.receive_damage(damage)


    def receive_damage(self, damage: Damage):
        self.health -= damage.value
        log(f"【{self.name}】的当前生命值为 {self.health}")

    def log_skill(self, skill_name):
        log(f"【{self.name}】的技能【{skill_name}】发动！")
