from dataclasses import dataclass

from namer import Namer

@dataclass(frozen=True)
class Status(Namer):
    cd: int = 0
    enable: bool = False
    
    def count_down(self):
        if self.cd > 0:
            self.cd -= 1
            self.enable = self.cd != 0
    
    def on_add(self, character: Character):
        pass


class 撕裂状态(Status):
    name: 

沉默状态 = Status('')