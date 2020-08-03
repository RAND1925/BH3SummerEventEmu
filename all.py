import operator
from util import use_log
from game import Game
from characters import *
import csv
Characters = [Kiana, Mei, Seele, Rita, Raven, Olenyevas, Theresas, SakuraKallen]
Characters = sorted(Characters, key=operator.attrgetter("speed"), reverse=True)

use_log = False
res_table = []

times = 100000
percent = times / 100
for Ch1 in Characters:
    for Ch2 in Characters:
        if Ch1 == Ch2:
            continue
        faster_win = 0
        slower_win = 0

        for turn in range(times):
            game = Game(Ch1, Ch2)
            res = game.autoplay()
            if res == 1:
                faster_win += 1
            elif res == 0:
                slower_win += 1
        if (Ch1.speed >= Ch2.speed):
            print(f"{Ch1.name} {int(faster_win // percent)} : {int(slower_win // percent)} {Ch2.name}")
            row = [Ch1.name, faster_win, Ch2.name, slower_win]
        else:
            print(f"{Ch1.name} {int(slower_win // percent)} : {int(faster_win // percent)} {Ch2.name}")
        row = [Ch1.name, faster_win, Ch2.name, slower_win]
        res_table.append(row)
    print("===================")

with open("res.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(('ch1', 'ch1_win', 'ch2_win', ))
    writer.writerows(res_table)