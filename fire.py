from headerfile import *
from items import *
from inherit_brick import *
from bricks import *

class fire:
    def __init__(self,x,y):
        self.cur_x = x
        self.cur_y = y
        self.initial_x = x
        self.initial_y = y
        self.alive = True
        self.ballcollide = False
        self.interactball = False

    def move(self,screen_array,bricks_class):
        self.fdraw(screen_array,False)
        self.cur_x += -1
        self.cur_y += 0
        (self.life,self.type,score) = self.collide(bricks_class)
        self.fdraw(screen_array,True)
        return (self.life,self.type,score)

    def cur_returnxy(self):
        return (self.cur_x,self.cur_y)

    def initial_returnxy(self):
        return (self.initial_x,self.initial_y)

    def collide(self,bricks_class):
        if(self.cur_x <= 5):
            self.alive = False
        else:
            bricks = bricks_class.bd_return()
            for i in range(0,bricks.shape[0]):
                for j in range(0,bricks[0].size):
                    size = bricks[i][j].returnbsize()
                    (x,y) = bricks[i][j].returnxy()
                    if(self.cur_x == x and (self.cur_y >= y and self.cur_y <= y+size) and self.alive ):
                        (self.life,self.type,score) = bricks[i][j].decrease_brick_life(1,False)
                        self.die()
                        return (self.life,self.type,score)
        return (0,0,0)
    
    def die(self):
        self.alive = False
        return self.alive
    
    #flag = True , draw otherwise clear

    def fdraw(self,screen_array,flag):
        if(self.alive):
            if(flag):
                screen_array[self.cur_x][self.cur_y] = '.'
            else:
                screen_array[self.cur_x][self.cur_y] = ' '
