import numpy as  np
from headerfile import *
from art import *

# bricks shape and sizes :
bricks = np.array(["[####]","[$$$$]","[++++]","[IIII]","[::::]"])

# Ball :
ball_graphic = "O"

# Paddle :
PADDLE_SIZE = np.array([7,9,13,7,9,13])
paddle_graphic = np.array(['<======>','<=======>','<===========>','|======|','|=======|','|===========|'])

# Brick Orientations :
b_1 = "1-1-1-1-1-1-2-2-1-1-1" + " " + \
      "2-2-3-3-3-3-3-3-0-0-2"
b_2 = "1-1-1-0-1-1-3-3-1-2-1" + " " + \
      "0-0-0-0-0-0-0-2-1-1-2" + " " + \
      "0-0-0-0-0-2-1-2-3-2-2"
b_3 = "1-1-3-3-3-1-0-0-1-1-1" + " " + \
      "2-2-0-0-0-0-0-0-0-0-2"
b_4 = "1-1-1-1-1-1-1-1-1-1-1"
b_5 = "2-2-2-2-2-2-2-2-2-2-2"
brick_orientation = np.array([b_1,b_2,b_3])
brick_life_store = [0,1,2,3,5000]

# instructions :
instructions = FRED + art.instructions_art + all_reset + "\n" + \
    FRED + "|" + all_reset + " > Press " + FRED + "q" + all_reset + " to quit the game                                               " + \
    "                                                                                         " + FRED + "|\n" + all_reset + \
    FRED + "|" + all_reset + " > Press " + FRED + "d" + all_reset + " to move paddle to right                                        " + \
    "                                                                                         " + FRED + "|\n" + all_reset + \
    FRED + "|" + all_reset + " > Press " + FRED + "a" + all_reset + " to move paddle to right                                        " + \
    "                                                                                         " + FRED + "|\n" + all_reset + \
    FRED + "|" + all_reset + " > Press " + FRED + "j" + all_reset + " to fire the ball                                               " + \
    "                                                                                         " + FRED + "|\n" + all_reset + \
    FRED + "|" + all_reset + " > Press " + FRED + "g" + all_reset + " to start the game                                              " + \
    "                                                                                         " + FRED + "|\n" + all_reset + \
    FRED + "|" + all_reset + " > Press " + FRED + "f" + all_reset + " to move to next level                                          " + \
    "                                                                                         " + FRED + "|\n" + all_reset + \
    FRED + "|" + all_reset + " > Press " + FRED + "k" + all_reset + " to release ball                                                " + \
    "                                                                                         " + FRED + "|\n" + all_reset + \
    FRED + "|" + all_reset + " > Power " + bmagenta + "P" + all_reset + " Expand Paddle                                                  " + \
    "                                                                                         " + FRED + "|\n" + all_reset + \
    FRED + "|" + all_reset + " > Power " + bgreen + "P" + all_reset + " Shrink Paddle                                                  " + \
    "                                                                                         " + FRED + "|\n" + all_reset + \
    FRED + "|" + all_reset + " > Power " + bred + "P" + all_reset + " Ball Multiplier                                                " + \
    "                                                                                         " + FRED + "|\n" + all_reset + \
    FRED + "|" + all_reset + " > Power " + byellow + "P" + all_reset + " Fast Ball                                                      " + \
    "                                                                                         " + FRED + "|\n" + all_reset + \
    FRED + "|" + all_reset + " > Power " + bblue + "P" + all_reset + " Thru-ball                                                      " + \
    "                                                                                         " + FRED + "|\n" + all_reset + \
    FRED + "|" + all_reset + " > Power " + bcyan + "P" + all_reset + " Paddle Grab                                                    " + \
    "                                                                                         " + FRED + "|\n" + all_reset + \
    FRED + "|" + all_reset + " > Power " + bbrightgreen + "P" + all_reset + " Shoot Bullets                                                  " + \
    "                                                                                         " + FRED + "|\n" + all_reset + \
    FRED + "*----------------------------------------------------------------------------------------------------------------------" + \
    "---------------------------------------------*\n"+ all_reset