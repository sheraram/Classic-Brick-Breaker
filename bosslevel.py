from headerfile import *
from art import art
import numpy as np
import random 
import time
import logging
from inherit_brick import *

class Boss:
    def __init__(self,py,score):
        self.py = py    #paddle y
        self.px = 7
        self.life = 100
        self.score = score
        self.sbricks = []
        self.pstart = 2
        self.pend = 2
        self.ufo = art.ufo.split('9')
        self.unb = [self.pstart + 10, self.pend - 20, len(self.ufo) + self.px]
        self.spawnbricks = (False,False)
        self.previousshot = time.time()
        self.bomb = []

    def cp(self):
        self.pstart = self.py - 22
        self.pend = self.py + 22
        if(self.pstart <= 2):
            self.pstart = 2
            self.pend = self.pstart + 44
        elif(self.pend >= WIDTH - 2):
            self.pend = WIDTH - 2
            self.pstart = self.pend - 44
        self.unb = [self.pstart + 10, self.pend - 20, len(self.ufo) + self.px]

    def updatepy(self,py,screen_array):
        self.clear(screen_array)
        self.binit()
        # self.check_spawing()
        self.py = py
        self.cbomb()
        self.draw(screen_array)

    def draw(self,screen_array):
        self.cp()
        self.bswfun(screen_array,True)
        for i in range(0,len(self.ufo)-1):
            for j in range(0,len(self.ufo[i])):
                screen_array[self.px+i][self.pstart + j] = self.ufo[i][j]

    def clear(self,screen_array):
        self.bswfun(screen_array,False)
        for i in range(0,len(self.ufo)-1):
            for j in range(0,len(self.ufo[i])):
                screen_array[self.px+i][self.pstart + j] = ' '

    def check_spawing(self):
        if(self.life <= 50 and self.life > 20 and not self.spawnbricks[0]):
            self.binit()
            self.spawnbricks = (True,False)
        if(self.life <= 20 and not self.spawnbricks[1]):
            self.binit()
            self.spawnbricks = (True,True)

    def decreaselife(self):
        self.life = self.life - 10
        self.score += 30

    def rlife(self):
        return self.life

    def collision(self,screen_array,x,y):
        if(x <= self.px + len(self.ufo)-1):
            self.decreaselife()
            return(self.score,0)
        else:
            for i in range(len(self.sbricks)):
                (x1,y1) = self.sbricks[i].returnxy()
                size = self.sbricks[i].returnbsize()
                if(x == x1 and (y >= y1 and y <= y1 + size)):
                    (life,typeb,score_) = self.sbricks[i].decrease_brick_life(1,False)
                    self.sbricks[i].clear(screen_array)
                    # self.sbricks[i].draw(screen_array)
                    self.score += score_
                    return(self.score,0)   # (score,choosen_value)
            return(0,0)

    def binit(self):
        # if(not self.spawnbricks[0] and not self.spawnbricks[1]):
        if(len(self.sbricks) < 2):
            self.sbricks.append(Brick_inherit(4,self.unb[2],self.unb[0]))
            self.sbricks.append(Brick_inherit(4,self.unb[2],self.unb[1]))
        # elif(self.spawnbricks[0] and not self.spawnbricks[1]):
        if(len(self.sbricks) < 5 and self.life > 20 and self.life <=50):
            lamda = 2
            while lamda < WIDTH - 8:
                self.sbricks.append(Brick_inherit(0,self.px + len(self.ufo) + 1,lamda))
                lamda += self.sbricks[-1].returnbsize()
        # elif(self.spawnbricks[1]):
        if(len(self.sbricks) <= 14 and self.life <= 20):
            lamda = 2
            while lamda < WIDTH - 8:
                self.sbricks.append(Brick_inherit(1,self.px + len(self.ufo) + 2,lamda))
                lamda += self.sbricks[-1].returnbsize()

    # use : True, then draw otherwise clear
    def bswfun(self,screen_array,use):
        for i in range(len(self.sbricks)):
            if(self.sbricks[i].return_alive()):
                if(use):
                    self.sbricks[i].draw(screen_array)
                else:
                    self.sbricks[i].clear(screen_array)

    def mbomb(self,screen_array,paddletuple):
        self.sdraw(screen_array,False)
        i = 0
        while i < len(self.bomb):
            if(self.bomb[i][0]<43):
                val = (self.bomb[i][0]+1,self.bomb[i][1])
                self.bomb[i] = val
                screen_array[self.bomb[i][0]][self.bomb[i][1]] = 'B'
            else:
                if(self.bomb[i][1]<= paddletuple[2]  and self.bomb[i][1] >= paddletuple[1]):
                    self.bomb.pop(i)
                    i-=1
                    return 1
                else:
                    self.bomb.pop(i)
                    i-=1
            i+=1
        return 0

    def cbomb(self):
        if(time.time() - self.previousshot > 0.5):
            self.previousshot = time.time()
            self.bomb.append((self.px+len(self.ufo),self.py))

    # falg : true, draw and  False ,clear
    def sdraw(self,screen_array,flag):
        for i in range(len(self.bomb)):
            if(flag):
                screen_array[self.bomb[i][0]][self.bomb[i][1]] = 'B'
            else:
                screen_array[self.bomb[i][0]][self.bomb[i][1]] = ' '