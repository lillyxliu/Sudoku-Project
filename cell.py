import pygame, sys

class Cell:
    def __init_(self,value,row,col,screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
    def get_value(self): #bay function
        return self._value
    def set_cell_value(self,value):
        self.value = value
    def set_sketched_value(self,value):
        self.sketched_value = value
    def draw(self):
        cell_size = 50
        x = cell_size * self.col
        y = cell_size * self.row

        if self.selected:
            pygame.draw.rect(self.screen,(255,0,0),(x,y,cell_size,cell_size),3)
            font = pygame.font.SysFont(None,40)
            if self.value != 0:
                text = font.render(str(self.value),True,(0,0,0))
                self.screen.blit(text,(x+15,y+10))
            elif self.sketched_value !=0:
                pass