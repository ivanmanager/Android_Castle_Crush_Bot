import time
from game_logic import GameLogic
from game_ui import GameUI
import keyboard

gl = GameLogic()
gui = GameUI()

while 1:
    gui.UpdateGameState()
    time.sleep(0.01)
    
    escape = keyboard.is_pressed("escape")
    if escape == 1:
        break

    
gui.log_info('Game bot has been stopped.')