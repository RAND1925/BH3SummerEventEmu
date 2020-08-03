import operator
from util import use_log
from game import Game
from characters import *
import csv
Characters = [Kiana, Mei, Seele, Rita, Raven, Olenyevas, Theresas, SakuraKallen]
Characters = sorted(Characters, key=operator.attrgetter("speed"), reverse=True)

use_log = False
res_table = []

for Ch1 in Characters:
    for Ch2 in Characters:
        ch1_win = 0
        ch2_win = 0

        for turn in range(100000):
            game = Game(Ch1, Ch2)
            res = game.autoplay()
            if res == 1:
                ch1_win += 1
            elif res == 0:
                ch2_win += 1
        print(f"{Ch1.name} {ch1_win} : {ch2_win} {Ch2.name}")
        row = [Ch1.name, ch1_win, Ch2.name, ch2_win]
        res_table.append(row)

with open("res.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(('ch1', 'ch1_win', 'ch2_win', ))
    writer.writerows(res_table)