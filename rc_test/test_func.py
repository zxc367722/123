__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '2021/7/17 17:18'

import pyautogui
from rc_util.game_util import find_image, check_image


# screen_path = "../imgs/full_snap__1626483257.png"
screen_path = "../imgs/full_snap__1627116037.png"
recaptha_path = "../rc_items/utils/tt.png"

head_path = "../rc_items/games/coinflip_game_head_img.png"
start_path = "../rc_items/utils/start_game_big.png"


# screenWidth, screenHeight = pyautogui.size()
# print(screenWidth, screenHeight)
res = find_image(recaptha_path, screen_path)
print(res)
