from headerfile import *
import numpy as np
import time
import logging

class gametop:
    ''' 
    This class handles the gameScore, Timeleft and score of the player
    '''
    def __init__(self,score,livesleft):
        self.timeleft = 1000
        self.previoustime = time.time()
        self.score = score
        self.livesleft = livesleft
        self.bosslife = -1
        self.level = 1
        self.shoottime = 0
        self.shoot = False

    def stimer(self):
        self.timeleft = 1000
    
    def update_level(self,level):
        self.level = level

    def updateshoot(self,val):
        self.shoot = val

    def updateshoottime(self,shoottime):
        self.shoottime = shoottime

    def update_life(self,bosslife):
        self.bosslife = bosslife

    def update_availabletime(self):
        cur_time = time.time()
        self.timeleft -= (cur_time - self.previoustime)
        self.previoustime = cur_time
        return self.timeleft

    def update_gametop(self,score,livesleft):
        '''
        For updating value of gametop items
        '''
        self.score = score
        self.livesleft = livesleft
    
    def update_gametop_onscreen(self,screen_array):
        ''' 
        For updating Gametop on screen
        '''
        string = np.array(["Time  : " + str(round(self.timeleft))+ '   ',"Lives : " + str(self.livesleft) + '   ',"Score : " + str(self.score) + '   ',"Level : " + str(self.level) + '   '])
        l = "Boss Lives : " + str(self.bosslife) + '   '
        s = "Power Time : " + str(self.shoottime) + '   '
        length = string.size
        for i in range(0,3):
            for j in range(0,len(string[i])):
                screen_array[i+1][j+4] = string[i][j]
        for i in range(3,string.size):
            for j in range(0,len(string[i])):
                screen_array[i+1-3][j+4+20] = string[i][j]
        if(self.bosslife >= 0 ):
            for j in range(0,len(l)):
                screen_array[4+1-3][j+4+20] = l[j]
        if(self.shoot):
            for j in range(0,len(s)):
                screen_array[4+1-3][j+4+20] = s[j]
        
