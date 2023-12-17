''' This file contains color defination and some needed variable 
'''
import numpy as np
# parameters :
GROUND = 1
SKY = 4
HEIGHT = 45
WIDTH = 165
CLEAR_SCREEN = "\033[0;0H"
PADDLE_SIZE = [7,9,13,7,9,13]
BALL_X_STARTING_CONSTANT_VELOCITY = -1
BALL_Y_STARTING_CONSTANT_VELOCITY = 1

#NOTE Colors 
# Foreground Colors :
FBLACK = "\033[30m"
FRED = "\033[31m"
FGREEN = "\033[32m"
FYELLOW = "\033[33m"
fblue = "\033[34m"
fmagenta = "\033[35m"
fcyan = "\033[36m"
fwhite = "\033[37m"

# Bright Versions :
fbrightblack = "\033[90m"
fbrightred = "\033[91m"
fbrightgreen = "\033[92m"
fbrightyellow = "\033[93m"
fbrightblue = "\033[94m"
fbrightmagenta = "\033[95m"
fbrightcyan = "\033[96m"
fbrightwhite = "\033[97m"

# Background Colors :
bblack = "\033[40m"
bred = "\033[41m"
bgreen = "\033[42m"
byellow = "\033[43m"
bblue = "\033[44m"
bmagenta = "\033[45m"
bcyan = "\033[46m"
bwhite = "\033[47m"

# Bright Versions :
bbrightblack = "\033[100m"
bbrightred = "\033[101m"
bbrightgreen = "\033[102m"
bbrightyellow = "\033[103m"
bbrightblue = "\033[104m"
bbrightmagenta = "\033[105m"
bbrightcyan = "\033[106m"
bbrightwhite = "\033[107m"

# reset :
all_reset = "\033[0m"
back_rest = "\033[49m"
fore_reset = "\033[39m"

bricks_color = np.array([bred,byellow,bcyan,bgreen,bmagenta])
bricks_font_color = np.array([fbrightred,fbrightyellow,fbrightblue,fbrightgreen,fbrightmagenta])
powerup_temper = [bmagenta+"P" + all_reset,bgreen + "P" + all_reset,bred + "P" + all_reset,byellow + "P" + all_reset,bblue + "P" + all_reset,bcyan + "P" + all_reset, bbrightgreen + "P" + all_reset]