# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 13:10:18 2021

@author: Group 1
"""
import pygame

objects = {}  # dictionary for storying clickable items


# Class element for the Board component
class Board:
    #create grid and initialize with 'B' for blank
    def __init__(self):
        self.grid = [['B','B','B'],\
                ['B','B','B'],\
                ['B','B','B']]
            
    #place X or O on board
    def place(self,row,col,marker):
        if type(row) is int and type(col) is int and 0<=row<3 and 0<=col<3:
            if marker.upper() == 'X' or marker.upper() =='O':
                self.grid[row][col]=marker.upper()
            else:
                raise ValueError("Must input either 'X' or 'O'")
        else:
            raise ValueError("Row and Column must be between 0 and 2 inclusive")
    
    # remove a marker
    # this is untested
    def remove(self, row, col):
        if type(row) is int and type(col) is int and 0<=row<3 and 0<=col<3:
            self.grid[row][col]='B'
        else:
            print("invalid grid location; no action taken")
            
    # Print board, for debuging puposes
    def print_board(self):
        for row in self.grid:
            for col in row:
                print(col + " ", end="")
            print()

# class element for Game element
class Game:
    pass

# contols the graphical content of the game
class GUI:
    
    # initialize
    def __init__(self):
        self.size = (750,500) # dimensions of the window
        self.background = (240,240,240) # background color of the window
        
        # add GUI interactable items in dictionary
        objects["game_button"] = pygame.Rect(25,25,75,35) # attributes of the game button
        
        self.line_color = (0,0,0) # color of button outline
        self.draw_color = (0,0,0) # color of shaps and text
        
        # create text images
        # create text for game button
        font = pygame.font.SysFont(None,24)
        label_font = pygame.font.SysFont(None, 50)
        self.game_text = font.render('Game',True, self.draw_color)
        self.game_text_location = (38,35)
        # create text for X label
        self.text_X = label_font.render('X',True, self.draw_color)
        self.text_X_location = (250,25)
         # create text for Y label
        self.text_Y = label_font.render('Y',True, self.draw_color)
        self.text_Y_location = (500,25)
    
    # start the gui window
    def start_gui(self):
        # set title bar
        pygame.display.set_caption("Tic-Tac-Toe")
    
        # create a surface on the screen
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill(self.background)
        
        # draw stuff on screen
        pygame.draw.rect(self.screen,self.line_color,objects["game_button"], 1)
        self.screen.blit(self.game_text, self.game_text_location)
        pygame.display.flip()
        
    # draws grid for the given board with win totals
    def draw_board_score(self, board, X_win, O_win):
        
        # constants
        line_level = 60
        thickness = 4
        
        # draw label line
        pygame.draw.line(self.screen,self.draw_color, (237, line_level), (285, line_level), thickness)
        pygame.draw.line(self.screen,self.draw_color, (488, line_level), (535, line_level), thickness)
        
        # print X and O label
        self.screen.blit(self.text_X, self.text_X_location)
        self.screen.blit(self.text_Y, self.text_Y_location)
        self.draw_board(board)
        
    # draws grid for the given board
    def draw_board(self, board):
        
        #define some constants
        box_size = 100 # size of each grid spot
        thickness = 10 #thickness of board line
        length = 3*box_size + 2*thickness #length of board line
        top_bound = 150 # bound of the top border
        left_bound = 225 # bound of the left border
        x_base = int(left_bound + box_size/2) # x coordinate marker starting position
        y_base = int(top_bound + box_size/2) # y coordinate marker starting position
        offset = box_size + thickness # offset for markers
        char_bound = 35 # defines the size of markers
        char_thickness = 10
        
        # clear previous board
        pygame.draw.rect(self.screen,self.background,(left_bound,top_bound,length,length))
        
        # draw grid
        pygame.draw.rect(self.screen,self.draw_color,(left_bound,top_bound+box_size,length,thickness))
        pygame.draw.rect(self.screen,self.draw_color,(left_bound,top_bound+2*box_size+thickness,length,thickness))
        pygame.draw.rect(self.screen,self.draw_color,(left_bound+box_size,top_bound,thickness,length))
        pygame.draw.rect(self.screen,self.draw_color,(left_bound+2*box_size+thickness,top_bound,thickness,length))
        
        # print the markers
        for row in range(0,3):
            for col in range(0,3):
                if board.grid[row][col] == 'X':
                    # draw X
                    pygame.draw.line(self.screen,self.draw_color,\
                        ( (x_base-char_bound)+(offset*col) ,(y_base-char_bound)+(offset*row) ),\
                        ( (x_base+char_bound)+(offset*col) ,(y_base+char_bound)+(offset*row) ),\
                        char_thickness)
                    pygame.draw.line(self.screen,self.draw_color,\
                        ( (x_base+char_bound)+(offset*col) ,(y_base-char_bound)+(offset*row) ),\
                        ( (x_base-char_bound)+(offset*col) ,(y_base+char_bound)+(offset*row) ),\
                        char_thickness)     
                elif board.grid[row][col] == 'O':
                    # draw O
                    pygame.draw.circle(self.screen,self.draw_color,\
                        (x_base+(offset*col),y_base+(offset*row)), char_bound, char_thickness)
        # draw board
        pygame.display.flip()



# function for the main loop
def main():
    
    # initialize pygame module
    pygame.init()
    
    #create the GUI
    gui = GUI()
    gui.start_gui()
    display = pygame.display
    myfont = pygame.font.SysFont(None,24)

    # testing code-------------------------
    B = Board()
    B.place(0,0,'O')
    B.place(2,2,'O')
    B.place(1,1,'X')
    B.place(0,2,'O')
    gui.draw_board_score(B,1,1)
    # endo of testing code ----------------
    
    # contrls the main loop
    running = True;
    menu = False
    outline = 1
    # main loop
    while running:
        # get all events from the event queue
        for event in pygame.event.get():
            # QUIT event handler
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN :
                mouse_poistion = pygame.mouse.get_pos()

                if objects["game_button"].collidepoint(mouse_poistion) and menu == False:
                    pygame.draw.rect(gui.screen, (230, 230, 230), (12, 100, 200, 300))

                    NewGame = myfont.render('New game', True, (0, 0, 0))
                    gui.screen.blit(NewGame, (70, 106))

                    pygame.draw.line(gui.screen, (0,0,0), (12, 127), (210, 127))

                    Best = myfont.render('Best:', True, (0, 0, 0))
                    gui.screen.blit(Best, (15, 130))

                    of1 = myfont.render('1 of 1', True, (0, 0, 0))
                    gui.screen.blit(of1, (25, 150))

                    of3 = myfont.render('2 of 3', True, (0, 0, 0))
                    gui.screen.blit(of3, (25, 170))

                    of5 = myfont.render('3 of 5', True, (0, 0, 0))
                    gui.screen.blit(of5, (25, 190))

                    of7 = myfont.render('4 of 7', True, (0, 0, 0))
                    gui.screen.blit(of7, (25, 210))

                    pygame.draw.line(gui.screen, (0,0,0), (12, 235), (210, 235))

                    playervplayer = myfont.render('Player vs. Player', True, (0, 0, 0))
                    gui.screen.blit(playervplayer, (47, 240))

                    pygame.draw.line(gui.screen, (0,0,0), (12, 261), (210, 261))

                    playervpc = myfont.render('Player vs. PC', True, (0, 0, 0))
                    gui.screen.blit(playervpc, (56, 267))

                    pygame.draw.line(gui.screen, (0,0,0), (12, 289), (210, 289))

                    difficultyLabel = myfont.render('Difficulty:', True, (0, 0, 0))
                    gui.screen.blit(difficultyLabel, (15, 300))

                    easyLabel = myfont.render('Easy', True, (0, 0, 0))
                    gui.screen.blit(easyLabel, (19, 317))

                    hardLabel = myfont.render('Hard', True, (0, 0, 0))
                    gui.screen.blit(hardLabel, (19, 335))

                    pygame.draw.line(gui.screen, (0,0,0), (12, 370), (210, 370))

                    hardLabel = myfont.render('Quit!', True, (0, 0, 0))
                    gui.screen.blit(hardLabel, (90, 375))

                    pygame.display.flip()
                    menu = True

                elif objects["game_button"].collidepoint(mouse_poistion) and menu == True:
                    pygame.draw.rect(gui.screen, gui.background, pygame.Rect(12, 100, 200, 300), )
                    pygame.display.flip()
                    menu = False





    
    
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
