from util import log
from game import Game
from characters import *
from config import Ch1, Ch2, total_games


faster, slower = Game.sort(Ch1(), Ch2())
faster_wins = 0

for i in range(total_games):
    log(f"==============game: {i}================")
    game = Game(Ch1(), Ch2())
    faster_wins += game.autoplay()


print(f"在{total_games}次对局中，【{faster.name}】获胜了 {faster_wins} 次，【{slower.name}】获胜了 {total_games-faster_wins} 次")