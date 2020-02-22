class Bullet:
    '''This module generates and checks the mario's movement and its position'''
    def __init__(self,x,y,direction = 'F'):
        '''Defining position and looks of Marios'''
        # Coordinates of Mario
        self.x = x
        self.y = y
        self.dir = direction
        
    def give_location(self,level,frame_no):
        '''Assigns position of mario in the level'''
        #if self.collision(level, frame_no):
        # Checking for colision with various objects
        if self.y < 1:
            return 0
        if self.y + frame_no > 999 or self.y > 79:
            return 0
        #if level[self.x,self.y + frame_no] == '*':
        #    return 1
        elif self.y + frame_no > frame_no + 100 or self.y + frame_no > 1000 or self.y > 79:
            return 2
        if self.dir == 'F':
            level[self.x,self.y + frame_no] = 'o'
        else:
            level[self.x,self.y + frame_no] = '0'
        return 0
        
    def change_location(self):
        #termios.tcflush(sys.stdin, termios.TCIOFLUSH)
        #getch = _Getch()
        if self.dir == 'F':
            self.y = self.y + 2
        elif self.dir == 'B':
            self.y = self.y - 2

    def reset_location(self,level,frame_no):
        if self.y + frame_no > 999 or self.y > 79 or self.y < 1:
            return 0
        level[self.x,self.y + frame_no] = ' '
        return 0