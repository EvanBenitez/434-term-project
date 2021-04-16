
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 13:10:18 2021
@author: Group 1
"""
import pygame
import random

objects = {}  # dictionary for storying clickable items


# Class element for the Board component
class Board:
    # create grid and initialize with 'B' for blank
    def __init__(self):
        self.grid = [['B', 'B', 'B'], \
                     ['B', 'B', 'B'], \
                     ['B', 'B', 'B']]

    # place X or O on board
    def place(self, row, col, marker):
        if type(row) is int and type(col) is int and 0 <= row < 3 and 0 <= col < 3:
            if marker.upper() == 'X' or marker.upper() == 'O':
                self.grid[row][col] = marker.upper()
            else:
                raise ValueError("Must input either 'X' or 'O'")
        else:
            raise ValueError("Row and Column must be between 0 and 2 inclusive")

    # remove a marker
    # this is untested
    def remove(self, row, col):
        if type(row) is int and type(col) is int and 0 <= row < 3 and 0 <= col < 3:
            self.grid[row][col] = 'B'
        else:
            print("invalid grid location; no action taken")

    # Print board, for debuging puposes
    def print_board(self):
        for row in self.grid:
            for col in row:
                print(col + " ", end="")
            print()


# Computer Player
class Computer_Player:

    # easy
    # pick a spot in the grid at random until there is an empty spot
    def easy(board, comp_char):
        turn = True
        while (turn == True):
            i = random.randrange(0, 3)
            j = random.randrange(0, 3)
            if board.grid[i][j] == 'B':
                #board.grid[i][j] = comp_char
                turn = False
                return (i, j)

    # hard
    def hard(board, comp_char):
        
         # get user_char
        user_char = ''
        if comp_char == 'X':
            user_char = 'O'
        else:
            user_char = 'X'
            
        # computer to check if it can win, if can win, wins
        if board.grid[0][0] == comp_char and board.grid[0][2] == comp_char and board.grid[0][1] == 'B':
            #board.grid[0][1] = comp_char
            return (0, 1)
        elif board.grid[1][0] == comp_char and board.grid[1][2] == comp_char and board.grid[1][1] == 'B':
            ##board.grid[2][1] = comp_char
            return (2, 1)
        elif board.grid[0][0] == comp_char and board.grid[0][1] == comp_char and board.grid[0][2] == 'B':
            board.grid[0][2] = comp_char
            return (0, 2)
        elif board.grid[1][0] == comp_char and board.grid[1][1] == comp_char and board.grid[1][2] == 'B':
            #board.grid[1][2] = comp_char
            return (1, 2)
        elif board.grid[2][0] == comp_char and board.grid[2][1] == comp_char and board.grid[2][2] == 'B':
            #board.grid[2][2] = comp_char
            return (2, 2)
        elif board.grid[0][1] == comp_char and board.grid[0][2] == comp_char and board.grid[0][0] == 'B':
            #board.grid[0][0] = comp_char
            return (0, 0)
        elif board.grid[1][1] == comp_char and board.grid[1][2] == comp_char and board.grid[1][0] == 'B':
            #board.grid[1][0] = comp_char
            return (1, 0)
        elif board.grid[2][1] == comp_char and board.grid[2][2] == comp_char and board.grid[2][0] == 'B':
            #board.grid[2][0] = comp_char
            return (2, 0)
        elif board.grid[1][1] == comp_char and board.grid[0][0] == comp_char and board.grid[2][2] == 'B':
            #board.grid[2][2] = comp_char
            return (2, 2)
        elif board.grid[1][1] == comp_char and board.grid[0][1] == comp_char and board.grid[2][1] == 'B':
            return (2, 1)
        elif board.grid[1][1] == comp_char and board.grid[2][1] == comp_char and board.grid[0][1] == 'B':
            return (0, 1)
        elif board.grid[1][1] == comp_char and board.grid[2][2] == comp_char and board.grid[0][0] == 'B':
            #board.grid[0][0] = comp_char
            return (0, 0)
        elif board.grid[1][1] == comp_char and board.grid[0][2] == comp_char and board.grid[2][0] == 'B':
            #board.grid[2][0] = comp_char
            return (2, 0)
        elif board.grid[1][1] == comp_char and board.grid[2][0] == comp_char and board.grid[0][2] == 'B':
            #board.grid[0][2] = comp_char
            return (0, 2)
        elif board.grid[0][0] == comp_char and board.grid[2][2] == comp_char and board.grid[1][1] == 'B':
            #board.grid[1][1] = comp_char
            return (1, 1)
        elif board.grid[0][2] == comp_char and board.grid[2][0] == comp_char and board.grid[1][1] == 'B':
            #board.grid[1][1] = comp_char
            return (1, 1)
        elif board.grid[0][0] == comp_char and board.grid[2][0] == comp_char and board.grid[1][0] == 'B':
            #board.grid[1][1] = comp_char
            return (1, 0)
        elif board.grid[0][1] == comp_char and board.grid[2][1] == comp_char and board.grid[1][1] == 'B':
            #board.grid[1][1] = comp_char
            return (1, 1)
        elif board.grid[0][2] == comp_char and board.grid[2][2] == comp_char and board.grid[1][2] == 'B':
            #board.grid[1][2] = comp_char
            return (1, 2)
        elif board.grid[0][2] == comp_char and board.grid[1][2] == comp_char and board.grid[2][2] == 'B':
            return (2, 2)

        # computer to check if user can win, if can win, blocks user
        elif board.grid[0][0] == user_char and board.grid[0][2] == user_char and board.grid[0][1] == 'B':
            #board.grid[0][1] = comp_char
            return (0, 1)
        elif board.grid[1][0] == user_char and board.grid[1][2] == user_char and board.grid[1][1] == 'B':
            #board.grid[1][1] = comp_char
            return (1, 1)
        elif board.grid[2][0] == user_char and board.grid[2][2] == user_char and board.grid[2][1] == 'B':
            #board.grid[2][1] = comp_char
            return (2, 1)
        elif board.grid[0][0] == user_char and board.grid[0][1] == user_char and board.grid[0][2] == 'B':
            #board.grid[0][2] = comp_char
            return (0, 2)
        elif board.grid[1][0] == user_char and board.grid[1][1] == user_char and board.grid[1][2] == 'B':
            #board.grid[1][2] = comp_char
            return (1, 2)
        elif board.grid[2][0] == user_char and board.grid[2][1] == user_char and board.grid[2][2] == 'B':
           #board.grid[2][2] = comp_char
            return (2, 2)
        elif board.grid[0][1] == user_char and board.grid[0][2] == user_char and board.grid[0][0] == 'B':
            #board.grid[0][0] = comp_char
            return (0, 0)
        elif board.grid[1][1] == user_char and board.grid[1][2] == user_char and board.grid[1][0] == 'B':
            #board.grid[1][0] = comp_char
            return (1, 0)
        elif board.grid[2][1] == user_char and board.grid[2][2] == user_char and board.grid[2][0] == 'B':
            #board.grid[2][0] = comp_char
            return (2, 0)
        elif board.grid[1][1] == user_char and board.grid[0][0] == user_char and board.grid[2][2] == 'B':
            #board.grid[2][2] = comp_char
            return (2, 2)
        elif board.grid[1][1] == user_char and board.grid[2][2] == user_char and board.grid[0][0] == 'B':
            #board.grid[0][0] = comp_char
            return (0, 0)
        elif board.grid[1][1] == user_char and board.grid[0][1] == user_char and board.grid[2][1] == 'B':
            return (2, 1)
        elif board.grid[1][1] == user_char and board.grid[2][1] == user_char and board.grid[0][1] == 'B':
            return (0, 1)
        elif board.grid[1][1] == user_char and board.grid[0][2] == user_char and board.grid[2][0] == 'B':
            #board.grid[2][0] = comp_char
            return (2, 0)
        elif board.grid[1][1] == user_char and board.grid[2][0] == user_char and board.grid[0][2] == 'B':
            #board.grid[0][2] = comp_char
            return (0, 2)
        elif board.grid[0][0] == user_char and board.grid[2][2] == user_char and board.grid[1][1] == 'B':
            #board.grid[1][1] = comp_char
            return (1, 1)
        elif board.grid[0][2] == user_char and board.grid[2][0] == user_char and board.grid[1][1] == 'B':
            #board.grid[1][1] = comp_char
            return (1, 1)
        elif board.grid[0][0] == user_char and board.grid[2][0] == user_char and board.grid[1][0] == 'B':
           # board.grid[1][1] = comp_char
            return (1, 0)
        elif board.grid[0][1] == user_char and board.grid[2][1] == user_char and board.grid[1][1] == 'B':
            #board.grid[1][1] = comp_char
            return (1, 1)
        elif board.grid[0][2] == user_char and board.grid[2][2] == user_char and board.grid[1][2] == 'B':
            #board.grid[1][2] = comp_char
            return (1, 2)
        elif board.grid[0][2] == user_char and board.grid[1][2] == user_char and board.grid[2][2] == 'B':
            return (2, 2)

        # computer to make a non winning or blocking move

        elif board.grid[1][1] == 'B' and board.grid[0][0] == user_char:
            #board.grid[1][1] == comp_char
            return (1, 1)
        elif board.grid[1][1] == 'B' and board.grid[2][0] == user_char:
            #board.grid[1][1] == comp_char
            return (1, 1)
        elif board.grid[1][1] == 'B' and board.grid[2][2] == user_char:
            #board.grid[1][1] == comp_char
            return (1, 1)
        elif board.grid[1][1] == 'B' and board.grid[0][2] == user_char:
            #board.grid[1][1] == comp_char
            return (1, 1)
        elif board.grid[0][0] == 'B'and board.grid[0][2] == 'B' and board.grid[2][2] == 'B' and board.grid[2][0] == 'B':
            #board.grid[0][0] = comp_char
            return (0, 0)        
        elif board.grid[1][1] == 'B':
           # board.grid[1][1] = comp_char
            return (1, 1)
        elif board.grid[0][2] == 'B':
            #board.grid[0][2] = comp_char
            return (0, 2)
        elif board.grid[2][2] == 'B':
           # board.grid[2][2] = comp_char
            return (2, 2)
        elif board.grid[2][0] == 'B':
            #board.grid[2][0] = comp_char
            return (2, 0)
        elif board.grid[0][1] == 'B':
            #board.grid[0][1] = comp_char
            return (0, 1)
        elif board.grid[1][0] == 'B':
            #board.grid[1][0] = comp_char
            return (1, 0)
        elif board.grid[2][1] == 'B':
           # board.grid[2][1] = comp_char
            return (2, 1)
        elif board.grid[1][2] == 'B':
            #board.grid[1][2] = comp_char
            return (1, 2)

        # class element for Game element


class Game:

    def __init__(self):
        self.xWinsCount = 0
        self.oWinsCount = 0
        self.B = Board()
        self.currentWinner = 'N'
        self.xCounter = 0
        self.oCounter = 0
        self.turn = 'X'
        self.postCoordinates = []
        self.matchState = 'N'

    def winTracker(self):

        xwin = False
        owin = False
        # top row X
        if self.B.grid[0][0] == 'X' and self.B.grid[0][1] == 'X' and self.B.grid[0][2] == 'X':
            xwin = True

        # middle row X
        elif self.B.grid[1][0] == 'X' and self.B.grid[1][1] == 'X' and self.B.grid[1][2] == 'X':
            xwin = True

        # self.bottom row X
        elif self.B.grid[2][0] == 'X' and self.B.grid[2][1] == 'X' and self.B.grid[2][2] == 'X':
            xwin = True

        # left column X
        elif self.B.grid[0][0] == 'X' and self.B.grid[1][0] == 'X' and self.B.grid[2][0] == 'X':
            xwin = True

        # middle column X
        elif self.B.grid[0][1] == 'X' and self.B.grid[1][1] == 'X' and self.B.grid[2][1] == 'X':
            xwin = True

        # right column X
        elif self.B.grid[0][2] == 'X' and self.B.grid[1][2] == 'X' and self.B.grid[2][2] == 'X':
            xwin = True

        # top left to bottom right diagonal X
        elif self.B.grid[0][0] == 'X' and self.B.grid[1][1] == 'X' and self.B.grid[2][2] == 'X':
            xwin = True

        # top right to bottom left diagonal X
        elif self.B.grid[0][2] == 'X' and self.B.grid[1][1] == 'X' and self.B.grid[2][0] == 'X':
            xwin = True

        # top row O
        elif self.B.grid[0][0] == 'O' and self.B.grid[0][1] == 'O' and self.B.grid[0][2] == 'O':
            owin = True

        # middle row O
        elif self.B.grid[1][0] == 'O' and self.B.grid[1][1] == 'O' and self.B.grid[1][2] == 'O':
            owin = True

        # self.bottom row O
        elif self.B.grid[2][0] == 'O' and self.B.grid[2][1] == 'O' and self.B.grid[2][2] == 'O':
            owin = True

        # left column O
        elif self.B.grid[0][0] == 'O' and self.B.grid[1][0] == 'O' and self.B.grid[2][0] == 'O':
            owin = True

        # middle column O
        elif self.B.grid[0][1] == 'O' and self.B.grid[1][1] == 'O' and self.B.grid[2][1] == 'O':
            owin = True

        # right column O
        elif self.B.grid[0][2] == 'O' and self.B.grid[1][2] == 'O' and self.B.grid[2][2] == 'O':
            owin = True

        # top left to bottom right diagonal 0
        elif self.B.grid[0][0] == 'O' and self.B.grid[1][1] == 'O' and self.B.grid[2][2] == 'O':
            owin = True

        # top right to bottom left diagonal 0
        elif self.B.grid[0][2] == 'O' and self.B.grid[1][1] == 'O' and self.B.grid[2][0] == 'O':
            owin = True

        if owin is True:
            print("Hey now!")
            self.oWinsCount += 1
            self.matchState = 'O'
            self.winComparator()

        if xwin is True:
            print("Win!")
            self.xWinsCount += 1
            self.matchState = 'X'
            self.winComparator()
            

    def turnTracker(self):
        xCounter = oCounter = 0
        
        for i in self.B.grid:
            for j in i:
                if j == 'X':
                    xCounter += 1
                elif j == 'O':
                    oCounter += 1
        if xCounter + oCounter >= 9:
            self.matchState = 'D'

        if xCounter <oCounter:
            self.turn = 'X'

        elif oCounter < xCounter:
            self.turn = 'O'

        elif oCounter == xCounter:
            if self.turn == 'O':
                self.turn = 'X'
            elif self.turn == 'X':
                self.turn = 'O'

    def winComparator(self):

        if self.xWinsCount < self.oWinsCount:
            self.currentWinner = 'O'

        elif self.xWinsCount > self.oWinsCount:
            self.currentWinner = 'X'

        elif self.xWinsCount == 0 and self.oWinsCount == 0:
            self.currentWinner = 'N'

        elif self.xWinsCount == self.oWinsCount:
            self.currentWinner = 'D'

    def place(self, row, col):
        if self.B.grid[row][col] != 'B':
            return False
        if self.turn == 'X':
            self.B.place(row, col, "X")
            self.turnTracker()
            self.winTracker()
        elif self.turn == 'O':
            self.B.place(row, col, "O")
            self.turnTracker()
            self.winTracker()
        return True

    def reprint(self):
        self.B.grid = [['B', 'B', 'B'], \
                       ['B', 'B', 'B'], \
                       ['B', 'B', 'B']]
        self.xCounter = 0
        self.oCounter = 0
        self.turn = 'X'
        self.matchState = 'N'


# contols the graphical content of the game
class GUI:
    # initialize
    def __init__(self):
        # set flags to False
        self.menu = False
        self.board = False
        self.size = (750, 500)  # dimensions of the window
        self.background = (240, 240, 240)  # background color of the window

        # set colors
        self.line_color = (0, 0, 0)  # color of button outline and text
        self.light_text = (180, 180, 180)  # color for grayed options
        self.draw_color = (0, 0, 0)  # color of shapes and text

        # create text images
        # create text for game button
        font = pygame.font.SysFont(None, 24)
        self.label_font = pygame.font.SysFont(None, 50)
        self.game_text = font.render('Game', True, self.draw_color)
        self.game_text_location = (38, 35)

        # create text for X label
        self.text_X = self.label_font.render('X', True, self.draw_color)
        self.text_X_location = (250, 25)

        # create text for Y label
        self.text_O = self.label_font.render('O', True, self.draw_color)
        self.text_O_location = (500, 25)

        # create menu options labels
        self.NewGame = font.render('New game', True, self.line_color)
        self.Best = font.render('Best:', True, self.line_color)
        self.of1 = font.render('1 of 1', True, self.line_color)
        self.of3 = font.render('2 of 3', True, self.line_color)
        self.of5 = font.render('3 of 5', True, self.line_color)
        self.of7 = font.render('4 of 7', True, self.line_color)
        self.playervplayer = font.render('Player vs. Player', True, self.line_color)
        self.playervpc = font.render('Player vs. PC', True, self.line_color)
        # two set of difficulty labels one darker and one lighter
        self.difficultyLabel = font.render('Difficulty:', True, self.line_color)
        self.easyLabel = font.render('Easy', True, self.line_color)
        self.hardLabel = font.render('Hard', True, self.line_color)
        self.pcLabel = font.render('Computer Character:', True, self.line_color)
        self.XLabel = font.render('X', True, self.line_color)
        self.OLabel = font.render('O', True, self.line_color)
        # lighter color
        self.light_difficultyLabel = font.render('Difficulty:', True, self.light_text)
        self.light_easyLabel = font.render('Easy', True, self.light_text)
        self.light_hardLabel = font.render('Hard', True, self.light_text)
        self.light_pc = font.render('Computer Character:', True, self.light_text)

        self.quitLabel = font.render('Quit!', True, self.line_color)

        # menu label dimensions
        self.menu_option_hor = 200
        self.menu_option_vert = 20

        # menu configurations
        self.loc_menu = (12, 65)
        self.menu_color = (220, 220, 220)
        self.main_menu = pygame.Rect(self.loc_menu[0], self.loc_menu[1], self.menu_option_hor,
                                     300)  # attributes of main menu

        # menu label location (interactive)
        self.loc_newgame = (self.loc_menu[0] + 58, self.loc_menu[1] + 6)
        self.loc_of1 = (self.loc_menu[0] + 13, self.loc_menu[1] + 50)
        self.loc_of3 = (self.loc_menu[0] + 13, self.loc_menu[1] + 70)
        self.loc_of5 = (self.loc_menu[0] + 13, self.loc_menu[1] + 90)
        self.loc_of7 = (self.loc_menu[0] + 13, self.loc_menu[1] + 110)
        self.loc_playervsplayer = (self.loc_menu[0] + 23, self.loc_menu[1] + 140)
        self.loc_playervspc = (self.loc_menu[0] + 23, self.loc_menu[1] + 167)
        self.loc_easy = (self.loc_menu[0] + 7, self.loc_menu[1] + 217)
        self.loc_hard = (self.loc_menu[0] + 7, self.loc_menu[1] + 235)
        self.loc_pc = (self.loc_menu[0] + 3, self.loc_menu[1] + 253)
        self.loc_XO = (self.loc_menu[0] + 180, self.loc_menu[1] + 253)
        self.loc_quit = (self.loc_menu[0] + 78, self.loc_menu[1] + 275)

        # menu label location (non-interactive)
        self.loc_best = (self.loc_menu[0] + 3, self.loc_menu[1] + 30)
        self.loc_diff = (self.loc_menu[0] + 3, self.loc_menu[1] + 200)
        self.loc_line1 = ((self.loc_menu[0], self.loc_menu[1] + 27), (self.loc_menu[0] + 198, self.loc_menu[1] + 27))
        self.loc_line2 = ((self.loc_menu[0], self.loc_menu[1] + 135), (self.loc_menu[0] + 198, self.loc_menu[1] + 135))
        self.loc_line3 = ((self.loc_menu[0], self.loc_menu[1] + 161), (self.loc_menu[0] + 198, self.loc_menu[1] + 161))
        self.loc_line4 = ((self.loc_menu[0], self.loc_menu[1] + 189), (self.loc_menu[0] + 198, self.loc_menu[1] + 189))
        self.loc_line5 = ((self.loc_menu[0], self.loc_menu[1] + 270), (self.loc_menu[0] + 198, self.loc_menu[1] + 270))

        # add GUI interactable items in dictionary
        self.objects = {}  # dictionary for storying clickable items
        self.objects["game_button"] = (pygame.Rect(25, 25, 75, 35), 0)  # attributes of the game button

        # menu attributes
        self.objects["new"] = (
            pygame.Rect(self.loc_menu[0], self.loc_newgame[1], self.menu_option_hor, self.menu_option_vert), 1)
        self.objects["1of1"] = (
            pygame.Rect(self.loc_menu[0], self.loc_of1[1], self.menu_option_hor, self.menu_option_vert), 1)
        self.objects["2of3"] = (
            pygame.Rect(self.loc_menu[0], self.loc_of3[1], self.menu_option_hor, self.menu_option_vert), 1)
        self.objects["3of5"] = (
            pygame.Rect(self.loc_menu[0], self.loc_of5[1], self.menu_option_hor, self.menu_option_vert), 1)
        self.objects["4of7"] = (
            pygame.Rect(self.loc_menu[0], self.loc_of7[1], self.menu_option_hor, self.menu_option_vert), 1)
        self.objects["pvp"] = (
            pygame.Rect(self.loc_menu[0], self.loc_playervsplayer[1], self.menu_option_hor, self.menu_option_vert), 1)
        self.objects["pvpc"] = (
            pygame.Rect(self.loc_menu[0], self.loc_playervspc[1], self.menu_option_hor, self.menu_option_vert), 1)
        self.objects["easy"] = (
            pygame.Rect(self.loc_menu[0], self.loc_easy[1], self.menu_option_hor, self.menu_option_vert), 1)
        self.objects["hard"] = (
            pygame.Rect(self.loc_menu[0], self.loc_hard[1], self.menu_option_hor, self.menu_option_vert), 1)
        self.objects["pc"] = (
            pygame.Rect(self.loc_menu[0], self.loc_pc[1], self.menu_option_hor, self.menu_option_vert), 1)
        self.objects["quit"] = (
            pygame.Rect(self.loc_menu[0], self.loc_quit[1], self.menu_option_hor, self.menu_option_vert), 1)

    # start the gui window
    def start_gui(self):
        # set title bar
        pygame.display.set_caption("Tic-Tac-Toe")

        # create a surface on the screen
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill(self.background)

        # draw stuff on screen
        pygame.draw.rect(self.screen, self.line_color, self.objects["game_button"][0], 1)
        self.screen.blit(self.game_text, self.game_text_location)
        pygame.display.flip()
        self.board = False
        self.menu = False

    # draws grid for the given board with win totals
    def draw_board_score(self, board, X_win, O_win):
        # clear the screen of menus
        self.start_gui()

        # constants
        line_level = 60
        thickness = 4

        # draw label line
        pygame.draw.line(self.screen, self.draw_color, (237, line_level), (285, line_level), thickness)
        pygame.draw.line(self.screen, self.draw_color, (488, line_level), (535, line_level), thickness)
        # win numbers
        self.text_Xwins = self.label_font.render(str(X_win), True, self.draw_color)
        self.text_Xwins_location = (250, 70)
        self.text_Ywins = self.label_font.render(str(O_win), True, self.draw_color)
        self.text_Ywins_location = (500, 70)

        # cover the last score
        pygame.draw.rect(self.screen, self.background, (250, 70, 50, 50))
        pygame.draw.rect(self.screen, self.background, (500, 70, 50, 50))

        # print X and O label
        self.screen.blit(self.text_X, self.text_X_location)
        self.screen.blit(self.text_O, self.text_O_location)
        self.screen.blit(self.text_Xwins, self.text_Xwins_location)
        self.screen.blit(self.text_Ywins, self.text_Ywins_location)

        self.draw_board(board)

    # draws grid for the given board
    def draw_board(self, board):
        # if menu flag is true clear the menu
        if self.menu is True:
            self.start_gui()

        # define some constants
        box_size = 100  # size of each grid spot
        thickness = 10  # thickness of board line
        length = 3 * box_size + 2 * thickness  # length of board line
        top_bound = 150  # bound of the top border
        left_bound = 225  # bound of the left border
        x_base = int(left_bound + box_size / 2)  # x coordinate marker starting position
        y_base = int(top_bound + box_size / 2)  # y coordinate marker starting position
        offset = box_size + thickness  # offset for markers
        char_bound = 35  # defines the size of markers
        char_thickness = 10
        box_correction = int(thickness / 2)

        # add board locations to objects dictionary
        # really should be in init, but it is too much work to move it
        self.objects["0,0"] = (pygame.Rect(left_bound, top_bound, box_size, box_size), 2)
        self.objects["0,1"] = (pygame.Rect(left_bound + box_size + thickness, top_bound, box_size, box_size), 2)
        self.objects["0,2"] = (pygame.Rect(left_bound + 2 * (box_size + thickness), top_bound, box_size, box_size), 2)

        self.objects["1,0"] = (pygame.Rect(left_bound, top_bound + box_size + thickness, box_size, box_size), 2)
        self.objects["1,1"] = (
            pygame.Rect(left_bound + box_size + thickness, top_bound + box_size + thickness, box_size, box_size), 2)
        self.objects["1,2"] = (
            pygame.Rect(left_bound + 2 * (box_size + thickness), top_bound + box_size + thickness, box_size, box_size),
            2)

        self.objects["2,0"] = (pygame.Rect(left_bound, top_bound + 2 * (box_size + thickness), box_size, box_size), 2)
        self.objects["2,1"] = (
            pygame.Rect(left_bound + box_size + thickness, top_bound + 2 * (box_size + thickness), box_size, box_size),
            2)
        self.objects["2,2"] = (
            pygame.Rect(left_bound + 2 * (box_size + thickness), top_bound + 2 * (box_size + thickness), box_size,
                        box_size), 2)

        # clear previous board
        pygame.draw.rect(self.screen, self.background, (left_bound, top_bound, length, length))

        # draw grid
        pygame.draw.rect(self.screen, self.draw_color, (left_bound, top_bound + box_size, length, thickness))
        pygame.draw.rect(self.screen, self.draw_color,
                         (left_bound, top_bound + 2 * box_size + thickness, length, thickness))
        pygame.draw.rect(self.screen, self.draw_color, (left_bound + box_size, top_bound, thickness, length))
        pygame.draw.rect(self.screen, self.draw_color,
                         (left_bound + 2 * box_size + thickness, top_bound, thickness, length))

        # set board flag
        self.board = True

        # print the markers
        for row in range(0, 3):
            for col in range(0, 3):
                if board.grid[row][col] == 'X':
                    # draw X
                    pygame.draw.line(self.screen, self.draw_color, \
                                     ((x_base - char_bound) + (offset * col), (y_base - char_bound) + (offset * row)), \
                                     ((x_base + char_bound) + (offset * col), (y_base + char_bound) + (offset * row)), \
                                     char_thickness)
                    pygame.draw.line(self.screen, self.draw_color, \
                                     ((x_base + char_bound) + (offset * col), (y_base - char_bound) + (offset * row)), \
                                     ((x_base - char_bound) + (offset * col), (y_base + char_bound) + (offset * row)), \
                                     char_thickness)
                elif board.grid[row][col] == 'O':
                    # draw O
                    pygame.draw.circle(self.screen, self.draw_color, \
                                       (x_base + (offset * col), y_base + (offset * row)), char_bound, char_thickness)
        # draw board
        pygame.display.flip()

    # returns the click on item
    def click_item(self, mouse_position):
        # check for mouse pos match in objects dic
        for item in self.objects:
            if self.objects[item][0].collidepoint(mouse_position):
                if self.menu is True and self.objects[item][1] == 1:
                    print(item)
                    return item
                elif self.board is True and self.objects[item][1] == 2:
                    print(item)
                    return item
                elif self.objects[item][1] == 0:
                    print(item)
                    return item

    # display menu
    # best_option to denote which best of option is selected either 1,2,3,4
    # pc_option to denote if pc_option is selected
    # diff to indicate pc difficulty 1 easy, 2 hard
    def show_menu(self, best_option=1, pc_option=False, diff=0, isX=False):

        if self.menu == False:
            pygame.draw.rect(self.screen, self.menu_color, self.main_menu)

            self.screen.blit(self.NewGame, self.loc_newgame)

            pygame.draw.line(self.screen, self.line_color, self.loc_line1[0], self.loc_line1[1])

            self.screen.blit(self.Best, self.loc_best)
            self.screen.blit(self.of1, self.loc_of1)
            self.screen.blit(self.of3, self.loc_of3)
            self.screen.blit(self.of5, self.loc_of5)
            self.screen.blit(self.of7, self.loc_of7)

            pygame.draw.line(self.screen, self.line_color, self.loc_line2[0], self.loc_line2[1])

            self.screen.blit(self.playervplayer, self.loc_playervsplayer)

            pygame.draw.line(self.screen, self.line_color, self.loc_line3[0], self.loc_line3[1])

            self.screen.blit(self.playervpc, self.loc_playervspc)

            pygame.draw.line(self.screen, self.line_color, self.loc_line4[0], self.loc_line4[1])

            # set difficulty options to appropriate shade and check proper box
            if pc_option is True:
                self.screen.blit(self.difficultyLabel, self.loc_diff)
                self.screen.blit(self.easyLabel, self.loc_easy)
                self.screen.blit(self.hardLabel, self.loc_hard)
                self.screen.blit(self.pcLabel, self.loc_pc)
                self.checkmark(self.loc_playervspc[0] + 160, self.loc_playervspc[1] + 12)
                if diff == 0:
                    self.checkmark(self.loc_easy[0] + 175, self.loc_easy[1] + 12)
                elif diff == 1:
                    self.checkmark(self.loc_hard[0] + 175, self.loc_hard[1] + 12)
                if isX == False:
                    self.screen.blit(self.OLabel, self.loc_XO)
                else:
                    self.screen.blit(self.XLabel, self.loc_XO)
            else:
                self.screen.blit(self.light_difficultyLabel, self.loc_diff)
                self.screen.blit(self.light_easyLabel, self.loc_easy)
                self.screen.blit(self.light_hardLabel, self.loc_hard)
                self.screen.blit(self.light_pc, self.loc_pc)
                self.checkmark(self.loc_playervsplayer[0] + 160, self.loc_playervsplayer[1] + 12)

            pygame.draw.line(self.screen, self.line_color, self.loc_line5[0], self.loc_line5[1])

            self.screen.blit(self.quitLabel, self.loc_quit)

            # check best of box
            if best_option == 1:
                self.checkmark(self.loc_of1[0] + 170, self.loc_of1[1] + 12)
            elif best_option == 2:
                self.checkmark(self.loc_of3[0] + 170, self.loc_of3[1] + 12)
            elif best_option == 3:
                self.checkmark(self.loc_of5[0] + 170, self.loc_of5[1] + 12)
            elif best_option == 4:
                self.checkmark(self.loc_of7[0] + 170, self.loc_of7[1] + 12)

            pygame.display.flip()
            self.menu = True
        else:
            pygame.draw.rect(self.screen, self.background, self.main_menu)
            pygame.display.flip()
            self.menu = False

    # auxilary function for placing checkmarks
    def checkmark(self, x, y):
        mark_size = 5
        thickness = 3
        pygame.draw.line(self.screen, self.line_color, (x - mark_size, y - mark_size), (x, y), thickness)
        pygame.draw.line(self.screen, self.line_color, (x + 2 * mark_size, y - 2 * mark_size), (x, y), thickness)

    # display winner
    def win_screen(self, mark):
        self.start_gui()
        font = pygame.font.SysFont(None, 150)
        winner = font.render(mark, True, self.draw_color)
        win = font.render("WINS!", True, self.draw_color)
        self.screen.blit(winner, (int(self.size[0] * (5 / 11)), int(self.size[1] * (1 / 5))))
        self.screen.blit(win, (int(self.size[0] * (3 / 10)), int(self.size[1] * (2 / 5))))
        pygame.display.flip()
        print("in the win")


# function for the main loop
def main():
    # initialize pygame module
    pygame.init()
    display = pygame.display  # solves some issues somehow

    # create the GUI
    gui = GUI()
    gui.start_gui()

    # create game
    G = Game()
    gamen = False

    # settings
    best_of = 1  # 1 game is default
    pc_player = False;
    diff = 0;
    pc_isX = False  # denotes if the computer is x or o

    # contrls the main loop
    running = True

    # main loop
    while running:
        # get all events from the event queue
        for event in pygame.event.get():
            # QUIT event handler (x in corner)
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
    
                # find item clicked if any
                clicked = gui.click_item(mouse_position)

                # game button clicked
                if clicked == "game_button":
                    gui.show_menu(best_of, pc_player, diff, pc_isX)

                # menu options

                # new button clicked
                elif clicked == "new":
                    G = Game()
                    gamen = True
                    if best_of == 1:
                        gui.draw_board(G.B)  # get board from game object
                    else:
                        gui.draw_board_score(G.B, G.xWinsCount,
                                             G.oWinsCount)  # get board from game object, pas in the win counts from game object

                # 1 of 1 button clicked
                elif clicked == "1of1":
                    best_of = 1
                    gui.menu = False  # needed to keep showing the menu
                    gui.show_menu(best_of, pc_player, diff, pc_isX)

                # 2 of 3 button clicked
                elif clicked == "2of3":
                    best_of = 2
                    gui.menu = False  # needed to keep showing the menu
                    gui.show_menu(best_of, pc_player, diff, pc_isX)

                # 3 of 5 button clicked
                elif clicked == "3of5":
                    best_of = 3
                    gui.menu = False  # needed to keep showing the menu
                    gui.show_menu(best_of, pc_player, diff, pc_isX)

                # 4 of 7 button clicked
                elif clicked == "4of7":
                    best_of = 4
                    gui.menu = False  # needed to keep showing the menu
                    gui.show_menu(best_of, pc_player, diff, pc_isX)

                # Player vs. Player button clicked
                elif clicked == "pvp":
                    pc_player = False
                    gui.menu = False  # needed to keep showing the menu
                    gui.show_menu(best_of, pc_player, diff, pc_isX)

                # Player vs. PC button clicked
                elif clicked == "pvpc":
                    pc_player = True
                    gui.menu = False  # needed to keep showing the menu
                    gui.show_menu(best_of, pc_player, diff, pc_isX)

                # easy button clicked and pc_player is true
                elif clicked == "easy" and pc_player == True:
                    diff = 0
                    gui.menu = False  # needed to keep showing the menu
                    gui.show_menu(best_of, pc_player, diff, pc_isX)

                # hard button clicked and pc_player is true
                elif clicked == "hard" and pc_player == True:
                    diff = 1
                    gui.menu = False  # needed to keep showing the menu
                    gui.show_menu(best_of, pc_player, diff, pc_isX)

                # computer character clicked
                elif clicked == "pc":
                    if pc_isX == False:
                        pc_isX = True
                    else:
                        pc_isX = False
                    gui.menu = False  # needed to keep showing the menu
                    gui.show_menu(best_of, pc_player, diff, pc_isX)


                # quit clicked and pc_player is true
                elif clicked == "quit":
                    running = False
                    pygame.display.quit()
                    pygame.quit()

                # the actual game starts HERE!!!

                # grid[[0]0]
                elif clicked == "0,0":
                    # place will place the marker of whos turn it is
                    # will return true if the marker is place and false if not
                    # this would be the case if someone try to place a marker in
                    # and already occupied spot
                    if G.place(0, 0):
                        if best_of == 1:
                            gui.draw_board(G.B)
                        else:
                            gui.draw_board_score(G.B, G.xWinsCount, G.oWinsCount)

                # grid[[0][1]
                elif clicked == "0,1":
                    if G.place(0, 1):
                        if best_of == 1:
                            gui.draw_board(G.B)
                        else:
                            gui.draw_board_score(G.B, G.xWinsCount, G.oWinsCount)

                # grid[[0][2]
                elif clicked == "0,2":
                    if G.place(0, 2):
                        if best_of == 1:
                            gui.draw_board(G.B)
                        else:
                            gui.draw_board_score(G.B, G.xWinsCount, G.oWinsCount)

                # grid[[1]0]
                elif clicked == "1,0":
                    if G.place(1, 0):
                        if best_of == 1:
                            gui.draw_board(G.B)
                        else:
                            gui.draw_board_score(G.B, G.xWinsCount, G.oWinsCount)

                # grid[[1][1]
                elif clicked == "1,1":
                    if G.place(1, 1):
                        if best_of == 1:
                            gui.draw_board(G.B)
                        else:
                            gui.draw_board_score(G.B, G.xWinsCount, G.oWinsCount)

                # grid[[1][2]
                elif clicked == "1,2":
                    if G.place(1, 2):
                        if best_of == 1:
                            gui.draw_board(G.B)
                        else:
                            gui.draw_board_score(G.B, G.xWinsCount, G.oWinsCount)

                # grid[[2]0]
                elif clicked == "2,0":
                    if G.place(2, 0):
                        if best_of == 1:
                            gui.draw_board(G.B)
                        else:
                            gui.draw_board_score(G.B, G.xWinsCount, G.oWinsCount)

                # grid[[2][1]
                elif clicked == "2,1":
                    if G.place(2, 1):
                        if best_of == 1:
                            gui.draw_board(G.B)
                        else:
                            gui.draw_board_score(G.B, G.xWinsCount, G.oWinsCount)

                # grid[[2][2]
                elif clicked == "2,2":
                    if G.place(2, 2):
                        if best_of == 1:
                            gui.draw_board(G.B)
                        else:
                            gui.draw_board_score(G.B, G.xWinsCount, G.oWinsCount)
                            
                # check for overall winner
            if G.xWinsCount == best_of or G.oWinsCount == best_of:
                gui.win_screen(G.currentWinner)
                G = Game()
                gamen = False
            # check for draw or winner
            elif G.matchState != 'N':
                G.reprint()
                if best_of == 1:
                    gui.draw_board(G.B)
                else:
                    gui.draw_board_score(G.B, G.xWinsCount, G.oWinsCount)

            # Computer makes it's move it if is its turn
            if pc_player and pc_isX == (G.turn == 'X') and gamen:
                print("Computer turn")
                move = ''
                if diff == 0:
                    # Computer player takes a copy of the board and the computers charater
                    # and returns a tuple with row and col that it was place in
                    if pc_isX == False:
                        move = Computer_Player.easy(G.B, 'O')
                    else:
                        move = Computer_Player.easy(G.B, 'X')
                    G.place(move[0], move[1]);
                else:
                    if pc_isX == False:
                        move = Computer_Player.hard(G.B, 'O')
                    else:
                        move = Computer_Player.hard(G.B, 'X')
                G.place(move[0], move[1]);
                if best_of == 1:
                    gui.draw_board(G.B)
                else:
                    gui.draw_board_score(G.B, G.xWinsCount, G.oWinsCount)

                # check for overall winner
                if G.xWinsCount == best_of or G.xWinsCount == best_of:
                    gui.win_screen(G.currentWinner)
                    gamen = False


if __name__ == "__main__":
    main()

