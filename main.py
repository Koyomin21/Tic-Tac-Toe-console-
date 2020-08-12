import os
import random
from Game import *


clear = lambda: os.system('cls')

def main():

    clear()
    game = Game()
    game.run()



if __name__ == '__main__':
    main()
    