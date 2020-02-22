'''This is the main module which is run in order to play the game'''
import os
import time
import termios
import sys
from checkInp import getch_noTimeout
from assets import Asset
from engine import Render
from greeter import *
from mario import Mario
from boss import Boss
from bullet import Bullet
#import multiprocessing

def hide_cursor():
    '''Hides the cursor on the screen while printing'''
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def quit_game():
    '''Quits the game with previous settings intact'''
    os.system('setterm -cursor on')
    os.system('exit')
    exit()

class Player:
    '''This class contains information of the player, its stats and also plays the game ( Gives
     Orders on rendering a frame)'''
    def __init__(self):
        '''Initialises the default valus of stats of players'''
        self.life = 3
        self.powerup = 'None'
        self.coins = 0
        self.fps = 16 # The fps of the game ( Running Speed)

    def reset(self):
        '''After losing the game, resets the default value for the player to start playing again'''
        get_end_screen()
        data = getch_noTimeout()
        if data == 'q':
            quit_game()
        elif data == 'r':
            self.life = 3
            self.powerup = 'None'
            self.coins = 0
            self.main_game()
        else:
            self.reset()

    def start(self):
        '''Loads the initial greeter screen and also explains controls of the game'''
        get_start_screen() # Greeter Screen
        #getch = _Getch()
        data = getch_noTimeout() ## Change to Getch --> Every Input Statement
        if data == 'q':
            quit_game()
        elif data == 'r':
            #print(self.life)
            self.main_game()
        else:
            self.start()
        return 0

    def main_game(self):
        '''This is the module which renders all the frames and checks the main
         functionality of the game'''
        hide_cursor()
        os.system('stty -echo') # Stops STDIN echo
        frame = Render()
        M1 = Mario()
        list_bullets = []
        i = 0
        speed = 0
        shield = 0

        while i < 0: # Movement of frame ==> Essentially Speed of game
            os.system('clear')
            if self.life < 1:
                break
                #exit()
            #os.system('echo "\033[;H"')
            ret_collision = M1.give_location(frame.frame,i)
            
            #Getting location of Moving Assets
            for j in list_bullets:
                val = j.give_location(frame.frame,i)
                if val == 2:
                    del j
            if ret_collision == 1:
                if self.powerup == 'None' or self.powerup == 'Speed':
                    self.life = self.life - 1
                if self.powerup == 'Drogon':
                    self.powerup = 'None'
            elif ret_collision == 2:
                self.coins = self.coins + 5
            elif ret_collision == 3:
                self.powerup = 'Speed'
            
            #Speeding up
            if self.powerup == 'Speed':
                i = i + 1
                speed = speed + 1
                if speed > 100:
                    self.powerup = 'None'
                    speed = 0

            #Shield
            if self.powerup == 'Shield':
                shield = shield + 1
                if shield > 50:
                    self.powerup = 'None'
            #Cooldown period
            if shield > 0 and self.powerup != 'Shield':
                shield = shield - 1

            #Printing the frame
            frame.print_frame(i,self.life, self.coins, self.powerup, shield)
            
            #Removing the previous instance of each frame
            for j in list_bullets:
                j.reset_location(frame.frame,i)
            M1.reset_location(frame.frame,i)
            
            #Updating location of each instance
            for j in list_bullets:
                j.change_location()
            ret_pow = M1.change_location()
            if ret_pow == 1:
                self.powerup = 'Shield'
            elif ret_pow == 2:
                list_bullets.append(Bullet(M1.get_x(),M1.get_y()))
            elif ret_pow == 3:
                self.powerup = 'Speed'

            time.sleep(1/self.fps)
            #Time step
            i = i + 1

        #Removing overhead
        del frame

        #Boss Fight
        self.fps = 16
        list_bullets = []
        V1 = Boss()
        frame = Render(False,80)
        V1.give_location(frame.frame)
        for i in range(200):
            os.system('clear')
            if self.life < 1:
                break
            
            for j in list_bullets:
                val = j.give_location(frame.frame,0)
                if val == 2:
                    del j
            ret_collision = M1.give_location(frame.frame,0)
            if ret_collision == 1:
                if self.powerup == 'None' or self.powerup == 'Speed':
                    self.life = self.life - 1
            V1.give_location(frame.frame)            

            frame.print_frame(0,self.life,self.coins,str(i),V1.life)
            
            for j in list_bullets:
                j.reset_location(frame.frame,0)
            M1.reset_location(frame.frame,0)
            V1.reset_location(frame.frame)
            
            for j in list_bullets:
                j.change_location()
            ret_pow = M1.change_location()
            if ret_pow == 2:
                list_bullets.append(Bullet(M1.get_x(),M1.get_y()))
            V1.change_location(M1.get_x())
            
            if i%10 == 0:
                list_bullets.append(Bullet(V1.get_x(),V1.get_y(),'B'))
            if V1.get_life() < 1:
                break

            time.sleep(1/self.fps)
        #Reset Check 
        if self.life < 1 or V1.get_life() > 0:
            self.reset()
            quit_game()
        won_screen()
        quit_game()
        return 0


if __name__ == "__main__":
    P1 = Player()
    os.system('setterm -cursor off')
    P1.start()
