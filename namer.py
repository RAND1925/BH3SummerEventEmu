from dataclasses import dataclass
from tkinter.messagebox import NO

@dataclass(frozen=True)
class Namer:
    @property
    def name(self):
        if self._name:
            return self.__class__.__name__
        return self._name
