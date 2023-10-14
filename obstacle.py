import pygame as pg
import math


class Obstacle():
    def __init__(self, pos, size,display):
        self.pos = pos
        self.size = size
        self.display = display
    
    def debug_draw(self):
        pg.draw.rect(self.display, (255,0,0), (self.pos-self.size/2, self.size), 2)