from Player import Player
from Bot import Bot
from Errors import *
import os
import random

class Game:

    def __init__(self):
        """
        function sets basic settings
        """
        self.winner = None
        self.board = [[1,2,3],[4,5,6],[7,8,9]]
        self.quit = False

    def run(self):
        """
        game's main menu
        """
        while not self.quit:
            os.system('cls')
            print('1.Singleplayer')
            print('2.Multiplayer')
            print('3.Exit')

            choice = input()

            if choice == '1':
                self.singleplayer()
            elif choice == '2':
                self.multiplayer()
            elif choice == '3':
                quit()


    def singleplayer(self):
        """
        function provides the game
        between player and bot
        """
        while True:
            os.system('cls')
            print('Enter the level of difficulty:')

            print('1.Easy')
            print('2.Medium')
            print('3.Hard')
            print('4.Exit')

            choice = int(input())

            if choice == 1:
                bot = Bot('O','easy')
            elif choice == 2:
                bot = Bot('O','medium')
            elif choice == 3:
                bot = Bot('O','hard')
            elif choice == 4:
                break

                
            turn = 1
            name = input("\nEnter your name: ")
            player = Player(name,'X')
            os.system('cls')

            while not self.check_win() and turn < 10:
                self.draw_board()
                if turn%2==1:
                    print("{}, your turn!".format(player.name))
                    move = player.get_move()
                    if self.is_available(move):
                        for row in self.board:
                            if move in row:
                                row[row.index(move)] = player.notation
                                turn+=1
                                continue
                else:
                    move = bot.make_move(self.board)
                    print(move) 
                    self.board[move[0]][move[1]] = bot.notation
                    turn+=1
                    
                os.system('cls')
            if self.check_win():
                self.winner = bot if turn%2==1 else player
            self.show_result()





    def multiplayer(self):
        """
        function provides the game
        rejime with 2 players
        """
        print('Enter the name of 1 player: ')
        name = input()
        player1 = Player(name,'X')
        print('Enter the name of 2 player: ')
        name = input()
        player2 = Player(name,'O')

        turn = 1
        os.system('cls')
        while not self.check_win() and turn < 10:
            self.draw_board()
            if turn % 2 == 1:
                print('{}, your turn!'.format(player1.name))
                move = player1.get_move()
                notation = player1.notation
            elif turn % 2 == 0:
                print('{}, your turn!'.format(player2.name))
                move = player2.get_move()
                notation = player2.notation
            
            os.system('cls')

            if self.is_available(move):
                for row in self.board:
                    if move in row:
                        row[row.index(move)] = notation
                turn+=1
            else:
                print('This field is already taken!\n')
        
        if self.check_win():
            self.winner = player2 if turn%2==1 else player1
        self.show_result()

        


            

    def check_win(self):
        """
        the function checks the board
        return False - if no one won yet
        return True - if one of the players won
        """
        # check horizontal lines
        for row in self.board:
            if len(set(row)) == 1:
                return True
        
        # check vertical lines
        column = set()
        for i in range(3):
            for j in self.board:
                column.add(j[i])
            if len(column) == 1:
                return True
            else:
                column.clear()
        # check 1 diagonal
        diagonal = {j[i] for i,j in enumerate(self.board)}
        if len(diagonal) == 1:
            return True
        
        # check 2 diagonal
        diagonal = {j[i] for i,j in enumerate(reversed(self.board))}
        if len(diagonal) == 1:
            return True
        
        return False


    def draw_board(self):
        """
        the function draws the board
        """
        ceil = ' --- --- ---'
        bar = '| {} | {} | {} |'

        for row in self.board:
            print(ceil)
            print(bar.format(row[0],row[1],row[2]))
        print(ceil)


    def is_available(self,field):
        """
        param field: certain value('X','O', or number(1-9))
        returns True if the given field exists
        returns False if there's no field with given value
        """
        for row in self.board:
            if field in row:
                return True
        return False

    def clear_settings(self):
        """
        function clears game settings
        """
        self.winner = None
        self.board = [[1,2,3],[4,5,6],[7,8,9]]
        self.quit = False

    def show_result(self):
        """
        shows the result of game and displays the board:
        who won
        """
        self.quit = True
        self.draw_board()
        if self.winner:
            print('{} won!\n'.format(self.winner.name))
        else:
            print('DRAW!\n')
        input("\nEnter any symbol to continue")
        self.clear_settings()
        