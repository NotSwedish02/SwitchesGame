import pygame as pg
import math
import utils

class Body():
    def __init__(self, pos, id, display, img):
        self.pos = pos
        self.id = id
        self.velocity = pg.Vector2(0,0)
        self.force = pg.Vector2(0,0)
        self.display = display
        
        self.debug_color = utils.debug_color_by_id[self.id]

        self.attrition = 0.999

        self.speed = 3000

        self.img = img

        self.hp = 100

        self.attack_timer = 0

        self.flip_h = False

        self.last_force = pg.Vector2(1,0)

        self.size = pg.Vector2(self.img.get_size()[0], self.img.get_size()[1])

    def set_input_controller(self, input_controller):
        self.input_controller = input_controller

    def debug_draw(self):
        pg.draw.rect(self.display, self.debug_color, (self.pos-pg.Vector2(10,10)*.5, pg.Vector2(10,10)))

    def draw(self):

        img = pg.transform.flip(self.img, self.flip_h,0).convert_alpha()
        self.display.blit(img, self.pos - .5*pg.Vector2(self.img.get_width(), self.img.get_height()))

        pg.draw.rect(self.display, utils.hp_color(self.hp), (self.pos - self.size/2, pg.Vector2(self.hp/2, 10)))
        pg.draw.rect(self.display, (26,26,26), (self.pos - self.size/2 - pg.Vector2(4,4), pg.Vector2(58, 18)),4)

    def move(self):

        self.force *= 0

        if self.input_controller.keys_pressed[self.input_controller.keys_by_word["up"]]:
            self.force.y -= 1
        if self.input_controller.keys_pressed[self.input_controller.keys_by_word["down"]]:
            self.force.y += 1
        if self.input_controller.keys_pressed[self.input_controller.keys_by_word["left"]]:
            self.force.x -= 1
            self.flip_h = True
        if self.input_controller.keys_pressed[self.input_controller.keys_by_word["right"]]:
            self.force.x += 1
            self.flip_h = False

        if self.force.length() != 0:
            self.force = self.force.normalize()
            self.last_force = self.force.copy()

        self.velocity += self.force * self.speed * utils.DELTA

        self.pos += self.velocity * utils.DELTA

            
        self.velocity -= self.velocity * self.attrition * utils.DELTA * 10

    


    def update_attack_timer(self):
        if self.attack_timer > 0:
            self.attack_timer -= utils.DELTA

    def attack(self):
        if not self.attack_timer > 0:
            self.attack_timer = .25
            print(self.id, " has attacked")

    def manage_general(self, all_bodies,obstacles):
        pass

    def take_dmg(self,dmg):
        self.hp -= dmg
        print(self.id, "takes ", dmg, "dmg")
        print(self.id, "has ", self.hp, "hp")