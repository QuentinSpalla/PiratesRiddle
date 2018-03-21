import constants
from game import Game

pirate_game = Game(constants.NBR_COINS, constants.NBR_PIRATES, constants.OUTPUT_FILE)

if not pirate_game.is_error:
    pirate_game.coins_distribution()

pirate_game.write_in_txt()