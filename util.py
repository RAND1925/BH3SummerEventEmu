from random import randint

use_log = False # 是否输出战局


def roll(x: int):
    assert (0 <= x <= 100)
    return randint(1, 100) <= x


def log(s: str):
    if use_log:
        print(s)


class LowerBoundedInteger(int):
    _lower_bound: int = 0

    @classmethod
    def lower_adjust(cls, value):
        return max(value, cls._lower_bound)

    def __new__(cls, value):
        return super().__new__(cls, round(cls.lower_adjust(value)))

    def __sub__(self, other) :
        return self.__class__(self.lower_adjust(super().__sub__(other)))

    def add_percent(self, other):
        return self.__class__(self + round(super().__mul__(other).__divmod__(100)[0]))


class DoubleBoundedInteger(LowerBoundedInteger):
    _upper_bound: int = 100

    @classmethod
    def upper_adjust(cls, value):
        return min(value, cls._upper_bound)

    @classmethod
    def double_adjust(cls, value):
        return cls.upper_adjust(cls.lower_adjust(value))

    def __new__(cls, value):
        return super().__new__(cls, cls.double_adjust(value))

    def __add__(self, other):
        return self.__class__(self.double_adjust(super().__add__(other)))

    def __sub__(self, other):
        return self.__class__(self.double_adjust(super().__sub__(other)))

    def add_percent(self, other):
        return self.__class__(round(super().__mul__(other).__divmod__(100)[0]))


class PositiveInteger(int):
    _lower_bound: int = 0

    @classmethod
    def lower_adjust(cls, value):
        return max(value, cls._lower_bound)

    def __new__(cls, value):
            return super().__new__(cls, round(cls.lower_adjust(value)))

    def __sub__(self, other) :
        return self.__class__(self.lower_adjust(super().__sub__(other)))

    def add_percent(self, other):
        return self.__class__(self + round(super().__mul__(other).__divmod__(100)[0]))

