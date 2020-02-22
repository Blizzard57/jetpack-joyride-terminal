from mario import Mario
import numpy as np

class Boss(Mario):
    def __init__(self):
        self.life = 10
        Mario.__init__(self,10,79)

    def get_life(self):
        return self.life

    def give_location(self,level):
        level[self.x - 5,self.y - 8] = ' '
        level[self.x - 5,self.y - 7] = ' '
        level[self.x - 5,self.y - 6] = '|'
        level[self.x - 5,self.y - 5] = '/'
        level[self.x - 5,self.y - 4] = '_'
        level[self.x - 5,self.y - 3] = '\\'
        level[self.x - 5,self.y - 2] = '|'
        level[self.x - 5,self.y - 1] = ' '
        level[self.x - 5,self.y] = ' '

        level[self.x - 4,self.y - 8] = '='
        level[self.x - 4,self.y - 7] = ')'
        level[self.x - 4,self.y - 6] = ' '
        level[self.x - 4,self.y - 5] = '0'
        level[self.x - 4,self.y - 4] = ' '
        level[self.x - 4,self.y - 3] = '0'
        level[self.x - 4,self.y - 2] = ' '
        level[self.x - 4,self.y - 1] = '('
        level[self.x - 4,self.y] = '='

        level[self.x - 3,self.y - 8] = ' '
        level[self.x - 3,self.y - 7] = '/'
        level[self.x - 3,self.y - 6] = '\\'
        level[self.x - 3,self.y - 5] = ' '
        level[self.x - 3,self.y - 4] = '"'
        level[self.x - 3,self.y - 3] = ' '
        level[self.x - 3,self.y - 2] = '/'
        level[self.x - 3,self.y - 1] = '\\'
        level[self.x - 3,self.y] = ' '

        level[self.x - 2,self.y - 8] = '|'
        level[self.x - 2,self.y - 7] = ' '
        level[self.x - 2,self.y - 6] = '|'
        level[self.x - 2,self.y - 5] = '\\'
        level[self.x - 2,self.y - 4] = '_'
        level[self.x - 2,self.y - 3] = '/'
        level[self.x - 2,self.y - 2] = '|'
        level[self.x - 2,self.y - 1] = ' '
        level[self.x - 2,self.y] = '|'

        level[self.x - 1,self.y - 8] = '\\'
        level[self.x - 1,self.y - 7] = '_'
        level[self.x - 1,self.y - 6] = '>'
        level[self.x - 1,self.y - 5] = '-'
        level[self.x - 1,self.y - 4] = '-'
        level[self.x - 1,self.y - 3] = '-'
        level[self.x - 1,self.y - 2] = '<'
        level[self.x - 1,self.y - 1] = '_'
        level[self.x - 1,self.y] = '/'

        level[self.x,self.y - 8] = '('
        level[self.x,self.y - 7] = '_'
        level[self.x,self.y - 6] = '_'
        level[self.x,self.y - 5] = '_'
        level[self.x,self.y - 4] = '|'
        level[self.x,self.y - 3] = '_'
        level[self.x,self.y - 2] = '_'
        level[self.x,self.y - 1] = '_'
        level[self.x,self.y] = ')'

        #Checking for collision
        if np.isin('o',level[self.x-7:self.x,self.y - 10 : self.y]):
            self.life = self.life - 1


    def change_location(self,x):
        print(x,self.x)
        if self.x > x:
            if self.x - 2 > 5:
                self.x = self.x - 2
        elif self.x < x:
            if self.x + 2 < 23:
                self.x = self.x + 2
            if self.x + 2 == 21:
                self.x = 21
        
    def reset_location(self, level):
        level[self.x - 5,self.y - 8] = ' '
        level[self.x - 5,self.y - 7] = ' '
        level[self.x - 5,self.y - 6] = ' '
        level[self.x - 5,self.y - 5] = ' '
        level[self.x - 5,self.y - 4] = ' '
        level[self.x - 5,self.y - 3] = ' '
        level[self.x - 5,self.y - 2] = ' '
        level[self.x - 5,self.y - 1] = ' '
        level[self.x - 5,self.y] = ' '

        level[self.x - 4,self.y - 8] = ' '
        level[self.x - 4,self.y - 7] = ' '
        level[self.x - 4,self.y - 6] = ' '
        level[self.x - 4,self.y - 5] = ' '
        level[self.x - 4,self.y - 4] = ' '
        level[self.x - 4,self.y - 3] = ' '
        level[self.x - 4,self.y - 2] = ' '
        level[self.x - 4,self.y - 1] = ' '
        level[self.x - 4,self.y] = ' '

        level[self.x - 3,self.y - 8] = ' '
        level[self.x - 3,self.y - 7] = ' '
        level[self.x - 3,self.y - 6] = ' '
        level[self.x - 3,self.y - 5] = ' '
        level[self.x - 3,self.y - 4] = ' '
        level[self.x - 3,self.y - 3] = ' '
        level[self.x - 3,self.y - 2] = ' '
        level[self.x - 3,self.y - 1] = ' '
        level[self.x - 3,self.y] = ' '

        level[self.x - 2,self.y - 8] = ''
        level[self.x - 2,self.y - 7] = ''
        level[self.x - 2,self.y - 6] = ''
        level[self.x - 2,self.y - 5] = ' '
        level[self.x - 2,self.y - 4] = ''
        level[self.x - 2,self.y - 3] = ''
        level[self.x - 2,self.y - 2] = ''
        level[self.x - 2,self.y - 1] = ''
        level[self.x - 2,self.y] = ' '

        level[self.x - 1,self.y - 8] = ' '
        level[self.x - 1,self.y - 7] = ''
        level[self.x - 1,self.y - 6] = ''
        level[self.x - 1,self.y - 5] = ''
        level[self.x - 1,self.y - 4] = ''
        level[self.x - 1,self.y - 3] = ''
        level[self.x - 1,self.y - 2] = ''
        level[self.x - 1,self.y - 1] = ''
        level[self.x - 1,self.y] = ' '

        level[self.x,self.y - 8] = ' '
        level[self.x,self.y - 7] = ''
        level[self.x,self.y - 6] = ''
        level[self.x,self.y - 5] = ''
        level[self.x,self.y - 4] = ''
        level[self.x,self.y - 3] = ''
        level[self.x,self.y - 2] = ''
        level[self.x,self.y - 1] = ''
        level[self.x,self.y] = ' '
