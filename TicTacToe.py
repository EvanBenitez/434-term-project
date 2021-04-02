# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 13:10:18 2021
@author: Group 1
"""
import pygame
import random
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
    def easy(self):
        while computer_turn == True:
            i = random.randInt(0, 2)
            j = random.randInt(0, 2)
            if self.grid[i][j] == 'B':
                self.grid[i][j] = 'X'
                computer_turn = False

    # hard
    def hard(self):
        while computer_turn == True:
            # computer to check if it can win, if can win, wins
            if self.grid[0][0] == 'X' and self.grid[0][2] == 'X' and self.grid[0][1] == 'B':
                self.grid[0][1] = 'X'
            elif self.grid[1][0] == 'X' and self.grid[1][2] == 'X' and self.grid[1][1] == 'B':
                self.grid[1][1] = 'X'
            elif self.grid[2][0] == 'X' and self.grid[2][2] == 'X' and self.grid[2][1] == 'B':
                self.grid[2][1] = 'X'
            elif self.grid[0][0] == 'X' and self.grid[0][1] == 'X' and self.grid[0][2] == 'B':
                self.grid[0][2] = 'X'
            elif self.grid[1][0] == 'X' and self.grid[1][1] == 'X' and self.grid[1][2] == 'B':
                self.grid[1][2] = 'X'
            elif self.grid[2][0] == 'X' and self.grid[2][1] == 'X' and self.grid[2][2] == 'B':
                self.grid[2][2] = 'X'
            elif self.grid[0][1] == 'X' and self.grid[0][2] == 'X' and self.grid[0][0] == 'B':
                self.grid[0][0] = 'X'
            elif self.grid[1][1] == 'X' and self.grid[1][2] == 'X' and self.grid[1][0] == 'B':
                self.grid[1][0] = 'X'
            elif self.grid[2][1] == 'X' and self.grid[2][2] == 'X' and self.grid[2][0] == 'B':
                self.grid[2][0] = 'X'
            elif self.grid[1][1] == 'X':
                if self.grid[0][0] == 'X' and self.grid[2][2] == 'B':
                    self.grid[2][2] = 'X'
                elif self.grid[2][2] == 'X' and self.grid[0][0] == 'B':
                    self.grid[0][0] = 'X'
                elif self.grid[0][2] == 'X' and self.grid[2][0] == 'B':
                    self.grid[2][0] = 'X'
                elif self.grid[2][0] == 'X' and self.grid[0][2] == 'B':
                    self.grid[0][2] = 'X'
            elif self.grid[0][0] == 'O' and self.grid[2][2] == 'O' and self.grid[1][1] == 'B':
                self.grid[1][1] = 'X'
            elif self.grid[0][2] == 'O' and self.grid[2][0] == 'O' and self.grid[1][1] == 'B':
                self.grid[1][1] = 'X'
            elif self.grid[0][0] == 'X' and self.grid[2][0] == 'X' and self.grid[1][0] == 'B':
                self.grid[1][1] = 'X'
            elif self.grid[0][1] == 'X' and self.grid[2][1] == 'X' and self.grid[1][1] == 'B':
                self.grid[1][1] = 'X'
            elif self.grid[0][2] == 'X' and self.grid[2][2] == 'X' and self.grid[1][2] == 'B':
                self.grid[1][2] = 'X'

            # computer to check if user can win, if can win, blocks user
            elif self.grid[0][0] == 'O' and self.grid[0][2] == 'O' and self.grid[0][1] == 'B':
                self.grid[0][1] = 'X'
            elif self.grid[1][0] == 'O' and self.grid[1][2] == 'O' and self.grid[1][1] == 'B':
                self.grid[1][1] = 'X'
            elif self.grid[2][0] == 'O' and self.grid[2][2] == 'O' and self.grid[2][1] == 'B':
                self.grid[2][1] = 'X'
            elif self.grid[0][0] == 'O' and self.grid[0][1] == 'O' and self.grid[0][2] == 'B':
                self.grid[0][2] = 'X'
            elif self.grid[1][0] == 'O' and self.grid[1][1] == 'O' and self.grid[1][2] == 'B':
                self.grid[1][2] = 'X'
            elif self.grid[2][0] == 'O' and self.grid[2][1] == 'O' and self.grid[2][2] == 'B':
                self.grid[2][2] = 'X'
            elif self.grid[0][1] == 'O' and self.grid[0][2] == 'O' and self.grid[0][0] == 'B':
                self.grid[0][0] = 'X'
            elif self.grid[1][1] == 'O' and self.grid[1][2] == 'O' and self.grid[1][0] == 'B':
                self.grid[1][0] = 'X'
            elif self.grid[2][1] == 'O' and self.grid[2][2] == 'O' and self.grid[2][0] == 'B':
                self.grid[2][0] = 'X'
            elif self.grid[1][1] == 'O':
                if self.grid[0][0] == 'O' and self.grid[2][2] == 'B':
                    self.grid[2][2] = 'X'
                elif self.grid[2][2] == 'O' and self.grid[0][0] == 'B':
                    self.grid[0][0] = 'X'
                elif self.grid[0][2] == 'O' and self.grid[2][0] == 'B':
                    self.grid[2][0] = 'X'
                elif self.grid[2][0] == 'O' and self.grid[0][2] == 'B':
                    self.grid[0][2] = 'X'
            elif self.grid[0][0] == 'O' and self.grid[2][2] == 'O' and self.grid[1][1] == 'B':
                self.grid[1][1] = 'X'
            elif self.grid[0][2] == 'O' and self.grid[2][0] == 'O' and self.grid[1][1] == 'B':
                self.grid[1][1] = 'X'
            elif self.grid[0][0] == 'O' and self.grid[2][0] == 'O' and self.grid[1][0] == 'B':
                self.grid[1][1] = 'X'
            elif self.grid[0][1] == 'O' and self.grid[2][1] == 'O' and self.grid[1][1] == 'B':
                self.grid[1][1] = 'X'
            elif self.grid[0][2] == 'O' and self.grid[2][2] == 'O' and self.grid[1][2] == 'B':
                self.grid[1][2] = 'X'

            # computer to make a non winning or blocking move
            elif self.grid[0][0] == 'B':
                self.grid[0][0] = 'X'
            elif self.grid[1][1] == 'B':
                self.grid[1][1] == 'X'
            elif self.grid[2][0] == 'B':
                self.grid[2][0] = 'X'
            elif self.grid[0][2] == 'B':
                self.grid[0][2] = 'X'
            elif self.grid[2][2] == 'B':
                self.grid[2][2] = 'X'
            elif self.grid[0][1] == 'B':
                self.grid[0][1] = 'X'
            elif self.grid[1][0] == 'B':
                self.grid[1][0] = 'X'
            elif self.grid[2][1] == 'B':
                self.grid[2][1] = 'X'
            elif self.grid[1][2] == 'B':
                self.grid[1][2] = 'X'

            computer_turn = False


# class element for Game element
class Game(Board):

    def winTracker(self):
        xwin = False
        owin = False
        # top row X
        if self.grid[0][0] == 'X' and self.grid[0][1] == 'X' and self.grid[0][2] == 'X':
            xwin = True

        # middle row X
        elif self.grid[1][0] == 'X' and self.grid[1][1] == 'X' and self.grid[1][2] == 'X':
            xwin = True

        # bottom row X
        elif self.grid[2][0] == 'X' and self.grid[2][1] == 'X' and self.grid[2][2] == 'X':
            xwin = True

        # left column X
        elif self.grid[0][0] == 'X' and self.grid[1][0] == 'X' and self.grid[2][0] == 'X':
            xwin = True

        # middle column X
        elif self.grid[0][1] == 'X' and self.grid[1][1] == 'X' and self.grid[2][1] == 'X':
            xwin = True

        # right column X
        elif self.grid[0][2] == 'X' and self.grid[1][2] == 'X' and self.grid[2][2] == 'X':
            xwin = True

        # top left to bottom right diagonal X
        elif self.grid[0][0] == 'X' and self.grid[1][1] == 'X' and self.grid[2][2] == 'X':
            xwin = True

        # top right to bottom left diagonal X
        elif self.grid[0][2] == 'X' and self.grid[1][1] == 'X' and self.grid[2][0] == 'X':
            xwin = True

        # top row O
        elif self.grid[0][0] == 'O' and self.grid[0][1] == 'O' and self.grid[0][2] == 'O':
            owin = True

        # middle row O
        elif self.grid[1][0] == 'O' and self.grid[1][1] == 'O' and self.grid[1][2] == 'O':
            owin = True

        # bottom row O
        elif self.grid[2][0] == 'O' and self.grid[2][1] == 'O' and self.grid[2][2] == 'O':
            owin = True

        # left column O
        elif self.grid[0][0] == 'O' and self.grid[1][0] == 'O' and self.grid[2][0] == 'O':
            owin = True

        # middle column O
        elif self.grid[0][1] == 'O' and self.grid[1][1] == 'O' and self.grid[2][1] == 'O':
            owin = True

        # right column O
        elif self.grid[0][2] == 'O' and self.grid[1][2] == 'O' and self.grid[2][2] == 'O':
            owin = True

        # top left to bottom right diagonal 0
        elif self.grid[0][0] == 'O' and self.grid[1][1] == 'O' and self.grid[2][2] == 'O':
            owin = True

        # top right to bottom left diagonal 0
        elif self.grid[0][2] == 'O' and self.grid[1][1] == 'O' and self.grid[2][0] == 'O':
            owin = True

        if owin is True:
            print("Hey now!")

        if xwin is True:
            print("Win!")


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
        self.line_color = (0, 0, 0)  # color of button outline
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
        self.text_Y = self.label_font.render('Y', True, self.draw_color)
        self.text_Y_location = (500, 25)

        # create menu options labels
        self.NewGame = font.render('New game', True, (0, 0, 0))
        self.Best = font.render('Best:', True, (0, 0, 0))
        self.of1 = font.render('1 of 1', True, (0, 0, 0))
        self.of3 = font.render('2 of 3', True, (0, 0, 0))
        self.of5 = font.render('3 of 5', True, (0, 0, 0))
        self.of7 = font.render('4 of 7', True, (0, 0, 0))
        self.playervplayer = font.render('Player vs. Player', True, (0, 0, 0))
        self.playervpc = font.render('Player vs. PC', True, (0, 0, 0))
        self.difficultyLabel = font.render('Difficulty:', True, (0, 0, 0))
        self.easyLabel = font.render('Easy', True, (0, 0, 0))
        self.hardLabel = font.render('Hard', True, (0, 0, 0))
        self.quitLabel = font.render('Quit!', True, (0, 0, 0))

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
        self.screen.blit(self.text_Y, self.text_Y_location)
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
    def show_menu(self):

        if self.menu == False:
            pygame.draw.rect(self.screen, self.menu_color, self.main_menu)

            self.screen.blit(self.NewGame, self.loc_newgame)

            pygame.draw.line(self.screen, (0, 0, 0), self.loc_line1[0], self.loc_line1[1])

            self.screen.blit(self.Best, self.loc_best)
            self.screen.blit(self.of1, self.loc_of1)
            self.screen.blit(self.of3, self.loc_of3)
            self.screen.blit(self.of5, self.loc_of5)
            self.screen.blit(self.of7, self.loc_of7)

            pygame.draw.line(self.screen, (0, 0, 0), self.loc_line2[0], self.loc_line2[1])

            self.screen.blit(self.playervplayer, self.loc_playervsplayer)

            pygame.draw.line(self.screen, (0, 0, 0), self.loc_line3[0], self.loc_line3[1])

            self.screen.blit(self.playervpc, self.loc_playervspc)

            pygame.draw.line(self.screen, (0, 0, 0), self.loc_line4[0], self.loc_line4[1])

            self.screen.blit(self.difficultyLabel, self.loc_diff)
            self.screen.blit(self.easyLabel, self.loc_easy)
            self.screen.blit(self.hardLabel, self.loc_hard)

            pygame.draw.line(self.screen, (0, 0, 0), self.loc_line5[0], self.loc_line5[1])

            self.screen.blit(self.quitLabel, self.loc_quit)

            pygame.display.flip()
            self.menu = True
        else:
            pygame.draw.rect(self.screen, self.background, self.main_menu)
            pygame.display.flip()
            self.menu = False


# function for the main loop
def main():
    # initialize pygame module
    pygame.init()

    # create the GUI
    gui = GUI()
    gui.start_gui()
    G = Game

    display = pygame.display

    # testing code-------------------------
    B = Board()
    B.place(0, 0, 'x')
    B.place(0, 1, 'x')
    B.place(0, 2, 'x')
    B.place(1, 1, 'O')
    B.place(1, 2, 'o')
    B.place(1, 0, 'o')


    Xwins = 0
    Ywins = 0
    gui.draw_board_score(B, Xwins, Ywins)
    # end of testing code ----------------

    # contrls the main loop
    running = True

    # main loop
    while running:
        # get all events from the event queue
        for event in pygame.event.get():
            # QUIT event handler
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                G.winTracker(B)
                Xwins +=1
                Ywins +=1
                gui.draw_board_score(B, Xwins, Ywins)

                if gui.click_item(mouse_position) == "game_button":
                    gui.show_menu()


if __name__ == "__main__":
    # test = Board()
    # i = 0
    # marker = 'X'

    # try:
    #     while i < 5:
    #         row = int(input("enter row: "))
    #         col = int(input("enter column: "))
    #         test.place(row,col,marker)
    #         if marker == 'X':
    #             marker = 'O'
    #         else:
    #             marker = 'X'
    #         i += 1
    #         test.print_board()
    # except:
    #     print("Enter a valid grid location")

    main()
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
    def easy(self):
        while computer_turn == True:
            i = random.randInt(0, 2)
            j = random.randInt(0, 2)
            if self.grid[i][j] == 'B':
                self.grid[i][j] = 'X'
                computer_turn = False

    # hard
    def hard(self):
        while computer_turn == True:
            # computer to check if it can win, if can win, wins
            if self.grid[0][0] == 'X' and self.grid[0][2] == 'X' and self.grid[0][1] == 'B':
                self.grid[0][1] = 'X'
            elif self.grid[1][0] == 'X' and self.grid[1][2] == 'X' and self.grid[1][1] == 'B':
                self.grid[1][1] = 'X'
            elif self.grid[2][0] == 'X' and self.grid[2][2] == 'X' and self.grid[2][1] == 'B':
                self.grid[2][1] = 'X'
            elif self.grid[0][0] == 'X' and self.grid[0][1] == 'X' and self.grid[0][2] == 'B':
                self.grid[0][2] = 'X'
            elif self.grid[1][0] == 'X' and self.grid[1][1] == 'X' and self.grid[1][2] == 'B':
                self.grid[1][2] = 'X'
            elif self.grid[2][0] == 'X' and self.grid[2][1] == 'X' and self.grid[2][2] == 'B':
                self.grid[2][2] = 'X'
            elif self.grid[0][1] == 'X' and self.grid[0][2] == 'X' and self.grid[0][0] == 'B':
                self.grid[0][0] = 'X'
            elif self.grid[1][1] == 'X' and self.grid[1][2] == 'X' and self.grid[1][0] == 'B':
                self.grid[1][0] = 'X'
            elif self.grid[2][1] == 'X' and self.grid[2][2] == 'X' and self.grid[2][0] == 'B':
                self.grid[2][0] = 'X'
            elif self.grid[1][1] == 'X':
                if self.grid[0][0] == 'X' and self.grid[2][2] == 'B':
                    self.grid[2][2] = 'X'
                elif self.grid[2][2] == 'X' and self.grid[0][0] == 'B':
                    self.grid[0][0] = 'X'
                elif self.grid[0][2] == 'X' and self.grid[2][0] == 'B':
                    self.grid[2][0] = 'X'
                elif self.grid[2][0] == 'X' and self.grid[0][2] == 'B':
                    self.grid[0][2] = 'X'
            elif self.grid[0][0] == 'O' and self.grid[2][2] == 'O' and self.grid[1][1] == 'B':
                self.grid[1][1] = 'X'
            elif self.grid[0][2] == 'O' and self.grid[2][0] == 'O' and self.grid[1][1] == 'B':
                self.grid[1][1] = 'X'
            elif self.grid[0][0] == 'X' and self.grid[2][0] == 'X' and self.grid[1][0] == 'B':
                self.grid[1][1] = 'X'
            elif self.grid[0][1] == 'X' and self.grid[2][1] == 'X' and self.grid[1][1] == 'B':
                self.grid[1][1] = 'X'
            elif self.grid[0][2] == 'X' and self.grid[2][2] == 'X' and self.grid[1][2] == 'B':
                self.grid[1][2] = 'X'

            # computer to check if user can win, if can win, blocks user
            elif self.grid[0][0] == 'O' and self.grid[0][2] == 'O' and self.grid[0][1] == 'B':
                self.grid[0][1] = 'X'
            elif self.grid[1][0] == 'O' and self.grid[1][2] == 'O' and self.grid[1][1] == 'B':
                self.grid[1][1] = 'X'
            elif self.grid[2][0] == 'O' and self.grid[2][2] == 'O' and self.grid[2][1] == 'B':
                self.grid[2][1] = 'X'
            elif self.grid[0][0] == 'O' and self.grid[0][1] == 'O' and self.grid[0][2] == 'B':
                self.grid[0][2] = 'X'
            elif self.grid[1][0] == 'O' and self.grid[1][1] == 'O' and self.grid[1][2] == 'B':
                self.grid[1][2] = 'X'
            elif self.grid[2][0] == 'O' and self.grid[2][1] == 'O' and self.grid[2][2] == 'B':
                self.grid[2][2] = 'X'
            elif self.grid[0][1] == 'O' and self.grid[0][2] == 'O' and self.grid[0][0] == 'B':
                self.grid[0][0] = 'X'
            elif self.grid[1][1] == 'O' and self.grid[1][2] == 'O' and self.grid[1][0] == 'B':
                self.grid[1][0] = 'X'
            elif self.grid[2][1] == 'O' and self.grid[2][2] == 'O' and self.grid[2][0] == 'B':
                self.grid[2][0] = 'X'
            elif self.grid[1][1] == 'O':
                if self.grid[0][0] == 'O' and self.grid[2][2] == 'B':
                    self.grid[2][2] = 'X'
                elif self.grid[2][2] == 'O' and self.grid[0][0] == 'B':
                    self.grid[0][0] = 'X'
                elif self.grid[0][2] == 'O' and self.grid[2][0] == 'B':
                    self.grid[2][0] = 'X'
                elif self.grid[2][0] == 'O' and self.grid[0][2] == 'B':
                    self.grid[0][2] = 'X'
            elif self.grid[0][0] == 'O' and self.grid[2][2] == 'O' and self.grid[1][1] == 'B':
                self.grid[1][1] = 'X'
            elif self.grid[0][2] == 'O' and self.grid[2][0] == 'O' and self.grid[1][1] == 'B':
                self.grid[1][1] = 'X'
            elif self.grid[0][0] == 'O' and self.grid[2][0] == 'O' and self.grid[1][0] == 'B':
                self.grid[1][1] = 'X'
            elif self.grid[0][1] == 'O' and self.grid[2][1] == 'O' and self.grid[1][1] == 'B':
                self.grid[1][1] = 'X'
            elif self.grid[0][2] == 'O' and self.grid[2][2] == 'O' and self.grid[1][2] == 'B':
                self.grid[1][2] = 'X'

            # computer to make a non winning or blocking move
            elif self.grid[0][0] == 'B':
                self.grid[0][0] = 'X'
            elif self.grid[1][1] == 'B':
                self.grid[1][1] == 'X'
            elif self.grid[2][0] == 'B':
                self.grid[2][0] = 'X'
            elif self.grid[0][2] == 'B':
                self.grid[0][2] = 'X'
            elif self.grid[2][2] == 'B':
                self.grid[2][2] = 'X'
            elif self.grid[0][1] == 'B':
                self.grid[0][1] = 'X'
            elif self.grid[1][0] == 'B':
                self.grid[1][0] = 'X'
            elif self.grid[2][1] == 'B':
                self.grid[2][1] = 'X'
            elif self.grid[1][2] == 'B':
                self.grid[1][2] = 'X'

            computer_turn = False


# class element for Game element
class Game(Board):

    def winTracker(self):
        xwin = False
        owin = False
        # top row X
        if self.grid[0][0] == 'X' and self.grid[0][1] == 'X' and self.grid[0][2] == 'X':
            xwin = True

        # middle row X
        elif self.grid[1][0] == 'X' and self.grid[1][1] == 'X' and self.grid[1][2] == 'X':
            xwin = True

        # bottom row X
        elif self.grid[2][0] == 'X' and self.grid[2][1] == 'X' and self.grid[2][2] == 'X':
            xwin = True

        # left column X
        elif self.grid[0][0] == 'X' and self.grid[1][0] == 'X' and self.grid[2][0] == 'X':
            xwin = True

        # middle column X
        elif self.grid[0][1] == 'X' and self.grid[1][1] == 'X' and self.grid[2][1] == 'X':
            xwin = True

        # right column X
        elif self.grid[0][2] == 'X' and self.grid[1][2] == 'X' and self.grid[2][2] == 'X':
            xwin = True

        # top left to bottom right diagonal X
        elif self.grid[0][0] == 'X' and self.grid[1][1] == 'X' and self.grid[2][2] == 'X':
            xwin = True

        # top right to bottom left diagonal X
        elif self.grid[0][2] == 'X' and self.grid[1][1] == 'X' and self.grid[2][0] == 'X':
            xwin = True

        # top row O
        elif self.grid[0][0] == 'O' and self.grid[0][1] == 'O' and self.grid[0][2] == 'O':
            owin = True

        # middle row O
        elif self.grid[1][0] == 'O' and self.grid[1][1] == 'O' and self.grid[1][2] == 'O':
            owin = True

        # bottom row O
        elif self.grid[2][0] == 'O' and self.grid[2][1] == 'O' and self.grid[2][2] == 'O':
            owin = True

        # left column O
        elif self.grid[0][0] == 'O' and self.grid[1][0] == 'O' and self.grid[2][0] == 'O':
            owin = True

        # middle column O
        elif self.grid[0][1] == 'O' and self.grid[1][1] == 'O' and self.grid[2][1] == 'O':
            owin = True

        # right column O
        elif self.grid[0][2] == 'O' and self.grid[1][2] == 'O' and self.grid[2][2] == 'O':
            owin = True

        # top left to bottom right diagonal 0
        elif self.grid[0][0] == 'O' and self.grid[1][1] == 'O' and self.grid[2][2] == 'O':
            owin = True

        # top right to bottom left diagonal 0
        elif self.grid[0][2] == 'O' and self.grid[1][1] == 'O' and self.grid[2][0] == 'O':
            owin = True

        if owin is True:
            print("Hey now!")

        if xwin is True:
            print("Win!")


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
        self.line_color = (0, 0, 0)  # color of button outline
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
        self.text_Y = self.label_font.render('Y', True, self.draw_color)
        self.text_Y_location = (500, 25)

        # create menu options labels
        self.NewGame = font.render('New game', True, (0, 0, 0))
        self.Best = font.render('Best:', True, (0, 0, 0))
        self.of1 = font.render('1 of 1', True, (0, 0, 0))
        self.of3 = font.render('2 of 3', True, (0, 0, 0))
        self.of5 = font.render('3 of 5', True, (0, 0, 0))
        self.of7 = font.render('4 of 7', True, (0, 0, 0))
        self.playervplayer = font.render('Player vs. Player', True, (0, 0, 0))
        self.playervpc = font.render('Player vs. PC', True, (0, 0, 0))
        self.difficultyLabel = font.render('Difficulty:', True, (0, 0, 0))
        self.easyLabel = font.render('Easy', True, (0, 0, 0))
        self.hardLabel = font.render('Hard', True, (0, 0, 0))
        self.quitLabel = font.render('Quit!', True, (0, 0, 0))

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
        self.screen.blit(self.text_Y, self.text_Y_location)
        self.screen.blit(self.text_Xwins, self.text_Xwins_location)
        self.screen.blit(self.text_Ywins, self.text_Ywins_location)

        self.draw_board(board)

    # draws grid for the given board
    def draw_board(self, board):

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
        self.menu = False

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
    def show_menu(self):

        if self.menu == False:
            pygame.draw.rect(self.screen, self.menu_color, self.main_menu)

            self.screen.blit(self.NewGame, self.loc_newgame)

            pygame.draw.line(self.screen, (0, 0, 0), self.loc_line1[0], self.loc_line1[1])

            self.screen.blit(self.Best, self.loc_best)
            self.screen.blit(self.of1, self.loc_of1)
            self.screen.blit(self.of3, self.loc_of3)
            self.screen.blit(self.of5, self.loc_of5)
            self.screen.blit(self.of7, self.loc_of7)

            pygame.draw.line(self.screen, (0, 0, 0), self.loc_line2[0], self.loc_line2[1])

            self.screen.blit(self.playervplayer, self.loc_playervsplayer)

            pygame.draw.line(self.screen, (0, 0, 0), self.loc_line3[0], self.loc_line3[1])

            self.screen.blit(self.playervpc, self.loc_playervspc)

            pygame.draw.line(self.screen, (0, 0, 0), self.loc_line4[0], self.loc_line4[1])

            self.screen.blit(self.difficultyLabel, self.loc_diff)
            self.screen.blit(self.easyLabel, self.loc_easy)
            self.screen.blit(self.hardLabel, self.loc_hard)

            pygame.draw.line(self.screen, (0, 0, 0), self.loc_line5[0], self.loc_line5[1])

            self.screen.blit(self.quitLabel, self.loc_quit)

            pygame.display.flip()
            Game()
            self.menu = True
        else:
            pygame.draw.rect(self.screen, self.background, self.main_menu)
            pygame.display.flip()
            self.menu = False


# function for the main loop
def main():
    # initialize pygame module
    pygame.init()

    # create the GUI
    gui = GUI()
    gui.start_gui()
    G = Game

    display = pygame.display

    # testing code-------------------------
    B = Board()
    B.place(0, 0, 'O')
    B.place(0, 1, 'O')
    B.place(2, 2, 'O')
    B.place(1, 1, 'X')
    B.place(0, 2, 'O')


    Xwins = 0
    Ywins = 0
    gui.draw_board_score(B, Xwins, Ywins)
    # end of testing code ----------------

    # contrls the main loop
    running = True

    # main loop
    while running:
        # get all events from the event queue
        for event in pygame.event.get():
            # QUIT event handler
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                G.winTracker(B)
                Xwins +=1
                Ywins +=1
                gui.draw_board_score(B, Xwins, Ywins)

                if gui.click_item(mouse_position) == "game_button":
                    gui.show_menu()


if __name__ == "__main__":
    # test = Board()
    # i = 0
    # marker = 'X'

    # try:
    #     while i < 5:
    #         row = int(input("enter row: "))
    #         col = int(input("enter column: "))
    #         test.place(row,col,marker)
    #         if marker == 'X':
    #             marker = 'O'
    #         else:
    #             marker = 'X'
    #         i += 1
    #         test.print_board()
    # except:
    #     print("Enter a valid grid location")

    main()
