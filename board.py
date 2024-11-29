import pygame
from cell import Cell
from suodoku_generator import generate_sudoku

class Board:
    def __init__(self,width,height,screen,difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.original_board = generate_sudoku(9,difficulty)
        self.board = [row[:] for row in self.original_board]
        self.cells = [
            [Cell(self.board[row][col],row,col,screen) for col in range(9)]
            for row in range(9)
        ]
        self.selected_cell = None

    def draw(self):
        for i in range(10):
            pygame.draw.line(self.screen,(0,0,0),(50*i,0),(50*i,450),2 if i%3 == 0 else 1)
            pygame.draw.line(self.screen,(0,0,0),(0,50*i),(450,50*i),2 if i%3 == 0 else 1)
        for row in self.cells:
            for cell in row:
                cell.draw()

    def select(self,row,col):
        if self.selected_cell:
            self.selected_cell.selected = False
        self.selected_cell = self.cells[row][col]
        self.selected_cell.selected = True

    def click(self,x,y):
        if 0 <= x < 450 and 0 <= y < 450:
            return y //50, x//50
        return None

    def clear(self):
        if self.selected_cell and self.selected_cell.value == 0:
            self.selected_cell.set_cell_value(0)
            self.selected_cell.set_sketched_value(0)
    # IDK what this is
    # def find_empty(self):
    #     for row in range(9):
    #         pass
    def sketch(self,value):
        if self.selected_cell and self.selected_cell.value == 0:
            self.selected_cell.set_sketched_value(value)

    def place_number(self,value):
        if self.sketched_cell and self.selected_cell.value == 0:
            self.selected_cell.set_cell_value(value)
            self.selected_cell.set_sketched_value(0)

    def reset_to_original(self):
        for row in range(9):
            for col in range(9):
                if self.original_board[row][col] == 0:
                    self.cells[row][col].set_cell_value(0)
                    self.cells[row][col].set_sketched_value(0)

    def is_full(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return False
        return True

    def update_board(self):
        for row in range(9):
            for col in range(9):
                self.board[row][col] = self.cells[row][col].value

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return row, col
        return None

    def check_board(self):
        for row in range(9):
            row_vals = set()
            for col in range(9):
                value = self.cells[row][col].value
                if value in row_vals or value == 0:
                    return False
                row_vals.add(value)
            for col in range(9):
                col_vals = set()
                for row in range(9):
                    value = self.cells[row][col].value
                    if value in col_vals or value == 0:
                        return False
                    col_vals.add(value)

            for box_row in range(0,9,3):
                for box_col in range(0,9,3):
                    box_vals = set()
                    for row in range(box_row,box_row+3):
                        for col in range(box_col,box,col+3):
                            value = self.clles[row][col].value
                            if value in box_vals or value == 0:
                                return False
                            box_vals.add(value)
            return True