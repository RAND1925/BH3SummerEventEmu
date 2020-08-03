from dataclasses import dataclass, field
from util import log, DoubleBoundedInteger, LowerBoundedInteger

class Buff:
    name: str

    def __init__(self, target, lasting = 1):
        self.target = target
        self.lasting = lasting
        self.on_add()

    def on_add(self):
        log(f"【{self.target.name}】获得了【{self.name}】")

    def on_turn_start(self):
        self.lasting -= 1

    def on_turn_end(self):
        if self.lasting == 0:
            log(f"【{self.target.name}】的【{self.name}】消失了")


@dataclass
class Damage:
    value: LowerBoundedInteger
    is_elemental: bool = False
    is_extra_skill: bool = False
    attacker = None
    receiver = None


@dataclass(order=True)
class Character:
    name: str
    attack: LowerBoundedInteger
    defence: LowerBoundedInteger
    speed: int
    extra_attack_turn: int
    health: DoubleBoundedInteger = DoubleBoundedInteger(100)
    # is_multiple: bool 姬子阿姐。。。
    status: list = field(default_factory=list)

    skills_enabled: bool = True
    movable: bool = True

    def log_skill(self, skill):
        log(f"{self.name} 的技能【{skill.skill_name}】 发动")

    def set_enemy(self, enemy):
        self.enemy = enemy

    def is_dead(self) -> bool:
        return self.health <= 0

    def move_status(self):
        for buff in self.status:
            buff.on_remove()
            self.status.remove(buff)

    def move(self, turn):
        if self.extra_attack_available(turn):
            return self.extra_attack()
        return self.normal_attack()

    def turn(self, turn):
        for buff in self.status:
            buff.on_turn_start()
        if self.movable:
            self.move(turn)
        else:
            log(f"【{self.name}】什么都做不到...")
        for buff in self.status:
            buff.on_turn_end()
            if buff.lasting == 0:
                self.status.remove(buff)

    def extra_attack_available(self, turn) -> bool :
        return self.skills_enabled and self.extra_attack_turn and turn % self.extra_attack_turn == 0

    def normal_attack(self):
        damage = self.get_normal_damage()
        return self.cause_damage(damage)

    def extra_attack(self):
        pass

    def get_damage_value(self, value: LowerBoundedInteger, is_elemental: bool = False) -> LowerBoundedInteger:
        return LowerBoundedInteger(value if is_elemental else value - self.enemy.defence)

    def get_normal_damage_value(self, is_elemental: bool = False) -> LowerBoundedInteger:
        return LowerBoundedInteger(self.get_damage_value(self.attack, is_elemental))

    def get_normal_damage(self) -> Damage:
        return Damage(self.get_normal_damage_value(False), False, False)

    def cause_damage(self, damage: Damage):
        log(f"【{self.name}】对【{self.enemy.name}】造成了 {damage.value} 点伤害")
        self.enemy.receive_damage(damage)

    def receive_damage(self, damage: Damage):
        self.health -= damage.value
        log(f"【{self.name}】的当前生命值为 {self.health}")

    def restore_health(self, health: int):
        self.health += health
        log(f"【{self.name}】回复了 {health} 点生命\n【{self.name}】的当前生命值为 {self.health}")

    def log_skill(self, skill_name):
        log(f"【{self.name}】的技能【{skill_name}】发动！")

