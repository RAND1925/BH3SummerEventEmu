from util import log
from game import Game
from characters import *
from config import Ch1, Ch2, total_games


faster, slower = Game.sort(Ch1(), Ch2())
faster_wins = 0

res = [0, 0, 0]
for i in range(total_games):
    log(f"==============game: {i}================")
    game = Game(Ch1(), Ch2())
    res[game.autoplay()] += 1


print(f"在 {total_games} 次对局中，【{faster.name}】获胜了 {res[1]} 次，【{slower.name}】获胜了 {res[0]} 次。平局 {res[2]} 次")