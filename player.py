import pygame as pg
import math
import utils
import input_controller
import timer_clock

class Player():
    def __init__(self, pos, id, display, keys, bodies):
        self.pos = pos
        self.id = id
        self.velocity = pg.Vector2(0,0)
        self.force = pg.Vector2(0,0)
        self.display = display
        
        self.debug_color = utils.debug_color_by_id[self.id]

        self.attrition = 0.999

        self.input_controller = input_controller.Controller(keys)
        self.input_controller.bind_keys(["up", "down", "left", "right", "switch", "attack"])

        self.speed = 3000

        self.bodies = bodies
        self.current_body = bodies[0]
        for body in self.bodies:
            body.set_input_controller(self.input_controller)

        self.just_switched = False

    
    def get_input(self, key, is_pressed):
        self.input_controller.handle_keys(key, is_pressed)

    def attack(self):
        if self.input_controller.keys_pressed[self.input_controller.keys_by_word["attack"]]:
            self.current_body.attack()
            

    def switch(self):
        if self.input_controller.keys_pressed[self.input_controller.keys_by_word["switch"]]:
            if not self.just_switched:
                idx = self.bodies.index(self.current_body)+1
                if idx > len(self.bodies)-1:
                    idx = 0
                self.current_body = self.bodies[idx]
                self.just_switched = True
        else:
            self.just_switched = False

    def debug_draw(self):
        for body in self.bodies:
            body.debug_draw()
    
    def draw(self):
        for body in self.bodies:
            body.draw()

    def move(self):
        self.current_body.move()
        self.current_body.update_attack_timer()