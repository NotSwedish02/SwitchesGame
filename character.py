import pygame as pg
import math
import utils
import player_body

class ShooterBody(player_body.Body):
    def __init__(self, pos, id, display, character):
        player_body.Body.__init__(self, pos, id, display, character)
        self.bullets = []
        self.bullet_img = utils.load_img("bullet",1)

    def attack(self):
        if not self.attack_timer > 0:
            self.attack_timer = .15
            b = [self.pos.copy(), self.last_force * 1200]
            self.bullets.append(b)
        
    def manage_general(self, all_bodies, obstacles):
        to_remove = []

        for b in self.bullets:
            #Drawing the bullet
            angle = -math.atan2(b[1].y, b[1].x)/math.pi*180 + 180
            img = pg.transform.rotate(self.bullet_img, angle).convert_alpha()
            
            self.display.blit(img, b[0] - .5 * pg.Vector2(self.bullet_img.get_width(), self.bullet_img.get_height()))

            #Moving the bullet and deleting it if too far away
            b[0] += b[1] * utils.DELTA
            if abs(b[0].x) > 2000 or abs(b[0].y) > 2000:
                to_remove.append(b)

            #Collision with players
            for body in all_bodies:
                if body != self:
                    if abs(b[0].x - body.pos.x) < 32 and abs(b[0].y - body.pos.y) < 32:
                        body.take_dmg(7)
                        if not b in to_remove:
                            to_remove.append(b)
            #Collision with rocks
            for body in obstacles:
                if abs(b[0].x - body.pos.x) < body.size.x/2 and abs(b[0].y - body.pos.y) < body.size.y/2:
                    if not b in to_remove:
                        to_remove.append(b)


        for b in to_remove:
            self.bullets.remove(b)


class SlimeBody(player_body.Body):
    def __init__(self, pos, id, display, character):
        player_body.Body.__init__(self, pos, id, display, character)
        self.bullets = []   
        self.bullet_img = utils.load_img("bullet2",2)


    def attack(self):
        if not self.attack_timer > 0:
            self.attack_timer = .5
            for i in range(8):
                b = [self.pos.copy(), pg.Vector2(1,0).rotate(i/8*360) * 700]
                self.bullets.append(b)

    def manage_general(self, all_bodies, obstacles):
        to_remove = []

        for b in self.bullets:
            #Drawing the bullet
            angle = -math.atan2(b[1].y, b[1].x)/math.pi*180 + 180
            img = pg.transform.rotate(self.bullet_img, angle).convert_alpha()
            
            self.display.blit(img, b[0] - .5 * pg.Vector2(self.bullet_img.get_width(), self.bullet_img.get_height()))

            #Moving the bullet and deleting it if too far away
            b[0] += b[1] * utils.DELTA
            if abs(b[0].x) > 2000 or abs(b[0].y) > 2000:
                to_remove.append(b)

            #Collision with players
            for body in all_bodies:
                if body != self:
                    if abs(b[0].x - body.pos.x) < 32 and abs(b[0].y - body.pos.y) < 32:
                        body.take_dmg(7)
                        if not b in to_remove:
                            to_remove.append(b)
            #Collision with rocks
            for body in obstacles:
                if abs(b[0].x - body.pos.x) < body.size.x/2 and abs(b[0].y - body.pos.y) < body.size.y/2:
                    if not b in to_remove:
                        to_remove.append(b)


        for b in to_remove:
            self.bullets.remove(b)