import time
import os
import random
import logging
from headerfile import *
from items import *
from keypressed import *
from screen import *
from paddle import *
from gametop import *
from bricks import *
from ball import *
from powerup import *

logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s',level=logging.DEBUG)
logging.debug('This will get logged to a file')
logging.debug('If you face any problem in powerup do check for the way __init__ is declared each time')

class Run:
    '''
    This is Main Game Class handling all the game flow
    '''
    def __init__(self):
        self.sys_random = random.SystemRandom()
        self.sticky_ball_motion = True
        self.sticky_ball_powerup = [False]
        self.ball_class = []
        self.screen_array = np.array([])
        self.Paddle = None
        self.paddle_array = np.array([])
        self.level = 1
        self.powerup_flag = [0,0,0,0,0,0,0]
        self.skipkey = False
        self.boss = None
        self.bbtime = time.time()

    def return_paddle_start_and_end(self):
        '''
        This function returns starting  and ending point of paddle
        '''
        half_size = int((PADDLE_SIZE[self.paddle_array[2]])/2)
        paddle_start = self.paddle_array[0] - half_size-1
        paddle_end = self.paddle_array[0] + half_size+1
        return (half_size,paddle_start,paddle_end)

    def move(self):
        '''
        This function is responsible for detecting user input and responding accordingly
        '''
        key = input_to()
        (half_size,paddle_start,paddle_end) = self.return_paddle_start_and_end()
        print(CLEAR_SCREEN)
        if(key == 'q'):
            os.system('clear')
            print(art.you_quit_art)
            return 0
        elif(key == 'a'):
            if(paddle_start > 4):
                self.paddle_array[0] -= 3
                if(self.level == 3):
                    self.boss.updatepy(self.paddle_array[0],self.screen_array)
                if(self.sticky_ball_motion):
                    self.ball_class[0].ball_sticky_motion(self.screen_array,0,-3)
                self.Paddle.update_paddle_value(self.paddle_array[0],self.paddle_array[1],self.paddle_array[2])
        elif(key == 'd'):
            if(paddle_end < WIDTH-3):
                self.paddle_array[0] += 3
                if(self.level == 3):
                    self.boss.updatepy(self.paddle_array[0],self.screen_array)
                if(self.sticky_ball_motion):
                    self.ball_class[0].ball_sticky_motion(self.screen_array,0,+3)
                self.Paddle.update_paddle_value(self.paddle_array[0],self.paddle_array[1],self.paddle_array[2])
        elif(key == 'k'):
            self.sticky_ball_motion = False
        elif(key == 'f' ):
            if( self.level < 3):
                self.skipkey = True
            else:
                print("Game Over")
                exit()
        return 1

    def starting_instruction(self):
        '''
        This function just gives instructions to the user
        '''
        print(instructions)
        while True:
            pressed_key = input_to()
            if(pressed_key == 'g'):
                break
            elif(pressed_key == 'q'):
                exit()
            else :
                pass
        os.system('clear')

    def puinit(self,powerups):
        powerups.clear()
        self.ball_class.clear()
        powerups.append(power0(0,0,0,0))
        powerups.append(power1(0,0,0,0))
        powerups.append(power2(0,0,0,0))
        powerups.append(power3(0,0,0,0))
        powerups.append(power4(0,0,0,0))
        powerups.append(power5(0,0,0,0))
        powerups.append(power6(0,0,0,0))

    def Go(self):
        '''
        This function has the main control flow of the game
        '''
        powerups = []
        self.puinit(powerups)
        self.starting_instruction()
        screen_board = screen(HEIGHT,WIDTH)
        screen_board.create_scenery()
        self.screen_array = screen_board.return_screenarray()
        self.paddle_array = np.array([80,43,1])
        self.Paddle = paddle(self.paddle_array[0],self.paddle_array[1],self.paddle_array[2])
        self.Paddle.update_paddle_onscreen(self.screen_array)
        bricks = Bricks(self.level)
        (half_size,paddle_start,paddle_end) = self.return_paddle_start_and_end()
        temp_random = self.sys_random.choice([i for i in range(paddle_start,paddle_end)])
        self.ball_class.append(Ball(BALL_X_STARTING_CONSTANT_VELOCITY,BALL_Y_STARTING_CONSTANT_VELOCITY,42,temp_random,self.screen_array,self.level))
        bricks.update_brick_onscreen(self.screen_array)
        score = 0
        choosen_value = 0
        start_time = time.time()
        livesleft = 3
        gametop_data = gametop(score,livesleft)
        gametop_data.stimer()
        gametop_data.update_gametop_onscreen(self.screen_array)
        screen_board.showscreen()
        tic_toc = time.time()
        while True:
            toc = time.time()
            frames = toc - tic_toc
            if(frames >= 0.11):
                tic_toc = toc
                move_return = self.move()
                if(not move_return):
                    break
                if(gametop_data.update_availabletime() < 0):
                    os.system('clear')
                    print(fmagenta + art.game_over + all_reset)
                    break
                
                if(not self.sticky_ball_motion):
                    (half_size,paddle_start,paddle_end) = self.return_paddle_start_and_end()
                    some_temp_val= self.ball_class[0].update_ball_motion(self.screen_array,bricks,paddle_start,paddle_end,self.boss)
                    if(some_temp_val is None):
                        (bavx,bavy,bax,bay) = self.ball_class[0].return_class_init()
                        self.ball_class[0].update_speed(-bavx,bavy)
                        val_zero = (0,0,0)
                        # logging.debug("inside mainrunning : " + str(self.level) + " : bricks length :" + str(len(bricks)))
                        bricks.remove_brick_onscreen(self.screen_array,bax-1,bay,powerups[4].check_time())
                        (ball_return_value,score_,choosen_value)  = val_zero
                    else:
                        (ball_return_value,score_,choosen_value) = some_temp_val
                    if(len(self.ball_class) > 1):
                        for i in range(1,len(self.ball_class)):
                            some_temp_val_2 = self.ball_class[i].update_ball_motion(self.screen_array,bricks,paddle_start,paddle_end,self.boss)
                    if(choosen_value!=0):
                        if(self.powerup_flag[choosen_value-1] != 1):
                            self.powerup_flag[choosen_value-1] = 1
                    score+=score_
                    score_ = 0
                    if(ball_return_value < 0):
                        livesleft -= 1
                        if(livesleft <= 0):
                            os.system('clear')
                            print(FRED + art.you_loose + all_reset)
                            break
                        (half_size,paddle_start,paddle_end) = self.return_paddle_start_and_end()
                        temp_random = self.sys_random.choice([i for i in range(paddle_start,paddle_end)])
                        self.ball_class[0] = Ball(BALL_X_STARTING_CONSTANT_VELOCITY,BALL_Y_STARTING_CONSTANT_VELOCITY,42,temp_random,self.screen_array)
                        for i in range(0,7):
                            if(self.powerup_flag[i] == 1): 
                                powerups[i].deactivate_time()
                                self.powerup_flag[i] = 0
                                powerups[i].undo(self.Paddle,self.paddle_array,self.ball_class,self.screen_array,self.ball_class[0],self.sticky_ball_powerup,bricks)
                                powerups[i].update_status(0)
                        self.sticky_ball_motion = True
                for i in range(0,7):
                    if(self.powerup_flag[i]):
                        if(powerups[i].return_status() == 0):
                            (bavx,bavy,bax,bay) = self.ball_class[0].return_class_init()
                            powerups[i].update_xy(bax,bay)
                            powerups[i].uballv(bavx,bavy)
                            powerups[i].make_powerup_active()
                        elif(powerups[i].return_status() == 1):
                            (half_size,paddle_start,paddle_end) = self.return_paddle_start_and_end()
                            ret_value = powerups[i].update_powerup_onscreen(self.screen_array,paddle_end,paddle_start,self.Paddle)
                            if(ret_value == True):
                                powerups[i].do(self.Paddle,self.paddle_array,self.ball_class,self.screen_array,self.ball_class[0],self.sticky_ball_powerup,bricks)
                                logging.debug("paddle_array do main : " + str(self.paddle_array))
                            if(powerups[i].return_status() == 0):
                                self.powerup_flag[i]=0
                        elif(powerups[i].return_status() == 2):
                            if(i == 6):
                                gametop_data.updateshoot(True)
                                (score_,timeleft) = powerups[i].do(self.Paddle,self.paddle_array,self.ball_class,self.screen_array,self.ball_class[0],self.sticky_ball_powerup,bricks)
                                score+=score_
                                gametop_data.updateshoottime(int(abs(timeleft)))
                            if(not powerups[i].check_time()):
                                self.powerup_flag[i] = 0
                                powerups[i].update_status(0)
                                powerups[i].deactivate_time()
                                powerups[i].undo(self.Paddle,self.paddle_array,self.ball_class,self.screen_array,self.ball_class[0],self.sticky_ball_powerup,bricks)
                                logging.debug("paddle_array undo2 main : " + str(self.paddle_array))
                                powerups[i].update_status(0)
                if(bricks.bkleft() == 0 and self.level != 3 ):
                    self.level += 1
                    if(self.level == 4):
                        print("You Won !!")
                        break
                    if(self.level < 4):
                        os.system('clear')
                        self.puinit(powerups)
                        gametop_data.update_level(self.level)
                        (half_size,paddle_start,paddle_end) = self.return_paddle_start_and_end()
                        temp_random = self.sys_random.choice([i for i in range(paddle_start,paddle_end)])
                        self.ball_class.append(Ball(BALL_X_STARTING_CONSTANT_VELOCITY,BALL_Y_STARTING_CONSTANT_VELOCITY,42,temp_random,self.screen_array,self.level))
                        self.Paddle = paddle(self.paddle_array[0],self.paddle_array[1],self.paddle_array[2])
                        bricks.killbs()
                        bricks.update_brick_onscreen(self.screen_array)
                        logging.debug("mainrunning.py/if(bricks.bkleft() == 0 and self.level != 3 ) : self.level : " + str(self.level))
                        bricks = Bricks(self.level)
                        
                if(self.level == 3):
                    bricks.ulevel(3)
                    for i in range(len(self.ball_class)):
                        self.ball_class[i].update_level(3)
                    logging.debug("inside self.level :- -:")
                    if(toc - self.bbtime > 2.503):
                        os.system("aplay -q funstuff/background.wav &")
                        self.bbtime = toc
                    if(self.boss == None):
                        self.boss = Boss(self.Paddle.return_xandy()[1],score)
                        self.boss.updatepy(self.paddle_array[0],self.screen_array)
                    gametop_data.update_life(self.boss.rlife())
                    if(self.boss.rlife() <=0 ):
                        os.system("aplay -q funstuff/captureflag.wav &")
                        print("You won")
                        break
                if(self.level == 3 and self.boss.mbomb(self.screen_array,self.return_paddle_start_and_end())):
                    livesleft -= 1 
                    if(livesleft <= 0):
                        os.system('clear')
                        print(FRED + art.you_loose + all_reset)
                        break
                gametop_data.update_gametop(score,livesleft)
                gametop_data.update_gametop_onscreen(self.screen_array)
                self.Paddle.update_type(self.paddle_array[2])
                self.Paddle.update_paddle_onscreen(self.screen_array)
                bricks.update_brick_onscreen(self.screen_array)
                screen_board.showscreen()

                if(self.skipkey):
                    bricks.killbs()
                    for i in range(8,len(self.screen_array)-2):
                        for j in range(3,len(self.screen_array)-2):
                            self.screen_array[i][j] = ' '
                    for i in range(len(self.ball_class)):
                        (vx,vy,bx,by) = self.ball_class[i].return_class_init()
                        self.screen_array[bx][by] = ' '
                    self.skipkey = False
                
                if(self.sticky_ball_powerup[0]):
                    (bavx,bavy,bax,bay) = self.ball_class[0].return_class_init()
                    (half_size,paddle_start,paddle_end) = self.return_paddle_start_and_end()
                    if(bax >= 42):
                        if(bay>=paddle_start and bay <= paddle_end):
                            self.sticky_ball_motion = True
