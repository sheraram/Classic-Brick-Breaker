import numpy as np
import sys

class screen:
    ''' 
    This class handle creating and displaying task of game screen
    '''
    def __init__(self,HEIGHT,WIDTH):
        self.width = WIDTH
        self.height = HEIGHT
        self.screenarray = np.full((HEIGHT,WIDTH),' ', dtype='<U25')

    def showscreen(self):
        '''
        Just printing on Screen
        '''
        for i in range(0,self.height):
            for j in range(0,self.width):
                sys.stdout.write(self.screenarray[i][j])
            sys.stdout.write('\n')

    def create_scenery(self):
        '''
        Used to create walls and top regions of the game screen
        '''
        for i in range(0,self.height):
            for j in range(0,self.width):
                if(not i or i==4 or i == self.height-1):
                    self.screenarray[i][j] = '-'
                if(not j or j == self.width -1):
                    self.screenarray[i][j] = '|'
                if((not i or i==4 or i == self.height-1) and (not j or j == self.width-1)):
                    self.screenarray[i][j] = '*'

    def return_screenarray(self):
        '''
        Return : self.screenarray
        '''
        return self.screenarray