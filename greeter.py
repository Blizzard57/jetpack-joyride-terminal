
'''This module has greeter screens'''
import os

def get_start_screen():
    '''A Welcome Screen which has the greeting and also instrustions on how to run the game'''
    #matr = np.full((24,80),"")
    os.system('clear')
    matr = '''
    
                          _      _                    _    
                         | |    | |                  | |   
                         | | ___| |_ _ __   __ _  ___| | __
                     _   | |/ _ \\ __| '_ \\ / _` |/ __| |/ /
                    | |__| |  __/ |_| |_) | (_| | (__|   < 
                     \\____/ \\___|\\__| .__/ \\__,_|\\___|_|\\_\\
                                    | |                    
                                    |_|                    
                                  
                                  r to play
                                  q to quit
                          _                  _     _      
                         | |                (_)   | |     
                         | | ___  _   _ _ __ _  __| | ___ 
                     _   | |/ _ \\| | | | '__| |/ _` |/ _ \\
                    | |__| | (_) | |_| | |  | | (_| |  __/
                     \\____/ \\___/ \\__, |_|  |_|\\__,_|\\___|
                                   __/ |                  
                                  |___/                   


'''
    print(matr)

def get_end_screen():
    '''Screen displayed when player loses all the lives'''
    os.system('clear')
    matr = '''


                             __     __         
                             \\ \\   / /         
                              \\ \\_/ /__  _   _ 
                               \\   / _ \\| | | |
                                | | (_) | |_| |
                                |_|\\___/ \\__,_|
                                               

                                  r to play
                                  q to quit
                              _               _   
                             | |             | |  
                             | |     ___  ___| |_ 
                             | |    / _ \\/ __| __|
                             | |___| (_) \\__ \\ |_ 
                             |______\\___/|___/\\__|



             
'''
    print(matr)

def won_screen():
    '''Screen displayed when won'''
    os.system('clear')
    matr = '''


                             __     __         
                             \\ \\   / /         
                              \\ \\_/ /__  _   _ 
                               \\   / _ \\| | | |
                                | | (_) | |_| |
                                |_|\\___/ \\__,_|
                                               

                                 
                                 
                             
                            __          __         
                            \\ \\        / /         
                             \\ \\  /\\  / /__  _ __  
                              \\ \\/  \\/ / _ \\| '_ \\ 
                               \\  /\\  / (_) | | | |
                                \\/  \\/ \\___/|_| |_|


             
'''
    print(matr)