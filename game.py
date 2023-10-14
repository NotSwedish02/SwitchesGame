import pygame as pg
import math
import utils
import player
import player_body
import character
import obstacle

class Game():
    def __init__(self, p1characters, p2characters):
        
        self.window_size = pg.Vector2(1440,720)
        self.display = pg.display.set_mode((self.window_size))

        self.running = True
        self.clock = pg.time.Clock()


        self.character_img_by_id = {
            0: utils.load_img("shroomshooter",1.5),
            1: utils.load_img("slime",1.5)
        }
        
        self.character_class_by_id = {
            0: character.ShooterBody,
            1: character.SlimeBody,

        }

        bodies = [] #creating the bodies
        for i in range(3):
            class_ = self.character_class_by_id[p1characters[i]]
            img_ = self.character_img_by_id[p1characters[i]]
            bodies.append(class_(pg.Vector2(0+100*i,200), i, self.display, img_))
        
        keys1 =  [pg.K_w, pg.K_s, pg.K_a, pg.K_d, pg.K_SPACE, pg.K_e]
        self.player = player.Player(pg.Vector2(0,0), 0, self.display, keys1, bodies)

        bodies2 = [] #creating the bodies
        for i in range(3):
            class_ = self.character_class_by_id[p2characters[i]]
            img_ = self.character_img_by_id[p2characters[i]]
            bodies2.append(class_(pg.Vector2(1000+100*i,200), i+3, self.display, img_))
            
        keys2 = [pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_p, pg.K_l]
        self.player2 = player.Player(pg.Vector2(0,0), 0, self.display, keys2, bodies2)


        self.all_bodies = bodies + bodies2
        
        self.bg = utils.load_img("map",1.5)
        
        self.obstacles = []

        #Dont even look at this
        for x in range(90):
            for y in range(45):
                try:
                    if self.bg.get_at((x*16,y*16))[1] < 200:
                        self.obstacles.append(obstacle.Obstacle(pg.Vector2(x*16,y*16), pg.Vector2(24,24), self.display))
                except:
                    pass


    def run(self):
        while self.running:
            self.display.fill((0,0,0))
            self.display.blit(self.bg, (0,0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    return False
                if event.type == pg.KEYDOWN:
                    self.player.get_input(event.key, True)
                    self.player2.get_input(event.key, True)

                if event.type == pg.KEYUP:
                    self.player.get_input(event.key, False)
                    self.player2.get_input(event.key, False)
                if event.type == pg.MOUSEBUTTONDOWN:
                    print("origin: ", pg.mouse.get_pos()[0]/45, pg.mouse.get_pos()[1]/45)

            for o in self.obstacles:
                o.debug_draw()

            self.player.draw()
            #self.player.debug_draw()

            self.player.move()
            self.player.switch()
            self.player.attack()

            self.player.current_body.manage_general(self.all_bodies, self.obstacles)

            self.player2.draw()
            #self.player.debug_draw()

            self.player2.move()
            self.player2.switch()
            self.player2.attack()

            self.player2.current_body.manage_general(self.all_bodies, self.obstacles)

            self.clock.tick(utils.FPS)
            pg.display.update()