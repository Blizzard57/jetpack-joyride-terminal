'''This module contains the main characters movement and other details'''
import numpy as np
from checkInp import getch

class Mario:
    '''This module generates and checks the mario's movement and its position'''
    def __init__(self, x=21, y=2):
        '''Defining position and looks of Mario'''
        # Coordinates of Mario
        self.x = x
        self.y = y
        # Mode ==> Powerup acquired
        # 0 --> No powerup, 1 --> Shield, 2 --> Speed, 3 --> Drogon (Yet to impliment) 
        self.mode = 0

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def give_location(self,level,frame_no):
        '''Assigns position of mario in the level'''
        if self.mode != 3: # If not drogon
            #if self.collision(level, frame_no):
            level[self.x,self.y + frame_no] = '/'
            level[self.x,self.y+2 + frame_no] = '\\'
            level[self.x-1,self.y + frame_no] = '/'
            level[self.x-1,self.y+1 + frame_no] = '|'
            level[self.x-1,self.y+2 + frame_no] = '\\'
            level[self.x-2,self.y+1 + frame_no] = '@'
            # Checking for colision with various objects
            if np.isin('*',level[self.x-3:self.x,self.y + frame_no -1 : self.y+3 + frame_no]):
                return 1
            if np.isin('0',level[self.x-3:self.x,self.y + frame_no -1 : self.y+3 + frame_no]):
                return 1
            elif np.isin('$',level[self.x-3:self.x,self.y + frame_no -1 : self.y+3 + frame_no]):
                return 2
            elif np.isin('p',level[self.x-3:self.x,self.y + frame_no -1 : self.y+3 + frame_no]):
                return 3
            return 0
        else:
            pass

    def change_location(self):
        data = getch()
        if data == 'w':
            if self.x > 3:
                self.x = self.x - 2
            elif self.x == 3:
                self.x = 2
        elif data == 'a':
            if self.y > 0:
                self.y = self.y - 2
                self.gravity()
        elif data == 'd':
            if self.y < 50:
                self.y = self.y + 2
                self.gravity()
        elif data == " ":
            self.gravity()
            return 1
        elif data == 'q':
            exit()
        elif data == 'z':
            self.gravity()
            return 2
        else:
            self.gravity()
        return 0

    def gravity(self):
        if self.x < 20:
            self.x = self.x + 2
        elif self.x == 20:
            self.x = 21

    def reset_location(self,level,frame_no):
        if self.mode != 3: # If not drogon
            level[self.x,self.y + frame_no] = ' '
            level[self.x,self.y+2 + frame_no] = ' '
            level[self.x-1,self.y + frame_no] = ' '
            level[self.x-1,self.y+1 + frame_no] = ' '
            level[self.x-1,self.y+2 + frame_no] = ' '
            level[self.x-2,self.y+1 + frame_no] = ' '

if __name__ == "__main__":
   pass