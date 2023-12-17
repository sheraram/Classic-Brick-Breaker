import numpy as np
from items import *
from headerfile import *
import logging

# -- incr_dec_paddle
# if - 0 then No obtianed
# if - 1 then incr obtained
# if - 2 then dec obtained

class paddle:
    '''
    Handles paddle
    '''
    def __init__(self,current_X,current_Y,current_type):
        self.cur_x = current_X
        self.cur_y = current_Y
        self.type = current_type
        self.free_ball = False
        self.Stick_powerup = False
        self.incr_dec_paddle = 0
        self.interactball = True

    def update_paddle_onscreen(self,screengrid):
        ''' 
        Focusses on updating paddle on screen
        '''
        paddle = paddle_graphic[self.type]
        (paddle_start,half_size ,paddle_end) = self.return_se()
        start_val = paddle_start-2 if paddle_start-2 < 1 else 1
        end_val = WIDTH-2 if paddle_end+3 > WIDTH-2 else paddle_end + 3
        for i in range(start_val,end_val):
            if((screengrid[self.cur_y][i]!='0' or screengrid[self.cur_y][i]!='|') and (self.cur_x != 0 or self.cur_x != WIDTH-1)):
                screengrid[self.cur_y][i] = ' '
        j=0
        for i in range(paddle_start,paddle_end):
            screengrid[self.cur_y][i] = paddle[j]
            j+=1        

    def update_paddle_value(self,changed_X,changed_Y,changed_type):
        ''' 
        For updating paddle value in the class
        '''
        self.cur_x = changed_X
        self.cur_y = changed_Y
        self.type = changed_type

    def update_type(self,changed_type):
        '''
        Updates type of paddle used for powerup implementation
        '''
        self.type = changed_type

    def return_xandy(self):
        '''
        Return : (self.cur_x,self.cur_y)
        '''
        return (self.cur_x,self.cur_y)
    
    def return_type(self):
        '''
        Returns type of the paddle
        '''
        return self.type

    def return_se(self):
        half_size = int((PADDLE_SIZE[self.type])/2)
        paddle_start = self.cur_x - half_size
        paddle_end = self.cur_x + half_size+1
        return (paddle_start,half_size,paddle_end)