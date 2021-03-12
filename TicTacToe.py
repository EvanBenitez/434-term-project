# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 13:10:18 2021

@author: Group 1
"""

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

class Game:
    pass

if __name__ == "__main__":
    test = Board()
    i = 0
    marker = 'X'
    
    try:
        while i < 5:
            row = int(input("enter row: "))
            col = int(input("enter column: "))
            test.place(row,col,marker)
            if marker == 'X':
                marker = 'O'
            else:
                marker = 'X'
            i += 1
            test.print_board()
    except:
       print("Enter a valid grid location")
