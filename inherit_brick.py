import numpy as np
from items import *
from headerfile import *
import random
import logging
import os

#   ^ (-x)
#   |
#   |
#    -----> (+y)
# Yes i know its fucked up :(

# Score : 
#     Super Ball Mode    Normal ball Mode
#   0   -> 10                 10
#   1   -> 20                 10
#   2   -> 30                 10
#   3   -> 50 //unbreakable  

class Brick_inherit:
    '''
    One class for all the bricks type
    '''
    def __init__(self,typeb,starting_x,starting_y):
        self.type = typeb
        self.life = brick_life_store[typeb]
        self.bricks_size = 6
        self.sx = starting_x
        self.sy = starting_y
        self.rainbow = False
        self.alive = True
        self.interactball = True
        
    def update_score(self,go_thru):
        score = 0
        if(go_thru):
            if(self.type == 0):
                score+=10
            elif(self.type == 1):
                score+=20
            elif(self.type == 2):
                score +=30
            else:
                score+=50
        else:
            score+=10
        return score

    def decrease_brick_life(self,value,go_thru):
        '''
        Decrease brick life and type as per the ball used and the collided brick
        '''
        score = 0
        score += self.update_score(go_thru)
        # print("Score : ",score)
        if(self.type < 0):
            self.die()
            return (0,0,0)
        if(go_thru):
            self.type = -1
            self.life = 0
            self.die()
        elif(self.type!= 4):
            if(self.type == 3):
                self.rainbow = True
            self.life = brick_life_store[self.type]
            self.type -= 1
            if(int(self.type) < 0):
                os.system("aplay -q funstuff/explosion.wav &")
                self.die()
        return (self.life,self.type,score)
    
    def change_color_brick(self,typeb):
        '''
        Just changes the color of the brick as per changes type
        '''
        self.color  = bricks_color[typeb]+bricks_font_color[typeb]
        return self.color

    def returnxy(self):
        '''
        Returns current X and Y coordinates of the brick
        '''
        return (self.sx,self.sy)

    def returnbsize(self):
        return self.bricks_size

    def die(self):
        self.alive = False

    def return_alive(self):
        return self.alive
    
    def return_type(self):
        return self.type

    def retrainbow(self):
        return self.rainbow

    def falldown(self):
        self.sx += 1

    def draw(self,screen_array):
        temp = bricks_color[self.type] + bricks_font_color[self.type]
        for z in range(0,self.bricks_size):
            screen_array[self.sx][self.sy+z] = temp + bricks[self.type][z] + all_reset

    def clear(self,screen_array):
        for z in range(0,self.bricks_size):
            screen_array[self.sx][self.sy+z] = ' '

    def update_type(self,btype):
        self.type = btype