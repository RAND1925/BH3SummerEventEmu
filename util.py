from random import randint

use_log = True # 是否输出战局

def roll(x: int):
    assert (0 <= x <= 100)
    return randint(1, 100) <= x


def log(s: str):
    if use_log:
        print(s)