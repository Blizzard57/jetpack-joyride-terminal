'''This module has all the assets which can be imported in the game and can be interacted with'''
import os
import numpy as np
import math
import colorama
from checkInp import getch
import termios
import time

colorama.init()

def prob(percentage):
    '''A probabilistic model which if returns true spawns a sprite, else does nothing'''
    x = np.random.random()
    return x*100 < percentage 

class Asset:
    '''This loads all the interacting assets'''
    
    def spawn_floor(self,level):
        '''Getting the floor'''
        level[22:23, :] = "="
        return
    
    def spawn_firebar(self,level,percentage = 5):
        '''Getting a firebar'''
        #Getting a horizontal fireball
        for i in range(22):
            if prob(percentage):
                # Max Value = y_len - 5
                y_axis = abs(math.floor(np.random.random() * len(level[0])) - 5)
                # Can increase by 5 ==> Max = y_len
                for j in range(math.floor(np.random.random() * 3 + 2)):
                    level[i,y_axis + j] = "*"
        #Generating Vertical fireball
        for i in range(len(level[0])):
            if prob(percentage):
                x_axis = abs(math.floor(np.random.random() * 22) - 5)
                for j in range(math.floor(np.random.random() * 3 + 2)):
                    level[x_axis + j,i] = "*"
        #Generating 45 firebar
        for i in range(17):
            if prob(percentage):
                y_axis = abs(math.floor(np.random.random() * len(level[0])) - 5)
                for j in range(math.floor(np.random.random() * 5 + 2)):
                    if level[i + j,y_axis + j] == " ":
                        level[i + j,y_axis + j] = "*"
        
        return
    
    def spawn_coins(self,level, percentage = 50):
       '''Somehow spawning coins'''
       # Grouped Coins ==> Very high probability apparently
       for i in range(18): # Should not appear down
           if prob(percentage):
                y_axis = abs(math.floor(np.random.random() * len(level[0])) - 5)
                size_box = math.floor(np.random.random() *3)
                level[i:i+size_box,y_axis:y_axis + size_box] = "$"
       return

    def powerup(self, level, percentage = 5):
        '''Random placement of powerups, which upgrades the player'''
        for i in range(10):
            if prob(percentage):
                y_axis = abs(math.floor(np.random.random() * len(level[0])) - 5)
                size_box = 3
                level[i:i+size_box,y_axis:y_axis + size_box] = "p"
        return

    def get_assets(self,level):
        '''The function used to get assets to the render engine'''
        self.spawn_floor(level)
        self.spawn_firebar(level)
        self.spawn_coins(level)
        self.powerup(level)
        return
    