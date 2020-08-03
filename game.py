import operator
from util import log
from character import Character


class Game:

    @staticmethod
    def sort(a: Character, b: Character):
        return sorted((a, b), key=operator.attrgetter("speed"), reverse=True)

    def __init__(self, a: Character, b: Character):
        # sort by speed
        self.faster, self.slower = self.sort(a, b)
        self.faster.set_enemy(self.slower)
        self.slower.set_enemy(self.faster)

    def autoplay(self):

        for turn in range(1, 30):
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
