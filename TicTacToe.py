# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 13:10:18 2021

@author: Group 1
"""
import pygame

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
        self.game_button = pygame.Rect(25,25,75,35) # attributes of the game button
        self.line_color = (0,0,0) # color of button outline
        self.draw_color = (0,0,0) # color of shaps and text
        
        # create text images
        # create text for game button
        font = pygame.font.SysFont(None,24)
        self.game_text = font.render('Game',True, self.draw_color)
        self.game_text_location = (38,35)
    
    # start the gui window
    def start_gui(self):
        # set title bar
        pygame.display.set_caption("Tic-Tac-Toe")
    
        # create a surface on the screen
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill(self.background)
        
        # draw stuff on screen
        pygame.draw.rect(self.screen,self.line_color,self.game_button, 1)
        self.screen.blit(self.game_text, self.game_text_location)
        pygame.display.flip()
        
    # draws grid for the given board
    def draw_board(self, board):
        
        #define some constants
        box_size = 100 # size of each grid spot
        thickness = 10 #thickness of board line
        length = 3*box_size + 2*thickness #length of board line
        top_bound = 125 # bound of the top border
        left_bound = 225 # bound of the left border
        x_base = left_bound + box_size/2 # x coordinate marker starting position
        y_base = top_bound + box_size/2 # y coordinate marker starting position
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
    
    # testing code-------------------------
    B = Board()
    B.place(0,0,'X')
    B.place(2,2,'O')
    B.place(1,1,'X')
    B.place(0,2,'O')
    gui.draw_board(B)
    
    # endo of testing code ----------------
    
    # contrls the main loop
    running = True;
    
    # main loop
    while running:
        # get all events from the event queue
        for event in pygame.event.get():
            # QUIT event handler
            if event.type == pygame.QUIT:
                running = False
    

    
    
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
