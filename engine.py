#   Game time = 2 min
#   Game runs at 10 fps
#   Hence no of frames required = 10 * 60 * 2 = 1200 frames
#   Speed of game = 2 colums per frame
#   Therefore no of columns required = 1200 * 2 + 80 = 2480
#import sys

'''This is the module which prints all the frames'''

import os
import numpy as np
from assets import Asset
from checkInp import getch
import colorama

colorama.init

class Render:
    '''This is the engie which renders each frame and also is a decider for collisions
    between character and object. This engine also decides the fps of gameplay'''
    def __init__(self,generate = True, length = 1000):
        '''Declares the initial frame and its placement with floor and ceiling'''
        # Asset is an array of all the object which can be interacted with
        # Actor is the main character
        self.frame = np.full((23, length), " ")
        self.gen_level(generate)
   
    def print_frame(self,frame_no,life,coins, powerup, shield):
        '''This function prints the matrix which is 80 x 24, hence a frame'''
        #M1.print_location(self.frame, frame_no)
        for i in range(23):
            for j in range(frame_no, 80 + frame_no):
                if self.frame[i][j] == "*":
                    print(colorama.Fore.RED + self.frame[i][j] + colorama.Style.RESET_ALL, end="")
                elif self.frame[i][j] == "$":
                    print(colorama.Fore.YELLOW + self.frame[i][j] + colorama.Style.RESET_ALL, end="")
                elif self.frame[i][j] == "=":
                    print(colorama.Back.BLUE + self.frame[i][j] + colorama.Style.RESET_ALL, end="")
                elif self.frame[i][j] == "p":
                    print(colorama.Back.GREEN + self.frame[i][j] + colorama.Style.RESET_ALL, end="")
                else :#self.frame[i][j] == " ":
                    print(self.frame[i][j], end="") 
            print()
        for _ in range(8):
            print(" ",end="")
        print("Lives Left : " + str(life),end="",flush=True) # 14
        for _ in range(8):
            print(" ",end="")
        print("Powerup : " + powerup,end="")
        for _ in range(6):
            print(" ",end="")
        print("Time : " + str(shield),end="")
        for _ in range(9):
            print(" ",end="")
        print(" Score : " + str(coins),end="",flush=True) # 10
        #os.system('echo "\033[K"')
        return 0

    def gen_level(self,generate):
        '''Generating the course for playing'''
        A1 = Asset()
        if generate:
            A1.get_assets(self.frame)
        else:
            A1.spawn_floor(self.frame)
        return 0
