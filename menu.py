from typing import Any
import pygame as pg
import math
import utils
from game import Game

class Menu():
    def __init__(self):

        self.window_size = pg.Vector2(1440,720)

        self.display = pg.display.set_mode(self.window_size)

        self.character_by_id = {
            0: "shroomshooter",
            1: "slime"
        }

        self.character_imgs = {
            "shroomshooter": utils.load_img("shroomshooter",3),
            "slime": utils.load_img("slime",3),

        }
        self.p1characters = [0,0,0]
        self.p2characters = [0,0,0]

        self.clock = pg.time.Clock()
        self.running = True

        self.pointing_to = 0
        self.player_pointing_to = 0

    def render_characters(self):
        origin = pg.Vector2(200,200)
        idx = 0
        for i in self.p1characters:
            char_name = self.character_by_id[i]
            img = self.character_imgs[char_name]
            self.display.blit(img, origin + pg.Vector2(idx*150, 0))
            if self.player_pointing_to == 0 and idx == self.pointing_to:
                pg.draw.rect(self.display, (230,230,230), (origin + pg.Vector2(idx*150, 0),
                             pg.Vector2(102,102)),4)
            idx += 1

        origin = pg.Vector2(800,200)
        idx = 0
        for i in self.p2characters:
            char_name = self.character_by_id[i]
            img = self.character_imgs[char_name]
            self.display.blit(img, origin + pg.Vector2(idx*150, 0))
            if self.player_pointing_to == 1 and idx == self.pointing_to:
                pg.draw.rect(self.display, (230,230,230), (origin + pg.Vector2(idx*150, 0),
                             pg.Vector2(102,102)),4)
            idx += 1
            
    def shift_pointer(self,n):
        self.pointing_to += n
        if self.pointing_to > 2:
            self.pointing_to = 0
            self.player_pointing_to += 1
            if self.player_pointing_to > 1:
                self.player_pointing_to = 0
            
        if self.pointing_to < 0:
            self.pointing_to = 2
            self.player_pointing_to -= 1
            if self.player_pointing_to < 0:
                self.player_pointing_to = 1

    def shift_character(self,n):
        if self.player_pointing_to == 0:
            self.p1characters[self.pointing_to] += n
            maximum = len(self.character_by_id.keys())-1
            if self.p1characters[self.pointing_to] > maximum:
                self.p1characters[self.pointing_to] = 0
            if self.p1characters[self.pointing_to] < 0:
                self.p1characters[self.pointing_to] = maximum
        if self.player_pointing_to == 1:
            self.p2characters[self.pointing_to] += n
            maximum = len(self.character_by_id.keys())-1
            if self.p2characters[self.pointing_to] > maximum:
                self.p2characters[self.pointing_to] = 0
            if self.p2characters[self.pointing_to] < 0:
                self.p2characters[self.pointing_to] = maximum


    def run(self):
        while self.running:
            self.display.fill((26,26,26))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        game_ = Game(self.p1characters, self.p2characters)
                        self.running = game_.run()
                        
                    if event.key == pg.K_RIGHT:
                        self.shift_pointer(1)
                    if event.key == pg.K_LEFT:
                        self.shift_pointer(-1)
                    if event.key == pg.K_UP:
                        self.shift_character(1)
                    if event.key == pg.K_DOWN:
                        self.shift_character(-1)

            self.render_characters()

            self.clock.tick(utils.FPS)
            pg.display.update()
