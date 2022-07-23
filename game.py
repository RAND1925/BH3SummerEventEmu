import operator
from util import log
from character import Character
from typing import *

class Game:
    characters: List[Character]


    def set_starter(character: Character):
        
    @staticmethod
    def sort(Characters):
        return sorted(Characters, key=operator.attrgetter("speed"), reverse=True)

    def __init__(self, A: type, B: type):
        # sort by speed
        Faster, Slower = self.sort((A, B))
        self.faster = Faster()
        self.slower = Slower()
        self.faster.set_enemy(self.slower)
        self.slower.set_enemy(self.faster)


    

    def autoplay(self):
        for turn in range(1, 50):
            log(f">>>>>>>>>>>>>>>turn: {turn}<<<<<<<<<<<<<<<<")
            self.faster.turn(turn)
            if self.slower.is_dead():
                log(f"【{self.slower.name}】失败")
                return 1
            log("--------------------------------------")
            self.slower.turn(turn)
            if self.faster.is_dead():
                log(f"【{self.faster.name}】失败")
                return 0
        return 2
