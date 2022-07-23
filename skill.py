from dataclasses import dataclass

from character import Character
from namer import Namer

@dataclass
class Action(Namer):
    name: str = 'do'
    player: Character = None
    target: Character = None
 
    def __call__(self, player: Character, target: Character):
        print('do nothing')

@dataclass 
class NormalAttack(Action):
    name: str = '通常攻击'
    def __call__(self, player: Character, target: Character):
        pass


@dataclass
class Skill(Action):
    name: str = '技能'

@dataclass
class KillingSkill(Skill):
    

@dataclass
class AfterAttackSkill(Skill):